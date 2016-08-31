import mlsql
from mlsql import execute

query = 'READ "data/chronic.csv" (separator = ",", header = 0) \
REPLACE ("?", "mode") SPLIT (train = .8, test = 0.2) CLASSIFY \
(predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],\
 label = 25, algorithm = logistic)'

def run_chronic(verbose=False):
    return execute(query, verbose=verbose)
if __name__ == "__main__":
    run_chronic(False)
