# PostgreSQL basics

A relational database stores structured information in tables.

Example:

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(160) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending'
);

INSERT INTO tasks (title) VALUES ('Learn PostgreSQL');
SELECT id, title, status FROM tasks;
```

`CREATE TABLE` defines the structure, `INSERT` adds a row, and `SELECT` reads rows.
