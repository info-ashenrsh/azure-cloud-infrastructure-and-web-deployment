# Application configuration

Configuration names used by the starter:

| Variable | Purpose | Secret? |
|---|---|---|
| `SECRET_KEY` | Flask signing/session secret | Yes |
| `DATABASE_URL` | Database connection | Yes |
| `AZURE_STORAGE_ACCOUNT_URL` | Blob endpoint | Usually no |
| `AZURE_STORAGE_CONTAINER` | Container name | No |
| `KEY_VAULT_URL` | Vault endpoint | No |
| `APPLICATIONINSIGHTS_CONNECTION_STRING` | Telemetry configuration | Treat as sensitive configuration |
| `MAX_CONTENT_LENGTH` | Upload request size limit | No |

Use `.env` locally and App Service application settings or Key Vault references in Azure. Never commit actual secret values.
