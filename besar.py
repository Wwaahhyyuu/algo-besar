import json 

nama_file='userfile.json'
data_barang='dataBarang.json'

def tulis(data,file): 
    with open(file,'w') as Dfile: 
       json.dump(data,Dfile,indent=4)

def daftar(role):
    username= input('Masukkan Username: ')
    password= input('Masukkan Password: ')
    data =  {
                "Username" : username,
                "Password" : password,
                "Role"     : role
            }
    new_data= baca(nama_file)
    new_data.append(data)
    tulis(new_data,nama_file)

def baca(file):
    with open (data_barang,'r') as Dfile:
        data = json.load(Dfile)
    return data

def login():
    role = 0
    data=baca(data_barang)
    username= input('Masukkan Username: ')
    password= input('Masukkan Password: ')
    for baris in data:
        if baris['Username']== username and baris['Password']== password:
            role = baris["Role"]
    return role

def menu_penjual():
    print('''   
    ===============
      ||||||||
      ||    ||
      ||||||||
      Welcome To
    Our Program
    ===============
    Silahkan Pilih Menu
    1. Baca
    2. Tulis
    3. Hapus
    ===============''')
    command=input('Silahkan pilih: ')
    if command == '1':
        show()
    elif command == '2':
        insert()
    elif command == '3':
        pass

def insert(): 
    nama=input('Masukkan Nama Barang= ')
    harga=input('Masukkan Harga Barang= ')
    Barang={
        "Nama": nama,
        "Harga": harga,
    }
    data_input=baca(data_barang) 
    data_input.append(Barang)  
    tulis(data_input,data_barang)

def show(): 
    data=baca(data_barang) 
    if len(data)==0: 
        print('Data Kosong')
    else:
        print('''Barang	        Harga''')
        for baris in data:
            print('''{}		{}'''.format(baris['Nama'],baris['Harga']))  

def menu_pembeli():
    print('''   
    ===============
      ||||||||
      ||    ||
      ||||||||
      Welcome To
    Our's Program
    ===============
    Silahkan Pilih Menu
    1. Daftar Barang
    2. Beli
    3. Keluar
    ===============''')
    komentar = input('Silahkan pilih: ')

def main():
    print(' Menu : 1. Login 2. Daftar 3. Keluar ' )
    user= input('Silahkan Pilih Menu : ')
    if user == '2':
        role = input('Penjual(1)/Pembeli(2): ')
        if role == '1':
            daftar('Penjual')
        elif role == '2':
            daftar('Pembeli')   

    elif user== '1': 
        role=login()
        if role:
            print("Berhasil")
            if role == 'Penjual':
                menu_penjual()
            elif role == 'Pembeli':
                print('Pembeli')
        else:
            print("Gagal")
main()