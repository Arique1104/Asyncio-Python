Purpose
• Learn: Practice Python, with a focus on asyncio, type hints, and testing.
• Build: CLI tool that ingests CSV data and writes to PostgreSQL and/or DynamoDB.
• Tools: pytest, mypy, pydantic


🧩 Environment Setup

```python
python3 -m venv venv # Create virtual environment
source venv/bin/activate             # Activate it
pip install -r requirements.txt      # Install dependencies (or install manually)
```

📦 Install Dependencies

```python
pip install pandas psycopg2-binary asyncpg pydantic python-dotenv mypy pytest
pip install types-psycopg2 pandas-stubs  # Optional: type stubs for mypy
```

🛠️ Run CSV Ingestion

Async version:

`python -m app.csv_ingest_async app/data/event-members.csv`


Sync version:

`python -m app.csv_ingest app/data/event-members.csv`


🧪 Test Data Was Inserted

Connect to Postgres:

`psql -h localhost -U postgres -d test_db`

Then inside psql:

```cli
\dt                         -- List tables
SELECT COUNT(*) FROM users; -- Confirm rows were inserted
SELECT * FROM users LIMIT 5;
\q                          -- Exit
```

🧹 Run Type Checking

```
mypy app/
# or, if you're getting module errors:
PYTHONPATH=. mypy app/
```

✅ Run Unit Tests

`PYTHONPATH=. pytest`

🗂️ Initialize Packages (only once)

`touch app/__init__.py app/models/__init__.py app/db/__init__.py`