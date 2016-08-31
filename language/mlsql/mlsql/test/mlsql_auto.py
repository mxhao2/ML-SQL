import mlsql
import os
from mlsql import execute
from get_data import download_file

query = 'READ "data/auto.csv" (separator = "\s+", header = 0)\
 REPLACE ("?", "mode") SPLIT (train = .8, test = .2, validation = .0)\
  REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = simple)'

path = 'data/auto.csv'
index = 0
def run_auto(verbose=False):
    if not os.path.exists(path):
        download_file(index)
    return execute(query, verbose=verbose)
    pass
if __name__ == "__main__":
	run_auto(False)
