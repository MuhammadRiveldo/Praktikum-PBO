# Muhammad Riveldo Hermawan Putra
# 122140037
# Tugas 1 Praktikum

# Dictionary untuk menyimpan data mahasiswa
mahasiswa = {}

# Fungsi untuk menambahkan mahasiswa baru ke dalam dictionary
def tambahkan_mahasiswa(nim, nama, nilai):
    mahasiswa[nim] = {'nama': nama, 'nilai': nilai}  # Menyimpan data mahasiswa dengan NIM sebagai key
    print("Mahasiswa berhasil ditambahkan!")
    
# Fungsi untuk menampilkan semua data mahasiswa
def view_mahasiswa():
    print("=== DATA MAHASISWA ===")
    print("NIM    | Nama | Nilai")
    print("-------------------------")
    for nim, data in mahasiswa.items():  # Loop untuk menampilkan setiap mahasiswa dalam dictionary
        print(f"{nim} | {data['nama']} | {data['nilai']}")

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def find_mahasiswa(nim):
    if nim in mahasiswa:  # Mengecek apakah NIM ada dalam dictionary
        data = mahasiswa[nim]
        print(f"Data Mahasiswa:\n NIM: {nim}\n Nama: {data['nama']}\n Nilai: {data['nilai']}")
    else:
        print("Mahasiswa tidak ditemukan")
        
# Fungsi untuk mengedit data mahasiswa berdasarkan NIM
def edit_mahasiswa(nim, NamaBaru=None, NilaiBaru=None):
    if nim in mahasiswa:
        if NamaBaru:  # Jika nama baru diinput, maka diperbarui
            mahasiswa[nim]['nama'] = NamaBaru
        if NilaiBaru:  # Jika nilai baru diinput, maka diperbarui
            mahasiswa[nim]['nilai'] = NilaiBaru
        print("Data Berhasil Diperbarui!")
    else:
        print("Mahasiswa tidak ditemukan")

# Fungsi untuk menghapus data mahasiswa berdasarkan NIM
def delete_mahasiswa(nim):
    if nim in mahasiswa:
        del mahasiswa[nim]  # Menghapus data mahasiswa dari dictionary
        print("Data Mahasiswa Berhasil dihapus")
    else:
        print("Mahasiswa tidak ditemukan")
        
# Fungsi untuk menyimpan data mahasiswa ke dalam file
def save_file(nama_file='mahasiswa.txt'):
    with open(nama_file, 'w') as file:  # Membuka file dalam mode tulis
        for nim, data in mahasiswa.items():
            file.write(f"{nim}, {data['nama']}, {data['nilai']}\n")  # Menyimpan setiap data mahasiswa ke file
    print(f"Data Mahasiswa Telah Disimpan dalam file '{nama_file}'")

# Fungsi untuk membaca data mahasiswa dari file
def read_file(nama_file='mahasiswa.txt'):
    global mahasiswa  # Menggunakan variabel global mahasiswa
    try:
        with open(nama_file, 'r') as file:  # Membuka file dalam mode baca
            for line in file:
                nim, nama, nilai = line.strip().split(',')  # Memisahkan data berdasarkan koma
                mahasiswa[nim] = {'nama': nama, 'nilai': nilai}  # Menyimpan kembali ke dalam dictionary
        print(f"Data Mahasiswa telah dimuat dari file '{nama_file}'")
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan")

# Fungsi untuk menampilkan menu interaktif
def menu():
    while True:
        print("\n=== SISTEM PENGELOLAAN DATA MAHASISWA ===")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa Berdasarkan NIM")
        print("4. Edit Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Simpan ke File")
        print("7. Baca File")
        print("8. Keluar")
        pilih = input("Pilihan: ")
        
        if pilih == '1':  # Menambahkan mahasiswa
            nim = input("Masukkan NIM: ")
            nama = input("Masukkan Nama: ")
            nilai = input("Masukkan Nilai: ")
            tambahkan_mahasiswa(nim, nama, nilai)
        elif pilih == '2':  # Menampilkan semua mahasiswa
            view_mahasiswa()
        elif pilih == '3':  # Mencari mahasiswa berdasarkan NIM
            nim = input("Masukkan NIM yang ingin dicari: ")
            find_mahasiswa(nim)
        elif pilih == '4':  # Mengedit data mahasiswa
            nim = input("Masukkan NIM yang ingin diedit: ")
            NamaBaru = input("Nama Baru (kosongkan jika tidak ingin diubah): ")
            NilaiBaru = input("Nilai Baru (kosongkan jika tidak ingin diubah): ")
            edit_mahasiswa(nim, NamaBaru if NamaBaru else None, NilaiBaru if NilaiBaru else None)
        elif pilih == '5':  # Menghapus data mahasiswa
            nim = input("Masukkan NIM yang ingin dihapus: ")
            delete_mahasiswa(nim)
        elif pilih == '6':  # Menyimpan data ke file
            save_file()
        elif pilih == '7':  # Membaca data dari file
            read_file()
        elif pilih == '8':  # Keluar dari program
            print("Thank You!")
            break
        else:
            print("Pilihan tidak ada!")
            
# Menjalankan program jika file ini dieksekusi langsung
if __name__ == "__main__":
    menu()
