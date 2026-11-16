# Managed identity access to Key Vault

1. Open the App Service.
2. Open **Identity** and enable the system-assigned identity.
3. Open the Key Vault's **Access control (IAM)**.
4. Assign the minimum role needed, such as a secrets-read role, at the vault scope.
5. Wait for role assignment propagation.
6. Test access from the application using an Azure identity SDK or supported Key Vault reference.
7. Verify success without printing the secret value.

Do not grant subscription-wide permissions to the app.
