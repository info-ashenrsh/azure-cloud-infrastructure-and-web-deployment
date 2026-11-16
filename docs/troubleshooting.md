# Troubleshooting

| Problem | Checks |
|---|---|
| Resource creation fails | Region, SKU availability, subscription quota, permissions, policy |
| VM cannot be reached | VM state, public/private IP, NSG, SSH key, source IP |
| App Service returns 500 | App logs, startup command, Python version, missing settings |
| Database connection fails | Host, database, username, TLS, firewall/private DNS, credentials |
| Blob access denied | Storage URL, container, managed identity, data-plane RBAC role |
| Key Vault access denied | Identity enabled, role scope, correct vault, role propagation |
| No monitoring data | Instrumentation/settings, diagnostic configuration, time range, ingestion delay |
| Quota exceeded | Subscription, region, resource provider, requested SKU |

Never share passwords, private keys, access tokens, or full connection strings in a public issue or screenshot.
