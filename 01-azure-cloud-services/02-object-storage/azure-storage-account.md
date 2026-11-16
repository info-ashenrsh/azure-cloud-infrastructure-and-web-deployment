# Azure Storage Account

A storage account is the top-level Azure resource that provides storage services.

## Portal exploration
1. Search **Storage accounts** in Azure Portal.
2. Inspect the create wizard and available region, performance, redundancy, and account options.
3. Check pricing and quota before creating.
4. Use a globally unique lowercase name if you proceed.
5. Keep anonymous/public blob access disabled.

## Security
Prefer Microsoft Entra ID authorization and narrowly scoped data roles. Do not put account keys in source code or GitHub.
