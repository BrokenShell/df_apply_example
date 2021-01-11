import pandas as pd
from labels import short_labels


def transformer(long_name: str) -> str:
    for short_name in short_labels:
        if short_name in long_name:
            return short_name
    return long_name


df = pd.read_csv('csv/data.csv')
df['new'] = df['old'].apply(transformer)
print(df)
