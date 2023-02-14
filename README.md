## <div align="center">Presence App</div>

<br/>

Repository ini berisi implementasi proyek tugas akhir yang berjudul "Perancangan Arsitektur Face Recognition Untuk Presensi Karyawan".
Sistem ini dikembangkan menggunakan bahasa pemrograman [python](https://www.python.org/), framework [flask](https://flask.palletsprojects.com/en/2.2.x/) dan [deepface](https://github.com/serengil/deepface) 
dengan model yang digunakan adalah [`Dlib`](https://sefiks.com/2020/07/11/face-recognition-with-dlib-in-python/) dan face detector [`OpenCV`](https://sefiks.com/2020/02/23/face-alignment-for-face-recognition-in-python-within-opencv/).

## Architecture Design

<img width="760" alt="Screenshot 2023-02-14 at 16 08 35" src="https://user-images.githubusercontent.com/30397639/218692115-c876854a-834f-4e83-8784-ebf28db02d8c.png">

## Database Design 

<img width="500" alt="Screenshot 2023-02-14 at 16 08 59" src="https://user-images.githubusercontent.com/30397639/218692304-462e6b5d-3d39-4dac-8d9b-7b1eec148196.png">

## How to Install Project

Project ini dikembangkan pada MacOS M1, jadi untuk instalasi library dan kebutuhannya bisa di sesuaikan.
Instalasi projek dapat mengikuti langkah-langkah berikut.
- Buat direktori baru untuk menyimpan projek
- Buka direktori tersebut melalui IDE Visual Studio Code atau code editor favorit
- Buka terminal, clone repository terlebih dahulu dengan menjalankan:
```shell
$ git clone https://github.com/hanifma/FaceRecognitionForPresenceApp.git
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
- Jalankan xampp dan buka http://localhost/phpmyadmin/index.php
- Buat sebuah database dengan nama ta_final
- Buka database tersebut lalu pilih import `ta_final.sql` 

## How to Use Project

- Jalankan aplikasi
```shell
$ python app.py
```
- Tambahkan data terlebih dahulu pada link http://127.0.0.1:5000/admin/tambah_data
- Lakukan presensi pada link http://127.0.0.1:5000/take_foto dan submit
- History presensi dapat dilihat pada link http://127.0.0.1:5000/history

## Snapshoot Presence App

![Snapshoot Presence App](https://user-images.githubusercontent.com/30397639/218708019-83275b89-7ef2-43e7-8196-705d2dd48da4.jpg)
