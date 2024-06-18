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

# Menghapus spasi atau karakter khusus dari nama kolom
data.columns = data.columns.str.strip().str.replace(';', '')

# Mengisi nilai yang hilang di kolom numerik dengan median dari masing-masing kolom
numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numerical_cols] = data[numerical_cols].fillna(data[numerical_cols].median())

# Mengisi nilai yang hilang di kolom kategorikal dengan modus dari masing-masing kolom
categorical_cols = data.select_dtypes(include=['object']).columns
for col in categorical_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Mengonversi kolom tanggal ke format datetime
if 'join_date' in data.columns:
    data['join_date'] = pd.to_datetime(data['join_date'], errors='coerce').dt.strftime('%Y-%m-%d')

# 4. Eksplorasi data awal
# Menghitung statistik deskriptif
print("\nStatistik deskriptif:")
print(data.describe(include='all'))

# 5. Visualisasi dasar

# Diagram Batang (Bar Chart)
plt.figure(figsize=(10, 6))
sns.barplot(x='department', y='salary', data=data, palette='viridis')
plt.title('Rata-rata Gaji per Departemen')
plt.xlabel('Departemen')
plt.ylabel('Gaji')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Diagram Garis (Line Chart)
# Membuat data waktu yang sesuai untuk plot
time_data = data.groupby('department')['salary'].mean().reset_index()
time_data['time'] = time_data.index  # Menggunakan index sebagai waktu
plt.figure(figsize=(10, 6))
sns.lineplot(x='time', y='salary', data=time_data, marker='o')
plt.title('Perubahan Rata-rata Gaji per Departemen Seiring Waktu')
plt.xlabel('Indeks Waktu')
plt.ylabel('Rata-rata Gaji')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Diagram Area (Area Chart)
plt.figure(figsize=(10, 6))
plt.fill_between(time_data['time'], time_data['salary'], color='skyblue', alpha=0.4)
plt.plot(time_data['time'], time_data['salary'], color='Slateblue', alpha=0.6, linewidth=2)
plt.title('Area Chart dari Rata-rata Gaji per Departemen Seiring Waktu')
plt.xlabel('Indeks Waktu')
plt.ylabel('Rata-rata Gaji')
plt.tight_layout()
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
data['salary'].hist(bins=30, color='purple')
plt.title('Distribusi Gaji')
plt.xlabel('Gaji')
plt.ylabel('Frekuensi')
plt.tight_layout()
plt.show()

# Scatter plot untuk melihat hubungan antara dua variabel numerik
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='salary', data=data)
plt.title('Scatter Plot antara Usia dan Gaji')
plt.xlabel('Usia')
plt.ylabel('Gaji')
plt.tight_layout()
plt.show()

# Heatmap dari matriks korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Heatmap dari Matriks Korelasi')
plt.tight_layout()
plt.show()


# Tampilkan data yang sudah dibersihkan
print("\nData yang sudah dibersihkan:")
print(data) 

# Simpan data yang sudah dibersihkan ke file baru
data.to_csv('data_pembersih.csv', index=False)
print("\nData yang sudah dibersihkan disimpan ke 'data_pembersih.csv'.")