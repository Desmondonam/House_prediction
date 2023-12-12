from helper import HousingHelper
import pandas as pd

class CleanHousingData:
    def __init__(self, data: pd.DataFrame):
        self.df = data
        
        print('Automation in Action...!!!')

    def drop_duplicate(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        data.drop_duplicates(inplace=True)

        return data

    def convert_to_datetime(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        convert column to datetime
        """

        data['salemon'] = pd.to_datetime(
            data['salemon'])
        data['saleyr'] = pd.to_datetime(
            data['saleyr'])

        return data

    def drop_columns_with_null_values(self, data: pd.DataFrame, threshold_in_percent=30) -> pd.DataFrame:
        Helper = HousingHelper()

        null_percent_df = pd.DataFrame(columns=['column', 'null_percent'])
        columns = data.columns.values.tolist()

        null_percent_df['column'] = columns
        null_percent_df['null_percent'] = null_percent_df['column'].map(
            lambda x: Helper.percent_missing_for_col(data, x))

        columns_to_be_dropped = null_percent_df[null_percent_df['null_percent']
                                                > threshold_in_percent]['column'].to_list()
        data = self.__drop_columns(data, columns_to_be_dropped)

        return data

    def drop_rows_with_null_values(self, data: pd.DataFrame, threshold_in_percent=1) -> pd.DataFrame:
        Helper = HousingHelper()

        null_percent_df = pd.DataFrame(columns=['column', 'null_percent'])
        columns = data.columns.values.tolist()

        null_percent_df['column'] = columns
        null_percent_df['null_percent'] = null_percent_df['column'].map(
            lambda x: Helper.percent_missing_for_col(data, x))
        
        columns_subset = null_percent_df[null_percent_df['null_percent']
                                         < threshold_in_percent]['column'].to_list()

        data = data.dropna(subset=columns_subset)

        return data

    def handle_missing_qantitative_data_with_mean(self, data: pd.DataFrame, method="mean"):

        numeric_data = ['int16', 'int32', 'int64',
                        'float16', 'float32', 'float64']

        all_cols = data.columns.to_list()
        num_cols = [c for c in all_cols if data[c].dtypes in numeric_data]

        if (method == "mean"):

            for col in num_cols:
                data[col] = data[col].fillna(data[col].mean())

            return data

        elif method == "ffill":

            for col in num_cols:
                data[col] = data[col].fillna(method='ffill')

            return data

        elif method == "bfill":

            for col in num_cols:
                data[col] = data[col].fillna(method='bfill')

            return data
        else:
            print("Method unknown")
            return data
    
    def handle_missing_categorical_data_with_mean(self, data: pd.DataFrame, method="ffill"):

        numeric_data = ['int16', 'int32', 'int64',
                        'float16', 'float32', 'float64']

        all_cols = data.columns.to_list()
        num_cols = [c for c in all_cols if not data[c].dtypes in numeric_data]
        
        if method == "ffill":

            for col in num_cols:
                data[col] = data[col].fillna(method='ffill')

            return data

        elif method == "bfill":

            for col in num_cols:
                data[col] = data[col].fillna(method='bfill')

            return data
        else:
            print("Method unknown")
            return data
    def __drop_columns(self, data, columns=[]):

        return data.drop(columns, axis=1)