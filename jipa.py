import json
from datetime import datetime as dt

data = {'tanggal': [], 'nama_barang': [], 'jumlah_barang': [], 'total_harga': []}


def tambahkanData():

    tanggal = dt.now().strftime('%d/%m/%Y')
    namabarang = str(input("masukkan nama_barang: "))
    jumlahbarang = int(input("masukkan jumlah_barang: "))
    hargaBarang = int(input("masukkan harga_barang: "))
    totalharga = jumlahbarang*hargaBarang

    data['tanggal'].append(tanggal)
    data['nama_barang'].append(namabarang)
    data['jumlah_barang'].append(jumlahbarang)
    data['total_harga'].append(totalharga)


def exportfilejson():
    j = json.dumps(data)
    with open('file.json', 'w') as target:
        target.write(j)
        target.close()


def hapusData():
    tampilkanData()
    kosong = []
    daftar = []
    hapus = input("Masukkan nama barang yang ingin dihapus: ")
    with open("tes.json", "r") as ass:
        pembaca = json.loads(ass.read())
        daftar.append(pembaca)
        try:
            for i in pembaca:
                if i["Nama barang"] == hapus:
                    continue
                else:
                    kosong.append(i)
        except:
            pass
    with open("tes.json", "w") as pol:
        penulis = json.dump(kosong, pol, indent=2)
    input("Tekan enter untuk kembali ke menu")
    tampilanMenu()
    

def tampilkanData():
    ambiljson = json.load(open('file.json'))
    print(ambiljson)


def tampilanMenu():
    print("""============Daftar============
    1.Tampilkan data
    2.Menambahkan data
    3.Hapus data
    4.Export ke file json
    5.Exit
    """)
    pilihDaftar = int(input("Masukkan Angka Sesuai Daftar: "))
    if pilihDaftar == 1:
        tampilkanData()
    elif pilihDaftar == 2:
        tambahkanData()
    elif pilihDaftar == 3:
        hapusData()
    elif pilihDaftar == 4:
        exportfilejson()
    else:
        print("=====Trimakasih=====")

        exit()


while True:
    tampilanMenu()
