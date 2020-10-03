# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:28:00 2020

@author: ryank
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_train = pd.read_csv('C:/Users/ryank/OneDrive/Desktop/Year 3/Semester 1/Group Project/train.csv')
df_test = pd.read_csv('C:/Users/ryank/OneDrive/Desktop/Year 3/Semester 1/Group Project/test.csv')

#print(df_train.shape)

#print(df_test.shape)

print(df_train.head())

#Check if there are missing values
total = df_train.isnull().sum().sort_values(ascending=False)
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total','Percent'])

#print(missing_data.head(20))

#fill in the missing values
df_train['Gender'] = df_train['Gender'].fillna(df_train['Gender'].dropna().mode().values[0])
df_train['Married'] = df_train['Married'].fillna(df_train['Married'].dropna().mode().values[0])
df_train['Dependents'] = df_train['Dependents'].fillna(df_train['Dependents'].dropna().mode().values[0])
df_train['Self_Employed'] = df_train['Self_Employed'].fillna(df_train['Self_Employed'].dropna().mode().values[0])
df_train['LoanAmount'] = df_train['LoanAmount'].fillna(df_train['LoanAmount'].dropna().mode().values[0])
df_train['Loan_Amount_Term'] = df_train['Loan_Amount_Term'].fillna(df_train['Loan_Amount_Term'].dropna().mode().values[0])
df_train['Credit_History'] = df_train['Credit_History'].fillna(df_train['Credit_History'].dropna().mode().values[0])

#Check that missing values are filled in
total = df_train.isnull().sum().sort_values(ascending=False)
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total','Percent'])
#print(missing_data.head(20))


'''#Explore the data through visualization
sns.countplot(y='Gender', hue='Loan_Status', data=df_train)
sns.countplot(y='Married', hue='Loan_Status', data=df_train)
sns.countplot(y='Education', hue='Loan_Status', data=df_train)
sns.countplot(y='Self_Employed', hue='Loan_Status', data=df_train)
sns.countplot(y='Loan_Amount_Term', hue='Loan_Status', data=df_train)
sns.countplot(y='Property_Area', hue='Loan_Status', data=df_train)

#Examine applicants income by comparing different factors e.g do married males have the highest income
grid = sns.FacetGrid(df_train, row='Gender', col='Married', size=2.2, aspect=1.6)
grid.map(plt.hist, 'ApplicantIncome', alpha=.5, bins=10)
grid.add_legend()

grid = sns.FacetGrid(df_train, row='Gender', col='Education', size=2.2, aspect=1.6)
grid.map(plt.hist, 'ApplicantIncome', alpha=.5, bins=10)
grid.add_legend()

grid = sns.FacetGrid(df_train, row='Gender', col='Married', size=2.2, aspect=1.6)
grid.map(plt.hist, 'ApplicantIncome', alpha=.5, bins=10)
grid.add_legend()

grid = sns.FacetGrid(df_train, row='Married', col='Dependents', size=2.2, aspect=1.6)
grid.map(plt.hist, 'ApplicantIncome', alpha=.5, bins=10)
grid.add_legend()

grid = sns.FacetGrid(df_train, row='Education', col='Credit_History', size=2.2, aspect=1.6)
grid.map(plt.hist, 'ApplicantIncome', alpha=.5, bins=10)
grid.add_legend()
'''

#map string values to int 
code_numeric = {'Male': 1, 'Female':2, 'Yes': 1, 'No' : 2, 'Graduate': 1, 'Not Graduate': 2, 
                'Urban': 3, 'Semiurban': 2, 'Rural': 1, 'Y': 1, 'N': 0, '3+': 3}

df_train = df_train.applymap(lambda s: code_numeric.get(s) if s in code_numeric else s)
df_test = df_test.applymap(lambda s: code_numeric.get(s) if s in code_numeric else s)

#drop unique loans id
df_train.drop('Loan_ID', axis=1, inplace=True)

#print(df_train['Dependents'].value_counts())

#print(df_train.info())

#dependents is object so need to convert to int
Dependents = pd.to_numeric(df_train.Dependents)
Dependents_ = pd.to_numeric(df_test.Dependents)

df_train.drop(['Dependents'], axis=1, inplace=True)
df_test.drop(['Dependents'], axis=1, inplace=True)

df_train = pd.concat([df_train, Dependents], axis=1)
df_test = pd.concat([df_test, Dependents_], axis=1)

#nprint(df_train.info())

#sns.heatmap(df_train.corr())

#seperate target for training 
y = df_train['Loan_Status']
X = df_train.drop('Loan_Status', axis=1)


from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
#from sklearn.metrics import accuracy_score
#from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

#split data: 80% for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

model = LogisticRegression()

model.fit(X_train, y_train)


#print(model)
#print(X)


def getApplicantDetails():
    #get user input
    gender = input("gender (m/f): ")
    if(gender == 'm'):
        gender = 1;
    elif(gender == 'f'):
        gender = 2;
    
    married = input("married (y/n): ")
    if(married == 'y'):
        married = 1;
    elif(married == 'n'):
        married = 2;
        
    education = input("graduate (y/n): ")
    if(education == 'y'):
        education = 1;
    elif(education == 'n'):
        education = 2;
        
    self_employed = input("self employed (y/n): ")
    if(self_employed == 'y'):
        self_employed = 1;
    elif(self_employed == 'n'):
        self_employed = 2;
        
    applicant_income = int(input("applicant income: "))
    
    coapplicant_income = int(input("coapplicant income: "))
    
    loan_amount = int(input("loan amount: "))
    
    loan_amount_term = int(input("loan amount term (60/120/180/360/480): "))
    
    credit_history = input("credit history (y/n): ")
    if(credit_history == 'y'):
        credit_history = 1;
    elif(credit_history == 'n'):
        credit_history = 2;
        
    property_area = input("property area: (u/r/s): ")
    if(property_area == 'u'):
        property_area = 1;
    elif(property_area == 'r'):
        property_area = 2;
    elif(property_area == 's'):
        property_area = 3;
        
    dependents = int(input("number of dependents: "))

    applicant_data = [[gender, married, education, self_employed, applicant_income, coapplicant_income, loan_amount, 
                   loan_amount_term,  credit_history, property_area, dependents]]
    
    return applicant_data


#ypred = model.predict(X_test)

#use model to make prediction
#print(df_test.head(20))
#df_test.drop('Loan_ID', axis=1, inplace=True)
applicant_data = getApplicantDetails()
prediction = model.predict(applicant_data)
print("Logistic Regression: ", end = " ")
if prediction == 1:
    print("approve")
else:
    print("reject")
#print(prediction)

model = LogisticRegression()

#evaluation = f1_score(y_test, prediction)
#print(evaluation)


#accuracy = accuracy_score(y_test, prediction)
#print(accuracy)



tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

ypred_tree = tree.predict(applicant_data)

print("Decison Tree: ", end = " ")
if ypred_tree == 1:
    print("approve")
else:
    print("reject")

forest = RandomForestClassifier()
forest.fit(X_train, y_train)

ypred_forest = forest.predict(applicant_data)

print("Random Forest: ", end = " ")
if ypred_forest == 1:
    print("approve")
else:
    print("reject")

#evaluation_forest = f1_score(y_test, ypred_forest)

#print(evaluation_forest)

