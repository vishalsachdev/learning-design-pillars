# Learning Design Pillars - Claude Skills

Claude Code skills for applying evidence-based learning design principles, with integration for Canvas LMS via [canvas-mcp](https://github.com/vishalsachdev/canvas-mcp).

## Overview

This repository provides:
1. **Structured learning design principles** - The Four Pillars framework in machine-readable format
2. **Claude Code skills** - Reusable workflows for applying these principles
3. **Canvas MCP integration** - Skills that work with canvas-mcp for LMS-specific tasks

## The Four Learning Design Pillars

| Pillar | Focus | Key Principles |
|--------|-------|----------------|
| 1. Clear, Purposeful Structure | Organization & Flow | Segmenting, sequencing, learning objectives, consistency |
| 2. Active, Engaging Content | Multimedia & Interaction | Visual content, activities, storytelling, accessibility |
| 3. Continuous Practice & Feedback | Assessment & Growth | Varied practice, immediate feedback, metacognition |
| 4. Simple, Intuitive UX | Navigation & Usability | Intuitive navigation, progress indicators, minimalist design |

## Skills

### Content Design Skills
- `/learning-design-review` - Review content against all four pillars
- `/learning-design-checklist` - Generate a compliance checklist for specific pillars

### Canvas Integration Skills (requires canvas-mcp)
- `/canvas-assignment-design` - Design Canvas assignments following learning principles
- `/canvas-course-audit` - Audit a Canvas course against the four pillars
- `/canvas-feedback-template` - Generate feedback templates with learning science backing

## Installation

### For Claude Code Users

```bash
# Clone to your skills directory
git clone https://github.com/YOUR_USERNAME/learning-design-pillars.git ~/.claude/skills/learning-design-pillars
```

### With Canvas MCP Integration

1. Install [canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) following its setup instructions
2. Clone this repository to your skills directory
3. Skills will automatically detect canvas-mcp availability

## Usage

```bash
# Review any educational content
/learning-design-review

# Audit a Canvas course
/canvas-course-audit COURSE_ID

# Design a new assignment
/canvas-assignment-design "Create a peer review assignment for research papers"
```

## Principles Source

Based on the "Four Learning Design Pillars" framework, synthesizing research from:
- Mayer's Multimedia Learning principles
- Cognitive load theory
- Evidence-based instructional design practices

See `principles/learning-design-pillars.yaml` for the complete structured framework.

## Contributing

Contributions welcome! Please ensure any additions reference established learning science research.

## License

MIT License - See [LICENSE](LICENSE)
