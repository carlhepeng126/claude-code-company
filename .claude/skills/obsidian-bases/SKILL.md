---
name: obsidian-bases
description: |
  Obsidian Bases 公式与函数参考。帮助编写 Obsidian Bases 视图中的表达式、公式和过滤器。
  当用户问 "Bases 公式怎么写"、"Bases 怎么计算日期"、"Bases 函数"、"Obsidian 数据库公式"、
  "公式报错"、"Bases 表达式" 时触发。
allowed-tools:
  - Read
  - Write
  - Edit
---

# Obsidian Bases 公式参考

## 环境

Obsidian Bases 插件提供类似 Notion 数据库的视图功能，支持在表格/卡片/看板视图中使用公式列。

## 核心概念

- **公式列**：以表达式形式定义，返回值动态计算
- **表达式语法**：`"expression"`，使用双引号包裹
- **类型系统**：Date、Duration、Number、String、List、File、Link、Object

## 常见场景速查

### 日期计算

```yaml
# 今天
"today()"

# 距截止日还有多少天
"(date(due_date) - today()).days"

# 7 天后
"today() + \"7d\""

# 格式化日期
"date(created_at).format(\"YYYY-MM-DD\")"
```

### 条件判断

```yaml
# 简单条件
"if(status = 'done', '已完成', '进行中')"

# 多条件
"if(priority = 'high', '紧急', if(priority = 'medium', '普通', '低'))"
```

### 字符串处理

```yaml
# 检查是否包含
"tags.contains('重要')"

# 拼接
"name + ' - ' + status"
```

### 列表操作

```yaml
# 过滤
"tags.filter(value, value != 'archive')"

# 计数
"tags.filter(value, value != '').length"
```

### 文件操作

```yaml
# 检查是否有标签
"file.hasTag('project')"

# 是否在某个文件夹
"file.inFolder('ACT笔记-深度思考')"
```

## 关键陷阱

1. **日期相减返回 Duration，不是数字** — 必须用 `.days`/`.hours` 等字段取出数值后才能做数学运算
2. **Duration 不支持 .round()/.floor()** — 先取数值字段再取整：`(date1 - date2).days.round(0)`
3. **字符串比较区分大小写** — 先用 `.lower()` 统一

## 完整函数参考

见 [FUNCTIONS_REFERENCE.md](references/FUNCTIONS_REFERENCE.md)
