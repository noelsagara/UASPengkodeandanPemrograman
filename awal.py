import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Memuat data
data = pd.read_csv('data.csv')

# 2. Memahami struktur data
print("Beberapa baris pertama dari data:")
print(data.head())

print("\nTipe data dari setiap kolom:")
print(data.dtypes)

# 3. Membersihkan data
# Mengecek nilai yang hilang
print("\nJumlah nilai yang hilang di setiap kolom:")
print(data.isnull().sum())

# Mengisi nilai yang hilang di kolom numerik dengan median dari masing-masing kolom
numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numerical_cols] = data[numerical_cols].fillna(data[numerical_cols].median())

# 4. Eksplorasi data awal
# Menghitung statistik deskriptif
print("\nStatistik deskriptif:")
print(data.describe())

# 5. Visualisasi dasar

# Diagram Batang (Bar Chart)
plt.figure(figsize=(10, 6))
sns.barplot(x='department', y='salary', data=data, palette='viridis')
plt.title('Bar Chart')
plt.show()

# Diagram Garis (Line Chart)
# Membuat data waktu yang sesuai untuk plot
time_data = data.groupby('department')['salary'].mean().reset_index()
time_data['time'] = time_data.index  # Menggunakan index sebagai waktu
plt.figure(figsize=(10, 6))
sns.lineplot(x='time', y='salary', data=time_data, hue='department', marker='o')
plt.title('Line Chart')
plt.xlabel('Department Index')
plt.ylabel('Average Salary')
plt.show()

# Diagram Area (Area Chart)
plt.figure(figsize=(10, 6))
plt.fill_between(time_data['time'], time_data['salary'], color='skyblue', alpha=0.4)
plt.plot(time_data['time'], time_data['salary'], color='Slateblue', alpha=0.6, linewidth=2)
plt.title('Area Chart')
plt.xlabel('Department Index')
plt.ylabel('Average Salary')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
data['salary'].hist(bins=30, color='purple')
plt.title('Histogram')
plt.show()

# Diagram Bagan (Chart Diagram)
plt.figure(figsize=(10, 6))
sns.catplot(x='department', y='salary', kind='bar', data=data, palette='muted')
plt.title('Chart Diagram')
plt.show()

# Scatter plot untuk melihat hubungan antara dua variabel numerik
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='salary', data=data)
plt.title('Scatter Plot antara age dan salary')
plt.show()

# Heatmap dari matriks korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Heatmap dari Matriks Korelasi')
plt.show()
