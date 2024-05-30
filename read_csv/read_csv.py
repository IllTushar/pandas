import pandas as pd

if __name__ == '__main__':
    # data_set = pd.read_csv(r'C:\Users\gtush\Desktop\SayaCsv\DrugBankData.csv')
    # print(data_set)

    # data_set = pd.read_csv(r'C:\Users\gtush\Desktop\SayaCsv\DrugBankData.csv', nrows=1)
    # print(data_set)

    # data_set = pd.read_csv(r'C:\Users\gtush\Desktop\SayaCsv\DrugBankData.csv', usecols=[1])
    # print(data_set)

    # data_set = pd.read_csv(r'C:\Users\gtush\Desktop\SayaCsv\DrugBankData.csv', skiprows=[1, 3])
    # print(data_set)

    data_set = pd.read_csv(r'C:\Users\gtush\Desktop\SayaCsv\DrugBankData.csv', index_col='Name')
    print(data_set)

  