import sqlalchemy
from sqlalchemy import create_engine
import urllib

# PostgreSQL connection
def get_postgres_engine():
    return create_engine(
        "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
    )

# SQL Server connection
def get_sqlserver_engine():
    import urllib
    from sqlalchemy import create_engine

    connection_string = (
        "DRIVER=/opt/homebrew/lib/libmsodbcsql.18.dylib;"
        "SERVER=localhost,1433;"
        "DATABASE=master;"
        "UID=sa;"
        "PWD=YourStrong!Passw0rd;"
        "TrustServerCertificate=yes;"
    )
    connection_url = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
    return create_engine(connection_url)