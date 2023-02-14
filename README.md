## <div align="center">Presence App</div>

<br/>

Repository ini berisi implementasi proyek tugas akhir yang berjudul "Perancangan Arsitektur Face Recognition Untuk Presensi Karyawan".
Sistem ini dikembangkan menggunakan bahasa pemrograman [python](https://www.python.org/), framework [flask](https://flask.palletsprojects.com/en/2.2.x/) dan [deepface](https://github.com/serengil/deepface) 
dengan model yang digunakan adalah [`Dlib`](https://sefiks.com/2020/07/11/face-recognition-with-dlib-in-python/) dan face detector [`OpenCV`](https://sefiks.com/2020/02/23/face-alignment-for-face-recognition-in-python-within-opencv/).

## How to Run Project

Project ini dikembangkan pada MacOS, jadi untuk instalasi di Windows bisa di sesuaikan.
Untuk menjalankan projek dapat mengikuti langkah-langkah berikut.
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
