import pandas as pd
import helper
from helper import HousingHelper
class OverViewAnalysis:
    
    def __init__(self, data):
        
        self.data = data
    
    
    def read_head(self, top=10):
        return self.data.head(top)
    
    # returning the number of rows and column information
    def get_info(self):
        row_count, col_count = self.data.shape
    
        print(f"Number of rows: {row_count}")
        print(f"Number of columns: {col_count}")
        print("================================")

        return (row_count, col_count), self.data.info()
    
    # gets number of distnict values in a given column
    def get_count(self, column_name):
        return self.data[column_name].value_counts()
    
    # getting the null count for every column
    def get_null_count(self, column_name):
        print("Null values count")
        print(self.data.isnull().sum())
        return self.data.isnull().sum()
    
    # getting the percentage of missing values
    def get_percent_missing(self):
        #Helper = helper.HousingHelper()
        Helper = HousingHelper()
        
        percent_missing = Helper.percent_missing(self.data)
        
        null_percent_df = pd.DataFrame(columns = ['column', 'null_percent'])
        columns = self.data.columns.values.tolist()
        
        null_percent_df['column'] = columns
        null_percent_df['null_percent'] = null_percent_df['column'].map(lambda x: Helper.percent_missing_for_col(self.data, x))
        
        
        return null_percent_df.sort_values(by=['null_percent'], ascending = False), percent_missing
    
    
    # returning the top property prices
    def PropPrice(self, top=10):
        
        return self.data['PropPrice'].value_counts().head(top)
    
    # returning the top property sizes
    def PropertySize(self, top=5):
        
        return self.data['PropertySize'].value_counts().head(top)
    
   