# Database setup

The application defaults to SQLite for local learning. When ready, use Azure Database for PostgreSQL Flexible Server.

## Connection configuration

Set `DATABASE_URL` in your local `.env` or Azure App Service settings. Example format:

```text
postgresql+psycopg://APP_USER:URL_ENCODED_PASSWORD@SERVER_HOST:5432/DB_NAME?sslmode=require
```

Replace all example values locally. Never commit a real connection string.

## Steps

1. Check Azure PostgreSQL region availability, quota, and price.
2. Decide private networking and DNS approach.
3. Create the server and database only after reviewing the estimate.
4. Create a dedicated application database role with limited permissions.
5. Configure TLS.
6. Set `DATABASE_URL` outside source control.
7. Test a task create/read operation.
8. Verify data persists after an application restart.

The starter uses `db.create_all()` for learning. For a serious application, introduce database migrations before making schema changes.
