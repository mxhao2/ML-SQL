import mlsql
import os
from mlsql import execute
from get_data import download_file

query = 'READ "data/census.csv" (separator = ",", header = 0) REPLACE ("NaN", "mode") SPLIT (train = .8, test = 0.2) CLASSIFY (predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], label = 15, algorithm = logistic)'

path = 'data/census.csv'
index = 2
def run_census(verbose=False):
    if not os.path.exists(path):
        download_file(index)
    return execute(query, verbose=verbose)
if __name__ == "__main__":
    run_census(False)
