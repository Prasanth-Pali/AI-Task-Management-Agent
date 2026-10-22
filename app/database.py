from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

connection_url = URL.create(
    "mssql+pyodbc",
    host=r"DESKTOP-8CEP79S\SQLEXPRESS",
    database="AITaskAssistantDB",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "Trusted_Connection": "yes",
        "TrustServerCertificate": "yes",
    },
)

engine = create_engine(connection_url, pool_pre_ping=True)

with engine.connect() as connection:
    database_name = connection.execute(
        text("SELECT DB_NAME()")
    ).scalar()

    print("Connected successfully to:", database_name)


engine = create_engine(
    connection_url,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)