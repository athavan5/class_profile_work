import os
import pylab as pl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectKBest, chi2

df = pd.read_csv('./BME25-Class-Profile/data/datasets/final_raw_1AB_info.csv')

df.rename(columns = {'aHardBme101': 'Difficulty of BME 101', 'aHardBme101L': 'Difficulty of BME 101L',
'aHardBme121': 'Difficulty of BME 121', 'aHardBme161': 'Difficulty of BME 161',
'aHardBme181': 'Difficulty of BME 181', 'aHardSyde111': 'Difficulty of SYDE 111',
'aHardSyde113': 'Difficulty of SYDE 113'}, inplace = True)

df.rename(columns = {'bHardBme162': 'Difficulty of BME 162', 'bHardBme186': 'Difficulty of BME 186',
'bHardBme122': 'Difficulty of BME 122', 'bHardSyde112': 'Difficulty of SYDE 112',
'bHardSyde114': 'Difficulty of SYDE 114', 'diffLvlCse': 'Difficulty of CSE'}, inplace = True)


#Scatter Plots (correlating between High School and University Grades)
df.rename(columns = {'aGrade': '1A Average (GPA)', 'bGrade': '1B Average (GPA)'}, inplace = True)
df.rename(columns = {'admitGrade': 'Admission Average (%)'}, inplace = True)

for num in range(1, len(df)):
    if df.loc[num, "1A Average (GPA)"] > 4.0:
        df.loc[num, "1A Average (GPA)"] = (df.loc[num, "1A Average (GPA)"]/20.0)-1.0

for num in range(1, len(df)):
    if df.loc[num, "1B Average (GPA)"] > 4.0:
        df.loc[num, "1B Average (GPA)"] = (df.loc[num, "1B Average (GPA)"]/20.0)-1.0

print("Total number of rows in dataset = {}".format(df.shape[0]))
print("Total number of columns in dataset = {}".format(df.shape[1]))



school = ['AP, Gifted', 'IB, Gifted', 'AP, University Courses', 'AP, French Immersion']

df['hsEnrichment'] = df['hsEnrichment'].replace(school, 'More than 1 program')

#Check to see if values were properly cleaned
print(df['hsEnrichment'].value_counts()) 


#Cleaning data (to create word cloud)

igor = ['Igor ❤️❤️', 'Igor', 'Igor ', 'Professor Igor', 'Prof Igor', 'Dr. Igor Ivkovic', 'Igor Igkovic',
'Igor :\'(', 'IGOR!!!!', 'Prof. Igor', 'Igor <3', 'Igor, always', 'igor <3', 'Igor ;;w;;', 'Professor Igor Ivkovic']

sean = ['Sean', 'Sean Speziale', 'Sean is a gem', 'Sean ', 'Sean Speziale ', 'Sean speziale',
'Sean!']

freeman = ['Freeman', 'George Freeman', 'freeman ', '121 prof']
howcroft = ['jenny', 'Howcroft', 'Howcroft ', 'Howcroft 100%']


df.aFavProf = df.aFavProf.replace(igor, 'Igor Ivkovic')
df.aFavProf = df.aFavProf.replace(sean, 'Sean Speziale')
df.aFavProf = df.aFavProf.replace(freeman, 'George Freeman')
df.aFavProf = df.aFavProf.replace(howcroft, 'Jenny Howcroft')
df.aFavProf = df.aFavProf.replace('Chrys', 'Chrystopher L. Nehaniv')

print(df.bFavProf.value_counts())
print("\n")

sean_2 = ['sean ', 'Speziale', 'Sean is a gem', 'Prof. Sean', 'Prof. Sean Speziale ', 'sean speziale',
'Sean', 'Sean ' 'Sean Speziale ', 'Sean!', 'Sean Speziale ', 'Prof. Sean Speziale']

howcroft_2 = ['Jenny', 'Howcroft', 'Jennifer Howcroft', 'Jenny ', 'Howcroft!!!!',
'jenny howcroft? legit no one', 'Professor Howcroft']

df.bFavProf = df.bFavProf.replace(sean_2, 'Sean Speziale')
df.bFavProf = df.bFavProf.replace(howcroft_2, 'Jenny Howcroft')
df.bFavProf = df.bFavProf.replace('Nima', 'Nima Khademmohtaram')
df.bFavProf = df.bFavProf.replace(['121 Prof!', 'Pourmohammadali'], 'Homeyra Pourmohammadali')

print(df.bFavProf.value_counts())

#creates bar graph of frequency of high school programs
ax = df['hsEnrichment'].value_counts().plot.barh(rot=0, fontsize = 5)
pl.suptitle("High School Programs")

#creates scatter plots of correlations between university averages and high school admission averages
scatter = df.plot.scatter(x = 'Admission Average (%)', y = '1A Average (GPA)', c = 'Purple')
pl.suptitle("Correlation Between High School Average and 1A University GPA")

scatter = df.plot.scatter(x = 'Admission Average (%)', y = '1B Average (GPA)', c = 'Blue')
pl.suptitle("Correlation Between High School Average and 1B University GPA")

#Boxplot (Difficulty with 1B Courses)
boxplot_2 = df.boxplot(column = [
'Difficulty of BME 162',
'Difficulty of BME 186',
'Difficulty of BME 122',
'Difficulty of SYDE 112',
'Difficulty of SYDE 114',
'Difficulty of CSE'
], grid=False, rot = 15, fontsize = 5)
pl.suptitle("Difficulty of 1B Courses (1 - Easy, 10 - Hard)")

#creates pie chart of where students will work after graduation by creating a new Pandas Dataframe
my_data = pd.DataFrame(df['gradWorkDomain'].value_counts())

pie = my_data.plot.pie(subplots=True, figsize=(5,5))
plt.title("What will you work in after graduation?")

plt.show()
