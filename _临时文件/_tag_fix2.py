"""Targeted tag cleanup — remove remaining non-standard tags from concepts/ and entities/."""
import re, os

ROOT = r"c:\Users\Admin\Documents\LLM Wiki\LLM Wiki知识应用"

# Standard tags to keep
STANDARD = {
    '培训','人才','跨文化','出海','央企','沟通','谈判','领导力','合规','属地化','信号','AI','工具',
    '区域/东南亚','区域/中东','区域/非洲','区域/南美','区域/拉美','区域/欧洲','区域/中亚','区域/南亚','区域/北美',
}

# Additional exact tags to remove (company names, too specific, industry jargon)
REMOVE_EXACT = {
    '组织管理', 'AML', 'VCC', '准入', '产品设计', '投资于人', '政策风向', '内训师',
    '反馈力', 'L4自动驾驶', '机器人', '医疗设备', '五矿', '多国指南', '打标分桶',
    '知识萃取', '腾讯投资', 'CROIC', '国家风险', '评级', '风险评估', '白皮书',
    '财经杂志', 'index', '体系化', '认证资质', '传音', '双向连接', '支付宝', '澳洲',
    '场景化', '投资环境', '税收政策', '跨学科', '全周期', '知识库', '华润',
    '交通基建', '交通建设', '汽车制造', '石油化工', '石油能源', '石油天然气',
    '能源建设', '能源基建', '核工业', '有色金属', '校企合作',
    '商务英语培训', '英语培训', '企业英语培训', '商务英语', '商务英语竞赛',
    '英语演讲', '英语竞赛', '员工英语培训', '海外人才培训',
    '- 核心卡', '- 笔记同步助手',
    # Round 2 — remaining non-standard tags (2026-05-15)
    '国别调研', '化学工程', '多元化集团', '气象', '建材行业', '建筑工程',
    '中文工坊', '疏浚工程', '科技互联网', '晶澳科技', '关系构建', '矿冶工程',
    'Speexx', '中国策略', '并购', '西门子', '学员故事', '贸促会', '中国建筑',
    '工程管理', 'PPP', '分包管理', '地缘风险', '现金流', '证据链', 'Carl业务',
    '公关危机', '危机传播', '项目融资', '俄语区', '新品类', '腾讯系', '中层管理',
}

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    m = re.search(r'tags:\s*\[([^\]]*)\]', content)
    if not m:
        return False

    old_tags = [t.strip() for t in m.group(1).split(',') if t.strip()]
    new_tags = []
    changed = False

    for t in old_tags:
        if t in STANDARD or t.startswith('区域/'):
            new_tags.append(t)
        elif t in REMOVE_EXACT:
            changed = True  # remove
        else:
            # Keep unknown — might be valid
            new_tags.append(t)

    if not changed:
        return False

    old_line = m.group(0)
    if new_tags:
        new_line = f"tags: [{', '.join(new_tags)}]"
    else:
        new_line = ""  # remove line entirely

    new_content = content.replace(old_line, new_line, 1)

    # Clean up empty tags line
    if not new_tags:
        new_content = re.sub(r'\n?\ntags:\s*\[\]', '', new_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

def main():
    changed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != 'raw']
        for fname in filenames:
            if not fname.endswith('.md') or fname == 'SCHEMA.md':
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                if fix_file(fpath):
                    changed += 1
                    print(f"  Fixed: {os.path.relpath(fpath, ROOT)}")
            except Exception as e:
                print(f"  ERROR: {fpath} — {e}")
    print(f"\nTotal fixed: {changed}")

if __name__ == "__main__":
    main()
