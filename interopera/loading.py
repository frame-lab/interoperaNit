import pandas as pd
import pandasql as psql

bigbase = pd.read_csv('csv/bigbase.csv',
                      encoding='utf8',
                      dtype=object)
query_base = ''


def pandaBoolean(query):
    global query_base
    query_base = bigbase.query(query)
    query_base.head()


def pandaSQL(query):
    global query_base
    query_base = psql.sqldf(query)
    query_base.head()
    query_base.to_csv(f'results/query.csv', index=False)


def export2CSV(path):
    query_base.to_csv(path, index=False)
