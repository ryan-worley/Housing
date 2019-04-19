import numpy as np
import pandas as pd
import var
import collections
import math
import time
import os
import sys
from sklearn import preprocessing

df = pd.load_csv('Train.csv')

######################### To Do ####################
# Scale Data
# Split data into different categories of features, 2 pandas
# Identify all features into different cases


def discreteFeatures(dictionary, df, title):
    for key, val in dictionary.items():
        col = 'title' + val
        df.loc[:, col] = df.where(df.loc[:, title] == key, 1, 0)
    return df

def scaleFeatures(df):
    scaler = preprocessing.StandardScaler()
    scaler.fit(df)
    scaler.transform(X_train)
    return scaler

def
