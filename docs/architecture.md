# Architecture explanation

## Main components

- **Browser:** the user interface.
- **Azure App Service (Linux):** runs the Flask application without requiring you to manage a virtual machine operating system.
- **PostgreSQL:** stores structured task records.
- **Azure Blob Storage:** stores uploaded files as blobs inside private containers.
- **Virtual Network and related networking controls:** define network address spaces and access paths. VNet integration and private endpoints are different features; configure them according to the exact service architecture.
- **Microsoft Entra ID and Azure RBAC:** provide identity and authorization.
- **Managed identity:** lets an Azure resource request identity tokens without storing a client secret.
- **Key Vault:** stores secrets centrally.
- **Azure Monitor and Application Insights:** help inspect platform metrics and application telemetry.

## Request flow

1. The browser connects to the application over HTTPS.
2. Flask validates the request and handles task operations.
3. Task data is stored in PostgreSQL.
4. Attachments are stored in a private Blob container.
5. The app uses managed identity for supported Azure service access.
6. Logs and telemetry help diagnose application behavior.

## Networking warning

Creating a VNet does not automatically make every Azure service private. App Service VNet integration, private endpoints, private DNS, routing, and service firewall rules must be configured and tested separately.
