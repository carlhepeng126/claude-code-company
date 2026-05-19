"""
Full retag: replace old flat tags with dimensions-based taxonomy + add maturity/context attributes.
Dry-run mode prints proposed changes; run with --apply to write.
"""
import re, os, sys, json
from pathlib import Path

ROOT = Path(r"c:\Users\Admin\Documents\LLM Wiki\LLM Wiki知识应用")

# ── Tag taxonomy ──────────────────────────────────────────────
TYPE_TAGS = {
    "模型": ["model", "framework", "模型", "框架", "体系", "model", "matrix",
             "四阶段", "三阶段", "三层", "四层", "全景", "操作系统", "公式",
             "金字塔", "漏斗", "阶梯", "路径"],
    "方法": ["methodology", "method", "sop", "流程", "方法", "萃取", "pipeline",
             "system", "rollout", "工作流", "synthesis", "方案", "设计",
             "推广", "开发", "建设", "结构化", "训练", "流程"],
    "案例": ["case", "案例", "实战", "项目", "实践", "经验", "故事"],
    "数据": ["market", "labor", "tax", "guide", "市场", "用工", "税务",
             "政策", "环境", "国别", "投资", "准入", "签证", "数据"],
    "工具": ["tool", "工具", "模板", "template", "checklist", "清单",
             "手册", "handbook", "workbook", "话术", "脚本", "剧本"],
    "报告": ["report", "报告", "研究", "白皮书", "调研", "洞察", "分析"],
    "索引": ["index", "索引", "目录", "汇总", "合集", "collection", "library"],
    "对比": ["comparison", "对比", "比较", "vs", "差异", "区域对比"],
    "方案": ["proposal", "提案", "方案", "计划", "建议", "赋能", "培训方案"],
    "信号": ["signal", "信号", "趋势", "动态", "监测", "日报", "周报", "缓存"],
}

DOMAIN_MAP = {
    "语言培训": ["english", "英语", "外语", "语言", "商务英语", "business-english",
                 "language", "bec", "口语", "听力", "词汇", "翻译", "drilling",
                 "石油英语", "工程英语", "行业英语", "职场英语", "presentation",
                 "演讲", "汇报", "邮件", "写作", "阅读", "竞赛", "测评"],
    "跨文化": ["cross-cultural", "跨文化", "cultural", "culture", "文化",
               "cross-culture", "cultural-intelligence", "CQ", "文化冲突",
               "文化融合", "文化适应", "文化差异", "文化冲击", "多元文化"],
    "领导力": ["leadership", "领导力", "leading", "leader", "管理力",
               "全球领导力", "团队管理", "组织管理", "授权", "赋能",
               "virtual-team", "虚拟团队", "远程管理", "coaching", "教练"],
    "合规风控": ["compliance", "合规", "risk", "风险", "legal", "法律",
                 "劳动法", "gdpr", "数据隐私", "税务", "tax", "tisax",
                 "esg", "反腐败", "制裁", "签证", "工作许可", "安全",
                 "合同", "contract", "fidic", "索赔", "仲裁", "尽职调查"],
    "属地化": ["localization", "属地化", "本地化", "local", "本地",
               "用工", "招聘", "薪酬", "绩效", "劳动", "工会",
               "属地", "本地员工", "本地化率", "本地化策略"],
    "谈判沟通": ["negotiation", "谈判", "沟通", "communication", "communicat",
                 "presentation", "演讲", "表达", "会议", "meeting",
                 "small-talk", "对话", "提问", "倾听", "反馈", "说服",
                 "商务会议", "商务沟通", "工作沟通", "职场沟通", "即兴",
                 "公开演讲", "路演", "汇报", "简报", "商务礼仪"],
    "出海战略": ["overseas", "出海", "global", "国际", "international",
                 "外派", "海外", "abroad", "franchise", "market-entry",
                 "全球化", "走出去", "一带一路", "跨国", "多国",
                 "扩张", "并购", "合资", "独资", "绿地", "区域战略"],
    "人才管理": ["talent", "人才", "hr", "人力资源", "od-td-ld", "od",
                 "td", "ld", "选拔", "培养", "培训体系", "competency",
                 "胜任力", "绩效", "教练", "导师", "hrbp", "组织发展",
                 "人才盘点", "继任", "IDP", "发展计划", "评鉴", "测评",
                 "人才梯队", "人才库", "人才画像", "选人", "用人", "育人"],
    "AI赋能": ["ai", "人工智能", "智能", "数字化", "digital", "llm",
               "agent", "自动化", "算法", "openai", "chatgpt", "claude",
               "acp", "ai-", "-ai", "大模型", "机器学习", "深度学习",
               "智能体", "机器人", "RPA", "数智化", "智能助手"],
    "知识管理": ["knowledge", "知识", "萃取", "方法论", "methodology",
                 "信息", "intelligence", "情报", "signal", "信号",
                 "wiki", "obsidian", "笔记", "工作流", "pipeline",
                 "第二大脑", "知识库", "知识管理", "知识体系", "学习体系",
                 "结构化", "模型", "框架", "framework"],
    "行业洞察": ["trend", "趋势", "行业", "industry", "市场", "market",
                 "竞争", "竞品", "competitor", "对标", "benchmark",
                 "洞察", "前瞻", "展望", "预测", "格局", "生态"],
}

# Type by directory
DIR_TYPE = {
    "concepts": "模型",
    "comparisons": "对比",
    "entities/案例": "案例",
    "entities/报告": "报告",
    "entities/区域": "数据",
    "entities/工具": "工具",
    "entities/训练产品": "工具",
    "entities/索引": "索引",
    "entities/书籍萃取": "方法",
    "entities/竞品": "报告",
    "entities/人物": "案例",
    "entities/其他": "方法",
}

def get_rel_path(filepath):
    return str(filepath.relative_to(ROOT)).replace("\\", "/")

def classify_type(filepath, frontmatter):
    """Determine type/ tag from directory + filename + content signals."""
    rel = get_rel_path(filepath)

    # Check directory mapping
    for d, t in DIR_TYPE.items():
        if rel.startswith(d + "/"):
            return t

    # Root-level entities/ — use filename signals
    fname = filepath.stem.lower()

    if any(kw in fname for kw in ["case", "案例"]):
        return "案例"
    if any(kw in fname for kw in ["report", "报告"]):
        return "报告"
    if any(kw in fname for kw in ["index", "索引", "collection", "library"]):
        return "索引"
    if any(kw in fname for kw in ["tool", "工具", "template", "checklist"]):
        return "工具"
    if any(kw in fname for kw in ["signal", "趋势", "trend", "监测"]):
        return "信号"
    if any(kw in fname for kw in ["comparison", "对比", "vs"]):
        return "对比"
    if any(kw in fname for kw in ["proposal", "提案", "方案"]):
        return "方案"

    # Entities root default → 报告 for research/insight, 方法 for process
    if any(kw in fname for kw in ["research", "study", "洞察", "分析", "insight",
                                    "summary", "总结", "摘要", "市场", "market"]):
        return "报告"
    return "方法"  # default for root entities

def classify_domains(title, old_tags, content_snippet):
    """Return list of domain tags based on keyword scoring."""
    text = (title + " " + " ".join(old_tags) + " " + content_snippet).lower()
    domains = []
    for domain, keywords in DOMAIN_MAP.items():
        score = sum(1 for kw in keywords if kw.lower() in text)
        if score >= 1:
            domains.append(domain)

    # Ensure at least one domain
    if not domains:
        domains.append("知识管理")  # fallback
    return domains

def classify_region(old_tags, title):
    """Extract region tags from old tags + title."""
    text = (title + " " + " ".join(old_tags)).lower()
    regions = []
    region_map = {
        "区域/东南亚": ["东南亚", "southeast-asia", "sea", "vietnam", "thailand",
                       "indonesia", "singapore", "malaysia", "菲律宾", "缅甸", "柬埔寨"],
        "区域/中东": ["中东", "middle-east", "mideast", "saudi", "沙特", "uae",
                     "阿联酋", "oman", "阿曼", "卡塔尔", "科威特", "伊朗", "伊拉克"],
        "区域/非洲": ["非洲", "africa", "ethiopia", "埃塞俄比亚", "angola",
                     "安哥拉", "肯尼亚", "尼日利亚", "埃及", "摩洛哥"],
        "区域/欧洲": ["欧洲", "europe", "eu", "欧盟", "芬兰", "德国", "法国",
                     "英国", "荷兰", "瑞典", "挪威", "俄语区", "russia", "俄罗斯"],
        "区域/北美": ["北美", "north-america", "namerica", "美国", "加拿大",
                     "canada", "墨西哥"],
        "区域/南美": ["南美", "south-america", "samerica", "巴西", "brazil",
                     "阿根廷", "智利", "秘鲁", "哥伦比亚"],
        "区域/拉美": ["拉美", "latin-america", "latin", "拉丁美洲"],
        "区域/中亚": ["中亚", "central-asia", "哈萨克", "乌兹别克", "吉尔吉斯"],
        "区域/南亚": ["南亚", "south-asia", "印度", "india", "巴基斯坦", "孟加拉"],
    }
    for region_tag, keywords in region_map.items():
        if any(kw.lower() in text for kw in keywords):
            regions.append(region_tag)

    # Also preserve old region tags that match
    for t in old_tags:
        if t.startswith("区域/") and t not in regions:
            regions.append(t)

    return regions

def classify_client(title, old_tags, content_snippet):
    """Check if 央企 tag applies."""
    text = (title + " " + " ".join(old_tags) + " " + content_snippet[:500]).lower()
    clients = []
    soe_kw = ["央企", "国企", "soe", "central-soe", "中央企业", "国有企业",
              "中信", "中交", "中核", "中铝", "当升", "中原对外", "中国建筑",
              "中建", "中石化", "中海油", "中石油", "中国路桥", "中国化学",
              "中广核", "中国能建", "中国电建", "华润", "五矿", "中车"]
    private_kw = ["民企", "民营", "比亚迪", "华为", "传音", "小米", "腾讯",
                  "阿里巴巴", "字节", "美团", "拼多多", "京东", "吉利"]

    if any(kw in text for kw in soe_kw):
        clients.append("央企")
    if any(kw in text for kw in private_kw):
        clients.append("民企")
    return clients

def classify_maturity(filepath, content):
    """Heuristic maturity classification."""
    length = len(content)
    has_sections = content.count("\n## ") >= 2
    has_sources = "source" in content[:500].lower() or "来源" in content[:500]
    has_frontmatter = content.startswith("---")

    if length < 500:
        return "seed"
    if has_sections and has_sources and length > 2000:
        return "tree"
    if has_sections and length > 800:
        return "sapling"
    return "seed"

def classify_context(filepath, type_tag, domains):
    """Heuristic context based on type and domain."""
    ctx = set()
    rel = get_rel_path(filepath)

    # Type-based defaults
    if type_tag == "案例":
        ctx.update(["提案", "方案设计"])
    elif type_tag == "模型":
        ctx.update(["方案设计", "课程交付"])
    elif type_tag == "方法":
        ctx.update(["内部运营", "方案设计"])
    elif type_tag == "工具":
        ctx.update(["课程交付", "方案设计"])
    elif type_tag == "报告":
        ctx.update(["市场分析", "提案"])
    elif type_tag == "数据":
        ctx.update(["市场分析", "方案设计"])
    elif type_tag == "信号":
        ctx.update(["市场分析", "内部运营"])
    elif type_tag == "对比":
        ctx.update(["市场分析", "提案"])
    elif type_tag == "方案":
        ctx.update(["提案", "课程交付"])
    else:
        ctx.add("内部运营")

    # Domain-based additions
    if "行业洞察" in domains:
        ctx.add("市场分析")
    if "知识管理" in domains:
        ctx.add("内部运营")
    if "AI赋能" in domains:
        ctx.add("内部运营")

    return sorted(ctx)

def parse_frontmatter(content):
    """Extract existing frontmatter as dict, return (fm_dict, body, fm_start, fm_end)."""
    if not content.startswith("---"):
        return {}, content, 0, 0

    end_idx = content.find("\n---", 3)
    if end_idx == -1:
        return {}, content, 0, 0

    fm_text = content[4:end_idx]
    body = content[end_idx + 4:]

    fm = {}
    for line in fm_text.strip().split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            # Parse list values: [a, b, c]
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
            elif val.startswith("-"):
                # Multi-line list not fully supported; store raw
                pass
            fm[key] = val

    return fm, body, 4, end_idx

def retag_file(filepath, dry_run=True):
    """Classify and generate new frontmatter for a file. Returns changes or None."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm, body, fm_start, fm_end = parse_frontmatter(content)
    title = fm.get("title", filepath.stem)
    old_tags = fm.get("tags", [])
    if isinstance(old_tags, str):
        old_tags = [t.strip() for t in old_tags.split(",")]

    # Content snippet for keyword analysis (first 1000 chars of body)
    snippet = body[:1000]

    # Classify
    type_tag = classify_type(filepath, fm)
    domains = classify_domains(title, old_tags, snippet)
    regions = classify_region(old_tags, title)
    clients = classify_client(title, old_tags, snippet)
    maturity = classify_maturity(filepath, content)
    context = classify_context(filepath, type_tag, domains)

    # Build new tags
    new_tags = [f"type/{type_tag}"] + domains + regions + clients

    # Build new frontmatter block
    new_fm_lines = ["---"]

    # Preserve essential fields, add new ones
    if "title" in fm:
        new_fm_lines.append(f"title: {fm['title']}")
    else:
        new_fm_lines.append(f"title: {filepath.stem}")

    if "created" in fm:
        new_fm_lines.append(f"created: {fm['created']}")
    if "updated" in fm:
        new_fm_lines.append(f"updated: {fm['updated']}")
    if "type" in fm:
        new_fm_lines.append(f"type: {fm['type']}")
    if "sources" in fm:
        src = fm["sources"]
        if isinstance(src, list):
            new_fm_lines.append("sources:")
            for s in src:
                new_fm_lines.append(f"  - {s}")
        else:
            new_fm_lines.append(f"sources: {src}")
    if "source" in fm:
        new_fm_lines.append(f"source: {fm['source']}")

    # New taxonomy fields
    new_fm_lines.append(f"tags: [{', '.join(new_tags)}]")
    new_fm_lines.append(f"maturity: {maturity}")
    new_fm_lines.append(f"context: [{', '.join(context)}]")

    # Preserve other custom fields
    preserved_keys = {"title", "created", "updated", "type", "sources", "source",
                       "tags", "maturity", "context"}
    for k, v in fm.items():
        if k not in preserved_keys and k not in ["confidence", "contested",
                                                   "related_concepts", "related_entities",
                                                   "related_raw", "related_projects",
                                                   "category", "lifecycle", "quality_score",
                                                   "aliases", "source_url", "ingested",
                                                   "sha256", "date_extracted"]:
            if isinstance(v, list):
                new_fm_lines.append(f"{k}:")
                for item in v:
                    new_fm_lines.append(f"  - {item}")
            else:
                new_fm_lines.append(f"{k}: {v}")

    # Add non-preserved known fields at the end (for consistent ordering)
    extra_fields = ["related_concepts", "related_entities", "related_raw",
                    "related_projects", "aliases", "confidence", "contested",
                    "lifecycle", "quality_score", "category", "date_extracted"]
    for k in extra_fields:
        if k in fm:
            v = fm[k]
            if isinstance(v, list):
                new_fm_lines.append(f"{k}:")
                for item in v:
                    new_fm_lines.append(f"  - {item}")
            else:
                new_fm_lines.append(f"{k}: {v}")

    new_fm_lines.append("---")
    new_fm = "\n".join(new_fm_lines) + "\n"

    # The body might start with a stray "-" from old format
    body_clean = body.strip()
    if body_clean.startswith("-"):
        body_clean = body_clean[1:].strip()

    new_content = new_fm + "\n" + body_clean + "\n"

    old_fm_block = content[:fm_end] if fm_end > 0 else ""

    changes = {
        "file": get_rel_path(filepath),
        "old_tags": old_tags,
        "new_tags": new_tags,
        "type_tag": type_tag,
        "domains": domains,
        "regions": regions,
        "clients": clients,
        "maturity": maturity,
        "context": context,
        "new_content": new_content,
    }
    return changes

def main():
    dry_run = "--apply" not in sys.argv
    mode = "[DRY RUN]" if dry_run else "[APPLY]"
    print(f"{mode} scanning files...\n")

    stats = {"total": 0, "changed": 0, "errors": 0, "domains": {}, "types": {}}

    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "raw"]
        for fname in filenames:
            if not fname.endswith(".md") or fname == "SCHEMA.md":
                continue
            fpath = Path(dirpath) / fname
            stats["total"] += 1
            try:
                changes = retag_file(fpath, dry_run)
                if changes:
                    stats["changed"] += 1
                    stats["types"][changes["type_tag"]] = stats["types"].get(changes["type_tag"], 0) + 1
                    for d in changes["domains"]:
                        stats["domains"][d] = stats["domains"].get(d, 0) + 1

                    if dry_run:
                        old = ", ".join(changes["old_tags"]) if changes["old_tags"] else "(none)"
                        new = ", ".join(changes["new_tags"])
                        print(f"  {changes['file']}")
                        print(f"    {old}  ->  {new}")
                        print(f"    maturity={changes['maturity']}  context={changes['context']}")
                    else:
                        with open(fpath, "w", encoding="utf-8") as f:
                            f.write(changes["new_content"])
                        print(f"  OK {changes['file']}")
            except Exception as e:
                stats["errors"] += 1
                print(f"  ERR {get_rel_path(fpath)} — {e}")

    print(f"\n── Stats ──")
    print(f"  Files: {stats['total']}  Changed: {stats['changed']}  Errors: {stats['errors']}")
    print(f"  Types: {dict(sorted(stats['types'].items()))}")
    print(f"  Domains: {dict(sorted(stats['domains'].items()))}")

    if dry_run:
        print("\nRun with --apply to write changes.")

if __name__ == "__main__":
    main()
