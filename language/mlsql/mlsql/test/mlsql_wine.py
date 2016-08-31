import mlsql
from mlsql import execute

query = 'READ "data/wine.csv" (separator = ";", header = 0) SPLIT (train = .8, test = 0.2) CLASSIFY (predictors = [1,2,3,4,5,6,7,8,9,10,11], label = 12, algorithm = knn)'

def run_wine(verbose=False):
    return execute(query, verbose=verbose)
if __name__ == "__main__":
    run_wine(False)
