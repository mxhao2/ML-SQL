import mlsql
import os
from mlsql import execute
from get_data import download_file
query = 'READ "data/spam.csv" SPLIT (train = .8, test = 0.2) CLASSIFY (predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56], label = 58, algorithm = bayes)'

path = 'data/spam.csv'
index = 7
def run_spam(verbose=False):
    if not os.path.exists(path):
        download_file(index)
    return execute(query, verbose=verbose)
if __name__ == "__main__":
    run_spam(False)
