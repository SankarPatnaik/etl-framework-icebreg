import pandas as pd
import pymysql

def read(config):
    conn = pymysql.connect(
        host=config['host'],
        port=config.get('port', 3306),
        user=config['user'],
        password=config['password'],
        database=config['database']
    )
    df = pd.read_sql(config['query'], conn)
    conn.close()
    return df
