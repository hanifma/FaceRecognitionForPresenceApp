## <div align="center">Verification System in Student Attendance Case Study</div>

<div align="center">
  <img src="https://i.ibb.co/HgNL1Cf/app-logo.png" alt="app-logo" border="0" width="150px">
</div>

<br/>

Repository ini berisi implementasi proyek tugas akhir yang berjudul "Perancangan Arsitektur Sistem Verifikasi Berbasis Face Recognition dalam Studi Kasus Absensi Mahasiswa".
Sistem ini dikembangkan menggunakan bahasa pemrograman [python](https://www.python.org/), framework [flask](https://flask.palletsprojects.com/en/2.2.x/) dan [deepface](https://github.com/serengil/deepface) 
dengan model yang digunakan adalah [`Facenet`](https://sefiks.com/2018/09/03/face-recognition-with-facenet-in-keras/) dan detector [`MTCNN`](https://sefiks.com/2020/09/09/deep-face-detection-with-mtcnn-in-python/).

## How to Run Project

Untuk menjalankan projek dapat mengikuti langkah-langkah berikut.
- Buat direktori baru untuk menyimpan projek
- Buka direktori tersebut melalui IDE Visual Studio Code atau code editor favorit
- Buka terminal, clone repository terlebih dahulu dengan menjalankan:
```shell
$ git clone https://github.com/muhammadramadhann/VerificationSystemAttendance.git
```
- Buat virtual environment
```shell
$ python -m venv venv
```
- Mengaktifkan virtual environment
```shell
$ cd venv/Scripts && activate
```
- Kembali ke path awal projek
```shell
$ cd .. && cd ..
```
- Menginstall seluruh requirement project dan tunggu hingga proses install semua library selesai
```shell
$ pip install -r requirements.txt
```
