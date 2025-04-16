import pandas as pd
from pymongo import MongoClient

def read(config):
    client = MongoClient(f"mongodb://{config['user']}:{config['password']}@{config['host']}:{config.get('port', 27017)}")
    db = client[config['database']]
    collection = db[config['collection']]
    data = list(collection.find())
    df = pd.DataFrame(data)
    return df
