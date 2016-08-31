import mlsql
from mlsql import execute

query = 'READ "data/seeds.csv" (separator = "\s+", header = 0) SPLIT (train = .8, test = .2, validation = .0) CLUSTER (predictors = [1,2,3,4,5,6,7], algorithm = kmeans)'


def run_seeds(verbose=False):
    return execute(query, verbose=verbose)
if __name__ == "__main__":
    run_seeds(False)
