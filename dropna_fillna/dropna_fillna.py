import pandas as pd

if __name__ == '__main__':
    read_csv = pd.read_csv(r'C:\Users\gtush\Desktop\SayaCsv\DrugBankData.csv')
    print(read_csv.columns)
    # drop complete row if any col contain NaN
    csv = read_csv.dropna(axis=0)

    # print(csv)

    csv1 = read_csv.dropna(subset=['Generic Name'])
    # print(csv1)

    csv2 = read_csv.fillna('python')
    # print(csv2)

    print(read_csv.fillna({"Name": "python", "Modified Name": "Java", "Description": "C"
                              , "Drug Weight": 'C++', "Generic Name": "Rust"}))
