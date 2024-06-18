Soal Kasus Analisis Data Karyawan Deskripsi Kasus Perusahaan ABC memiliki data karyawan yang berisi informasi mengenai ID, nama, usia, gaji, departemen, dan tanggal bergabung. Manajemen perusahaan ingin melakukan analisis terhadap data ini untuk memahami distribusi usia dan gaji karyawan, hubungan antara usia dan gaji, serta tren dan distribusi karyawan berdasarkan departemen dan tahun bergabung.

Tugas

Memuat Data: Muatlah data dari file CSV yang bernama your_data.csv

Memahami Struktur Data: Tampilkan 5 baris pertama dari data yang telah dimuat. Tampilkan tipe data dari setiap kolom dalam data.

Membersihkan Data: Periksa apakah ada nilai yang hilang di setiap kolom dalam data. Jika terdapat nilai yang hilang, isilah nilai yang hilang tersebut dengan median dari kolom yang bersangkutan.

Eksplorasi Data Awal: Hitung statistik deskriptif dari kolom numerik dalam data. Buat histogram untuk melihat distribusi dari kolom 'age' dan 'salary'. Buat scatter plot untuk melihat hubungan antara kolom 'age' dan 'salary'. Buat heatmap dari matriks korelasi antara kolom numerik dalam data.

Analisis Tambahan: Hitung rata-rata gaji per department. Hitung jumlah karyawan per department. Buat bar plot untuk visualisasi jumlah karyawan per department. Buat line plot untuk melihat trend jumlah karyawan yang bergabung per tahun.

4.2 Visualisasi Hasil
Dari data-data diatas, diolah dengan kode python menghasilkan visualisasi dari data data diatas, berikut hasil visualisasinya.

 (gambar 1)
![image](https://github.com/noelsagara/UASPengkodeandanPemrograman/assets/166829920/bb9faf18-c998-4e49-ac94-215c39f66cb7)

Grafik yang ditampilkan adalah diagram batang yang menunjukkan distribusi gaji rata-rata berdasarkan departemen. Berikut adalah interpretasi dari grafik tersebut:
•	Sumbu X (Horizontal): Menunjukkan berbagai departemen yang terdiri dari Sales, Marketing, HR, Finance, dan IT.
•	Sumbu Y (Vertikal): Menunjukkan jumlah gaji dalam satuan yang tertera.
•	Batang (Bar): Menunjukkan gaji rata-rata untuk setiap departemen.
•	Garis Vertikal (Error Bar): Menunjukkan rentang variabilitas atau deviasi standar dari gaji di setiap departemen.
Pengamatan dari Grafik:
•	Departemen dengan Gaji Tertinggi: Departemen Finance memiliki gaji rata-rata tertinggi, mencapai sekitar 85.000.
•	Departemen dengan Gaji Terendah: Departemen IT memiliki gaji rata-rata terendah, sekitar 50.000.
•	Variabilitas Gaji: Error bar pada setiap batang menunjukkan rentang variabilitas gaji di masing-masing departemen. Finance memiliki variasi yang cukup besar, sedangkan IT memiliki variasi yang relatif kecil.
•	Gaji di Departemen Lain:
o	Sales memiliki gaji rata-rata sekitar 65.000.
o	Marketing memiliki gaji rata-rata sekitar 55.000.
o	HR memiliki gaji rata-rata sekitar 45.000.
Ini memberikan gambaran bahwa terdapat variasi gaji yang signifikan di antara berbagai departemen dalam perusahaan. Finance tampaknya menjadi departemen dengan kompensasi tertinggi, sedangkan IT memiliki gaji rata-rata terendah. Variabilitas gaji juga bervariasi, dengan beberapa departemen menunjukkan rentang yang lebih luas dibandingkan yang lain.

 (gambar 2)
![image](https://github.com/noelsagara/UASPengkodeandanPemrograman/assets/166829920/ad571f99-42d5-4876-b231-cce0c6ae3121)

Grafik yang ditampilkan adalah diagram garis yang menunjukkan distribusi gaji rata-rata berdasarkan departemen. Berikut adalah interpretasi dari grafik tersebut:
•	Sumbu X (Horizontal): Menunjukkan indeks departemen.
•	Sumbu Y (Vertikal): Menunjukkan jumlah gaji rata-rata dalam satuan yang tertera.
•	Titik (Point): Menunjukkan gaji rata-rata untuk setiap departemen.
•	Warna Titik: Menunjukkan departemen yang berbeda berdasarkan legenda.
Pengamatan dari Grafik:
•	Departemen dengan Gaji Tertinggi:
o	Departemen Finance memiliki gaji rata-rata tertinggi, mencapai sekitar 85.000.
•	Departemen dengan Gaji Terendah:
o	Departemen HR memiliki gaji rata-rata terendah, sekitar 45.000.
•	Gaji di Departemen Lain:
o	IT memiliki gaji rata-rata sekitar 50.000.
o	Marketing memiliki gaji rata-rata sekitar 55.000.
o	Sales memiliki gaji rata-rata sekitar 65.000.
Ini memberikan gambaran bahwa terdapat variasi gaji yang signifikan di antara berbagai departemen dalam perusahaan. Finance tampaknya menjadi departemen dengan kompensasi tertinggi, sedangkan HR memiliki gaji rata-rata terendah. Grafik ini dapat membantu dalam analisis lebih lanjut terkait struktur gaji dan pengambilan keputusan mengenai kebijakan kompensasi di perusahaan.

 (gambar 3)
![image](https://github.com/noelsagara/UASPengkodeandanPemrograman/assets/166829920/007e12ae-6b6d-4dc1-b210-28154d095b76)

Grafik yang ditampilkan adalah diagram area yang menunjukkan distribusi gaji rata-rata berdasarkan departemen. Berikut adalah interpretasi dari grafik tersebut:
•	Sumbu X (Horizontal): Menunjukkan indeks departemen.
•	Sumbu Y (Vertikal): Menunjukkan jumlah gaji rata-rata dalam satuan yang tertera.
•	Area Berwarna: Menunjukkan total gaji rata-rata di setiap departemen, dengan warna biru muda mengisi area di bawah garis.
Pengamatan dari Grafik:
•	Departemen dengan Gaji Tertinggi:
o	Departemen Finance memiliki gaji rata-rata tertinggi, mencapai sekitar 85.000.
•	Departemen dengan Gaji Terendah:
o	Departemen HR memiliki gaji rata-rata terendah, sekitar 45.000.
•	Gaji di Departemen Lain:
o	IT memiliki gaji rata-rata sekitar 50.000.
o	Marketing memiliki gaji rata-rata sekitar 55.000.
o	Sales memiliki gaji rata-rata sekitar 65.000.
Ini memberikan gambaran bahwa terdapat variasi gaji yang signifikan di antara berbagai departemen dalam perusahaan. Finance tampaknya menjadi departemen dengan kompensasi tertinggi, sedangkan HR memiliki gaji rata-rata terendah. Grafik ini dapat membantu dalam analisis lebih lanjut terkait struktur gaji dan pengambilan keputusan mengenai kebijakan kompensasi di perusahaan.

 (gambar 4)
![image](https://github.com/noelsagara/UASPengkodeandanPemrograman/assets/166829920/b5ad328d-c858-46c4-8f71-f5f1d95b6e0f)

Grafik yang ditampilkan adalah histogram yang menunjukkan distribusi gaji rata-rata berdasarkan departemen. Berikut adalah interpretasi dari grafik tersebut:
•	Sumbu X (Horizontal): Menunjukkan rentang gaji rata-rata.
•	Sumbu Y (Vertikal): Menunjukkan frekuensi atau jumlah kejadian untuk setiap rentang gaji.
•	Batang (Bar): Menunjukkan berapa banyak data (frekuensi) yang berada dalam rentang gaji tertentu.
Pengamatan dari Grafik:
•	Rentang Gaji yang Paling Sering Muncul:
o	Rentang gaji sekitar 50.000 hingga 60.000 memiliki frekuensi tertinggi, dengan beberapa nilai mencapai hingga 2.
•	Rentang Gaji yang Lebih Jarang Muncul:
o	Rentang gaji sekitar 70.000 hingga 90.000 memiliki frekuensi yang lebih rendah, dengan sebagian besar nilai hanya mencapai 0.75.
Grafik ini memberikan gambaran bahwa sebagian besar data gaji rata-rata berkonsentrasi di rentang 50.000 hingga 60.000. Rentang gaji yang lebih tinggi seperti 70.000 hingga 90.000 jarang muncul, menunjukkan bahwa gaji rata-rata di sebagian besar departemen berada di kisaran yang lebih rendah. Ini dapat membantu dalam analisis lebih lanjut terkait struktur gaji dan pengambilan keputusan mengenai kebijakan kompensasi di perusahaan.

 (gambar 5)
![image](https://github.com/noelsagara/UASPengkodeandanPemrograman/assets/166829920/57304129-809d-4959-b9b5-f996157a505b)

Grafik yang ditampilkan adalah diagram batang yang menunjukkan distribusi gaji rata-rata berdasarkan departemen. Berikut adalah interpretasi dari grafik tersebut:
Interpretasi Grafik
1.	Sumbu X (Horizontal): Menunjukkan departemen (Sales, Marketing, HR, Finance, IT).
2.	Sumbu Y (Vertikal): Menunjukkan gaji rata-rata.
3.	Batang (Bar): Menunjukkan rata-rata gaji untuk masing-masing departemen. Setiap batang dilengkapi dengan garis error bar yang menunjukkan variasi (seperti standar deviasi atau kesalahan standar) dari gaji di setiap departemen.
Pengamatan dari Grafik:
•	Gaji Rata-Rata Tertinggi:
o	Departemen Finance memiliki gaji rata-rata tertinggi, mendekati 85.000.
•	Gaji Rata-Rata Menengah:
o	Departemen Sales memiliki gaji rata-rata sekitar 65.000.
o	Departemen IT memiliki gaji rata-rata sedikit di bawah 60.000.
•	Gaji Rata-Rata Terendah:
o	Departemen Marketing dan HR memiliki gaji rata-rata yang hampir sama, sekitar 55.000.
•	Variasi Gaji:
o	Garis error bar di atas setiap batang menunjukkan variasi gaji dalam masing-masing departemen. Finance menunjukkan variasi tertinggi, sementara IT menunjukkan variasi yang paling rendah.
Grafik ini memberikan gambaran bahwa departemen Finance memiliki gaji rata-rata tertinggi dengan variasi gaji yang cukup besar, sementara departemen Marketing dan HR memiliki gaji rata-rata yang paling rendah dengan variasi yang moderat. Ini dapat membantu dalam analisis lebih lanjut terkait struktur gaji dan pengambilan keputusan mengenai kebijakan kompensasi di perusahaan. Data ini menunjukkan bahwa mungkin ada kebutuhan untuk menilai kembali struktur gaji di departemen yang memiliki gaji lebih rendah atau mempertimbangkan penyesuaian gaji untuk mengurangi kesenjangan.

 
(Gambar 6)
![image](https://github.com/noelsagara/UASPengkodeandanPemrograman/assets/166829920/a31aa7a6-ba24-46f8-99b5-cfda409583c3)

Grafik yang ditampilkan adalah scatter plot yang menunjukkan hubungan antara usia (age) dan gaji (salary). Berikut adalah interpretasi dari grafik tersebut:
Interpretasi Grafik
•	Sumbu X (Horizontal): Menunjukkan usia karyawan.
•	Sumbu Y (Vertikal): Menunjukkan gaji karyawan.
•	Titik (Dot): Setiap titik mewakili seorang karyawan dengan nilai usia tertentu dan gaji tertentu.
Pengamatan dari Grafik:
•	Hubungan antara Usia dan Gaji:
o	Terdapat korelasi positif antara usia dan gaji. Seiring bertambahnya usia, gaji juga cenderung meningkat.
•	Usia dan Gaji yang Paling Sering Muncul:
o	Karyawan dengan usia sekitar 25 hingga 35 tahun memiliki gaji berkisar antara 50.000 hingga 60.000.
•	Usia dan Gaji yang Lebih Jarang Muncul:
o	Karyawan dengan usia di atas 40 tahun memiliki gaji yang lebih tinggi, berkisar antara 70.000 hingga 90.000.
Grafik ini memberikan gambaran bahwa terdapat korelasi positif antara usia dan gaji. Artinya, semakin bertambah usia karyawan, semakin tinggi gaji yang mereka terima. Data ini dapat digunakan untuk analisis lebih lanjut terkait dengan pengalaman kerja, lama bekerja, dan pengambilan keputusan terkait dengan promosi atau penyesuaian gaji di perusahaan. Ini juga menunjukkan bahwa karyawan yang lebih tua cenderung memiliki gaji yang lebih tinggi, yang mungkin disebabkan oleh pengalaman dan masa kerja yang lebih lama.
 
(Gambar 7)
![image](https://github.com/noelsagara/UASPengkodeandanPemrograman/assets/166829920/50d93cfd-1cff-441c-bc15-53f92f9f8ad0)

Grafik yang ditampilkan adalah heatmap yang menunjukkan matriks korelasi antara usia (age) dan gaji (salary). Berikut adalah interpretasi dari grafik tersebut:
Interpretasi Grafik
•	Sumbu X dan Y: Menunjukkan dua variabel yang dibandingkan, yaitu usia (age) dan gaji (salary).
•	Warna: Menunjukkan tingkat korelasi antara variabel. Warna merah menunjukkan korelasi positif yang tinggi, sementara warna biru menunjukkan korelasi yang lebih rendah. Skala di sebelah kanan menunjukkan nilai korelasi dari 0.95 hingga 1.00.
Pengamatan dari Grafik:
•	Korelasi Antar Variabel:
o	Korelasi antara usia dengan dirinya sendiri adalah 1, yang menunjukkan korelasi sempurna (sebagaimana diharapkan).
o	Korelasi antara gaji dengan dirinya sendiri juga adalah 1, menunjukkan korelasi sempurna.
o	Korelasi antara usia dan gaji adalah 0.95, menunjukkan korelasi positif yang sangat kuat.
Grafik heat map ini memberikan gambaran tentang seberapa kuat hubungan antara usia dan gaji. Dengan korelasi sebesar 0.95, kita dapat menyimpulkan bahwa terdapat hubungan yang sangat kuat antara usia dan gaji, di mana kenaikan usia cenderung diikuti oleh kenaikan gaji. Hal ini bisa digunakan untuk analisis lebih lanjut mengenai faktor-faktor yang mempengaruhi gaji di perusahaan, serta untuk merancang kebijakan kompensasi yang adil dan berbasis data. Korelasi yang kuat ini mungkin juga mencerminkan pentingnya pengalaman dan masa kerja dalam menentukan tingkat gaji.
