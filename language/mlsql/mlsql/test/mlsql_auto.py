import mlsql
from mlsql import execute

query = 'READ "data/auto.csv" (separator = "\s+", header = 0)\
 REPLACE ("?", "mode") SPLIT (train = .8, test = .2, validation = .0)\
  REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = simple)'

def run_auto(verbose=False):
    return execute(query, verbose=verbose)
    pass
if __name__ == "__main__":
	run_auto(False)
