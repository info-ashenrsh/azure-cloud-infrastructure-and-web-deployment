# Local configuration

1. Copy the repository `.env.example` to `.env`.
2. Replace the local `SECRET_KEY` placeholder with a unique random value.
3. Keep `.env` in `.gitignore`.
4. Load variables with `python-dotenv` in local development.
5. Never upload `.env` to GitHub.

Check Git status before committing:

```bash
git status
```

If `.env` appears as a file to be committed, stop and fix `.gitignore` before pushing.
