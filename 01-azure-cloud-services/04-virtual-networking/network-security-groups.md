# Network Security Groups

An NSG contains inbound and outbound allow/deny rules.

A rule includes priority, source, destination, protocol, port, and action. Lower priority numbers are evaluated first.

Common ports:
- SSH: TCP 22
- HTTP: TCP 80
- HTTPS: TCP 443
- PostgreSQL: TCP 5432

Only allow the traffic required. Never allow database port 5432 from `Any` / the whole internet for this project.
