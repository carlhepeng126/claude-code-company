"""
Retag v3 final: Robustly strip ALL frontmatter variants, reclassify, write clean output.
Handles:
  - Proper ---...--- (standard)
  - Malformed ---...- (single dash separator)
  - Double-frontmatter from failed v2 run
  - No frontmatter at all

Strategy: Find the first markdown heading (#) or real content line.
Everything before that is "frontmatter zone". Parse it for old tags/title.
Then write clean new frontmatter + remaining body.
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
          "中国路桥", "华润", "五矿", "中车", "中广核", "中国能建", "中国电建"]

PRIVATE_KW = ["民企", "民营", "比亚迪", "华为", "传音", "小米", "腾讯",
              "阿里巴巴", "字节", "美团", "京东", "吉利", "byd"]

def relpath(fp):
    return str(fp.relative_to(ROOT)).replace("\\", "/")

def strip_frontmatter(content):
    """
    Strip ALL frontmatter-like content from the beginning of the file.
    Returns (extracted_fm_dict, clean_body).

    The body is everything from the first real markdown line onward
    (line starting with #) or from the first non-YAML, non-separator line.
    """
    lines = content.split("\n")

    # Collect all YAML-like lines from the start for metadata extraction
    fm_lines_text = []
    body_start = 0

    in_frontmatter_zone = True
    consecutive_non_yaml = 0

    for i, line in enumerate(lines):
        stripped = line.strip()

        if not in_frontmatter_zone:
            break

        # Skip opening ---
        if i == 0 and stripped in ("---", "-"):
            continue

        # Closing --- or - (standalone)
        if stripped in ("---", "-", "--"):
            continue

        # Empty line within frontmatter zone
        if not stripped:
            consecutive_non_yaml += 1
            if consecutive_non_yaml >= 2:
                # Two blank lines — probably end of frontmatter zone
                in_frontmatter_zone = False
                body_start = i + 1
            continue

        # Check if this is a YAML-like line (key: value or indented list item)
        if ":" in stripped and not stripped.startswith("#") and not stripped.startswith(">") and not stripped.startswith("|"):
            fm_lines_text.append(line)
            consecutive_non_yaml = 0
            continue

        # Indented list item (part of YAML list)
        if line.startswith("  - ") or line.startswith("    - "):
            fm_lines_text.append(line)
            consecutive_non_yaml = 0
            continue

        # This line doesn't look like YAML — it's body
        body_start = i
        in_frontmatter_zone = False

    # Parse collected YAML lines, handling multi-line lists
    fm = {}
    current_key = None
    for line in fm_lines_text:
        stripped = line.strip()
        # Indented list item — append to current key
        if line.startswith("  - ") or line.startswith("    - "):
            item = stripped.lstrip("- ").strip().strip("'\"")
            if current_key and item:
                if isinstance(fm.get(current_key), list):
                    fm[current_key].append(item)
                else:
                    fm[current_key] = [item]
            continue
        # Key: value line
        if ":" in stripped and not stripped.startswith("-") and not stripped.startswith("#"):
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
            elif v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            fm[k] = v
            current_key = k
        # Blank line resets current_key
        elif not stripped:
            current_key = None

    # Clean body
    body_lines = lines[body_start:]
    # Remove leading blank lines
    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)
    body = "\n".join(body_lines)

    return fm, body

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

def build_frontmatter(fm, new_tags, maturity, context, title):
    """Build clean frontmatter block."""
    lines = ["---"]
    lines.append(f"title: {title}")

    for key in ["created", "updated", "type", "source"]:
        if key in fm:
            v = fm[key]
            if isinstance(v, list):
                lines.append(f"{key}:")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{key}: {v}")

    lines.append(f"tags: [{', '.join(new_tags)}]")
    lines.append(f"maturity: {maturity}")
    lines.append(f"context: [{', '.join(context)}]")

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

            fm, body = strip_frontmatter(content)

            # Get title from extracted fm, or from first heading in body
            title = fm.get("title", "")
            if isinstance(title, list):
                title = title[0] if title else ""
            if not title:
                # Try to grab from body's first heading
                m = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
                title = m.group(1).strip() if m else fp.stem

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
                print(f"    old: {old_tag_str}")
                print(f"    new: {', '.join(new_tags)}")
                print(f"    title={title}  maturity={maturity}")
            else:
                new_fm = build_frontmatter(fm, new_tags, maturity, context, title)
                with open(fp, "w", encoding="utf-8") as f:
                    f.write(new_fm + "\n" + body.strip() + "\n")
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
