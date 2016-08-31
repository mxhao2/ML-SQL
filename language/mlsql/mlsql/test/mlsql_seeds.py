import mlsql
import os
from mlsql import execute
from get_data import download_file

query = 'READ "data/seeds.csv" (separator = "\s+", header = 0) SPLIT (train = .8, test = .2, validation = .0) CLUSTER (predictors = [1,2,3,4,5,6,7], algorithm = kmeans)'

path  = 'data/seeds.csv'
index = 6
def run_seeds(verbose=False):
    if not os.path.exists(path):
        download_file(index)
    return execute(query, verbose=verbose)
if __name__ == "__main__":
    run_seeds(False)
