# Azure RBAC

Azure Role-Based Access Control controls access to Azure resources.

A role assignment combines:
- Security principal (user, group, service principal, or managed identity).
- Role definition (permissions).
- Scope (where permissions apply).

Prefer a resource-level or resource-group-level role when sufficient. Avoid granting Owner or broad Contributor access to an application runtime identity.
