import os
from pprint import pprint

import mytests
import pandas as pd
import psycopg2

# import the data quality checks
from dataqualitychecks import (
    check_for_duplicates,
    check_for_min_max,
    check_for_nulls,
    check_for_valid_values,
    run_data_quality_check,
)
from tabulate import tabulate

# connect to database
pgpassword = os.environ.get("POSTGRES_PASSWORD")
conn = psycopg2.connect(
    user="postgres",
    password=pgpassword,
    host="localhost",
    port="5432",
    database="billingDW",
)

print("Connected to data warehouse")

# Start of data quality checks
results = []
tests = {
    key: value for key, value in mytests.__dict__.items() if key.startswith("test")
}

for testname, test in tests.items():
    test["conn"] = conn
    results.append(run_data_quality_check(**test))

# #print(results)
# df=pd.DataFrame(results)
# df.index+=1
# df.columns = ['Test Name', 'Table','Column','Test Passed']
# print(tabulate(df,headers='keys',tablefmt='psql'))
# #End of data quality checks
# conn.close()
# print("Disconnected from data warehouse")
