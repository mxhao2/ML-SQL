import mlsql
import os
from mlsql import execute
from get_data import download_file

query = 'READ "data/train.csv" (separator = ",", header = 0) \
REPLACE ("NaN", "mode") SPLIT (train = .8, test = 0.2) \
CLASSIFY (predictors = [1,3,4,5,6,7,8,9,10,11,12], label = 2, algorithm = forest)'

path = 'data/titanic'
index = 8
def run_titanic(verbose=False):
    if not os.path.exists(path):
        download_file(index)
    return execute(query, verbose=verbose)

if __name__ == "__main__":
    run_titanic(False)
