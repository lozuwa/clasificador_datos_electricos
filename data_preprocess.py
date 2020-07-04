import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


class DataPreprocess(object):
  
  @staticmethod
  def load_data_from_excel(filepath=None, sheetname=None):
    assert os.path.isfile(filepath) == True, f"Ruta archivo: {filepath} no existe."
    assert sheetname != None, "sheetname no puede ser null."
    return pd.read_excel(filepath, sheet_name=sheetname)

  @staticmethod
  def preprocessing_data(X_train=None, X_valid=None, X_test=None):
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_valid = scaler.transform(X_valid)
    X_test = scaler.transform(X_test)
    return X_train, X_valid, X_test

  @staticmethod
  def split_dataset(data_input=None, data_output=None, test_size=None):
    x_d1, x_d2, y_d1, y_d2 = train_test_split(data_input, data_output, test_size=test_size, random_state=0)
    return x_d1, x_d2, y_d1, y_d2

