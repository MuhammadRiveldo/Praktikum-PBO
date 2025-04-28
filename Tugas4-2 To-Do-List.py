# Muhammad Riveldo Hermawan Putra
# 122140037
# Tugas 4-2 Manajemen Daftar Tugas (To-Do List)

def main():
    to_do_list = []  # Membuat list kosong untuk menyimpan daftar tugas

    while True:  # Loop utama agar program terus berjalan sampai user memilih keluar
        try:
            # Menampilkan menu pilihan ke pengguna
            print("\nPilih aksi:")
            print("1. Tambah tugas")
            print("2. Hapus tugas")
            print("3. Tampilkan daftar tugas")
            print("4. Keluar")
            pilihan = input("Masukkan pilihan (1/2/3/4): ")

            if pilihan == "1":
                # Menambahkan tugas baru ke daftar
                tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
                if not tugas:
                    raise ValueError("Tugas tidak boleh kosong.")  # Validasi input kosong
                to_do_list.append(tugas)  # Menambahkan tugas ke list
                print("Tugas berhasil ditambahkan!")

            elif pilihan == "2":
                # Menghapus tugas dari daftar
                if not to_do_list:
                    print("Daftar tugas kosong. Tidak ada yang bisa dihapus.")
                    continue  # Langsung kembali ke awal loop

                try:
                    nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))  # Input nomor tugas
                    if nomor < 1 or nomor > len(to_do_list):
                        raise IndexError("Tugas dengan nomor tersebut tidak ditemukan.")  # Validasi nomor di luar batas
                    removed_task = to_do_list.pop(nomor - 1)  # Hapus tugas (index list mulai dari 0)
                    print(f"Tugas '{removed_task}' berhasil dihapus!")
                except ValueError:
                    print("Error: Masukkan nomor tugas yang valid.")  # Menangani input nomor yang salah (bukan angka)
                except IndexError as e:
                    print(f"Error: {e}")  # Menangani input nomor di luar rentang daftar tugas

            elif pilihan == "3":
                # Menampilkan semua tugas dalam daftar
                if not to_do_list:
                    print("Daftar Tugas kosong.")
                else:
                    print("Daftar Tugas:")
                    for i, tugas in enumerate(to_do_list, start=1):
                        print(f"- {i}. {tugas}")  # Menampilkan daftar dengan nomor

            elif pilihan == "4":
                # Keluar dari program
                print("Keluar dari program.")
                break

            else:
                # Jika input pilihan tidak sesuai 1–4
                print("Pilihan tidak valid. Masukkan angka 1, 2, 3, atau 4.")

        except Exception as e:
            # Menangkap error tidak terduga secara umum
            print(f"Terjadi kesalahan: {e}")

# Memastikan program hanya berjalan saat file ini dijalankan langsung (bukan diimpor)
if __name__ == "__main__":
    main()
