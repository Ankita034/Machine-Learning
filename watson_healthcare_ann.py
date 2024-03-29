
# -*- coding: utf-8 -*-
"""watson_healthcare_ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ai_JwMwfvtfxK29ibWxcR2lxbWPOq5Hm
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import random

watson_data=pd.read_csv("/content/watson_healthcare_modified.csv")
watson_data.head()

watson_data.info()

watson_data.isna().sum()

watson_data.dtypes

watson_data.drop("EmployeeID",axis=1,inplace=True)

watson_data.drop("MaritalStatus",axis=1,inplace=True)

watson_data.drop("Over18",axis=1,inplace=True)

watson_data.dtypes

watson_data.OverTime.values

def col_unique_value(d):
  for col in d:
    print(col,":",d[col].unique())

col_unique_value(watson_data)

watson_data_pro=pd.get_dummies(data=watson_data,columns=["BusinessTravel","Department","EducationField","JobRole"])

watson_data_pro

from sklearn.preprocessing import MinMaxScaler

col_unique_value(watson_data_pro)

col_to_scale=["Age","Attrition","DailyRate","DistanceFromHome","Education","EmployeeCount","EnvironmentSatisfaction","HourlyRate","JobInvolvement","JobLevel","JobSatisfaction","MonthlyIncome","MonthlyRate","NumCompaniesWorked","OverTime","PercentSalaryHike","PerformanceRating","RelationshipSatisfaction","StandardHours","Shift","TotalWorkingYears","TrainingTimesLastYear","WorkLifeBalance","YearsAtCompany","YearsInCurrentRole","YearsSinceLastPromotion","YearsWithCurrManager","BusinessTravel_Non-Travel","BusinessTravel_Travel_Frequently","BusinessTravel_Travel_Rarely","Department_Cardiology","Department_Maternity","Department_Neurology","EducationField_Human Resources", "EducationField_Life Sciences",
"EducationField_Marketing","EducationField_Medical","EducationField_Other","EducationField_Technical Degree","JobRole_Admin","JobRole_Administrative","JobRole_Nurse","JobRole_Other","JobRole_Therapist"]
scaler=MinMaxScaler()
watson_data_pro[col_to_scale]=scaler.fit_transform(watson_data_pro[col_to_scale])

watson_data_pro

col_unique_value(watson_data_pro)

yes_no_col=["Attrition","OverTime","Gender"]

for i in yes_no_col:
  watson_data_pro[i].replace({"Yes":1,"No":0},inplace=True)
  watson_data_pro[i].replace({'Female':0,'Male':1},inplace=True)

col_unique_value(watson_data_pro)

watson_data_pro.dtypes

X=watson_data_pro.drop("Attrition",axis="columns")
y=watson_data_pro["Attrition"]

X=pd.get_dummies(X)
X

from sklearn.model_selection  import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

X_train.shape,X_test.shape,y_train.shape,y_test.shape

model=keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(1,input_shape=(44,),activation='sigmoid',kernel_initializer='ones',bias_initializer='zeros')])

model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=["accuracy"])
model.fit(X_train,y_train,epochs=100)

model=keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(1,input_shape=(44,),activation='sigmoid',kernel_initializer='ones',bias_initializer='zeros')])

model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=["accuracy"])
model.fit(X_test,y_test,epochs=100)

model.get_weights()

model.evaluate(X_test,y_test)

y_test_pre1=model.predict(X_test)

y_test_label1=[np.argmax(i) for i in y_test_pre1]
y_test_label1=np.array(y_test_label1)

y_test_label1.shape

cm1=tf.math.confusion_matrix(y_test,y_test_label1)
type(cm1)

sns.heatmap(cm1, annot=True, fmt="d")

