---
name: 个人wiki系统MVP搭建计划
overview: 基于LLM Wiki设计思想，搭建一个简洁的个人wiki系统MVP版本，包含基础目录结构、配置文件、模板和说明文档，支持未来的静态网站扩展能力。
design:
  architecture:
    framework: html
  styleKeywords:
    - Minimal
    - Structured
    - Extensible
  fontSystem:
    fontFamily: Roboto
    heading:
      size: 32px
      weight: 600
    subheading:
      size: 18px
      weight: 500
    body:
      size: 16px
      weight: 400
  colorSystem:
    primary:
      - "#2196F3"
    background:
      - "#FFFFFF"
    text:
      - "#212121"
    functional:
      - "#4CAF50"
      - "#FF9800"
todos:
  - id: create-directory-structure
    content: 创建完整的目录结构（raw、wiki、templates、site）
    status: completed
  - id: create-schema-config
    content: 创建CLAUDE.md Schema配置文件，定义LLM工作流程和规范
    status: completed
    dependencies:
      - create-directory-structure
  - id: create-initial-wiki-files
    content: 创建wiki初始文件（index.md、log.md、about.md）
    status: completed
    dependencies:
      - create-directory-structure
  - id: create-page-templates
    content: 创建三种页面模板（entity.md、concept.md、source.md）
    status: completed
    dependencies:
      - create-directory-structure
  - id: create-readme
    content: 创建README.md系统说明文档
    status: completed
  - id: create-gitkeep
    content: 创建site/.gitkeep占位文件
    status: completed
    dependencies:
      - create-directory-structure
---

## 产品概述

一个基于LLM的个人知识管理系统MVP版本，用户只需添加原始文档到raw目录，LLM自动将知识整理并写入wiki目录，实现知识的累积和交叉引用。系统设计简洁，未来可扩展为静态网站公开分享。

## 核心功能

1. **三层架构**：raw（原始资源）→ wiki（知识内容）→ schema（LLM指令）
2. **四种页面类型**：entities（实体）、concepts（概念）、sources（源文档摘要）、synthesis（综合分析）
3. **核心操作**：ingest（导入）、query（查询）、check（健康检查）
4. **知识累积**：自动维护交叉引用、索引和操作日志
5. **扩展能力**：英文命名、YAML frontmatter占位、静态网站兼容

## 用户价值

- 零维护负担：LLM承担所有整理工作
- 知识复利增长：每次添加新内容都让wiki更丰富
- Obsidian实时查看：使用Obsidian浏览和查看知识网络
- 未来可发布：预留静态网站扩展能力

## 技术栈

- **文件格式**：Markdown（纯文本，无需编译）
- **浏览工具**：Obsidian（推荐）或任何Markdown编辑器
- **维护工具**：LLM Agent（Claude Code / ChatGPT等）
- **版本控制**：Git（可选）
- **未来扩展**：VitePress / Hugo（静态网站生成）

## 实现方案

### 架构设计

采用纯文件系统架构，无需数据库或后端服务。所有内容以Markdown文件形式存储，天然支持Git版本控制和静态网站发布。

### 三层架构详解

1. **Raw层（原始资源）**：用户提供的源文档，不可变，作为事实来源
2. **Wiki层（知识内容）**：LLM维护的结构化内容，支持双向链接和交叉引用
3. **Schema层（配置指令）**：指导LLM如何工作的配置文件

### 核心文件设计

- **CLAUDE.md**：Schema配置，定义LLM的角色、工作流程、命名规范
- **wiki/index.md**：内容索引，按类别组织所有页面
- **wiki/log.md**：操作日志，仅追加的时间线记录
- **templates/**：页面模板，保持内容结构一致性

### 扩展性设计

- 文件命名使用英文（URL友好）
- YAML frontmatter以注释形式占位
- raw/和log.md明确标注为不发布内容
- 目录结构映射未来网站导航

## 性能与可靠性

- 文件级操作，无性能瓶颈
- 基于Git的版本历史，可随时回滚
- 纯文本格式，永不过时
- 无外部依赖，系统极其稳定

## 注意事项

- LLM摄入时需确认关键信息，避免错误分类
- 定期进行健康检查，发现孤立页面和矛盾信息
- 重要修改前建议Git提交，便于回滚

## 设计理念

本系统是一个纯文件结构的知识管理系统，不涉及UI界面开发。设计重点是清晰的目录结构、规范的文件命名和完整的内容模板。

## 目录结构设计

```
personal-wiki/
├── CLAUDE.md              # Schema配置（指导LLM工作）
├── README.md              # 系统说明文档
├── site/                  # 预留：静态网站配置
│   └── .gitkeep
├── raw/                   # 原始资源（私有，不发布）
│   ├── articles/          # 文章
│   │   ├── markdown/
│   │   ├── pdf/
│   │   └── html/
│   ├── papers/            # 论文
│   │   ├── pdf/
│   │   └── notes/
│   ├── notes/             # 个人笔记
│   │   ├── journal/
│   │   ├── meeting/
│   │   └── ideas/
│   ├── media/             # 媒体资源
│   │   ├── images/
│   │   ├── audio/
│   │   └── transcripts/
│   ├── data/              # 数据文件
│   │   ├── csv/
│   │   └── json/
│   └── books/             # 书籍
│       ├── pdf/
│       └── highlights/
├── wiki/                  # 知识内容（未来可发布）
│   ├── index.md           # 内容索引
│   ├── log.md             # 操作日志（私有）
│   ├── about.md           # 关于页面
│   ├── entities/          # 实体页面
│   ├── concepts/          # 概念页面
│   ├── sources/           # 源文档摘要
│   └── synthesis/         # 综合分析
└── templates/             # 页面模板
    ├── entity.md
    ├── concept.md
    └── source.md
```

## 文件命名规范

- 使用小写英文和连字符：`machine-learning-basics.md`
- 实体：`entity-[name].md`
- 概念：`concept-[name].md`
- 源文档：`source-[YYYY-MM-DD]-[short-title].md`
- 综合：`synthesis-[topic].md`

## 双向链接格式

采用Obsidian兼容格式：`[[page-name]]`
未来转换为静态网站时可通过脚本批量转换为标准链接。