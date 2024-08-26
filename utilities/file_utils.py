import pandas as pd


def read_urls(file_path):
    return pd.read_csv(file_path)


def write_results(file_path, df):
    df.to_csv(file_path, index=False)
