# Rules for AI agents

Verify: none. This repo holds only Markdown, YAML and 1 image; check YAML forms parse
(`python -c "import yaml,glob;[yaml.safe_load(open(f)) for f in glob.glob('ISSUE_TEMPLATE/*.yml')]"`).

The Solarity-AI organisation's default community files. Every repository without its own copy uses them, so a change
here changes every such repository at once.

**Edits here change every repo's defaults at once:** treat each change as an org-wide change, not a normal repo edit.

## What lives here

- `PULL_REQUEST_TEMPLATE.md`: the default pull request template (What changed, `Fixes #`, How verified with the
  command and its result).
- `ISSUE_TEMPLATE/`: the default issue forms (`bug.yml`, `feature.yml`, `question.yml`) and `config.yml` (blank
  issues off, contact links). A repository with its own
  `.github/ISSUE_TEMPLATE/` folder uses only its own forms.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`: the default guides.
- `workflow-templates/`: org starter workflows offered on every repo's "New workflow" page (`node-ci.yml` calls the
  shared Node test job in `ci-platform` at `@v1`; each template needs a matching `.properties.json`).
- `.github/workflows/links.yml`: checks the links in every Markdown file on pull requests (hosted runner, public repo).
- `profile/README.md`: the public organisation profile page; it is public, so no private repo names, people or numbers.

## Rules

- Keep the files generic: no repository-specific commands or paths.
- No keyboard shortcuts anywhere.

## Shipping

- 1 issue per change, then a branch `feat/<issue>-<slug>` or `fix/<issue>-<slug>`.
- Commit subjects `<type>: … (#<issue>)`; the pull request says `Fixes #<issue>`.
- Squash merge.
