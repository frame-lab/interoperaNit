import pandas as pd
import pandasql as psql


class Consultant:
    def __init__(self) -> None:
        self.bigbase = pd.read_csv(
            'csv/bigbase.csv',
            encoding='utf8',
            dtype=object)

    def run_queries(self, queries):
        for index in range(0, len(queries)):
            self.run_query(queries[index], index)

    def run_query(self, query, index):
        splitted_query = query.split(" ")
        if splitted_query[0].upper() == "SELECT":
            query_base = psql.sqldf(query)
            query_base.to_csv(f'results/query_{index}.csv', index=False)
        else:
            query_base = self.bigbase.query(query)
            query_base.to_csv(f'results/query_{index}.csv', index=False)

