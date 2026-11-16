# Managed identities

A managed identity gives an Azure resource an identity in Microsoft Entra ID. The resource can obtain tokens without storing a client secret.

For CloudTask, enable a system-assigned identity on App Service and grant only the necessary data-plane permissions for Blob Storage or secret retrieval. Role changes can take time to propagate.
