import pandas as pd

if __name__ == '__main__':
    values = [[1, 3, 4], [2, 3, 1]]
    data_frame1 = pd.DataFrame(values)
    # print(data_frame1[0][1])

    dict = {1: ["jvj"], "a": [2], "j": [7.5]}
    data_frame2 = pd.DataFrame(dict)
    print(data_frame2)
