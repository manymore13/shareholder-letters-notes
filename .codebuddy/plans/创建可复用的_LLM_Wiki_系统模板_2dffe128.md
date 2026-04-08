---
name: 创建可复用的 LLM Wiki 系统模板
overview: 从当前项目提取 wiki 系统核心文件（不包括数据），创建一个可复用的模板系统，保存到 d:/codebuddySpace/llm-wiki-template/
todos:
  - id: create-dirs
    content: 创建目标目录结构（raw子目录、wiki子目录、site）
    status: completed
  - id: copy-system-files
    content: 复制系统文件（CLAUDE.md、llm-wiki.md、llm-wiki-理解.md、README.md、README_zh.md）
    status: completed
    dependencies:
      - create-dirs
  - id: copy-templates
    content: 复制 templates 模板目录
    status: completed
    dependencies:
      - create-dirs
  - id: create-wiki-templates
    content: 创建空白 wiki 模板文件（index.md、log.md、about.md）
    status: completed
    dependencies:
      - create-dirs
  - id: create-gitignore
    content: 创建 .gitignore 文件
    status: completed
  - id: init-git
    content: 初始化 Git 仓库并提交
    status: completed
    dependencies:
      - copy-system-files
      - copy-templates
      - create-wiki-templates
      - create-gitignore
---

## 用户需求

将当前项目的 LLM Wiki 系统模板提取并保存到 `d:/codebuddySpace/llm-wiki-template/`，以便将来复用于其他知识库项目。

## 核心要求

- **复制系统文件**：CLAUDE.md、llm-wiki.md、llm-wiki-理解.md、README.md、README_zh.md、templates/
- **排除数据文件**：raw/、wiki/（已有内容）、temp/、Python 脚本等
- **创建空白模板**：wiki/ 目录下的基础起始文件（index.md、log.md、about.md）
- **创建空目录结构**：raw/ 下的子目录、site/
- **初始化 Git 仓库**：便于版本管理和分发

## 目标结构

```
llm-wiki-template/
├── CLAUDE.md              # 从当前项目复制
├── llm-wiki.md            # 从当前项目复制
├── llm-wiki-理解.md       # 从当前项目复制
├── README.md              # 从当前项目复制
├── README_zh.md           # 从当前项目复制
├── .gitignore             # 新建
├── templates/             # 从当前项目复制
│   ├── concept.md
│   ├── entity.md
│   └── source.md
├── raw/                   # 创建空目录结构
│   ├── articles/
│   ├── papers/
│   ├── notes/
│   ├── media/
│   ├── data/
│   └── books/
├── wiki/                  # 创建空白起始文件
│   ├── index.md
│   ├── log.md
│   ├── about.md
│   ├── entities/
│   ├── concepts/
│   ├── sources/
│   └── synthesis/
└── site/
    └── .gitkeep
```

## 技术方案

简单的文件复制和目录创建操作，不涉及复杂技术栈。

## 实现步骤

1. **创建目标目录结构** - 在 `d:/codebuddySpace/llm-wiki-template/` 下创建完整目录
2. **复制系统文件** - 复制 CLAUDE.md、llm-wiki.md、llm-wiki-理解.md、README.md、README_zh.md
3. **复制模板目录** - 复制 templates/ 整个目录
4. **创建空白 wiki 模板文件** - 创建 index.md、log.md、about.md 的空白模板
5. **创建 .gitignore** - 排除数据文件和临时文件
6. **创建空目录占位** - raw/ 子目录和 site/.gitkeep
7. **初始化 Git 仓库** - git init 并提交

## 文件来源与去向

| 源文件 | 目标位置 | 操作 |
| --- | --- | --- |
| `CLAUDE.md` | `llm-wiki-template/CLAUDE.md` | 复制 |
| `llm-wiki.md` | `llm-wiki-template/llm-wiki.md` | 复制 |
| `llm-wiki-理解.md` | `llm-wiki-template/llm-wiki-理解.md` | 复制 |
| `README.md` | `llm-wiki-template/README.md` | 复制 |
| `README_zh.md` | `llm-wiki-template/README_zh.md` | 复制 |
| `templates/` | `llm-wiki-template/templates/` | 复制整个目录 |
| - | `llm-wiki-template/.gitignore` | 新建 |
| - | `llm-wiki-template/wiki/index.md` | 新建空白模板 |
| - | `llm-wiki-template/wiki/log.md` | 新建空白模板 |
| - | `llm-wiki-template/wiki/about.md` | 新建空白模板 |
| - | `llm-wiki-template/raw/*` | 创建空目录 |
| - | `llm-wiki-template/site/.gitkeep` | 创建占位文件 |