# Blob Storage integration guide

The initial CloudTask app does not yet upload files. This document is the implementation activity for adding that capability.

## Target design

- Keep the container private.
- Use the Storage Account Blob endpoint.
- Enable the App Service managed identity.
- Grant a narrowly scoped Blob data role to the app identity.
- Use Azure Identity SDK authentication (`DefaultAzureCredential`) rather than embedding an account key.
- Validate file type and size on the server.
- Generate safe blob names; do not trust user-supplied paths.
- Do not log file contents or secrets.

## Learning steps

1. Complete the private container activity in Activity 01.
2. Read the Azure SDK documentation for `azure-storage-blob` and `azure-identity`.
3. Implement a server-side upload route.
4. Add strict size/type validation and safe filenames.
5. Test upload and download using an authorized identity.
6. Confirm anonymous access is denied.

Do not claim file upload is implemented until you have written and tested the integration.
