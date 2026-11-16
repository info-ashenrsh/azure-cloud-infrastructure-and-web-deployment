# Azure App Service application settings

In Azure Portal:
1. Open your App Service.
2. Find **Settings → Environment variables** (portal wording may vary).
3. Add non-secret configuration values as app settings.
4. Store secrets in Key Vault or use supported Key Vault references.
5. Save and restart if the portal indicates a restart is required.
6. Verify application behavior without printing secret values.

App settings are injected into the application environment. Restrict who can read or modify them.
