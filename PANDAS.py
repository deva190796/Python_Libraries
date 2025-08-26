#pandas class
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = 6,5
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\FSDS\LIBRARIES\DATASETS\data.csv")
print(df)
print(len(df))
print(df.columns)
print(df.isnull())
print(df.isna())
print(df.isnull().sum())
print(df.head())
print(df.tail())
print(df.info())
print(df[1:6])
print(df.describe())
print(df['CountryName'])
print(df[['CountryName','CountryCode']])
df_cat = df[['CountryName','CountryCode','IncomeGroup']]
print(df_cat)
df_num = df[['BirthRate','InternetUsers']]
print(df_num)
df['Calc'] = df.BirthRate * df.InternetUsers    #adding new column
print(df)
df = df.drop('Calc',axis = 1)#axis 1 means column
print(df)
print(df.InternetUsers < 2)
print(df.BirthRate > 40)
Filter = df.BirthRate > 40
Filter2 = df.InternetUsers < 2
print(df[Filter & Filter2])

#
print(df[df.IncomeGroup == 'High income'])
print(df.IncomeGroup.unique())
print(df.IncomeGroup.nunique())

#visualisations
# print(df.columns)
# print(df.InternetUsers)
# vis1 = sns.displot(df['InternetUsers'])
# print(vis1)
# plt.show()
# vis2 = sns.distplot(df['InternetUsers'], bins = 15)
# plt.show()
# vis3 = sns.boxplot(data = df,x = "IncomeGroup",y = "BirthRate")
# plt.show()
# vis4 = sns.lmplot(data = df,x = "InternetUsers",y = "BirthRate",hue = 'IncomeGroup')
# plt.show()

row_0 = df.iloc[0]
print(row_0)
print(row_0['CountryName'])
print(df.iloc[[0,5,10]])
print(df.isnull().any().any())