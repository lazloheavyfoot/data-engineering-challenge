
# 🧠 Data Engineer Challenge

This project implements a full ETL pipeline that extracts data from a public API, loads raw data into a PostgreSQL container, transforms it using Python, and finally loads the result into a Microsoft SQL Server container.

The solution uses Docker, pandas, SQLAlchemy, and ODBC drivers to ensure cross-platform compatibility, making it easy to run on Windows, macOS, or Linux.

---

## 🚀 Project Structure

```
data-engineer-challenge/
├── etl/
│   ├── extract.py              # Extracts data from JSONPlaceholder API
│   ├── load_postgres.py        # Loads raw CSV data into PostgreSQL
│   ├── transform.py            # Aggregates and transforms data
│   ├── load_sqlserver.py       # Loads transformed data into SQL Server
│   └── test_connections.py     # Verifies both DB connections
├── utils/
│   └── db_connections.py       # Connection helpers for SQLAlchemy
├── docker-compose.yml          # Defines Postgres & SQL Server containers
├── requirements.txt            # Python dependencies
├── README.md                   # This file
```

---

## 📦 Prerequisites

- Python 3.12+
- Docker & Docker Compose
- `pip` installed in your Python environment

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Project

```bash
git clone <your-repo-url>
cd data-engineer-challenge
```

### 2️⃣ Start Docker Containers

```bash
docker-compose up -d
```

This launches:
- PostgreSQL (localhost:5432)
- SQL Server (localhost:1433)

### 3️⃣ Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Run the ETL Pipeline

### ✅ Step-by-step

```bash
python etl/extract.py
python etl/load_postgres.py
python etl/transform.py
python etl/load_sqlserver.py
```

### ✅ Optional: Test DB Connections

```bash
python etl/test_connections.py
```

---

## 🧠 Troubleshooting

### On macOS (Apple Silicon - M1/M2):

```bash
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
```

Add it to your `~/.zprofile` to persist.

### If `pyodbc` gives build issues:

```bash
ARCHFLAGS="-arch arm64" pip install pyodbc --no-binary :all:
```

### If `psycopg2` gives import errors:

Use the binary wheel:
```bash
pip install psycopg2-binary
```

---

## ✅ Output

Once successful, the following will be created:
- `users.csv`, `posts.csv` → Raw extracted data
- `transformed_post_counts.csv` → Aggregated result
- SQL tables: `users`, `posts` in Postgres; `user_post_counts` in SQL Server

---

## 👤 Author

**James Cundall**  
Email: cundall.alex@gmail.com  
GitHub: [github.com/<your-username>](https://github.com/)  
LinkedIn: [linkedin.com/in/alexcundall](https://linkedin.com/in/alexcundall)
