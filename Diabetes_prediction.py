# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:01:47 2018

@author: Anand
"""
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


diabetes = pd.read_csv('diabetes.csv')
print("Diabetes data set dimension:{}".format(diabetes.shape))

diabetes.groupby('Outcome').hist(figsize = (9,9))
diabetes.isnull().sum()

print(diabetes[diabetes.BloodPressure == 0].groupby('Outcome')['Age'].count())

import seaborn as sns
axis = sns.barplot