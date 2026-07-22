# CLAUDE.md

## Workflow Orchestration

### 1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately — don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One tack per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update tasks/lessons.md with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes — don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Project Structure

| Folder | Purpose |
|--------|---------|
| `agent/` | Companion app — Deno Desktop GUI (`agent/desktop`), runs Playwright headlessly |
| `extension/` | Chrome Extension MV3 — records DOM interactions and executes test runs in the browser; communicates with the companion app and the Nuxt server |
| `nuxt_template/` | Nuxt 4 web app — the primary codebase replacing the legacy Electron app |
| `manual-qa/` | Legacy Electron + Playwright desktop app being migrated to `nuxt_template/` |
| `server-qa/` | Legacy Express.js backend that supported `manual-qa/`; superseded by Nuxt server routes |
| `docs/` | Obsidian documentation vault — architecture, project spec, missions, design references |

> Always work in `nuxt_template/`, `extension/`, or `agent/`. Do not modify `manual-qa/` or `server-qa/` — they are reference-only.

---

## Obsidian Integration

### Vault as Knowledge Base
- The Obsidian vault lives in the `docs/` folder — treat it as the single source of truth for project knowledge, decisions, and lessons
- Read relevant vault notes at session start before planning any non-trivial task
- All notes are plain Markdown — edit files directly in `docs/`

### Note Conventions
- Use `[[wikilinks]]` to connect related notes; prefer linking over duplicating content
- Add YAML frontmatter (tags, date, project, status) to every note created or updated
- Follow existing folder structure and naming conventions in the vault — don't invent new ones
- Keep atomic notes: one concept per note, linked together rather than one giant file

### Capturing Work in Obsidian
- Mirror important entries from tasks/lessons.md into `docs/Lessons/` with backlinks to the relevant project note
- After completing significant tasks, write a brief decision log note: what was done, why, and alternatives considered
- Log architectural decisions as ADR-style notes (context, decision, consequences)
- Update the project's index/MOC (Map of Content) note when adding new notes so nothing gets orphaned

### Hygiene
- Never delete or rewrite existing vault notes without explicit approval — append or create new linked notes instead
- Don't touch the `docs/.obsidian/` config folder
- Preserve existing tags and links when editing a note

## Task Management
1. Plan First: Write plan to tasks/todo.md with checkable items
2. Verify Plan: Check in before starting implementation
3. Track Progress: Mark items complete as you go
4. Explain Changes: High-level summary at each step
5. Document Results: Add review section to tasks/todo.md
6. Capture Lessons: Update tasks/lessons.md after corrections

## Core Principles
- Simplicity First: Make every change as simple as possible. Impact minimal code.
- No Laziness: Find root causes. No temporary fixes. Senior developer standards.
- Minimal Impact: Changes should only touch what's necessary. Avoid introducing bugs.