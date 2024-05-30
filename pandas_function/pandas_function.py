import pandas as pd

if __name__ == '__main__':
    read_csv = pd.read_csv(r'C:\Users\gtush\Desktop\SayaCsv\DrugBankData.csv')

    # print data in range -> it's print 0: n-1 data
    data = read_csv.head(n=100)

    # print data in range -> it's print n-1:0 data
    data2 = read_csv.tail(n=20)
    # print(data2)

    # columns header
    print(read_csv.columns)

    # if you want to print specific col and row
    print(read_csv.loc[:2, ['Name', 'Description']])

    # if you want to print specific element of the give row x col
    print(read_csv.iloc[0, 1])

    # sort value using ascending
    print(read_csv.sort_values(by='Name', ascending=False).tail(n=5))
