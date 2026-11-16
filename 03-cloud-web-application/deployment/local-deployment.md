# Local deployment

1. Install Python 3.10 or newer.
2. Open a terminal in `application/backend`.
3. Create and activate a virtual environment.
4. Run `pip install -r requirements.txt`.
5. Copy root `.env.example` to root `.env` and set a unique local secret key.
6. Start with `flask --app app run --debug`.
7. Open `http://127.0.0.1:5000/`.
8. Test task creation, listing, completion, and deletion.
9. Visit `/health`.

SQLite is used by default, so no Azure resources are required for this activity.
