from get_data import download_data
from mlsql_auto import run_auto
from mlsql_boston import run_boston
from mlsql_census import run_census
from mlsql_chronic import run_chronic
from mlsql_computer import run_computer
from mlsql_iris import run_iris
from mlsql_seeds import run_seeds
from mlsql_spam import run_spam
from mlsql_titanic import run_titanic
from mlsql_wine import run_wine



if __name__ == "__main__":
    print('\n\n\n')    
    run_auto()
    print('\n\n\n')
    run_boston()
    print('\n\n\n')
    run_census()
    print('\n\n\n')
    run_chronic()
    print('\n\n\n')
    run_computer()
    print('\n\n\n')
    run_iris()
    print('\n\n\n')
    run_spam()
    print('\n\n\n')
    run_titanic()
    print('\n\n\n')
    run_wine()
    print('\n\n\n')
    print('Accuracy Tests Complete')
