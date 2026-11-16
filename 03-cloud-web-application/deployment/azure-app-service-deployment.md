# Azure App Service deployment

## Before deployment
- Confirm the app works locally and tests pass.
- Check App Service plan price, region, runtime availability, and quota.
- Create or identify the intended App Service plan.
- Configure app settings outside Git.
- Plan managed identity, database, storage, and networking access.

## High-level portal steps
1. Open Azure Portal and search **App Services**.
2. Create a Linux Web App using a supported Python runtime.
3. Select a reviewed App Service plan and inspect the estimated cost.
4. Configure deployment from your chosen source.
5. Set the startup command if required by the selected runtime/deployment layout.
6. Configure app settings such as `SECRET_KEY` and `DATABASE_URL` securely.
7. Enable HTTPS-only.
8. Configure managed identity when integrating with Azure services.
9. Deploy and inspect application logs.
10. Verify the HTTPS root page and `/health`.

Portal labels and supported runtime versions can change. Check current Azure documentation before deployment.
