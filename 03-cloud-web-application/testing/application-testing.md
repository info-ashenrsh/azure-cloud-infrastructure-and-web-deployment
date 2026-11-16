# Application testing

From `03-cloud-web-application/application/backend`:

```bash
pip install -r requirements.txt
pytest -q
```

The included tests cover health, task creation/listing, validation, update, and deletion using an in-memory SQLite database.

Add further tests when implementing PostgreSQL and Blob Storage integrations.
