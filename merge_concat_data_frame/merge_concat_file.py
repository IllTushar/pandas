import pandas as pd

if __name__ == '__main__':
    data_set1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [22, 33, 44, 55]})
    data_set2 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'C': [34, 55, 22, 11, 29]})

    # how = 'outer' -> union
    # how = 'inner' -> intersection
    # print(pd.merge(data_set1, data_set2, how='inner'))

    print(pd.concat([data_set1, data_set2], axis=0))


