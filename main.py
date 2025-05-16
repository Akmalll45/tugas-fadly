from flask import Flask, render_template, request

app = Flask(__name__)

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

def konversi_nilai_huruf(nilai_akhir):
    if nilai_akhir >= 95:
        return 'A'
    elif nilai_akhir >= 90:
        return 'A-'
    elif nilai_akhir >= 85:
        return 'B'
    elif nilai_akhir >= 80:
        return 'B-'
    elif nilai_akhir >= 75:
        return 'C'
    elif nilai_akhir >= 70:
        return 'C-'
    elif nilai_akhir >= 60:
        return 'D'
    else:
        return 'E'

@app.route('/')
def index():
    return render_template('index.html', nilai_akhir=None)

@app.route('/hitung', methods=['POST'])
def hitung():
    """
    Fungsi untuk menghitung nilai akhir dan nilai huruf berdasarkan inputan
    tugas, uts, dan uas dari user.
    """
    tugas = float(request.form['tugas'])
    uts = float(request.form['uts'])
    uas = float(request.form['uas'])
    
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

    nilai_huruf = konversi_nilai_huruf(nilai_akhir)

    
    return render_template('index.html', nilai_akhir=round(nilai_akhir, 2), nilai_huruf=nilai_huruf)
if __name__ == '__main__':
    app.run(debug=True)
