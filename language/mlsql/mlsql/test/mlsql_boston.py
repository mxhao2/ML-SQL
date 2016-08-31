import mlsql
from mlsql import execute

query = 'READ "data/boston.csv" (separator = "\s+", header = 0) SPLIT (train = .8, test = .2, validation = .0) REGRESS (predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13], label = 14, algorithm = elastic)'

def run_boston(verbose=False):
    return execute(query, verbose=verbose)
if __name__ == "__main__":
    run_boston(False)
