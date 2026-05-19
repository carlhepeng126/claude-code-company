# 实战案例：Country Navigator 全站下载

## 背景

从 my.countrynavigator.com 下载 249 个国家/地区的文化指南，包括：
- Flight Pack PDF + Mindset Map PDF（每个国家 2 个）
- 20 篇结构化文章（每个国家约 20 篇）

## 最终结果

- 249 个国家目录
- 208 个 PDF（104 国 × 2）
- 3,622 篇 Markdown 文章
- 总耗时约 3 小时

## 关键发现

1. **SPA + Bearer Token**：网站是 Angular SPA，API 使用 Bearer Token（非 Cookie）
2. **PDF 链接无文本**：`<a>` 标签的 PDF 链接文本为空（仅图标），必须用 `[href*=".pdf"]` 匹配
3. **networkidle 必须**：`domcontentloaded` 时 PDF 链接未渲染，必须 `networkidle` + 额外等待
4. **API 比 DOM 快**：文章内容通过 API（Bearer Token）获取比页面解析快 10 倍
5. **断点续传关键**：249 个国家中途必然遇到网络波动，`_progress.json` 确保不重来

## 脚本架构

```
Phase 1: 文章下载（API）
  - 登录 → 捕获 token
  - 获取国家列表（API: /countries?allInWorld=1）
  - 逐个国家：获取文章结构 + 批量获取文章内容
  - 每个国家 1 次 page.evaluate（内部并行 5 个 fetch）
  - 速度：~5 秒/国

Phase 2: PDF 下载（浏览器）
  - 逐个国家：访问 /country-home/{id}
  - 等待 networkidle + 4s
  - 查找 a[href*=".pdf"] 链接
  - waitForEvent('download') + click → saveAs
  - 速度：~12 秒/国
```
