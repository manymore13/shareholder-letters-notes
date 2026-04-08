# About This Wiki

---

<!--
# YAML Frontmatter Placeholder
---
title: About This Wiki
description: Personal knowledge management system based on LLM Wiki
date: 2026-04-08
---
-->

## What is This?

This is a personal knowledge management system designed to help you build a growing, interconnected knowledge base with minimal maintenance effort.

## How It Works

### Three-Layer Architecture

1. **Raw Layer** (`raw/`): You place source documents here - papers, articles, notes, books, etc.
2. **Wiki Layer** (`wiki/`): LLM automatically organizes knowledge into structured pages with cross-references
3. **Schema Layer** (`CLAUDE.md`): Instructions that guide LLM behavior

### Core Operations

- **Ingest**: Add new documents to the wiki
- **Query**: Ask questions and explore knowledge
- **Check**: Verify wiki health and fix issues

## Design Philosophy

### Inspired by LLM Wiki

This system is based on the LLM Wiki concept, which treats a structured file system as a database that LLMs can maintain autonomously.

### Key Principles

1. **Zero Maintenance**: LLM handles all organization work
2. **Knowledge Compound Interest**: Each addition enriches the entire wiki
3. **Bidirectional Links**: Every connection is mutual and discoverable
4. **Source Traceability**: All knowledge traces back to source documents
5. **Future-Proof**: Pure Markdown files, no vendor lock-in

## Features

### Current (MVP)

- ✅ Structured directory organization
- ✅ Four page types (entities, concepts, sources, synthesis)
- ✅ Obsidian-compatible bidirectional links
- ✅ Automatic cross-referencing
- ✅ Operation logging
- ✅ Health checking

### Future Extensions

- 🔄 Static site generation (VitePress/Hugo)
- 🔄 Public knowledge sharing
- 🔄 Advanced search and visualization
- 🔄 Integration with note-taking apps

## How to Use

### Adding Knowledge

1. Place document in appropriate `raw/` subdirectory
2. Ask LLM: "Ingest [filename]"
3. LLM will:
   - Extract entities and concepts
   - Create structured pages
   - Add cross-references
   - Update index

### Exploring Knowledge

1. Browse `wiki/index.md` for overview
2. Follow `[[links]]` to related pages
3. Ask LLM questions about any topic
4. Use Obsidian for visual exploration

### Maintaining Quality

1. Periodically run health checks
2. Review and fix orphan pages
3. Resolve contradictions
4. Update outdated information

## Tools

### Recommended

- **Obsidian**: Visual knowledge exploration and editing
- **Any Markdown Editor**: Simple viewing and editing
- **Git**: Version control and history tracking

### Future

- **VitePress**: Static site generation
- **Hugo**: Alternative static site generator
- **Custom Tools**: Specialized wiki tools

## File Structure

```
wiki/
├── index.md        # Main navigation hub
├── about.md        # This file
├── log.md          # Operation log (private)
├── entities/       # People, organizations, projects
├── concepts/       # Ideas, theories, methods
├── sources/        # Document summaries
└── synthesis/      # Comprehensive analyses
```

## Contributing

This is a personal wiki, but you can create similar systems for your own use. See `CLAUDE.md` for the schema configuration.

## License

Personal knowledge base - All rights reserved unless otherwise noted.

---

*Built with ❤️ based on LLM Wiki principles*
