import numpy as np
import pandas as pd

class HousingHelper:
  
  def __init__(self):
    pass
  
  def read_csv(self, csv_path, missing_values=[]):
    try:
        data = pd.read_csv(csv_path, na_values=missing_values)
        print("file read as csv")
        return data
    except FileNotFoundError:
        print("file not found")
  
  def save_csv(self, data, csv_path):
    try:
        data.to_csv(csv_path, index=False)
        print('File Successfully Saved.!!!')

    except Exception:
        print("Save failed...")

    return data
    
  def percent_missing(self, data: pd.DataFrame) -> float:

    totalCells = np.product(data.shape)
    missingCount = data.isnull().sum()
    totalMissing = missingCount.sum()
    return round((totalMissing / totalCells) * 100, 2)
  
  def percent_missing_for_col(self, data: pd.DataFrame, col_name: str) -> float:
    total_count = len(data[col_name])
    if total_count <= 0:
        return 0.0
    missing_count = data[col_name].isnull().sum()

    return round((missing_count / total_count) * 100, 2)
  
  def convert_bytes_to_megabytes(self, data: pd.DataFrame, bytes_data):

    megabyte = 1*10e+5
    megabyte_col = data[bytes_data] / megabyte

    return megabyte_col