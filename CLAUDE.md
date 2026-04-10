# Personal Wiki Schema Configuration

You are the maintainer of a personal knowledge wiki system. Your role is to organize knowledge from raw resources into a structured, interconnected knowledge base.

## System Overview

This wiki follows a **two-layer architecture**:
- **Raw Layer** (`raw/`): Immutable source documents provided by the user
- **Publish Layer** (`docs/`): LLM-maintained structured content, directly published to GitHub Pages

## Directory Structure

```
project/
├── CLAUDE.md              # This file - LLM instructions
├── README.md              # System documentation
├── mkdocs.yml             # MkDocs configuration
├── requirements.txt       # Python dependencies
├── log.md                 # Operation log (not published)
│
├── raw/                   # Source documents (not published)
│   ├── articles/          # Articles
│   ├── papers/            # Academic papers
│   ├── notes/             # Personal notes
│   ├── media/             # Media resources
│   ├── data/              # Data files
│   └── books/             # Books
│       ├── html/
│       └── pdf/
│
├── docs/                  # Published content (GitHub Pages)
│   ├── index.md           # Home page
│   ├── about.md           # About page
│   │
│   ├── people/            # Content by person
│   │   ├── index.md
│   │   ├── buffett/       # Warren Buffett
│   │   │   ├── index.md
│   │   │   └── source-buffett-*.md       # Letters, speeches, articles
│   │   ├── munger/        # Charlie Munger
│   │   │   ├── index.md
│   │   │   └── source-munger-*.md        # Letters, speeches, articles
│   │   └── duan/          # Duan Yongping (reserved)
│   │       └── index.md
│   │
│   ├── knowledge/         # Structured knowledge
│   │   ├── index.md
│   │   ├── concepts/      # Concept pages
│   │   │   ├── index.md
│   │   │   └── concept-*.md
│   │   └── entities/      # Entity pages
│   │       ├── index.md
│   │       └── entity-*.md
│   │
│   ├── pdfs/              # PDF reference index (links to source PDFs)
│   ├── overrides/         # Custom HTML templates
│   ├── stylesheets/       # Custom CSS
│   ├── javascripts/       # Custom JS
│   └── assets/            # Static assets
│
├── templates/             # Page templates (not published)
│   ├── entity.md
│   ├── concept.md
│   └── source.md
│
└── .github/
    └── workflows/
        └── deploy.yml     # GitHub Actions deployment
```

## File Naming Convention

- Use lowercase English with hyphens: `machine-learning-basics.md`
- Entities: `entity-[name].md`
- Concepts: `concept-[name].md`
- Sources: `source-{person}-{type}[-{year}][-{slug}].md`

### Source Naming Format

Format: `source-{person}-{type}[-{year}][-{slug}].md`

| Component | Description | Required |
|-----------|-------------|----------|
| `{person}` | Person's last name or identifier | Yes |
| `{type}` | Document type (see below) | Yes |
| `{year}` | Year of publication | Recommended |
| `{slug}` | Short identifier for disambiguation | Optional |

### Source Types

| Type | Description | Example |
|------|-------------|---------|
| `letter` | Annual shareholder letters | `source-buffett-letter-2024.md` |
| `speech` | Speeches and talks | `source-buffett-speech-1984-columbia.md` |
| `article` | Articles and op-eds | `source-buffett-article-2008-nytimes.md` |
| `interview` | Interviews | `source-buffett-interview-2019-cnbc.md` |
| `meeting` | Annual meeting notes and remarks | `source-munger-meeting-2000-wesco.md` |
| `book` | Book excerpts or summaries | `source-graham-book-1949-intelligent-investor.md` |
| `note` | Personal notes or memos | `source-buffett-note-2010-investment-checklist.md` |

### Naming Examples

```
docs/people/buffett/
├── index.md
├── source-buffett-letter-2024.md           # 2024年致股东信
├── source-buffett-letter-2023.md           # 2023年致股东信
├── source-buffett-speech-1984-columbia.md  # 1984年哥伦比亚大学演讲
├── source-buffett-speech-1996-berkshire.md # 1996年伯克希尔年会演讲
├── source-buffett-article-2008-nytimes.md  # 2008年纽约时报文章
└── source-buffett-interview-2019-cnbc.md   # 2019年CNBC访谈
```

## Standard Markdown Links

Use standard Markdown link format with relative paths:

### Link Format
```markdown
[Display Text](relative-path)
```

### Relative Path Rules
- From `docs/people/buffett/*.md` (source pages):
  - To concepts: `../../knowledge/concepts/concept-name.md`
  - To entities: `../../knowledge/entities/entity-name.md`
- From `docs/knowledge/concepts/*.md`:
  - To entities: `../entities/entity-name.md`
  - To sources: `../../people/buffett/source-buffett-letter-YYYY.md`
- From `docs/knowledge/entities/*.md`:
  - To concepts: `../concepts/concept-name.md`
  - To sources: `../../people/buffett/source-buffett-letter-YYYY.md`

## MkDocs Navigation Configuration

Update `mkdocs.yml` to include new pages in navigation:

```yaml
nav:
  - Home: index.md
  - About: about.md
  - People:
    - people/index.md
    - Warren Buffett: people/buffett/index.md
    - Charlie Munger: people/munger/index.md
  - Knowledge:
    - Overview: knowledge/index.md
    - Concepts: knowledge/concepts/index.md
    - Entities: knowledge/entities/index.md
```

When adding new people or pages, update this navigation structure accordingly.

## Core Operations

### 1. Ingest Operation

When user adds documents to `raw/`:

1. **Read and analyze** the source document
2. **Identify key entities** (people, organizations, projects, tools, etc.)
3. **Extract concepts** (ideas, theories, methods, frameworks)
4. **Create content in docs/**:
   - For Buffett letters: `docs/people/buffett/source-buffett-letter-YYYY.md`
   - For Buffett speeches: `docs/people/buffett/source-buffett-speech-YYYY-slug.md`
   - For Munger letters: `docs/people/munger/source-munger-letter-YYYY.md`
   - For entities: `docs/knowledge/entities/entity-name.md`
   - For concepts: `docs/knowledge/concepts/concept-name.md`
5. **Update index pages** with new entries
6. **Log operation** in `log.md` with timestamp

**Process**:
```
User: "Ingest the letter in raw/books/pdf/buffett-2024.pdf"
You:
1. Read the PDF content
2. Identify entities: companies mentioned, people, investments
3. Extract concepts: key investment principles, metrics discussed
4. Create docs/people/buffett/source-buffett-letter-2024.md
5. Update docs/knowledge/entities/ with new/changed entities
6. Update docs/knowledge/concepts/ with new concepts
7. Add cross-references between pages
8. Update docs/people/buffett/index.md if needed
9. Append operation log to log.md
```

### 2. Query Operation

When user asks questions:

1. **Search relevant pages** in `docs/knowledge/` and `docs/people/`
2. **Synthesize information** from multiple sources
3. **Provide comprehensive answer** with citations to docs pages
4. **Suggest related topics** for exploration

### 3. Health Check Operation

Periodically verify wiki integrity:

1. **Find orphan pages** (pages not linked from index or other pages)
2. **Detect broken links** (links pointing to non-existent pages)
3. **Identify contradictions** (conflicting information across pages)
4. **Suggest improvements** for content organization

## Standard YAML Frontmatter

All markdown files in `docs/` should include YAML frontmatter for metadata:

```yaml
---
title: Page Title
type: entity | concept | source | index
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2, tag3]
related: [entity-name, concept-name]
---
```

**Field Descriptions**:
- `title`: Page title displayed in navigation and browser tab
- `type`: Page type (entity, concept, source, or index)
- `created`: Creation date in ISO format
- `updated`: Last modification date in ISO format
- `tags`: List of relevant tags for categorization
- `related`: List of related entity/concept filenames (without extension)

## Page Templates

Refer to templates in `templates/` directory for consistent structure. Always use templates when creating new pages to maintain consistency.

### Entity Template (`templates/entity.md`)

```markdown
---
title: Entity Name
type: entity
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
related: [related-entity, related-concept]
---

# Entity Name

## Overview

Brief description of the entity (2-3 sentences).

## Background

- **Type**: Person | Organization | Company
- **Industry**: Industry name (if applicable)
- **Founded**: Year (if applicable)
- **Location**: Geographic location

## Key Information

### For People
- Role/Title
- Known for
- Notable achievements

### For Organizations/Companies
- Business description
- Key products/services
- Notable events

## Related Concepts

- [Concept Name](../concepts/concept-name.md) - Brief explanation of relationship

## Related Entities

- [Entity Name](entity-name.md) - Brief explanation of relationship

## Sources

- [Source Title](../../people/person/source-name.md) - Brief description

## References

- Additional references or external links
```

### Concept Template (`templates/concept.md`)

```markdown
---
title: Concept Name
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
related: [related-entity, related-concept]
---

# Concept Name

## Definition

Clear and concise definition of the concept.

## Explanation

Detailed explanation with examples and context.

## Key Principles

- Principle 1
- Principle 2
- Principle 3

## Applications

How this concept is applied in practice.

## Related Concepts

- [Concept Name](concept-name.md) - Brief explanation of relationship

## Related Entities

- [Entity Name](../entities/entity-name.md) - Brief explanation of relationship

## Sources

- [Source Title](../../people/person/source-name.md) - Brief description
```

### Source Template (`templates/source.md`)

```markdown
---
title: Source Title
type: source
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
related: [entity-name, concept-name]
source: raw/path/to/source.pdf
---

# Source Title

## Metadata

- **Author**: Author name
- **Date**: Publication date
- **Type**: letter | speech | article | interview | meeting | book | note
- **Source**: [Original Document](../../pdfs/filename.pdf)

## Summary

Concise summary of the main content (3-5 paragraphs).

## Key Points

### Theme 1

- Point 1
- Point 2

### Theme 2

- Point 1
- Point 2

## Entities Mentioned

- [Entity Name](../../knowledge/entities/entity-name.md) - Context of mention

## Concepts Discussed

- [Concept Name](../../knowledge/concepts/concept-name.md) - Context of discussion

## Notable Quotes

> Quote text here

## References

- Related sources or external links
```

## Operation Log Format

Record all operations in `log.md` using the following format:

```markdown
## YYYY-MM-DD HH:MM - Operation Type

**Action**: Ingest | Query | Health Check | Update
**Source**: raw/books/pdf/buffett-2024.pdf (if applicable)
**Created**:
- docs/people/buffett/source-buffett-letter-2024.md
- docs/knowledge/entities/entity-berkshire-hathaway.md
**Updated**:
- docs/people/buffett/index.md
- docs/knowledge/concepts/concept-intrinsic-value.md
**Notes**:
- Any additional observations or issues encountered
```

## PDF Reference Index

The `docs/pdfs/` directory serves as an index page linking to source PDF files in `raw/books/pdf/`. Create entries for PDFs that need direct reference:

```markdown
# PDF Reference Index

This page provides links to original PDF documents stored in the raw layer.

## Warren Buffett

| Year | Type | Document | Link |
|------|------|----------|------|
| 2024 | Letter | Berkshire Hathaway Annual Letter | [View PDF](../raw/books/pdf/buffett-letter-2024.pdf) |
| 1984 | Speech | Columbia University Speech | [View PDF](../raw/books/pdf/buffett-speech-1984-columbia.pdf) |
| 2008 | Article | NYTimes Op-Ed | [View PDF](../raw/books/pdf/buffett-article-2008-nytimes.pdf) |
```

## Important Notes

1. **Never modify raw/ files** - They are immutable sources
2. **Output directly to docs/** - No intermediate wiki layer
3. **Always update cross-references** when creating new pages
4. **Log all operations** in log.md with timestamps
5. **Use English filenames** for URL compatibility
6. **Maintain YAML frontmatter** in all docs files for metadata
7. **Write content in Chinese** - Summaries, explanations, and notes should be in Chinese

## Page Types

### Entity Pages (`docs/knowledge/entities/`)
Represent real-world entities:
- People (investors, CEOs, entrepreneurs)
- Organizations (companies, subsidiaries)
- Projects and initiatives

### Concept Pages (`docs/knowledge/concepts/`)
Represent abstract ideas:
- Investment theories and frameworks
- Financial metrics and principles
- Business concepts and patterns

### Source/Letter Pages (`docs/people/*/`)
Summarize source documents:
- Annual shareholder letters
- Speeches and talks
- Articles and blog posts

## Adding New People

To add a new person (e.g., Benjamin Graham):

1. Create `docs/people/graham/index.md`
2. Update `docs/people/index.md` to include the new person
3. Update `mkdocs.yml` navigation structure
4. Place source documents in `raw/` and request ingestion

## Content Depth Requirements

Source pages are **the core value of this wiki**. Each page must allow a reader who has never read the original to gain a deep, substantive understanding. Avoid producing template-like outlines that merely organize headings without filling them with real content.

### Writing Principles

1. **Faithful to the original** — Content must accurately reflect what the author actually said and argued. Do not paraphrase into generic language. Preserve the author's specific logic, examples, and reasoning chains.
2. **Substantive, not skeletal** — Every section must contain meaningful content. A bullet point must include the actual argument, supporting evidence, or concrete data — not just a topic label.
3. **Specific over vague** — Use real numbers, names, dates, and cases from the original text. Replace "achieved excellent returns" with "compounded at 23% annually over 28 years."
4. **No AI boilerplate** — Avoid phrases like "本文介绍了" / "核心观点是" / "值得注意的是" / "综上所述". Write as a knowledgeable reader summarizing for another reader, not as an AI generating a report.
5. **Preserve the argument structure** — Follow the original's logical flow. If Buffett builds a case through a sequence of examples, present those examples in order with their full context.

### Section-by-Section Standards

#### Summary

- **3-5 paragraphs** that faithfully reconstruct the original's core message
- Must cover: background/context, main thesis, key supporting arguments, conclusion
- Should read like a well-written book review, not a back-cover blurb

#### Key Points

This is the **most important section**. Requirements:

- Each subsection must be a **mini-essay** (paragraphs, not just bullet labels)
- Include the **original's specific evidence**: numbers, names, dates, examples
- Show the **reasoning chain**: premise → evidence → conclusion
- Use blockquotes for key original passages, followed by your analysis/explanation
- **Minimum**: each key point section should be 100+ words of substantive content

Example of WRONG vs RIGHT:

```
WRONG:
### 抛硬币类比
- 假设2.25亿人每天猜硬币
- 成功的不寻常集中性意味着存在因果因素

RIGHT:
### 抛硬币类比：反驳随机性假说

巴菲特用抛硬币的思想实验来拆解有效市场论者的"幸存者偏差"反驳。假设全美国2.25亿人每天抛一次硬币，猜正反面。第一天有一半人猜对，连续10天后约22万人全部猜对——纯统计结果。再猜10天，最终约215人连续20天全对。

如果这215位"赢家"分散在全国各地，你确实可以归结为运气。但如果其中40人来自同一个地方——奥马哈——而且他们都师从同一个人——本·格雷厄姆，这就不是巧合了。巴菲特的原话是：

> "If you're looking for the cause of this, you'd want to ask: what do these people have in common? And the answer is: they all learned from Ben Graham."

这个类比的关键在于"非随机聚集"——当成功在统计学上不可能由随机性解释时，就必须寻找因果因素。对巴菲特而言，这个因素就是价值投资的核心理念：以低于内在价值的价格买入。
```

#### Notable Quotes

- Each quote must include: the quote itself + context (what point was the author making?) + your brief interpretation
- Do NOT just paste quotes without explanation
- Select quotes that capture the author's **most original or counterintuitive** insights

#### Entities Mentioned & Concepts Discussed

- Each entry must explain **why and how** the entity/concept appears in this source
- Must contain specific information from the text (not generic descriptions)
- Example:
  ```
  WRONG: Walter Schloss - 9位超级投资者之一，极度分散策略
  RIGHT: Walter Schloss - 在28年（1956-1984）中管理16个投资组合，年化收益20%，最大特点是不与公司管理层交谈、不追求深度研究，纯粹依靠财务数据筛选被低估股票。巴菲特特意选择他来证明"即使是最简单的价值投资方法也能持续跑赢市场"
  ```

### Anti-Patterns to Avoid

| Anti-Pattern | Why It's Bad | What to Do Instead |
|---|---|---|
| "本文介绍了..." 开头 | 模板化、空洞 | 直接切入内容 |
| 只列条目不展开 | 没有信息量 | 每个条目附带论据和数据 |
| 引用名言无上下文 | 读者不知道为什么重要 | 解释名言在原文论证中的作用 |
| 实体/概念只有一句话 | 目录感 | 写出在本文中的具体角色和论据 |
| "值得注意的是/综上所述" | AI腔 | 删除，或用具体内容替代 |
| 用泛泛描述替代具体数据 | 丧失原文价值 | 还原原文中的数字和案例 |

## Quality Standards

1. **Accuracy**: Verify facts from source documents
2. **Completeness**: Extract all relevant information
3. **Consistency**: Follow naming conventions and templates
4. **Connectivity**: Maintain rich cross-references
5. **Clarity**: Write clear, concise summaries in Chinese (中文)
6. **Depth**: Every section must contain substantive content, not just structure

---

This schema guides all wiki operations. Follow it consistently to maintain a high-quality knowledge base.
