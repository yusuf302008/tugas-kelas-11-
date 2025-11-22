import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('nilai_siswa.csv')
print(data.info())
print(data.head())
print(data.describe())

print("Rata Rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])
 
# Matematika = data[data['Matpel'] == 'Matematika']
# print(Matematika)
  
# Inggris = data[data['Matpel'] == 'Bahasa Inggris']
# print( Bahasa Inggris)

# Fisika = data[data['Matpel'] == 'Fisika']
# print(Fisika)

# Indonesia = data[data['Matpel'] == 'Produktif']
# print(Produktif)

