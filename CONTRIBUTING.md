# Contributing to D4C

D4C is a focused personal assistant system built for fast, reliable execution.

Contributions are welcome when they improve stability, clarity, or core functionality.

This project is under an [MIT License](LICENSE), meaning you are free to use, modify, and distribute this software under the terms of the license.

---

## Core Principles

Contributions should aim to:

- Improve reliability
- Keep the system simple and predictable
- Reduce friction in execution
- Maintain consistency across features

If a change adds unnecessary complexity, it may not be merged.

---

## Scope of D4C

D4C is focused on:

- Voice-driven command execution
- Task management
- Local recording system
- Web search capability
- Local system interaction
- Lightweight modular features

Changes outside this scope may not be included in the project.

---

## Project Structure

Please follow the existing structure:

- `core/` → command routing (sensitive area)
- `tools/` → modular feature implementations
- `data/` → persistent storage (must remain backward compatible)
- `utils/` → shared helper functions
- `recordings/` → stored audio data
- `main.py` → main project entry

If a change affects multiple areas, it’s best to discuss it first.

## Contribution Flow

### Issues

For anything non-trivial, opening an issue first is preferred. It helps keep changes aligned with the direction of the project.

### Branch Naming

Format:
`type-short-description`

Examples:

- `fix-audio-overflow`
- `feat-task-priority`
- `refactor-command-router`

### Commits

Format:
type: short description

Common types:

- `fix`
- `feat`
- `refactor`
- `perf`

Examples:

- `fix: resolve wake-word latency`
- `feat: add task deadlines`
- `perf: improve recording startup speed`

---

## READY-FOR-PR System

Before requesting a review, please ensure your PR is in a finished state:

- [ ] READY FOR PR (final state, ready for review)

If this is not checked, the PR may be treated as work-in-progress.

---

## Pull Request Guidelines

A good PR includes:

- What changed
- Why it changed
- How it was tested
- Any potential impact or risks

This helps keep reviews fast and clear.

---

## Things to Avoid

To keep D4C stable and focused:

- Major architecture changes without discussion
- Introducing external cloud dependencies
- Turning D4C into a general chatbot framework
- Mixing unrelated changes in one PR
- Large refactors combined with new features
- Changing command syntax without a migration plan

---

## Design Direction

D4C is built around one idea:

> Make intent turn into action with minimal friction.

If a change makes the system more complex or slower to use, it’s likely not aligned with the project direction.

---

## Stability Expectations

Contributions should aim to preserve:

- Wake-word reliability
- Command routing behavior
- Backward compatibility in stored data
- Fast response times in core loops

---

## Review Process

- PRs marked "work in progress" may be held until complete
- PRs without sufficient detail may need revision
- PRs that don’t align with scope may not be merged

---

## Final Note

D4C is a focused system, not a general playground. The goal is to keep it fast, stable, and easy to use over time.
