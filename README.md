# Tugas-UAS-Program
*Deskripsi Program*

Program ini adalah sistem pencatatan nilai siswa. Terdapat tiga komponen utama:

Class Data: Untuk menyimpan data siswa dan nilainya.

Class View: Untuk menampilkan data ke layar, termasuk dalam bentuk tabel.

Class Process: Untuk memproses data, termasuk menambah siswa dan memvalidasi input.

---

# Penjelasan
*Class Data:*

Menyimpan data siswa berupa nama dan nilai.
Fungsi `add_student` digunakan untuk menambahkan data siswa ke dalam daftar.

*Class View:*

Fungsi `display_table` menampilkan data siswa dalam format tabel menggunakan library **PrettyTable**.
Fungsi `display_message` digunakan untuk menampilkan pesan singkat

*Class Process:*

Mengelola proses seperti menambahkan siswa dan menampilkan data.
Fungsi `add_student` dilengkapi validasi input dengan **try-except**.

*Main Program:*

Mengimplementasikan menu interaktif untuk pengguna.

Cara Menjalankan:

1. Simpan kode dalam file Python (misalnya `student_management.py`).

2. Jalankan file tersebut menggunakan terminal/command prompt.

3. Pilih opsi dari menu untuk menambahkan atau menampilkan data siswa.

---

*1. Tambahkan Screenshot Hasil Eksekusi*

Jalankan programmu di terminal, seperti contoh output berikut:

Menu:
1. Add Student
2. Show Students
3. Exit
Choose an option: 1
Enter student name: John
Enter student score (0-100): 90
Student added successfully!

Menu:
1. Add Student
2. Show Students
3. Exit
Choose an option: 2
+----+-------+-------+
| No | Name  | Score |
+----+-------+-------+
|  1 | John  |   90  |
+----+-------+-------+

Ambil screenshot terminal yang menampilkan hasil tersebut, kemudian:

1. Simpan file gambar (misalnya output.png) ke repositorimu.


2. Perbarui file README.md dengan menambahkan gambar, seperti ini:

## Hasil Output
Berikut adalah contoh hasil eksekusi program:

![](<Output program_20250101_233404_782_4.jpg>)

---

*2. Tambahkan Penjelasan Hasil Program*

Tambahkan penjelasan tentang bagaimana program bekerja, misalnya:

## Cara Kerja Program
1. Program memiliki tiga menu utama:
   - Tambah data mahasiswa.
   - Tampilkan data mahasiswa.
   - Keluar dari program.

2. Pengguna memasukkan nama dan nilai mahasiswa. Program akan memvalidasi input sebelum menyimpan data.

3. Data mahasiswa ditampilkan dalam tabel.

### Contoh Output
Berikut adalah contoh eksekusi program:
- **Menambahkan Data Mahasiswa**
  ```plaintext
  Enter student name: Alice
  Enter student score (0-100): 85
  Student added successfully!

Menampilkan Data Mahasiswa

+----+-------+-------+
| No | Name  | Score |
+----+-------+-------+
|  1 | Alice |   85  |
+----+-------+-------+
