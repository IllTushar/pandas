import pandas as pd

if __name__ == '__main__':
    data_set = pd.DataFrame({"Name": ['a', 'b', 'c', 'd', 'f'],
                             "S_1": ['1', '2', '3', '4', '5']})
    name = data_set.groupby('Name')
    for x, y in name:
        print(x, y)
