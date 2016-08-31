import mlsql
import os
from mlsql import execute
from get_data import download_file

query = 'READ "data/iris.csv" SPLIT (train = .8, test = 0.2) CLASSIFY (predictors = [1,2,3,4], label = 5, algorithm = svm)'


path = 'data/iris.csv'
index = 5

def run_iris(verbose=False):
    print("run iris")
    if not os.path.exists(path):
        print("downloading file")
        download_file(index)
    return execute(query, verbose=verbose)

if __name__ == "__main__":
    run_iris(False)
