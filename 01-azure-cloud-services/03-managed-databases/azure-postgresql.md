# Azure Database for PostgreSQL

Azure Database for PostgreSQL Flexible Server is the managed database target for CloudTask.

Before creating it:
1. Check whether the service is available in your chosen region.
2. Check subscription quota and permitted compute SKUs.
3. Review compute, storage, backup, and networking cost.
4. Choose private networking where feasible.
5. Plan a dedicated application database role with limited permissions.
6. Require TLS for connections.

Do not expose port 5432 to all internet addresses. If a temporary public-access lab is unavoidable, restrict the firewall rule to your own IP and remove it after the exercise.
