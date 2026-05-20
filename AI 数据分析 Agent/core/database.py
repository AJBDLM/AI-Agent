import duckdb
import pandas as pd

conn = duckdb.connect()


def load_csv(path: str, table_name: str):
    df = pd.read_csv(path)
    conn.register(table_name, df)
    return df


def run_sql(sql: str):
    return conn.execute(sql).fetchdf()
