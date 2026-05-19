"""
Retag v3: Fix frontmatter parsing to handle both proper --- and malformed - closing.
Also properly removes old frontmatter before inserting new.
"""
import re, os, sys
from pathlib import Path
from collections import Counter

ROOT = Path(r"c:\Users\Admin\Documents\LLM Wiki\LLM Wiki知识应用")
DRY = "--apply" not in sys.argv

# ── Config ─────────────────────────────────────────────────────
OLD_TO_DOMAIN = {
    "培训": "语言培训", "跨文化": "跨文化", "领导力": "领导力",
    "合规": "合规风控", "属地化": "属地化",
    "谈判": "谈判沟通", "沟通": "谈判沟通",
    "出海": "出海战略", "人才": "人才管理",
    "AI": "AI赋能", "信号": "行业洞察",
}

TITLE_KW = {
    "语言培训": ["英语", "外语", "语言", "商务英语", "english-training", "speaking",
                 "listening", "口语", "写作", "邮件", "词汇", "drilling",
                 "行业英语", "职场英语", "竞赛", "翻译", "评测", "语言培训"],
    "跨文化": ["跨文化", "cross-cultural", "文化冲突", "文化融合", "文化适应",
               "多元文化", "cultural-bridge", "文化差异", "文化智力"],
    "领导力": ["领导力", "leadership", "团队管理", "global-leader", "coaching",
               "授权", "虚拟团队", "组织领导"],
    "合规风控": ["合规", "compliance", "风险", "gdpr", "劳动法", "tisax", "esg",
                 "反腐败", "制裁", "fidic", "合同", "税务", "用工合规", "法律"],
    "属地化": ["属地化", "localization", "本地化", "属地", "本地员工", "用工环境"],
    "谈判沟通": ["谈判", "negotiation", "沟通", "communicat", "演讲", "会议",
                 "meeting", "small-talk", "表达", "即兴", "路演", "礼仪", "presenter"],
    "出海战略": ["出海", "overseas", "全球化", "international", "外派", "海外",
                 "franchise", "market-entry", "跨国", "一带一路", "国别", "区域战略"],
    "人才管理": ["人才", "talent", "人力资源", "od-td", "组织发展", "胜任力",
                 "人才盘点", "继任", "idp", "评鉴", "选拔", "hrbp", "培养",
                 "人才梯队", "人力资本", "人才画像"],
    "AI赋能": ["ai-", "-ai", "人工智能", "数字化", "大模型", "agent", "智能体",
               "openai", "chatgpt", "claude", "自动化", "数智化", "ai工具", "ai赋能"],
    "知识管理": ["知识管理", "knowledge-base", "知识库", "知识体系", "萃取",
                 "情报", "signal", "obsidian", "第二大脑", "笔记系统", "工作流",
                 "deep-extraction", "intelligence", "methodology", "方法论"],
    "行业洞察": ["趋势", "洞察", "前瞻", "展望", "格局", "白皮书", "行业报告",
                 "竞品", "competitor", "benchmark"],
}

DIR_TYPE = {
    "concepts": "模型", "comparisons": "对比",
    "entities/案例": "案例", "entities/报告": "报告",
    "entities/区域": "数据", "entities/工具": "工具",
    "entities/训练产品": "工具", "entities/索引": "索引",
    "entities/书籍萃取": "方法", "entities/竞品": "报告",
    "entities/人物": "案例", "entities/其他": "方法",
    "方法工具箱": "方法", "索引": "索引", "诊断报告": "报告",
}

REGION_KW = {
    "区域/东南亚": ["东南亚", "southeast-asia", "vietnam", "thailand",
                    "indonesia", "singapore", "malaysia", "菲律宾", "缅甸"],
    "区域/中东": ["中东", "middle-east", "mideast", "saudi", "沙特",
                  "uae", "阿联酋", "oman", "阿曼", "卡塔尔"],
    "区域/非洲": ["非洲", "africa", "ethiopia", "埃塞俄比亚", "angola", "安哥拉"],
    "区域/欧洲": ["欧洲", "europe", "eu", "欧盟", "芬兰", "德国", "法国", "英国", "俄罗斯", "russia"],
    "区域/北美": ["北美", "north-america", "美国", "canada", "加拿大", "墨西哥", "mexico"],
    "区域/南美": ["南美", "south-america", "巴西", "brazil", "阿根廷", "智利", "秘鲁"],
    "区域/拉美": ["拉美", "latin-america", "拉丁美洲"],
    "区域/中亚": ["中亚", "central-asia", "哈萨克", "乌兹别克"],
    "区域/南亚": ["南亚", "south-asia", "印度", "india", "巴基斯坦", "孟加拉"],
}

SOE_KW = ["央企", "国企", "soe", "中央企业", "中信", "中交", "中核", "中铝",
          "当升", "中原对外", "中国建筑", "中建", "中石化", "中海油", "中石油",
          "中国路桥", "华润", "五矿", "中车", "中广核", "中国能建", "中国电建",
          "中国化学", "国投", "中粮", "中色", "中冶", "中铁"]

PRIVATE_KW = ["民企", "民营", "比亚迪", "华为", "传音", "小米", "腾讯",
              "阿里巴巴", "字节", "美团", "京东", "吉利", "byd", "ozon"]

def relpath(fp):
    return str(fp.relative_to(ROOT)).replace("\\", "/")

def parse_frontmatter(content):
    """Parse frontmatter. Returns (fm_dict, body_text).
    Handles both:
      ---\n...\n---\n  (proper)
      ---\n...\n-\n    (malformed, dash as separator)
    """
    if not content.startswith("---"):
        return {}, content

    # Find where the YAML ends and body begins
    # Look for pattern: \n---\n or \n-\n after the opening ---
    # But not matching --- that's part of YAML content

    # Remove opening ---
    rest = content[3:].lstrip("\n")

    # Try to find closing --- first
    idx = rest.find("\n---\n")
    if idx >= 0:
        fm_text = rest[:idx]
        body = rest[idx + 5:]  # skip \n---\n
        return parse_yaml_lines(fm_text), body

    # Try malformed closing: \n-\n (single dash on its own line)
    idx = rest.find("\n-\n")
    if idx >= 0:
        fm_text = rest[:idx]
        body = rest[idx + 3:]  # skip \n-\n
        return parse_yaml_lines(fm_text), body

    # No closing found at all — return whole thing as body
    return {}, rest

def parse_yaml_lines(text):
    """Parse simple YAML key: value lines into dict. Handles list values."""
    fm = {}
    for line in text.strip().split("\n"):
        if ":" in line and not line.strip().startswith("-"):
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
            elif v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            fm[k] = v
    return fm

def get_type(fp):
    rel = relpath(fp)
    for d, t in DIR_TYPE.items():
        if rel.startswith(d + "/"):
            return t
    stem = fp.stem.lower()
    if any(kw in stem for kw in ["case", "案例"]): return "案例"
    if any(kw in stem for kw in ["report", "报告"]): return "报告"
    if any(kw in stem for kw in ["index", "索引", "collection", "library"]): return "索引"
    if any(kw in stem for kw in ["tool", "工具", "template", "checklist"]): return "工具"
    if any(kw in stem for kw in ["signal", "趋势", "trend", "监测"]): return "信号"
    if any(kw in stem for kw in ["comparison", "对比", "vs"]): return "对比"
    if any(kw in stem for kw in ["proposal", "提案", "方案"]): return "方案"
    if any(kw in stem for kw in ["research", "洞察", "insight", "summary"]): return "报告"
    return "方法"

def get_domains(title, old_tags):
    domains = set()
    for t in old_tags:
        mapped = OLD_TO_DOMAIN.get(t)
        if mapped:
            domains.add(mapped)
    tl = title.lower()
    for domain, kws in TITLE_KW.items():
        if domain in domains:
            continue
        if any(kw.lower() in tl for kw in kws):
            domains.add(domain)
    if not domains:
        domains.add("知识管理")
    return sorted(domains)

def get_regions(title, old_tags):
    regions = set()
    for t in old_tags:
        if t.startswith("区域/"):
            regions.add(t)
    tl = title.lower()
    for region_tag, kws in REGION_KW.items():
        if region_tag not in regions and any(kw.lower() in tl for kw in kws):
            regions.add(region_tag)
    return sorted(regions)

def get_client(title, old_tags):
    clients = set()
    text = (title + " " + " ".join(old_tags)).lower()
    if any(kw in text for kw in SOE_KW):
        clients.add("央企")
    if any(kw in text for kw in PRIVATE_KW):
        clients.add("民企")
    return sorted(clients)

def get_maturity(content):
    n = len(content)
    sections = content.count("\n## ")
    if n < 400: return "seed"
    if sections >= 3 and n > 2000: return "tree"
    if sections >= 1 and n > 600: return "sapling"
    return "seed"

def get_context(type_tag, domains):
    ctx = set()
    if type_tag == "案例": ctx.update(["提案", "方案设计"])
    elif type_tag == "模型": ctx.update(["方案设计", "课程交付"])
    elif type_tag == "方法": ctx.update(["内部运营", "方案设计"])
    elif type_tag == "工具": ctx.update(["课程交付", "方案设计"])
    elif type_tag == "报告": ctx.update(["市场分析", "提案"])
    elif type_tag == "数据": ctx.update(["市场分析", "方案设计"])
    elif type_tag == "信号": ctx.update(["市场分析", "内部运营"])
    elif type_tag == "对比": ctx.update(["市场分析", "提案"])
    elif type_tag == "方案": ctx.update(["提案", "课程交付"])
    else: ctx.add("内部运营")
    if "行业洞察" in domains: ctx.add("市场分析")
    if "知识管理" in domains: ctx.add("内部运营")
    if "AI赋能" in domains: ctx.add("内部运营")
    return sorted(ctx)

def build_frontmatter(fm, new_tags, maturity, context):
    """Build clean frontmatter block."""
    lines = ["---"]
    title = fm.get("title", "Untitled")
    if isinstance(title, list):
        title = title[0] if title else "Untitled"
    lines.append(f"title: {title}")

    # Pass through important metadata
    for key in ["created", "updated", "type", "source"]:
        if key in fm:
            v = fm[key]
            if isinstance(v, list):
                lines.append(f"{key}:")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{key}: {v}")

    # New taxonomy
    lines.append(f"tags: [{', '.join(new_tags)}]")
    lines.append(f"maturity: {maturity}")
    lines.append(f"context: [{', '.join(context)}]")

    # Pass through other useful fields
    for key in ["sources", "related_concepts", "related_entities", "related_raw",
                "related_projects", "aliases", "confidence", "contested",
                "lifecycle", "quality_score", "category", "date_extracted",
                "source_url", "ingested", "sha256"]:
        if key not in fm:
            continue
        v = fm[key]
        if isinstance(v, list):
            lines.append(f"{key}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {v}")

    lines.append("---")
    return "\n".join(lines) + "\n"

# ── Main ────────────────────────────────────────────────────────
mode = "[DRY RUN]" if DRY else "[APPLY]"
print(f"{mode} scanning...\n")

stats = {"files": 0, "changed": 0, "errors": 0}
type_ctr, dom_ctr = Counter(), Counter()

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "raw"]
    for fname in filenames:
        if not fname.endswith(".md") or fname == "SCHEMA.md":
            continue
        fp = Path(dirpath) / fname
        stats["files"] += 1
        try:
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()

            # Parse frontmatter
            fm, body = parse_frontmatter(content)

            title = fm.get("title", fp.stem)
            if isinstance(title, list):
                title = title[0] if title else fp.stem
            old_tags = fm.get("tags", [])
            if isinstance(old_tags, str):
                old_tags = [t.strip() for t in old_tags.split(",")]

            type_tag = get_type(fp)
            domains = get_domains(title, old_tags)
            regions = get_regions(title, old_tags)
            clients = get_client(title, old_tags)
            maturity = get_maturity(content)
            context = get_context(type_tag, domains)

            new_tags = list(dict.fromkeys([f"type/{type_tag}"] + domains + regions + clients))

            if DRY:
                old_tag_str = ", ".join(old_tags) if old_tags else "(none)"
                print(f"  {relpath(fp)}")
                print(f"    {old_tag_str}  ->  {', '.join(new_tags)}")
                print(f"    title={title}  maturity={maturity}")
            else:
                new_fm = build_frontmatter(fm, new_tags, maturity, context)
                body_clean = body.strip()
                with open(fp, "w", encoding="utf-8") as f:
                    f.write(new_fm + "\n" + body_clean + "\n")
                print(f"  OK {relpath(fp)}")

            stats["changed"] += 1
            type_ctr[type_tag] += 1
            for d in domains:
                dom_ctr[d] += 1

        except Exception as e:
            stats["errors"] += 1
            print(f"  ERR {relpath(fp)}: {e}")

print(f"\nFiles: {stats['files']}  Changed: {stats['changed']}  Errors: {stats['errors']}")
print(f"Types: {dict(type_ctr.most_common())}")
print(f"Domains: {dict(dom_ctr.most_common())}")
if DRY:
    print("\nRun with --apply to write changes.")
