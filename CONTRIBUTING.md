# Contributing

This guide applies to every Solarity-AI repository that doesn't have its own `CONTRIBUTING.md`.

## Workflow

1. **Start from an issue.** Search open and closed issues first and reuse one if it fits.
2. **Branch from the default branch** with a short, descriptive name, for example `fix/login-timeout` or `feat/weekly-report`. Never commit straight to the default branch.
3. **Commit in small, logical steps**, each message saying what changed and referencing the issue (`#123`).
4. **Run the project's checks locally** (build, typecheck, lint and tests) before you push.
5. **Open a pull request** with the template filled in and `Fixes #<issue>` for each issue it closes.
6. **Merge when CI is green** and no review comment asks for changes. Repositories with an Auto-merge workflow merge a ready pull request on their own once every check passes; keep it a draft until it's ready.

## Never commit

- Secrets: API keys, tokens, passwords, private keys, `.env` files. Use the `.env.example` pattern and the hosting provider's secret store.
- Personal data of users or teammates.
- Build output and dependencies (`node_modules`, `dist`, `build`).

If a secret is ever pushed, rotate it first, then tell the repository owner. Removing the commit isn't enough.

## Security

Report vulnerabilities privately, as described in [SECURITY.md](SECURITY.md).

## Code of conduct

Everyone taking part is expected to follow the [code of conduct](CODE_OF_CONDUCT.md).
