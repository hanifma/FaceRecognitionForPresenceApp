from flask import Flask, request, render_template
from deepface import DeepFace
import os
from flask import Flask, request, render_template
import base64, os
from deepface import DeepFace
import time
from datetime import datetime
import mysql.connector


app = Flask(__name__)

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ta_final'
)

app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

def find_file(filename, path):
    for root, dirs, files in os.walk(path):
        if filename in files:
            return os.path.join(root, filename)
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin/index.html')

@app.route('/admin/tambah_data')
def tambah():
    return render_template('admin/tambah_data.html')

@app.route('/admin/save_data', methods=['POST'])
def save_data():
    nip = request.form['nip']
    nama = request.form['nama']
    jabatan = request.form['jabatan']
    kantor = request.form['kantor']
    foto = request.files['foto']
    status = 0

    foto_url = 'static/Dataset/' + nip + '.jpg'
    foto.save(foto_url)

    cursor = conn.cursor()
    query = "INSERT INTO data_karyawan (nip, nama, jabatan, kantor, foto, status_presensi) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (nip, nama, jabatan, kantor, foto_url, status))
    
    conn.commit()
    
    return 'Form data saved to database'

@app.route('/take_foto')
def take_foto():
    return render_template('take_foto.html')

@app.route("/recognition", methods=['POST','GET'])
def recognition():

    start = time.time()

    sekarang = datetime.now()
    tanggal = sekarang.strftime("%d-%m-%Y")
    jam = sekarang.strftime("%H:%M:%S")
    end = time.time()
    durasi = "%s detik" %(end-start)

    if request.method == 'POST':

        nip = request.form['nip']
        img = request.form['img']

        cursor = conn.cursor()
        # cek = cursor.execute("select * from data_karyawan where nip='{}';".format(nip))

        query = "select * from data_karyawan where nip like '%s'"
        cek = cursor.execute(query % nip)
        result = cursor.fetchall()

        print (result)

        if (result == None or result == ''):
                a = "NIP yang kamu masukan tidak terdaftar. Silahkan coba periksa kembali bahwa NIP yang telah kamu masukan sudah benar atau kamu dapat langsung menghubungi HR"
                return render_template('salah.html', a = a)
        else:
            while True:
                try:
                    select_foto = result[0][4]
                    recognition = (DeepFace.verify(img1_path = select_foto, img2_path = img, model_name='Dlib', detector_backend='opencv'))
                    print(recognition)
                    if recognition['verified'] == True:

                        select_status = result[0][5]

                        if (select_status == 0):

                            img = img.split(',')[1]
                            save_image = "static/foto_log/" + nip + "_" + tanggal + "_check_in_" + jam + ".jpg" 
                            with open(save_image, "wb") as f:
                                f.write(base64.decodebytes(img.encode())) 

                            cursor = conn.cursor()
                            query = "INSERT INTO log_presensi (nip, tanggal, jam_in, img_in, jam_out, img_out) VALUES (%s, %s, %s, %s, %s, %s)"
                            cursor.execute(query, (nip, tanggal, jam, save_image, '', ''))

                            cursor.execute("UPDATE data_karyawan SET status_presensi = 1 WHERE nip ='{}'".format(nip))
                            conn.commit()
                            
                            end = time.time()
                            durasi = "%s detik" %(end-start)
                            a = result[0][1] + " berhasil presensi datang " + tanggal + " pada jam " + jam + " dengan durasi " + durasi
                            print(a)
                            return render_template('berhasil.html', a = a)
                        
                        else:
                            
                            img = img.split(',')[1]
                            save_image = "static/foto_log/" + nip + "_" + tanggal + "_check_out_" + jam + ".jpg" 
                            with open(save_image, "wb") as f:
                                f.write(base64.decodebytes(img.encode())) 

                            cursor = conn.cursor()
                            cursor.execute("UPDATE log_presensi SET jam_out = '{}', img_out = '{}' WHERE nip ='{}' AND jam_out=''".format(jam, save_image, nip))
                            cursor.execute("UPDATE data_karyawan SET status_presensi = 0 WHERE nip ='{}'".format(nip))
                            conn.commit()

                            end = time.time()
                            durasi = "%s detik" %(end-start)
                            a = result[0][1] + " berhasil presensi pulang " + tanggal + " pada jam " + jam + " dengan durasi " + durasi
                            print(a)
                            return render_template('berhasil.html', a = a)

                    else:
                        a = "Wajah dan NIP tidak cocok, silahkan coba cek kembali data yang telah kamu masukan dan pastikan NIP nya sudah benar."
                        end = time.time()
                        durasi = "%s detik" %(end-start)
                        print(a, durasi)
                        return render_template('salah.html', a = a)

                except ValueError:
                    a = "Wajah tidak terdeteksi, silahkan lepas aksesoris pada wajah. Pastikan wajah terlihat dengan jelas."
                    end = time.time()
                    durasi = "%s detik" %(end-start)
                    print(a, durasi)
                    return render_template('salah.html', a = a)

            
                    
@app.route('/history')
def history():
    cursor = conn.cursor()
    cursor.execute("select a.tanggal, a.nip, b.nama, b.jabatan, b.kantor, a.jam_in, a.jam_out from log_presensi a left join data_karyawan b on a.nip = b.nip order by a.tanggal desc""")
    history = cursor.fetchall()
    print(history)

    return render_template('admin/history.html', history=history)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)