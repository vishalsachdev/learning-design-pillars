# Canvas MCP Integration Guide

This document explains how the Learning Design Pillars skills integrate with [canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) to apply evidence-based learning design principles directly in Canvas LMS.

## Prerequisites

1. **canvas-mcp installed and configured** - Follow the [canvas-mcp setup guide](https://github.com/vishalsachdev/canvas-mcp#installation)
2. **Learning Design Pillars skills installed** - Clone to `~/.claude/skills/learning-design-pillars`
3. **Canvas API access** - Valid Canvas API token configured in canvas-mcp

## Integration Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Claude Code                              │
├─────────────────────────────────────────────────────────────┤
│  Learning Design Skills          Canvas MCP Tools            │
│  ┌─────────────────────┐        ┌─────────────────────┐     │
│  │ /learning-design-   │        │ list_courses        │     │
│  │    review           │───────▶│ list_assignments    │     │
│  │ /canvas-course-     │        │ get_course_details  │     │
│  │    audit            │        │ create_assignment   │     │
│  │ /canvas-assignment- │        │ bulk_grade          │     │
│  │    design           │        │ ...40+ tools        │     │
│  └─────────────────────┘        └─────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   Canvas LMS    │
                    │   (via API)     │
                    └─────────────────┘
```

## Skill-to-Tool Mapping

### `/canvas-course-audit`

Uses these canvas-mcp tools to analyze course structure:

| Pillar | canvas-mcp Tools Used | What's Analyzed |
|--------|----------------------|-----------------|
| 1. Structure | `list_modules`, `get_course_details` | Module organization, naming, prerequisites |
| 2. Content | `list_pages`, `list_files` | Content variety, multimedia presence |
| 3. Practice | `list_assignments`, `list_quizzes` | Assessment types, rubric presence |
| 4. UX | `get_course_details`, `list_modules` | Navigation, progress tracking settings |

### `/canvas-assignment-design`

Creates assignments using:

| Design Step | canvas-mcp Tools | Principles Applied |
|-------------|-----------------|-------------------|
| Setup | `create_assignment` | 1.3.1 Clear objectives, 3.2.5 Clear instructions |
| Rubric | `create_rubric` | 3.2.1 Targeted feedback, 1.3.4 Expectation setting |
| Peer Review | `create_peer_review` | 3.3.4 Social learning, 3.1.1 Varied practice |
| Due Dates | `update_assignment` | 1.4.1 Spaced exposure, 3.1.3 Spaced practice |

### `/canvas-feedback-template`

Generates feedback using:

| Feedback Type | canvas-mcp Tools | Principles Applied |
|---------------|-----------------|-------------------|
| Individual | `grade_submission` | 3.2.1 Targeted, 3.2.2 Encouraging |
| Bulk | `bulk_grade_submissions` | 3.2.3 Immediate feedback |
| Rubric-based | `grade_with_rubric` | 3.2.1 Targeted, 1.3.3 Aligned |

## Example Workflows

### Workflow 1: New Course Setup

```bash
# 1. Audit an existing course for baseline
/canvas-course-audit BADM_350

# 2. Review the audit findings
# Output shows pillar scores and specific improvements

# 3. Design improved assignments
/canvas-assignment-design "Create peer review assignment for case analysis"

# 4. The skill will:
#    - Guide through principle-based design decisions
#    - Generate Canvas-ready assignment settings
#    - Optionally create in Canvas via canvas-mcp
```

### Workflow 2: Mid-Semester Check

```bash
# Quick audit focusing on feedback pillar
/canvas-course-audit COURSE_ID --pillar 3

# Review shows:
# - % of assignments with rubrics
# - Average feedback turnaround time
# - Practice quiz availability
```

### Workflow 3: Assignment Redesign

```bash
# Review existing assignment against principles
/learning-design-review

# Paste the current assignment description
# Get specific improvement suggestions with principle citations

# Then redesign with guided workflow
/canvas-assignment-design "Improve existing case study assignment"
```

## Principle-to-Canvas Feature Mapping

| Principle | Canvas Feature | How to Enable |
|-----------|---------------|---------------|
| 1.1.1 Small segments | Modules with requirements | Module settings → Add requirements |
| 1.3.1 Learning objectives | Module descriptions | Edit module → Add description |
| 2.2.2 Activity-based | Discussions, Peer Reviews | Create discussion/peer review assignment |
| 3.1.6 Low-stakes | Practice quizzes | Quiz settings → Ungraded survey or multiple attempts |
| 3.2.3 Immediate feedback | Quiz answer feedback | Quiz → Show correct answers immediately |
| 4.1.2 Progress indicators | Module progression | Course settings → Enable progression |
| 4.3.2 Time estimates | Assignment descriptions | Include "Estimated time: X minutes" |

## Canvas-Specific Recommendations by Pillar

### Pillar 1: Clear, Purposeful Structure
- **Module Naming**: Use consistent format: "Week 1: Topic Name"
- **Prerequisites**: Set module requirements to enforce sequencing
- **Home Page**: Create a visual course map with links

### Pillar 2: Active, Engaging Content
- **Canvas Studio**: Use for video hosting with analytics
- **H5P Integration**: Add interactive elements to pages
- **Embedded Media**: Test mobile rendering

### Pillar 3: Continuous Practice & Feedback
- **Question Banks**: Create banks for varied quiz questions
- **SpeedGrader**: Enable for faster feedback
- **Rubrics**: Attach to every graded assignment

### Pillar 4: Simple, Intuitive UX
- **Navigation**: Hide unused items (Files, Outcomes, etc.)
- **Course Home**: Use Modules view for clearest structure
- **Mobile Testing**: Preview course in Canvas Student app

## Troubleshooting

### "canvas-mcp tools not available"
Ensure canvas-mcp is properly configured in your Claude Desktop MCP settings.

### "Course not found"
Use `list_courses` first to find the correct course identifier (Canvas ID, course code, or SIS ID).

### "Permission denied"
Some tools require educator-level access. Check your Canvas role for the course.
