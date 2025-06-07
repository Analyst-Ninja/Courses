import sqlite3

import pandas as pd

conn = sqlite3.connect("Movies.db")

query = """
        SELECT * FROM Top_50
        LIMIT 10
        """

df = pd.read_sql(query, conn)

print(df)

conn.close()
