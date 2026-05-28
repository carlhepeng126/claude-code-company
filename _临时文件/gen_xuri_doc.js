const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, BorderStyle, WidthType,
  ShadingType, VerticalAlign, PageNumber
} = require("docx");

const FONT_BODY = "FangSong";
const FONT_HEAD = "SimHei";
const SIZE_BODY = 28;
const SIZE_H1 = 44;
const SIZE_H2 = 32;
const SIZE_H3 = 28;
const SIZE_TITLE = 52;
const SIZE_SUBTITLE = 36;
const SIZE_TABLE = 20;
const LINE_SPACING = 520;
const FIRST_INDENT = 560;
const MARGIN = 1440;

const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "999999" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };

function bodyPara(text, opts = {}) {
  return new Paragraph({
    spacing: { line: LINE_SPACING, lineRule: "exact", before: opts.before || 0, after: opts.after || 0 },
    indent: opts.noIndent ? {} : { firstLine: FIRST_INDENT },
    alignment: opts.align || AlignmentType.JUSTIFIED,
    children: [new TextRun({ text, font: FONT_BODY, size: opts.size || SIZE_BODY, bold: opts.bold || false })],
  });
}

function heading1(text) {
  return new Paragraph({
    spacing: { line: LINE_SPACING, lineRule: "exact", before: 400, after: 200 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text, font: FONT_HEAD, size: SIZE_H1, bold: true })],
  });
}

function heading3(text) {
  return new Paragraph({
    spacing: { line: LINE_SPACING, lineRule: "exact", before: 200, after: 100 },
    children: [new TextRun({ text, font: FONT_HEAD, size: SIZE_H3, bold: true })],
  });
}

function emptyLine() {
  return new Paragraph({
    spacing: { line: LINE_SPACING, lineRule: "exact" },
    children: [new TextRun({ text: "", font: FONT_BODY, size: SIZE_BODY })],
  });
}

function cellPara(text, opts = {}) {
  return new Paragraph({
    spacing: { line: 300, lineRule: "exact", before: 50, after: 50 },
    alignment: opts.align || AlignmentType.LEFT,
    children: [new TextRun({ text, font: FONT_BODY, size: SIZE_TABLE, bold: opts.bold || false, color: opts.color || "000000" })],
  });
}

function makeCell(text, opts = {}) {
  const children = Array.isArray(text) ? text : [cellPara(text, opts)];
  return new TableCell({
    borders: cellBorders,
    width: opts.width ? { size: opts.width, type: WidthType.DXA } : undefined,
    shading: opts.shading ? { fill: opts.shading, type: ShadingType.CLEAR } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    children,
  });
}

function makeRow(cells, header = false) {
  return new TableRow({ tableHeader: header, children: cells });
}

const LQ = "“"; // "
const RQ = "”"; // "
const LQ2 = "「"; // 「
const RQ2 = "」"; // 」

// Cover
const coverPage = [
  emptyLine(), emptyLine(), emptyLine(), emptyLine(), emptyLine(),
  new Paragraph({
    spacing: { line: 600, lineRule: "exact", after: 200 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: `${LQ2}旭日领导力发展项目${RQ2}`, font: FONT_HEAD, size: SIZE_TITLE, bold: true, color: "C04000" })],
  }),
  new Paragraph({
    spacing: { line: 600, lineRule: "exact", after: 100 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: `新晋项目经理三年培养品牌方案`, font: FONT_HEAD, size: SIZE_SUBTITLE, bold: true })],
  }),
  emptyLine(),
  new Paragraph({
    spacing: { line: LINE_SPACING, lineRule: "exact", after: 100 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: `旭日点将  ${"→"}  旭日出征  ${"→"}  旭日凯旋`, font: FONT_BODY, size: 32, color: "666666" })],
  }),
  emptyLine(), emptyLine(), emptyLine(),
  new Paragraph({
    spacing: { line: LINE_SPACING, lineRule: "exact" },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: `摩根世纪  ${"×"}  当升科技`, font: FONT_BODY, size: SIZE_H3 })],
  }),
  new Paragraph({
    spacing: { line: LINE_SPACING, lineRule: "exact" },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: `2026年5月`, font: FONT_BODY, size: SIZE_BODY, color: "999999" })],
  }),
];

// Main
const mainContent = [

  heading1(`一、品牌概述`),
  bodyPara(`${LQ2}旭日领导力发展项目${RQ2}是摩根世纪为当升科技量身打造的新晋项目经理三年培养品牌。项目以${LQ}旭日${RQ}为核心意象，以${LQ}点将→出征→凯旋${RQ}为成长主线，三年三步，一步一个品牌，帮助新晋项目经理完成从${LQ}业务能手${RQ}到${LQ}胜任管理者${RQ}再到${LQ}能打胜仗的将才${RQ}的完整蜕变。`),
  bodyPara(`品牌名取意于当升科技${LQ}旭日东升${RQ}之名。${LQ}旭日${RQ}既是当升的文化基因，也是新晋管理者成长的最佳隐喻——从黎明破晓到烈日当空，从被选中到打胜仗，每一步都对应一种真实的管理者成长状态。`),

  heading1(`二、命名渊源`),
  bodyPara(`本项目品牌命名取意于当升科技企业名称——${LQ}当升${RQ}即${LQ}旭日东升${RQ}。以${LQ}旭日${RQ}命名的培训品牌，天然嵌入当升的文化基因。`),
  bodyPara(`${LQ}旭日${RQ}——正气、上升、照亮他人。太阳意象天然契合央企${LQ}排头兵${RQ}${LQ}奋进${RQ}${LQ}创新${RQ}的人才发展理念。项目经理不是被教出来的，而是经历黑夜、穿过破晓、最终高悬当空的。`),

  heading1(`三、三年三阶品牌架构`),
  bodyPara(`${LQ}旭日领导力发展项目${RQ}包含三个独立且连续的子品牌，对应三年的能力成长阶梯：`, { noIndent: true }),

  new Table({
    columnWidths: [2000, 2800, 2200, 2360],
    rows: [
      makeRow([
        makeCell(`阶段`, { bold: true, shading: "C04000", color: "FFFFFF", width: 2000, align: AlignmentType.CENTER }),
        makeCell(`品牌核心`, { bold: true, shading: "C04000", color: "FFFFFF", width: 2800, align: AlignmentType.CENTER }),
        makeCell(`学员状态`, { bold: true, shading: "C04000", color: "FFFFFF", width: 2200, align: AlignmentType.CENTER }),
        makeCell(`核心问题`, { bold: true, shading: "C04000", color: "FFFFFF", width: 2360, align: AlignmentType.CENTER }),
      ], true),
      makeRow([
        makeCell(`第1年\n旭日点将`, { bold: true, width: 2000, align: AlignmentType.CENTER }),
        makeCell([cellPara(`站上点将台`, { bold: true }), cellPara(`从人群中被选中，从技术骨干到管理者`, { size: 18, color: "666666" })], { width: 2800 }),
        makeCell(`被选中，既兴奋又不安`, { width: 2200 }),
        makeCell(`凭什么选我？`, { width: 2360, align: AlignmentType.CENTER }),
      ]),
      makeRow([
        makeCell(`第2年\n旭日出征`, { bold: true, width: 2000, align: AlignmentType.CENTER }),
        makeCell([cellPara(`带兵上战场`, { bold: true }), cellPara(`走出舒适区，在真实战场上带队攻坚`, { size: 18, color: "666666" })], { width: 2800 }),
        makeCell(`在现场，真刀真枪干`, { width: 2200 }),
        makeCell(`凭什么跟我走？`, { width: 2360, align: AlignmentType.CENTER }),
      ]),
      makeRow([
        makeCell(`第3年\n旭日凯旋`, { bold: true, width: 2000, align: AlignmentType.CENTER }),
        makeCell([cellPara(`带着战功回来`, { bold: true }), cellPara(`项目交付，方法论沉淀，培养下一代`, { size: 18, color: "666666" })], { width: 2800 }),
        makeCell(`独立操盘，沉淀战功`, { width: 2200 }),
        makeCell(`凭什么记住我？`, { width: 2360, align: AlignmentType.CENTER }),
      ]),
    ],
  }),
  emptyLine(),

  heading1(`四、旭日点将 — 第1年：站上点将台`),
  bodyPara(`${LQ}点将${RQ}取自古代拜将台——真正的将军不是自己站上去的，是被组织${LQ}点${RQ}上去的。第1年的核心主题是身份转化。`),
  heading3(`学员画像`),
  bodyPara(`刚从技术/业务岗位被选拔为新晋管理者，管理经验0–2年。最大的心理状态是${LQ}为什么选我？我准备好了吗？${RQ}。这个阶段不急于给工具，先完成心智上的转身。`),
  heading3(`能力焦点`),
  bodyPara(`角色转身（从${LQ}把事做好${RQ}到${LQ}通过他人把事做好${RQ}）、自我认知（管理风格、优势与盲区）、管理基本功（目标拆解、绩效管理基础、基本管理语言）。`),
  heading3(`关键产出`),
  bodyPara(`个人发展计划（IDP）、管理者角色认知报告、目标拆解与绩效管理基础工具。`),

  heading1(`五、旭日出征 — 第2年：带兵上战场`),
  bodyPara(`${LQ}出征${RQ}是组织对项目经理最郑重的一步——你不再是学员，你是扛旗的人。第2年的核心主题是带队实战。`),
  heading3(`学员画像`),
  bodyPara(`已度过身份焦虑期，进入真实的管理困境——团队冲突、跨部门推诿、资源不足、绩效压力。${LQ}凭什么跟我走？我怎么让别人愿意被我带领？${RQ}`),
  heading3(`能力焦点`),
  bodyPara(`带队实战（授权赋能、绩效面谈、冲突管理）、跨部门协同（打通部门墙、向上管理）、复盘方法论（从${LQ}工作总结${RQ}到${LQ}系统复盘${RQ}的能力跃迁）。`),
  heading3(`关键产出`),
  bodyPara(`团队绩效突破成果、行动学习课题中期报告、复盘方法论实战应用记录。`),

  heading1(`六、旭日凯旋 — 第3年：带着战功回来`),
  bodyPara(`${LQ}凯旋${RQ}不是结束，而是新的起点。第3年的核心主题是沉淀与传承——你能给组织留下什么？`),
  heading3(`学员画像`),
  bodyPara(`已能独立操盘项目，具备经营思维和风险决策能力。开始思考${LQ}我能带出下一个谁？${RQ}。从被培养者转变为培养者。`),
  heading3(`能力焦点`),
  bodyPara(`海外项目独立操盘（属地团队管理、合同风控、跨文化沟通）、经营思维（从${LQ}交付项目${RQ}到${LQ}经营项目${RQ}）、方法论沉淀与人才输出（案例库建设、带新人PM）。`),
  heading3(`关键产出`),
  bodyPara(`当升项目管理案例库、至少带出1–2名新晋PM、结业答辩与${LQ}旭日认证项目经理${RQ}授予。`),

  heading1(`七、与当升领导力建设三年行动嵌套`),
  bodyPara(`${LQ}旭日领导力发展项目${RQ}的三阶段设计与当升科技${LQ}领导力建设三年行动（2026–2028）${RQ}天然对应：`, { noIndent: true }),

  new Table({
    columnWidths: [2800, 3300, 3260],
    rows: [
      makeRow([
        makeCell(`当升三年行动`, { bold: true, shading: "C04000", color: "FFFFFF", width: 2800, align: AlignmentType.CENTER }),
        makeCell(`旭日阶段`, { bold: true, shading: "C04000", color: "FFFFFF", width: 3300, align: AlignmentType.CENTER }),
        makeCell(`学员视角`, { bold: true, shading: "C04000", color: "FFFFFF", width: 3260, align: AlignmentType.CENTER }),
      ], true),
      makeRow([
        makeCell(`2026 夯基固本`, { width: 2800, align: AlignmentType.CENTER }),
        makeCell(`旭日点将（被选中、转身）`, { width: 3300 }),
        makeCell(`${LQ}我被点了${RQ}`, { width: 3260 }),
      ]),
      makeRow([
        makeCell(`2027 深化提升`, { width: 2800, align: AlignmentType.CENTER }),
        makeCell(`旭日出征（上战场、带队）`, { width: 3300 }),
        makeCell(`${LQ}我在路上${RQ}`, { width: 3260 }),
      ]),
      makeRow([
        makeCell(`2028 全面跃升`, { width: 2800, align: AlignmentType.CENTER }),
        makeCell(`旭日凯旋（沉淀战功、带新人）`, { width: 3300 }),
        makeCell(`${LQ}我打完了，我带新人${RQ}`, { width: 3260 }),
      ]),
    ],
  }),
  bodyPara(`两个框架的嵌套关系可在客户汇报中快速呈现——一页双重嵌套图，客户直接认领。`, { before: 100 }),

  heading1(`八、品牌仪式体系`),
  bodyPara(`三年三阶对应三个标志性仪式，让品牌不只是名称，而是学员生命中可感知的时刻：`),
  heading3(`点将仪式（第1年开营）`),
  bodyPara(`学员签署承诺书、直线上级授章、董事长见证。这一刻，他不再只是${LQ}技术骨干${RQ}，他是被组织正式点了将的人。`),
  heading3(`出征仪式（第2年开营）`),
  bodyPara(`学员带领团队接受一项真实业务攻坚任务，向管理层做战前汇报。这一刻，他从${LQ}学员${RQ}变成${LQ}指挥官${RQ}，带着旗帜出发。`),
  heading3(`凯旋仪式（第3年结业）`),
  bodyPara(`学员述职答辩、展示三年战功、授予${LQ}旭日认证项目经理${RQ}。同时担任下一届${LQ}点将仪式${RQ}的见证嘉宾——从被点将到点将别人，品牌完成自循环。`),

  heading1(`九、品牌视觉方向（示意）`),
  bodyPara(`${LQ}旭日${RQ}系列为三年三阶配备了差异化的视觉系统：`, { noIndent: true }),

  new Table({
    columnWidths: [2000, 2460, 2450, 2450],
    rows: [
      makeRow([
        makeCell(`维度`, { bold: true, shading: "C04000", color: "FFFFFF", width: 2000, align: AlignmentType.CENTER }),
        makeCell(`旭日点将（第1年）`, { bold: true, shading: "F5E6D3", width: 2460, align: AlignmentType.CENTER }),
        makeCell(`旭日出征（第2年）`, { bold: true, shading: "F5E6D3", width: 2450, align: AlignmentType.CENTER }),
        makeCell(`旭日凯旋（第3年）`, { bold: true, shading: "F5E6D3", width: 2450, align: AlignmentType.CENTER }),
      ], true),
      makeRow([
        makeCell(`主色调`, { bold: true, width: 2000 }),
        makeCell(`晨曦蓝 · 破晓鱼肚白`, { width: 2460 }),
        makeCell(`朝阳橙 · 日出金`, { width: 2450 }),
        makeCell(`正午红 · 烈日赤`, { width: 2450 }),
      ]),
      makeRow([
        makeCell(`核心符号`, { bold: true, width: 2000 }),
        makeCell(`地平线 + 将印`, { width: 2460 }),
        makeCell(`上升旭日 + 旗帜`, { width: 2450 }),
        makeCell(`当空烈日 + 勋章`, { width: 2450 }),
      ]),
      makeRow([
        makeCell(`仪式道具`, { bold: true, width: 2000 }),
        makeCell(`${LQ}将印${RQ}徽章`, { width: 2460 }),
        makeCell(`${LQ}在路上${RQ}臂章`, { width: 2450 }),
        makeCell(`${LQ}旭日认证${RQ}证书框`, { width: 2450 }),
      ]),
    ],
  }),

  heading1(`十、下一步建议`),
  bodyPara(`品牌概念确认后，建议按以下优先级推进：`),
  bodyPara(`1. 向当升科技管理层汇报「旭日领导力发展项目」品牌概念，收集反馈并确认方向。`),
  bodyPara(`2. 对接当升现有新晋经理培训方案，完成三年三阶段详细能力地图与课程模块设计。`),
  bodyPara(`3. 设计「点将仪式」详细SOP——这是品牌第一次与学员（57人）和客户管理层见面，开场即定调。`),
  bodyPara(`4. 开发品牌视觉识别系统（Logo、主色调方案、仪式物料设计稿）。`),
  bodyPara(`5. 编写摩根内部团队销售话术——如何在30秒内讲清「旭日点将→出征→凯旋」。`),
  emptyLine(),
  emptyLine(),

  new Paragraph({
    spacing: { line: LINE_SPACING, lineRule: "exact", before: 200 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: `摩根世纪  ·  2026年5月  ·  内部资料`, font: FONT_BODY, size: 20, color: "999999" })],
  }),
];

// Build
const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT_BODY, size: SIZE_BODY } } },
  },
  sections: [
    {
      properties: { page: { margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN } } },
      children: coverPage,
    },
    {
      properties: { page: { margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN } } },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [new TextRun({ text: `旭日领导力发展项目 · 品牌方案`, font: FONT_BODY, size: 18, color: "999999" })],
          })],
        }),
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({ text: `摩根世纪  |  内部资料  |  `, font: FONT_BODY, size: 16, color: "999999" }),
              new TextRun({ children: [PageNumber.CURRENT], font: FONT_BODY, size: 16, color: "999999" }),
            ],
          })],
        }),
      },
      children: mainContent,
    },
  ],
});

const outPath = `C:/Users/Admin/Documents/LLM Wiki/_临时文件/旭日领导力发展项目-品牌方案.docx`;
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(outPath, buf);
  console.log(`Done: ${outPath}`);
});
