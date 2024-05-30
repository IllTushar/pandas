import pandas as pd

if __name__ == '__main__':
    data_set = {"A": [1, 2, 3, 4], "B": [11, 22, 33, 44]}
    data_frame = pd.DataFrame(data_set)

    # Add
    data_frame['C'] = data_frame['A'] + data_frame['B']
    print(data_frame)

    # Sub
    data_frame['C'] = data_frame['A'] - data_frame['B']
    print(data_frame)

    # Multiply
    data_frame['C'] = data_frame['A'] * data_frame['B']
    print(data_frame)

    # Divide
    data_frame['C'] = data_frame['A'] / data_frame['B']
    print(data_frame)

    # Boolean
    # Sub
    data_frame['C'] = data_frame['A'] <= 5
    print(data_frame)
