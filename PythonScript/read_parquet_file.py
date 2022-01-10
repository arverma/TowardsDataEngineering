import pyarrow.parquet as pq

table = pq.read_table("<FileName>.parquet")
pd = table.to_pandas()
print(pd.head)
# print(pd.columns)
