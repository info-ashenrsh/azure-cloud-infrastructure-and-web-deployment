# Application logging

Logs are timestamped records of application events. They help explain what happened when a request succeeds or fails.

Use levels:
- DEBUG: detailed development information.
- INFO: normal operational events.
- WARNING: unexpected but recoverable conditions.
- ERROR: an operation failed.
- CRITICAL: a severe failure.

Never log passwords, tokens, cookies, or full connection strings.
