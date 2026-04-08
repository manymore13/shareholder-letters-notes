# Personal Wiki System

> A knowledge management system powered by LLM, based on the LLM Wiki design philosophy

---

## Overview

This is a personal knowledge management system that leverages Large Language Models (LLM) to automatically organize and maintain your knowledge base. Simply add raw documents, and the LLM will extract knowledge, create connections, and build a growing network of information.

### Key Features

- **Zero Maintenance**: LLM handles all organization work
- **Knowledge Compound Interest**: Each addition enriches the entire wiki
- **Bidirectional Links**: Every connection is mutual and discoverable
- **Source Traceability**: All knowledge traces back to source documents
- **Future-Proof**: Pure Markdown files, no vendor lock-in

---

## Quick Start

### 1. Initial Setup

```bash
# Clone or create the wiki directory
git init  # Optional: for version control
```

### 2. Add Your First Document

```bash
# Place a document in the appropriate raw/ subdirectory
# Example: raw/articles/markdown/my-article.md
```

### 3. Ingest with LLM

Ask your LLM assistant:
```
"Ingest the article in raw/articles/markdown/my-article.md"
```

The LLM will:
1. Read and analyze the document
2. Extract entities and concepts
3. Create structured wiki pages
4. Add cross-references
5. Update the index

### 4. Explore Your Wiki

- Open `wiki/index.md` in Obsidian or any Markdown editor
- Follow `[[links]]` to navigate between pages
- Ask LLM questions about your knowledge

---

## Architecture

### Three-Layer Design

```
┌─────────────────────────────────────┐
│     Schema Layer (CLAUDE.md)        │  ← LLM Instructions
├─────────────────────────────────────┤
│     Wiki Layer (wiki/)              │  ← Knowledge Content
├─────────────────────────────────────┤
│     Raw Layer (raw/)                │  ← Source Documents
└─────────────────────────────────────┘
```

- **Raw Layer**: Immutable source documents (papers, articles, notes, books)
- **Wiki Layer**: LLM-maintained structured content with cross-references
- **Schema Layer**: Configuration that guides LLM behavior

### Page Types

1. **Entities** (`wiki/entities/`): People, organizations, projects, tools
2. **Concepts** (`wiki/concepts/`): Theories, frameworks, methods, principles
3. **Sources** (`wiki/sources/`): Document summaries and analyses
4. **Synthesis** (`wiki/synthesis/`): Comprehensive analyses and comparisons

---

## Directory Structure

```
personal-wiki/
├── CLAUDE.md              # Schema configuration (LLM instructions)
├── README.md              # This file
├── site/                  # Reserved for static site generation
│   └── .gitkeep
├── raw/                   # Source documents (private)
│   ├── articles/          # Articles and blog posts
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
│   └── books/             # Books and highlights
│       ├── pdf/
│       └── highlights/
├── wiki/                  # Knowledge content (can be published)
│   ├── index.md           # Main navigation hub
│   ├── log.md             # Operation log (private)
│   ├── about.md           # About this wiki
│   ├── entities/          # Entity pages
│   ├── concepts/          # Concept pages
│   ├── sources/           # Source summaries
│   └── synthesis/         # Comprehensive analyses
└── templates/             # Page templates
    ├── entity.md
    ├── concept.md
    └── source.md
```

---

## Core Operations

### 1. Ingest: Adding Knowledge

**Purpose**: Transform raw documents into structured knowledge

**Usage**:
```
"Ingest the paper in raw/papers/pdf/machine-learning.pdf"
```

**Process**:
1. LLM reads the source document
2. Identifies entities (people, organizations, tools)
3. Extracts concepts (ideas, methods, frameworks)
4. Creates source summary page
5. Creates/updates entity and concept pages
6. Adds bidirectional cross-references
7. Updates `wiki/index.md`
8. Logs operation in `wiki/log.md`

### 2. Query: Exploring Knowledge

**Purpose**: Ask questions and discover connections

**Usage**:
```
"What are the key concepts in machine learning?"
"How does concept A relate to concept B?"
"What papers discuss neural networks?"
```

**Process**:
1. LLM searches relevant wiki pages
2. Synthesizes information from multiple sources
3. Provides comprehensive answer with citations
4. Suggests related topics for exploration

### 3. Check: Maintaining Quality

**Purpose**: Verify wiki health and fix issues

**Usage**:
```
"Check the wiki health"
"Find orphan pages"
"Identify broken links"
```

**Process**:
1. LLM scans all wiki pages
2. Finds orphan pages (not linked anywhere)
3. Detects broken links (pointing to non-existent pages)
4. Identifies contradictions across pages
5. Suggests improvements and fixes

---

## Usage Guide

### Adding Documents

1. **Identify document type**: Paper, article, book, note, etc.
2. **Place in appropriate directory**: 
   - Papers → `raw/papers/pdf/`
   - Articles → `raw/articles/markdown/`
   - Books → `raw/books/pdf/`
   - Notes → `raw/notes/journal/`
3. **Ingest with LLM**: "Ingest [filename]"

### Browsing Knowledge

#### With Obsidian (Recommended)
1. Open this directory as a vault in Obsidian
2. Navigate to `wiki/index.md`
3. Click `[[links]]` to explore connected pages
4. Use graph view to visualize connections

#### With Any Markdown Editor
1. Open `wiki/index.md` in your editor
2. Follow links manually (search for link text)
3. Use search function to find topics

### Asking Questions

Use natural language to query your knowledge:

```
"What did I learn about [topic]?"
"Explain [concept-name]"
"What are the key entities in [domain]?"
"Summarize [source-document]"
```

### Maintaining the Wiki

**Regular Maintenance**:
```
"Check wiki health"
"Find pages that need updates"
"Update statistics in index"
```

**Version Control** (Recommended):
```bash
git add wiki/
git commit -m "Add knowledge about [topic]"
```

---

## Supported Formats

### Direct Support (LLM can read)
- Markdown (`.md`)
- Text files (`.txt`)
- PDF (`.pdf`)
- HTML (`.html`)
- JSON (`.json`)
- CSV (`.csv`)
- Code files (`.py`, `.js`, `.java`, etc.)

### Requires Multimodal LLM
- Images (`.png`, `.jpg`)
- Scanned documents

### Requires Preprocessing
- Audio (`.mp3`, `.wav`) → Transcribe first
- Video (`.mp4`) → Extract audio/transcript

---

## Tools

### Recommended

- **Obsidian**: Visual knowledge exploration with graph view
- **Any Markdown Editor**: Simple viewing and editing
- **Git**: Version control and history tracking
- **LLM Assistant**: Claude Code, ChatGPT, or similar

### Future

- **VitePress**: Static site generation for public wiki
- **Hugo**: Alternative static site generator
- **Custom Tools**: Specialized wiki management tools

---

## File Naming Convention

- Use lowercase English with hyphens: `machine-learning-basics.md`
- Entities: `entity-[name].md`
- Concepts: `concept-[name].md`
- Sources: `source-[YYYY-MM-DD]-[short-title].md`
- Synthesis: `synthesis-[topic].md`

---

## Future Extensions

This MVP is designed for extensibility:

### Static Site Generation
- Files ready for VitePress/Hugo
- YAML frontmatter placeholders in templates
- English filenames for URL compatibility
- Public/private content separation

### Planned Features
- [ ] Static site deployment
- [ ] Advanced search indexing
- [ ] Graph visualization tools
- [ ] Integration with note-taking apps
- [ ] Collaborative features

---

## Design Philosophy

### Based on LLM Wiki Principles

This system implements the LLM Wiki concept, treating a structured file system as a knowledge database that LLMs can maintain autonomously.

### Key Principles

1. **Simplicity**: Pure Markdown files, no complex infrastructure
2. **LLM-Native**: Designed for LLM maintenance from the ground up
3. **Bidirectional**: Every connection flows both ways
4. **Traceable**: All knowledge links back to sources
5. **Extensible**: Ready for future enhancements

---

## Configuration

### Schema File

`CLAUDE.md` contains the LLM schema configuration:
- Role definition
- Directory structure
- Naming conventions
- Operation workflows
- Page templates

### Customization

You can customize the system by:
1. Editing `CLAUDE.md` to change LLM behavior
2. Modifying templates in `templates/`
3. Adjusting directory structure as needed
4. Adding custom page types

---

## Best Practices

### For Document Management
- Organize raw documents by type
- Use descriptive filenames
- Keep raw documents immutable
- Backup important sources

### For Knowledge Quality
- Verify extracted information
- Review auto-generated pages
- Fix broken links promptly
- Update outdated information

### For LLM Interaction
- Be specific in your requests
- Provide context when needed
- Verify critical information
- Use Git for important changes

---

## Troubleshooting

### Orphan Pages
```
"Find orphan pages and suggest where to link them"
```

### Broken Links
```
"Identify and fix broken links"
```

### Missing Information
```
"Review [page-name] and suggest improvements"
```

### Contradictions
```
"Find contradictory information in the wiki"
```

---

## Contributing

This is a personal wiki system, but you can create similar systems using:
1. The provided directory structure
2. The `CLAUDE.md` schema configuration
3. The page templates in `templates/`

---

## License

Personal Knowledge Base - All rights reserved unless otherwise noted.

---

## Resources

- **LLM Wiki Design**: Based on the LLM Wiki concept
- **Obsidian**: [https://obsidian.md](https://obsidian.md)
- **VitePress**: [https://vitepress.dev](https://vitepress.dev)
- **Hugo**: [https://gohugo.io](https://gohugo.io)

---

## Support

For issues or questions:
1. Check `CLAUDE.md` for configuration details
2. Review `wiki/about.md` for system overview
3. Consult the LLM Wiki design principles

---

*Built with ❤️ based on LLM Wiki principles*

**Version**: MVP 1.0  
**Last Updated**: 2026-04-08
