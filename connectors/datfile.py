import pandas as pd

def read(config):
    return pd.read_csv(config['path'], sep=config.get('sep', '\t'))
