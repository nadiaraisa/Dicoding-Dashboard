# Panduan Menggunakan Dashboard

1. Pastikan Anda memiliki Python dan library berikut yang terinstal:
- streamlit
- pandas
- matplotlib
- seaborn
Jika belum, maka Anda dapat menginstalnya menggunakan perintah berikut di terminal: pip install streamlit pandas matplotlib seaborn

2. Menjalankan dashboard:
Buka terminal atau command prompt di direktori tempat kode Python ("dashboard-streamlit.py") berada.
Jalankan perintah berikut: streamlit run dashboard-streamlit.py

3. Dashboard akan terbuka di browser web Anda, biasanya di alamat http://localhost:8501.

4. Di panel samping kiri, Anda dapat memilih rentang data yang ingin ditampilkan:
- "Custom date": Pilih tanggal awal dan akhir yang diinginkan.
- "All time": Tampilkan semua data.
- "7 days", "14 days", atau "30 days": Tampilkan data 7 hari, 14 hari, atau 30 hari terakhir.

5. Dashboard akan menampilkan informasi berikut:
- Jumlah total pengguna terdaftar dan pengguna kasual.
- Statistik cuaca rata-rata (suhu, suhu terasa, kelembapan, dan kecepatan angin).
- Tren jumlah pengguna berdasarkan tanggal dan musim dalam bentuk grafik garis.
- Dataframe yang menampilkan data mendetail.
- Korelasi antara atribut cuaca dan jumlah pengguna dalam bentuk heatmap dan pairplot.

4. Cara menghentikan dashboard:
Tekan Ctrl+C di terminal untuk menghentikan dashboard.

Catatan:

Pastikan file "day.csv" berada di direktori yang sama dengan kode Python.
Jika Anda mengubah nama file atau direktori, sesuaikan nama file dalam kode Python.