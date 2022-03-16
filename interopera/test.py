import pandas as pd

bigbase = pd.read_csv('samples/familia_logradouro.csv',
                      encoding='utf8',
                      quotechar='"',
                      sep=',',
                      dtype=object)
print(bigbase.loc[:, "nome"][0])
