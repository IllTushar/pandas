import pandas as pd

if __name__ == '__main__':
    series = pd.Series(data=[1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], dtype=float)
    print(series)
    print(type(series))

    series1 = pd.Series(data=12, index=[1, 2, 3, 4, 5])
    print(series1)
