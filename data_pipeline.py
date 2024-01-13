import pandas as pd

if __name__ == '__main__':

    print(pd.__version__) #version check
    
    #main
    path = 'dataset/Titanic_dataset.xlsx'
    path2 = 'dataset/Titanic.csv'
    df = pd.read_excel(path, dtype=str,header = 0, index_col=None, usecols=None)
    df.to_csv(path2, sep = ';', index = False) #no index in csv
    print(df.head)