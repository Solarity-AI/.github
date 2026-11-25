# Rules for AI agents

Verify: none. This repo holds only Markdown, YAML and 1 image; check YAML forms parse
(`python -c "import yaml,glob;[yaml.safe_load(open(f)) for f in glob.glob('ISSUE_TEMPLATE/*.yml')]"`).

The Solarity-AI organisation's default community files. Every repository without its own copy uses them, so a change
here changes every such repository at once.

## What lives here

- `PULL_REQUEST_TEMPLATE.md`: the default pull request template (What changed, `Fixes #`, How verified with the
  command and its result).
- `ISSUE_TEMPLATE/`: the default issue forms (`bug.yml`, `feature.yml`) and `config.yml`. A repository with its own
  `.github/ISSUE_TEMPLATE/` folder uses only its own forms.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`: the default guides.
- `profile/README.md`: the public organisation profile page; it is public, so no private repo names, people or numbers.

## Rules

- Keep the files generic: no repository-specific commands or paths.
- No keyboard shortcuts anywhere.

## Shipping

- 1 issue per change, then a branch `feat/<issue>-<slug>` or `fix/<issue>-<slug>`.
- Commit subjects `<type>: … (#<issue>)`; the pull request says `Fixes #<issue>`.
- Squash merge.
