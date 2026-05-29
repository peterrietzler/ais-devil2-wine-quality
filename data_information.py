import pandas as pd
import os


data = pd.read_parquet('data/winequality.parquet')
print(data.dtypes)

data_size  = os.path.getsize('example-data/2025-01-01.taxi-rides.parquet')

print(f'Data Size: {data_size  / 1024 / 1024:.1f} MB')
