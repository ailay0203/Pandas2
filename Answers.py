import pandas as pd
df = pd.read_excel("people.xlsx")
# df1
df1 = df['age'].min()
# df2
df2 = df['age'].mean()
# df3
df3 = df['name'].count()
# df4
df4 = df['age'].sum()
# df5
df5 = df.loc[(df['gender'] == 'M')]
grouped = df5.groupby('gender')
# df6
df6 = df.loc[(df['age'] > 20)]
grouped2 = df6.groupby('age')
# df7
df7 = df.loc[(df['age'] > 17) |
             (df['age'] < 35)]
grouped3 = df7.groupby('age')
# df8
df8 = df.loc[(df['age'] == 9) |
             (df['age'] == 16) &
             (df['age'] == 25) |
             (df['age'] == 36) |
             (df['age'] == 49)]
grouped4 = df8.groupby('age')
# df9
df9 = df.loc[(df['gender'] == 'F')]
grouped5 = df9.groupby('name')
# df10
df10 = df.loc[(df['gender'] == 'F')]
grouped6 = df10.groupby('gender')
# df11
df11 = df.loc[(df['gender'] == 'M') & (df['name'] != 'Tal')]
grouped7 = df11.groupby('gender')
# df12
df12 = df['name'].unique()
# df13
df13 = df.groupby('name')
# df14
df14 = df.loc[(df['gender'] == 'M')]
grouped8 = df14.groupby('name')
# df15
df15 = df.groupby('name')
# df16
df16 = df.loc[(df['name'] != 'Tal')]
grouped9 = df16.groupby('gender')
# df17
df17 = df.loc[(df['name'] == 'Ido') | (df['name'] == 'Shani')]
grouped10 = df17.groupby('name')
# df18
df18 = df.loc[(df['age'] >= 20) & (df['age'] <= 30)]
# df19
df19 = df.loc[(df['age'] < 20) & (df['age'] > 30)]
# df20
df20 = df.loc[(df['gender'] == 'F') & (df['age'] == 20) | (df['age'] <= 30)]
# df21
df21 = df.groupby('gender')
# df22
df22 = df.groupby('gender')
# df23
df23 = df.groupby('birth_date')
# df24
df24 = df.birth_date.value_counts()
df24 = df24[df24 > 1]
# df25
df25 = df.name.value_counts()
df25 = df25[df25 > 1]

