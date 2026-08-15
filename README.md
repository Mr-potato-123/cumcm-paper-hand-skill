# 数模 SKILL —— 数学建模竞赛论文写作与全流程辅助

> 与 AI Agent(如 Claude Code 等)配合,在**你的参赛文件夹**里完成数学建模竞赛的建模、求解与论文写作,最终**以 LaTeX 交付论文**(论文.tex + 编译 PDF)。内置获奖优秀论文参考库(OCR 可读版)、论文 LaTeX 模板与目录结构模板。

![CUMCM](https://img.shields.io/badge/适用-国赛%20CUMCM-blue)
![MCM/ICM](https://img.shields.io/badge/适用-美赛%20MCM%2FICM-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

## 📦 这是什么

面向全国大学生数学建模竞赛(CUMCM)、美国大学生数学建模竞赛(MCM/ICM)参赛者的 **Agent Skill**。核心思路:

1. **参赛者把"原始题目、每道题的建模和解答"分文件夹整理好**,在这个文件夹里打开 AI Agent;
2. Skill 指导 Agent 按 **摸底 → 核对建模求解材料 → 论文撰写** 三步工作;
3. 论文按写作规范主干([数模.md](skills/cumcm-paper-hand-skill/数模.md))撰写,**LaTeX 交付**(XeLaTeX 编译零错误,产出 PDF);
4. 写作时参考 [ref/](skills/cumcm-paper-hand-skill/ref/) 的获奖优秀论文——**特意覆盖国赛三大题型**(A 优化 / B 物理 / C 数据),且 B、C 各有一对"同题不同法"对照(详见 [选篇说明](skills/cumcm-paper-hand-skill/ref/README.md))。

### 🖊️ 定位:论文手(Paper Writer)

本技能定位是**论文手**——职责是基于你**已有的建模笔记与求解结果**撰写论文,不重复建模:

- **已有建模/求解时**:Agent 直接采用,不会重新建模、重新求解;你已有的 `建模笔记.md`、`代码/`、`结果/` 就是论文的全部素材;
- **材料缺失时**:Agent 会先问你;若经你同意补做求解,会在交付说明中注明"本次新增求解:…";
- **需要重新建模/求解时**:明确告诉 Agent(如"帮我重新建个模型"),它才会执行完整建模流程。

简单说:建模和编程自己或队友干,论文的活儿交给它。

## 🚀 安装(以 Claude Code 为例)

```bash
git clone https://github.com/Mr-potato-123/cumcm-paper-hand-skill.git

# 方式一: 全局安装(所有项目可用)
cp -r cumcm-paper-hand-skill/skills/cumcm-paper-hand-skill ~/.claude/skills/

# 方式二: 项目级安装(仅当前项目)
cp -r cumcm-paper-hand-skill/skills/cumcm-paper-hand-skill .claude/skills/
```

> 安装的是 `skills/cumcm-paper-hand-skill/` 这个自包含目录——它只包含 SKILL.md 及其引用的全部文件,不会出现"装了但引用文件缺失"的问题。安装后用 `/skills` 确认可见。**无需安装也行**:把 `skills/cumcm-paper-hand-skill/` 整个复制进参赛文件夹,Agent 同样会按 SKILL.md 工作。

## 🎯 使用流程

1. 按 [目录结构模板](skills/cumcm-paper-hand-skill/templates/目录结构模板.md) 建好参赛文件夹:

```
my-mcm-project/
├── 题目/          # 原始题目与附件(不修改)
├── 问题A/         # 建模笔记.md + 代码/ + 结果/ + 解答.md
├── 问题B/
├── 问题C/
├── 论文/          # 最终论文:论文.tex + 论文.pdf
└── 参考资料/
```

2. 在参赛文件夹里打开 AI Agent,说:"帮我做这道数学建模题" / "帮我写数模论文"。
3. Agent 按 SKILL.md 流程工作:摸底 → 逐题建模求解 → 按写作规范主干写论文 → XeLaTeX 编译 → 交付 PDF。

## 📁 仓库结构

```
.
├── README.md                    # 本文件(人向说明)
├── LICENSE
└── skills/                      # 技能本体(自包含,官方 anthropics/skills 同款布局)
    └── cumcm-paper-hand-skill/
        ├── SKILL.md             # 技能入口:触发描述 + 三步工作流 + 检查清单
        ├── 数模.md              # 论文写作规范主干(被 SKILL.md 引用)
        ├── templates/           # 模板
        │   ├── 论文模板.tex     # 论文唯一模板(XeLaTeX,交付 .tex + PDF)
        │   ├── 论文模板.pdf     # 模板编译预览(无 TeX 也能看效果)
        │   ├── 建模笔记模板.md  # 每题建模笔记模板
        │   ├── 目录结构模板.md  # 参赛文件夹结构模板
        │   └── README.md
        ├── ref/                 # 获奖优秀论文(原 PDF + OCR 可读版,含选篇说明)
        └── scripts/
            └── ocr_pdfs.py      # 图片型 PDF → Markdown 可读版(添加新参考论文用)
```

## ✍️ 论文写作规范(主干)

- **结构骨架**:摘要 → 问题重述 → 问题分析 → 模型假设 → 符号说明 → 模型建立与求解 → 模型评价与推广 → 参考文献 → 附录
- **每问闭环**:问题分析 → 模型建立 → 模型求解 → 结果分析 → 小结;子问题间必须有承接
- **摘要技法**:最后写,每问"针对…问题,首先…,建立…模型,采用…算法求解,得到…结果;通过…检验",直接写数值
- **结果可信**:误差分析、残差分析、交叉验证、敏感性分析、多模型对比
- 完整规范见 [数模.md](skills/cumcm-paper-hand-skill/数模.md),Agent 写论文前须完整读取并逐条执行

## 📖 参考论文怎么用

`ref/` 的获奖论文是**图片型 PDF**(无文字层),每篇都附带 OCR 生成的 `*.md` 可读版。Agent 写作时:学习其摘要写法、章节结构、图表设计,**只学不抄**。选篇逻辑(三种题型覆盖 + 同题双篇对照)与逐篇学习点见 [ref/README.md](skills/cumcm-paper-hand-skill/ref/README.md)。添加自己的论文:运行 [ocr_pdfs.py](skills/cumcm-paper-hand-skill/scripts/ocr_pdfs.py)。

## ⚠️ 说明

- OCR 版论文由自动识别生成,公式、上下标可能有误差,仅供通读;原 PDF 为准。
- 本技能提供的是**写作规范与工作流程**,论文内容与建模结果的真实性由使用者负责。

## 📄 License

MIT
