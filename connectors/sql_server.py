import pandas as pd
import pyodbc

def read(config):
    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={config['host']};DATABASE={config['database']};UID={config['user']};PWD={config['password']}"
    conn = pyodbc.connect(conn_str)
    df = pd.read_sql(config['query'], conn)
    conn.close()
    return df
