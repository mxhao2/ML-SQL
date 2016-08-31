import mlsql
from mlsql import execute

query = 'READ "data/iris.csv" SPLIT (train = .8, test = 0.2) CLASSIFY (predictors = [1,2,3,4], label = 5, algorithm = svm)'

execute(query)

def run_iris(verbose=False):
    return execute(query, verbose=verbose)

if __name__ == "__main__":
    run_iris(False)
