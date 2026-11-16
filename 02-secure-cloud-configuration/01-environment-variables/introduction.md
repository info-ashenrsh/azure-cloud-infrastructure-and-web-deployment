# Environment variables

Environment variables are name/value settings supplied to a running process. They let the same code run in development and cloud environments with different configuration.

Examples: `DATABASE_URL`, `SECRET_KEY`, and `AZURE_STORAGE_ACCOUNT_URL`.

Do not store secret values in source code. `.env.example` should contain variable names and harmless placeholders only.
