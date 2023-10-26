#%%
import psycopg2
import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
import matplotlib_inline     
sns.set(color_codes=True)

connection = psycopg2.connect(
    database="analyz_dannyx",
    user="postgres",
    password="13092002",
    host="localhost",
    port=5432,
)


if connection:
    print("connection is set...")
else:
    print("connection is not set...")


query = "select * from mtcars"
df = pd.read_sql_query(query, connection)
#%%
#Деректерді деректер шеңберіне жүктеу
print(df)
#%%

print(df.head(5))
# %%
df.tail(5)
# %%
#Деректер түрлерін тексеру
df.dtypes
# %%
df = df.drop(['mpg', 'disp', 'wt', 'vs', 'am'], axis=1)
df.head(5)
# %%
#Бағандардың атын өзгерту
df = df.rename(columns={"mpg": "MPGNEW", "disp": "Disperse", "wt": "WTTT", "vs": "VVSS", "am": "MA"})
df.head(5)
# %%
#Қайталанатын жолдарды жою
df.shape
# %%
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)
# %%
df.count()
# %%
df = df.drop_duplicates()
df.head(5)
# %%
df.count()
# %%
df = df.dropna()    # Өткізіп алған мәндерді жою
df.count()
# %%
#Өткізіп алған немесе нөлдік мәндерді жою
print(df.isnull().sum())   #Мәндерді жойғаннан кейін
# %%
#Шығарындыларды анықтау
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
# %%
df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape
# %%
#Әр түрлі объектілерді бір-бірімен, жиілікпен салыстыру
df.model.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("model")
plt.ylabel('cyl')
plt.xlabel('drat');
# %%
plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c

# %%
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()
#%%
