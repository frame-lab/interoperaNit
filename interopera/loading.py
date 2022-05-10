import pandas as pd
import pandasql as psql

bigbase = pd.read_csv('csv/bigbase.csv',
                      encoding='utf8',
                      dtype=object)
query_base = ''


def pandaBoolean(query):
    global query_base
    query_base = bigbase.query(query)


def pandaSQL(query):
    global query_base
    query_base = psql.sqldf(query)


def export2CSV(path):
    query_base.to_csv(path, index=False)
