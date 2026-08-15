# 数模 SKILL —— 数学建模竞赛论文写作与全流程辅助

> 与 AI Agent(如 Claude Code / Cursor / Windsurf 等)配合,在**你的参赛文件夹**里完成数学建模竞赛的建模、求解与论文写作。论文写作规范经过实战打磨,内置**获奖优秀论文参考库**(OCR 可读版),并提供**论文模板、建模笔记模板、目录结构模板**。

![CUMCM](https://img.shields.io/badge/适用-国赛%20CUMCM-blue)
![MCM/ICM](https://img.shields.io/badge/适用-美赛%20MCM%2FICM-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

## 📦 这是什么

一个面向全国大学生数学建模竞赛(CUMCM)、美国大学生数学建模竞赛(MCM/ICM)参赛者的 **Agent Skill**。它的核心思路:

1. **参赛者把"原始题目、每道题的建模和解答"分文件夹整理好**,在这个文件夹里打开 AI Agent;
2. Skill 指导 Agent 按 **建模分析 → 代码求解 → 论文撰写** 三阶段工作;
3. 论文按一套完整的**写作规范**产出(结构骨架、逐节写法、过渡衔接、结果呈现、摘要技法);
4. 写作时参考 `ref/` 目录下的**获奖优秀论文**(提供 OCR 可读版,方便 Agent 通读)。

## 🚀 快速开始

### 安装(以 Claude Code 为例)

```bash
# 方式一: 复制到全局技能目录
git clone https://github.com/Mr-potato-123/cumcm-paper-hand-skill.git
cp -r cumcm-paper-hand-skill/SKILL.md cumcm-paper-hand-skill/templates cumcm-paper-hand-skill/ref ~/.claude/skills/cumcm-paper-hand-skill/

# 方式二: 项目级安装(只对当前项目生效)
mkdir -p .claude/skills && cp -r cumcm-paper-hand-skill .claude/skills/cumcm-paper-hand-skill/
```

> 其他支持 skill 机制的 Agent(如 Cursor Rules、Windsurf 等)参考各自文档,把本仓库放到对应 skills 目录即可。**无需安装到全局也行**——把 `SKILL.md`、`templates/`、`ref/` 三个部分直接放进参赛文件夹,Agent 也会按 SKILL.md 的规范工作。
>
> 📌 仓库地址: [github.com/Mr-potato-123/cumcm-paper-hand-skill](https://github.com/Mr-potato-123/cumcm-paper-hand-skill)

### 使用流程

1. **建文件夹**:复制 `templates/目录结构模板.md` 中的结构:

```
my-mcm-project/
├── README.md          # 项目说明
├── 题目/              # 原始题目与附件(不修改)
├── 问题A/             # 建模笔记.md + 代码/ + 结果/ + 解答.md
├── 问题B/
├── 问题C/
├── 论文/              # 最终论文
└── 参考资料/
```

2. **把本仓库的 `SKILL.md`、`templates/`、`ref/` 放进参赛文件夹**(或安装为 skill)。
3. 在文件夹里打开 AI Agent,说:
   - "帮我做这道数学建模题"
   - "帮我写数模论文"
   - "这题的建模思路怎么写"
4. Agent 会按 SKILL.md 的流程工作:先读题目和建模笔记,逐题建模求解,最后按模板与规范写论文。

## 📁 目录结构

```
.
├── SKILL.md            # 核心技能文件:工作流程 + 论文写作规范 + 检查清单
├── README.md           # 本文件
├── templates/          # 模板
│   ├── 论文模板.tex    # 论文唯一模板(XeLaTeX,交付 .tex + PDF)
│   ├── 论文模板.pdf    # 模板编译预览
│   ├── 建模笔记模板.md # 每题建模笔记模板
│   ├── 目录结构模板.md # 参赛文件夹结构模板
│   └── README.md
├── ref/                # 获奖优秀论文(原 PDF + OCR 可读版 Markdown)
│   ├── A196.pdf / A196.md
│   ├── B060.pdf / B060.md
│   ├── B157.pdf / B157.md
│   ├── C023.pdf / C023.md
│   ├── C132.pdf / C132.md
│   └── README.md       # 逐篇说明
└── _tools/
    └── ocr_pdfs.py     # 把图片型 PDF 转为 Markdown(需要 Python)
```

## ✍️ 论文写作规范亮点

- **结构骨架**:摘要 → 问题重述 → 问题分析 → 模型假设 → 符号说明 → 模型建立与求解 → 模型评价与推广 → 参考文献 → 附录
- **每问闭环**:问题分析 → 模型建立 → 模型求解 → 结果分析 → 小结
- **叙事逻辑**:子问题之间必须有承接——前问的输出成为后问的输入,后问验证前问
- **摘要技法**:最后写,每问句式"针对…问题,首先…,建立…模型,采用…算法求解,得到…结果;通过…检验,表明模型…",直接写数值不写空话
- **结果可信**:误差分析、残差分析、交叉验证、敏感性分析、多模型对比
- **交付检查清单**:写完论文后逐项自检

## 📖 参考论文怎么用

`ref/` 内置的获奖论文是**图片型 PDF**,AI Agent 无法直接读取文字层,因此每篇都附带 OCR 生成的 `*.md` 可读版。Agent 写作时:

- 学习其**摘要写法、章节结构、图表设计、结果呈现**;
- **只学不抄**:借鉴思路与表达方式,绝不复制原文;
- 需要精确公式/数据时对照原 PDF。

你也可以把自己的参考论文放进 `ref/`(图片型 PDF 可运行 `_tools/ocr_pdfs.py` 生成可读版,需 Python + `rapidocr_onnxruntime`)。

## ⚠️ 说明

- OCR 版论文由自动识别生成,公式、上下标可能有误差,仅供通读参考;原 PDF 为准。
- 本技能提供的是**写作规范与工作流程**,论文内容与建模结果的真实性由使用者负责。

## 📄 License

MIT
