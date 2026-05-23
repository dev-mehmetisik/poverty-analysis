import duckdb
import pandas as pd

pd.set_option("display.max_columns", None)   # show all columns
pd.set_option("display.max_rows", None)      # show all rows
pd.set_option("display.width", None)         # don't wrap at terminal width
pd.set_option("display.max_colwidth", None)  # don't truncate cell contents

results = duckdb.sql(results = duckdb.sql("""
    SELECT *
    FROM 'data/dataset.csv'
    WHERE country = 'USA'
       OR country = 'Germany'
       OR country = 'Turkey'
""").df()).df()
print (results)