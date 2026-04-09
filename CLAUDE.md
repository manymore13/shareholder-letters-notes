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
│   │   │   └── letters/   # Letter summaries
│   │   ├── munger/        # Charlie Munger
│   │   │   ├── index.md
│   │   │   └── wesco/
│   │   └── duan/          # Duan Yongping (reserved)
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
│   ├── pdfs/              # PDF preview pages
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
- Sources/Letters: `source-buffett-letters-YYYY.md`

## Standard Markdown Links

Use standard Markdown link format with relative paths:

### Link Format
```markdown
[Display Text](relative-path)
```

### Relative Path Rules
- From `docs/people/buffett/letters/*.md`:
  - To concepts: `../../knowledge/concepts/concept-name.md`
  - To entities: `../../knowledge/entities/entity-name.md`
- From `docs/knowledge/concepts/*.md`:
  - To entities: `../entities/entity-name.md`
  - To letters: `../../people/buffett/letters/source-buffett-letters-YYYY.md`
- From `docs/knowledge/entities/*.md`:
  - To concepts: `../concepts/concept-name.md`
  - To letters: `../../people/buffett/letters/source-buffett-letters-YYYY.md`

## Core Operations

### 1. Ingest Operation

When user adds documents to `raw/`:

1. **Read and analyze** the source document
2. **Identify key entities** (people, organizations, projects, tools, etc.)
3. **Extract concepts** (ideas, theories, methods, frameworks)
4. **Create content in docs/**:
   - For Buffett letters: `docs/people/buffett/letters/source-buffett-letters-YYYY.md`
   - For Munger letters: `docs/people/munger/wesco/source-wesco-letter-YYYY.md`
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
4. Create docs/people/buffett/letters/source-buffett-letters-2024.md
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

## Page Templates

Refer to templates in `templates/` directory for consistent structure:
- `templates/entity.md`: For people, organizations, companies
- `templates/concept.md`: For ideas, theories, methods, frameworks
- `templates/source.md`: For document summaries

Always use templates when creating new pages to maintain consistency.

## Important Notes

1. **Never modify raw/ files** - They are immutable sources
2. **Output directly to docs/** - No intermediate wiki layer
3. **Always update cross-references** when creating new pages
4. **Log all operations** in log.md with timestamps
5. **Use English filenames** for URL compatibility
6. **Maintain YAML frontmatter** in source files for metadata

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

### Source/Letter Pages (`docs/people/*/letters/`)
Summarize source documents:
- Annual shareholder letters
- Speeches and talks
- Articles and blog posts

## Adding New People

To add a new person (e.g., Benjamin Graham):

1. Create `docs/people/graham/index.md`
2. Create `docs/people/graham/letters/` or appropriate subdirectory
3. Update `docs/people/index.md` to include the new person
4. Update `mkdocs.yml` navigation if needed
5. Place source documents in `raw/` and request ingestion

## Quality Standards

1. **Accuracy**: Verify facts from source documents
2. **Completeness**: Extract all relevant information
3. **Consistency**: Follow naming conventions and templates
4. **Connectivity**: Maintain rich cross-references
5. **Clarity**: Write clear, concise summaries in Chinese

---

This schema guides all wiki operations. Follow it consistently to maintain a high-quality knowledge base.
