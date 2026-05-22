# Tool Template Patterns

所有工具模板在HTML中使用以下CSS类构建，不要使用ASCII框线或代码块。

## 表单容器

```html
<div class="form-sheet">
  <div class="form-title">工具名称</div>
  <div class="form-meta">编号/版本/日期等元信息</div>
  <!-- 内容区 -->
</div>
```

## 表单区块标签

```html
<div class="form-section-label">区块名称（如"岗位基本信息"）</div>
```

## 表单行（标签+填空值）

```html
<div class="form-row">
  <span class="fr-label">字段名</span>
  <span class="fr-value"></span>
  <span class="fr-tag">标签（可选）</span>
</div>
```

## 勾选框

```html
<div class="form-check">
  <span class="form-check-box"></span> 选项文字
</div>
```

## 评分行

```html
<div class="body-text-sm">
  <strong>A. 配偶职业影响</strong> ____ / 5
</div>
```

## 场景卡片（用于情景剧本/案例）

```html
<div class="scenario-card">
  <span class="sc-num">01</span>
  <span class="sc-title">标题</span>
  <div class="sc-body">内容...</div>
</div>
```

## SOP层级

```html
<div class="sop-level">
  <div class="sl-name">第一级：名称</div>
  <div class="sl-info"><strong>触发：</strong>... | <strong>责任人：</strong>... | <strong>时限：</strong>...<br><strong>流程：</strong>...</div>
</div>
```

## 小表格

```html
<table class="tool-table">
  <thead><tr><th>列1</th><th>列2</th></tr></thead>
  <tbody>
    <tr><td>...</td><td>...</td></tr>
  </tbody>
</table>
```

## 流程步骤

```html
<div class="flow-row">
  <span class="step">步骤1</span><span class="arr">→</span>
  <span class="step">步骤2</span><span class="arr">→</span>
  <span class="step">步骤3</span>
</div>
```

## 四象限卡片

```html
<div class="quad-row">
  <div class="quad-card">
    <h6>区域名</h6>
    <div class="stars">难度 ★★★★★</div>
    <dl>
      <dt>选人侧重</dt><dd>...</dd>
      <dt>角色配置</dt><dd>...</dd>
      <dt>关键动作</dt><dd>...</dd>
    </dl>
  </div>
</div>
```

## 时间轴

```html
<div class="timeline-row">
  <div class="tl-phase"><h6>阶段名</h6><div class="tlt">时间</div><div class="tld">内容</div></div>
</div>
```

## 路线图块

```html
<div class="road-block rb1">
  <div class="rb-num">I</div>
  <div class="rb-header"><span class="rbl">阶段名</span><span class="rbt">时间</span></div>
  <div class="rb-goal">目标描述</div>
  <div class="rb-items">具体行动</div>
  <div class="rb-effect">预期效果</div>
</div>
```

## 三天课程卡片

```html
<div class="day-cols">
  <div class="day-card">
    <h5>Day 1 · 主题</h5>
    <div class="ag"><em>上午</em> ...<br><em>下午</em> ...</div>
    <div class="pr">实战：...</div>
  </div>
</div>
```
