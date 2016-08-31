import mlsql
from mlsql import execute

query = 'READ "data/computer.csv" (separator = ",", header = 0) \
SPLIT (train = .8, test = .2, validation = .0) \
REGRESS (predictors = [1,2,3,4,5,6,7,8,9], label = 10, algorithm = ridge)'

def run_computer(verbose=False):
    return execute(query, verbose=verbose)

if __name__ == "__main__":
    run_computer(False)
