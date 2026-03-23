# Git Workflow

This project follows a simple and clean Git workflow focused on readability and maintainability.

## Branches

- `main` — stable, production-ready code
- `develop` — integration branch for ongoing work

## Workflow

1. Create a branch from `develop`
2. Implement your changes
3. Write/update tests
4. Ensure all tests pass
5. Open a Pull Request into `develop`
6. After review, merge into `develop`
7. Periodically, `develop` is merged into `main`

---

## Commit Message Rules

We follow a simplified Conventional Commits style:

### Format

`<type>: <short description>`

### Types

- feat — new feature
- fix — bug fix
- refactor — code change without feature/bug impact
- test — adding or updating tests
- docs — documentation changes
- chore — maintenance tasks

### Examples

- feat: add median coffee report
- fix: handle missing csv files
- refactor: simplify report registry logic
- test: add tests for median calculation
- docs: update README with usage example
- chore: apply code formatting with black

### Rules

- Use present tense ("add", not "added")
- Keep message concise (max ~70 chars)
- One logical change per commit
