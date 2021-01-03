import os

import pandas as pd


number_of_rows_extracted = 0
final_rows_arr = []


class NEPSEDATASETEXTRACTOR:

    def __init__(self,parent_directory_path=r'',year='2012', month='', day='', symbol='ADBL'):
        self.mainpath = parent_directory_path
        self.year = year
        self.month = month
        self.day = day
        self.symbol = symbol
        print('Object Initialized')
        self.row_array = []
        # self.column_names = []

    def does_file_exist(self, path2, file2):
        if os.path.isfile(f'{path2}\{file2}.csv'):
            print(f'{file2}.csv')
            return True
        else:
            return False

    def row_extractor(self, path11, file11):
        global final_rows_arr,number_of_rows_extracted
        fullname = path11 + '\\' + file11 + '.csv'
        # fullname = fullname + file11
        print(fullname)
        df = pd.read_csv(f"{fullname}")
        df = df.drop(['S.No','Conf.', 'VWAP', 'Vol', 'Prev. Close', 'Trans.', 'Diff', 'Range', 'Diff %', 'Range %', 'VWAP %',
                      '52 Weeks High', '52 Weeks Low'], axis=1)

        try:

            index_val = int(df[df['Symbol'] == f'{self.symbol}'].index.values)

            row_data = df.loc[index_val]

            row_data = list(row_data)
            dates1 = self.day + '/' + self.month + '/' + self.year
            row_data.append(dates1)

            # row_data.pop()

            print(row_data)
            # self.row_array.append(row_data)
            final_rows_arr.append(row_data)

        except Exception as e:
            print("Exception Caught, Exception is  ==>> ", e)

    def file_parser(self):
        self.month = ''
        self.day = ''

        for i in range(1, 13):
            for j in range(1, 32):
                if j < 10:
                    self.day = f'0{j}'
                else:
                    self.day = f'{j}'

                if i < 10:
                    self.month = f'0{i}'
                else:
                    self.month = f'{i}'

                file_name = f'{self.year}-{self.month}-{self.day}'

                if self.does_file_exist(self.mainpath, file_name) == True:
                    self.row_extractor(self.mainpath, file_name)



