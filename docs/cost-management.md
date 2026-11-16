# Cost management for Azure Student

Student credits and free offers have eligibility rules and limits. Never assume a service is free.

## Before creating a resource

1. Open Azure Portal and check your subscription offer and remaining credit.
2. Check **Subscriptions → Usage + quotas** for relevant limits.
3. Confirm the service is available in your chosen region.
4. Review the pricing estimate and billing dimensions.
5. Choose a small development option that is actually available to your subscription.
6. Record the resource name and cleanup method.

## Cost factors to understand

- Virtual Machines: VM size, running time, disks, public IP, and outbound data.
- App Service: App Service plan tier and duration; an idle app may still incur plan charges.
- Blob Storage: capacity, redundancy, operations, and data transfer.
- PostgreSQL: compute, storage, backup retention, and networking.
- Key Vault: operation volume and selected features.
- Monitoring: data ingestion and retention.
- Networking: public IPs, private endpoints, gateways, and data transfer.

## Cleanup

Stop or delete temporary compute when finished, but understand that stopping an app or VM does not necessarily stop every associated charge. Check disks, IP addresses, databases, storage, backups, monitoring workspaces, private endpoints, and DNS resources. Delete a resource group only after confirming it contains only disposable lab resources.
