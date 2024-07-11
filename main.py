import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dataset.csv', sep=';', header=0)



print(df.head())

import networkx as nx

G = nx.Graph()


G.add_nodes_from(df['TARIH'])
G.add_nodes_from(df["GERCEKLESEN_URETIM"])
G.add_nodes_from(df["PLANLANAN_URETIM"])


for index, row in df.iterrows():
    G.add_edge(row["PLANLANAN_URETIM"], row["GERCEKLESEN_URETIM"])


max_planned_production = df["PLANLANAN_URETIM"].max()
print("Max planned production:", max_planned_production)



df['PLANLANAN_URETIM'] = df['PLANLANAN_URETIM'].str.replace(',', '.').astype(float)
df['GERCEKLESEN_URETIM'] = df['GERCEKLESEN_URETIM'].str.replace(',', '.').astype(float)
df['DIFFERENCE'] = df["GERCEKLESEN_URETIM"] - df["PLANLANAN_URETIM"]

print(df.head())

plt.plot(df['TARIH'], df["PLANLANAN_URETIM"], label='Planned Production')
plt.plot(df['TARIH'], df['GERCEKLESEN_URETIM'], label='Actual Production')
plt.xlabel('TARIH')
plt.ylabel('Production Quantity')
plt.title('Change in Production Over Time')
plt.legend()
plt.show()

plt.hist(df['DIFFERENCE'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Production Difference')
plt.ylabel('Frequency')
plt.title('Distribution of the Difference Between Planned and Actual Production')
plt.show()
