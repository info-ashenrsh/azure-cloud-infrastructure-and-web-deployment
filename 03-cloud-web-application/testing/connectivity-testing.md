# Connectivity testing

Test one connection at a time:

1. Browser → App Service: HTTPS endpoint responds.
2. App Service → PostgreSQL: application can create and read a task.
3. App Service → Blob Storage: authorized upload/download succeeds after integration.
4. App Service → Key Vault: authorized secret access succeeds without printing the value.
5. App Service → Application Insights: telemetry appears.

For failures, check DNS, network path, TLS, firewall rules, managed identity, RBAC scope, and application logs. Do not solve a connectivity problem by opening all ports to the internet.
