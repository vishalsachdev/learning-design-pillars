# CLAUDE.md - Learning Design Pillars

Project-specific instructions for Claude Code sessions.

---

## Project Overview

This repository provides Claude Code skills for applying evidence-based learning design principles, based on the Four Learning Design Pillars framework. It includes Canvas LMS integration via [canvas-mcp](https://github.com/vishalsachdev/canvas-mcp).

**Repository:** https://github.com/vishalsachdev/learning-design-pillars

### Key Components

| Component | Location | Description |
|-----------|----------|-------------|
| Principles | `principles/learning-design-pillars.yaml` | 46 principles in 4 pillars, machine-readable |
| Skills | `skills/` | 5 Claude Code skills for educators |
| Article | `articles/` | Newsletter article with cover images |
| Documentation | `docs/` | Canvas MCP integration guide |

### Skills Overview

1. **learning-design-review** - Review content against all four pillars
2. **learning-design-checklist** - Generate compliance checklists
3. **canvas-assignment-design** - Design Canvas assignments (requires canvas-mcp)
4. **canvas-course-audit** - Audit Canvas courses (requires canvas-mcp)
5. **canvas-feedback-template** - Generate feedback templates (requires canvas-mcp)

---

## Current Focus

- [ ] Publish article to Substack and share on LinkedIn/Twitter

---

## Roadmap

### Phase 1: Initial Release (COMPLETE)
- [x] Extract learning design principles from PDF to YAML/JSON
- [x] Create 5 Claude Code skills for educators
- [x] Validate skills with skill-creator
- [x] Set up GitHub repository
- [x] Write article: "Building Shareable Learning Design Skills with Canvas MCP Integration"
- [x] Generate cover images for all platforms (LinkedIn, Substack, Twitter)
- [x] Create HTML version of article

### Phase 2: Community & Feedback
- [ ] Publish article to Substack
- [ ] Share on LinkedIn and Twitter
- [ ] Gather community feedback on skills
- [ ] Add more example use cases to documentation

### Phase 3: Enhancements
- [ ] Add principle-specific deep-dive skills
- [ ] Create video tutorials for skill usage
- [ ] Add rubric generation skill
- [ ] Integrate with additional LMS platforms (Moodle, Blackboard)

### Phase 4: Advanced Features
- [ ] AI-powered content gap analysis
- [ ] Automatic principle mapping from course exports
- [ ] Batch course auditing capability
- [ ] Analytics dashboard for audit results

---

## Session Log

### 2024-12-27
- Completed: PDF extraction to YAML/JSON (46 principles), created 5 Claude Code skills, validated all skills with skill-creator, set up GitHub repo, wrote article, generated cover images (LinkedIn 1200x628, Substack 1100x220, Twitter 1200x675), created HTML article version, Python cover generation script
- Key decisions: Used YAML as primary format for principles (human-readable), structured skills to detect canvas-mcp availability, cross-referenced previous articles (Skills Creating Skills, Canvas MCP Evolution, Teaching in Age of AI)
- Next: Publish article to Substack and share on social media

---

## Technical Notes

### Skill Installation

Users should clone to their skills directory:
```bash
git clone https://github.com/vishalsachdev/learning-design-pillars.git ~/.claude/skills/learning-design-pillars
```

### Canvas MCP Integration

Skills that require canvas-mcp will check for its availability and gracefully handle cases where it's not installed. See `docs/canvas-mcp-integration.md` for setup details.

### Principles Schema

The principles YAML follows this structure:
```yaml
pillars:
  - id: "1"
    name: "Clear, Purposeful Structure"
    categories:
      - id: "1.1"
        name: "Content Organization"
        principles:
          - id: "1.1.1"
            name: "Segmenting"
            description: "..."
```

---

## Related Projects

- [canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) - Canvas LMS MCP server
- Origin inspiration: [LinkedIn post](https://www.linkedin.com/posts/activity-7408914018960093185-0mzO) by an instructional designer sharing the Four Pillars framework

---

## Code Style

This is primarily a documentation and skills repository. When modifying:

- **YAML files**: Use 2-space indentation, maintain hierarchical principle IDs
- **Skill SKILL.md files**: Include proper frontmatter with name and description
- **Articles**: Follow The Hybrid Builder newsletter style (see `~/.claude/skills/write-article/`)
