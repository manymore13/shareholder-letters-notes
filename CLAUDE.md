# Personal Wiki Schema Configuration

You are the maintainer of a personal knowledge wiki system. Your role is to organize knowledge from raw resources into a structured, interconnected knowledge base.

## System Overview

This wiki follows a three-layer architecture:
- **Raw Layer** (`raw/`): Immutable source documents provided by the user
- **Wiki Layer** (`wiki/`): LLM-maintained structured content with bidirectional links
- **Schema Layer** (`CLAUDE.md`): Instructions for LLM operation

## Directory Structure

```
personal-wiki/
├── CLAUDE.md              # This file - LLM instructions
├── README.md              # System documentation
├── site/                  # Reserved for static site configuration
│   └── .gitkeep
├── raw/                   # Source documents (private, not published)
│   ├── articles/          # Articles
│   │   ├── markdown/
│   │   ├── pdf/
│   │   └── html/
│   ├── papers/            # Academic papers
│   │   ├── pdf/
│   │   └── notes/
│   ├── notes/             # Personal notes
│   │   ├── journal/
│   │   ├── meeting/
│   │   └── ideas/
│   ├── media/             # Media resources
│   │   ├── images/
│   │   ├── audio/
│   │   └── transcripts/
│   ├── data/              # Data files
│   │   ├── csv/
│   │   └── json/
│   └── books/             # Books
│       ├── pdf/
│       └── highlights/
├── wiki/                  # Knowledge content (can be published)
│   ├── index.md           # Content index
│   ├── log.md             # Operation log (private)
│   ├── about.md           # About page
│   ├── entities/          # Entity pages
│   ├── concepts/          # Concept pages
│   ├── sources/           # Source document summaries
│   └── synthesis/         # Comprehensive analysis
└── templates/             # Page templates
    ├── entity.md
    ├── concept.md
    └── source.md
```

## File Naming Convention

- Use lowercase English with hyphens: `machine-learning-basics.md`
- Entities: `entity-[name].md`
- Concepts: `concept-[name].md`
- Sources: `source-[YYYY-MM-DD]-[short-title].md`
- Synthesis: `synthesis-[topic].md`

## Bidirectional Links

Use Obsidian-compatible format: `[[page-name]]`

When creating links:
- Link to related entities, concepts, and sources
- Ensure target pages exist or create them
- Maintain bidirectional connections by updating related pages

## Core Operations

### 1. Ingest Operation

When user adds documents to `raw/`:

1. **Read and analyze** the source document
2. **Identify key entities** (people, organizations, projects, tools, etc.)
3. **Extract concepts** (ideas, theories, methods, frameworks)
4. **Create source summary** with metadata and key insights
5. **Update existing pages** with new information and cross-references
6. **Update index.md** with new entries
7. **Log operation** in log.md with timestamp

**Process**:
```
User: "Ingest the paper in raw/papers/pdf/example.pdf"
You: 
1. Read the PDF content
2. Identify entities: author names, institutions, key tools
3. Extract concepts: main theories, methodologies, frameworks
4. Create source-[YYYY-MM-DD]-example-paper.md
5. Create/update entity pages: entity-author-name.md, entity-institution.md
6. Create/update concept pages: concept-method-name.md
7. Add cross-references between pages
8. Update wiki/index.md
9. Append operation log to wiki/log.md
```

### 2. Query Operation

When user asks questions:

1. **Search relevant pages** in wiki/ using keywords and links
2. **Synthesize information** from multiple sources
3. **Provide comprehensive answer** with citations to wiki pages
4. **Suggest related topics** for exploration

**Process**:
```
User: "What is the relationship between concept A and concept B?"
You:
1. Search for entity-A.md and entity-B.md in wiki/entities/
2. Search for concept-A.md and concept-B.md in wiki/concepts/
3. Find related synthesis pages in wiki/synthesis/
4. Synthesize findings with citations: "According to [[concept-A]], ..."
5. Suggest: "You might also be interested in [[concept-C]] which relates to both."
```

### 3. Health Check Operation

Periodically verify wiki integrity:

1. **Find orphan pages** (pages not linked from index or other pages)
2. **Detect broken links** (links pointing to non-existent pages)
3. **Identify contradictions** (conflicting information across pages)
4. **Suggest improvements** for content organization

**Process**:
```
User: "Check the wiki health"
You:
1. Scan all wiki/ pages
2. Find pages not referenced in index.md or other pages
3. Check all [[links]] and identify broken ones
4. Look for contradictory information
5. Report findings and suggest fixes
```

## Page Templates

Refer to templates in `templates/` directory for consistent structure:
- `templates/entity.md`: For people, organizations, projects, tools
- `templates/concept.md`: For ideas, theories, methods, frameworks
- `templates/source.md`: For document summaries

Always use templates when creating new pages to maintain consistency.

## Workflow Example

### Adding a new research paper:

1. User places paper in `raw/papers/pdf/new-paper.pdf`
2. User requests: "Ingest the new paper"
3. You:
   - Read the PDF
   - Create `wiki/sources/source-2024-01-15-new-paper.md`
   - Extract entities → create/update in `wiki/entities/`
   - Extract concepts → create/update in `wiki/concepts/`
   - Add cross-references between pages
   - Update `wiki/index.md`
   - Log: "2024-01-15: Ingested new-paper.pdf → created 3 entities, 2 concepts"

### Asking about a topic:

1. User asks: "Tell me about machine learning"
2. You:
   - Find `wiki/concepts/concept-machine-learning.md`
   - Find related entity pages
   - Find related source summaries
   - Synthesize answer with citations
   - Suggest: "See also [[concept-deep-learning]], [[entity-tensorflow]]"

## Important Notes

1. **Never modify raw/ files** - They are immutable sources
2. **Always update cross-references** when creating new pages
3. **Keep index.md updated** as the main navigation hub
4. **Log all operations** in log.md with timestamps
5. **Use English filenames** for URL compatibility (future static site)
6. **Maintain YAML frontmatter placeholders** in comments for future static site generation

## Page Types

### Entity Pages (`wiki/entities/`)
Represent real-world entities:
- People (researchers, authors, influencers)
- Organizations (companies, universities, teams)
- Projects (software projects, research initiatives)
- Tools (software, frameworks, platforms)

### Concept Pages (`wiki/concepts/`)
Represent abstract ideas:
- Theories and frameworks
- Methods and methodologies
- Principles and patterns
- Technical concepts

### Source Pages (`wiki/sources/`)
Summarize source documents:
- Research papers
- Articles and blog posts
- Books and chapters
- Meeting notes and journals

### Synthesis Pages (`wiki/synthesis/`)
Comprehensive analysis:
- Comparative studies
- Literature reviews
- Topic overviews
- Cross-reference analyses

## Future Extensions

This system is designed to be extensible:
- Static site generation: Files are ready for VitePress/Hugo
- Metadata: YAML frontmatter placeholders exist in templates
- Publication: wiki/ content can be published independently
- Private content: raw/ and log.md are marked as private

## Quality Standards

1. **Accuracy**: Verify facts from source documents
2. **Completeness**: Extract all relevant information
3. **Consistency**: Follow naming conventions and templates
4. **Connectivity**: Maintain rich cross-references
5. **Clarity**: Write clear, concise summaries

---

This schema guides all wiki operations. Follow it consistently to maintain a high-quality knowledge base.
