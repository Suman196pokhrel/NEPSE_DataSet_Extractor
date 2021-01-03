# Python Script for Indivisual Company Selection and csv file creaction


from Nepse_Dataset_Extracter_Final_LOGIC_1_copy import NEPSEDATASETEXTRACTOR,final_rows_arr
import pandas as pd

column_names = [] # Executes ONly ONce
column_headers = ['Symbol','Open','Close','High','Low','Turnover','Date']

def column_names_extractore():
    dffa = pd.read_csv(
        r'D:\Coding-Projects\pandas_full_tut\Nepali_Stock_Market _Data__2012-2020\2012\2012-01-01.csv')
    for i in dffa['Symbol']:
        column_names.append(f'{i}')
    print('COLUMN EXTRACTION COMPLETED')
    return column_names


column_names_extractore()


class Nepse_Dataset_Extractor_Final_Class:
    global column_names,column_headers

    def __init__(self, company_symbol='ADBL',main_path=r'', save_to='',column_names1=column_names):
        self.main_path = main_path
        self.save_to = save_to
        self.company_symbol = company_symbol
        self.column_names1 = column_names
        self.column_headers = column_headers


    def datalist_creator(self):
        for i in range(2012, 2021):
            path1 = self.main_path + '\\' + str(i)

            obj = NEPSEDATASETEXTRACTOR(parent_directory_path=path1, year=str(i), month='', day='',
                                        symbol=self.company_symbol)
            obj.file_parser()


    def dataset_converter(self):
        from Nepse_Dataset_Extracter_Final_LOGIC_1_copy import final_rows_arr

        final_df = pd.DataFrame(final_rows_arr, columns=self.column_headers)


        final_df.to_csv(self.save_to)
        final_rows_arr.clear()



