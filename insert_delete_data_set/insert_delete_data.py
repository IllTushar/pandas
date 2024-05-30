import pandas as pd

if __name__ == '__main__':
    data_set = {"A": [1, 2, 3, 4], "B": [11, 22, 33, 44]}
    data_frame = pd.DataFrame(data_set)

    # insert data set at particular index
    data_frame.insert(loc=1, column="python", value=data_frame['A'])
    print(data_frame)

    # insert limited data
    data_frame.insert(loc=2, column='python_1', value=data_frame['B'][:2])
    print(data_frame)

    data_frame1 = data_frame.pop('python_1')
    print(data_frame)

    del data_frame['python']
    print(data_frame)
