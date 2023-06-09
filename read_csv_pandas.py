import pandas as pd

df = pd.read_csv('DATA/knights.csv', header=None)
df.columns = 'name title color quest comment number ladies'.split()

print(df)

print(df.value_counts('color'))
print()

df_chi = pd.read_csv('TEMP/chi_data.csv')
print(df_chi)
print()

print(df_chi.info())
