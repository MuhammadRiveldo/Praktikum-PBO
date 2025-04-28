# Muhammad Riveldo Hermawan Putra
# 122140037
# Tugas 4-3 Sistem Manajemen Hewan (Zoo Management System)

# Mengimpor modul ABC untuk membuat kelas abstrak
from abc import ABC, abstractmethod

# Kelas abstrak Animal
class Animal(ABC):
    def __init__(self, name: str, age: int):
        # Validasi nama tidak boleh kosong
        if not name.strip():
            raise ValueError("Nama hewan tidak boleh kosong.")
        # Validasi umur tidak boleh negatif
        if age < 0:
            raise ValueError("Umur hewan tidak boleh negatif.")
        
        # Enkapsulasi atribut menggunakan private variable
        self.__name = name    
        self.__age = age      

    # Getter untuk nama
    def get_name(self):
        return self.__name

    # Getter untuk umur
    def get_age(self):
        return self.__age

    # Setter untuk nama (dengan validasi)
    def set_name(self, name):
        if not name.strip():
            raise ValueError("Nama hewan tidak boleh kosong.")
        self.__name = name

    # Setter untuk umur (dengan validasi)
    def set_age(self, age):
        if age < 0:
            raise ValueError("Umur hewan tidak boleh negatif.")
        self.__age = age

    # Method abstrak make_sound wajib diimplementasikan di subclass
    @abstractmethod
    def make_sound(self):
        pass

    # Method abstrak info wajib diimplementasikan di subclass
    @abstractmethod
    def info(self):
        pass

# Subclass Lion mewarisi Animal
class Lion(Animal):
    # Override method make_sound
    def make_sound(self):
        return "Roarrr!"

    # Override method info
    def info(self):
        return f"Singa bernama {self.get_name()} berusia {self.get_age()} tahun."

# Subclass Elephant mewarisi Animal
class Elephant(Animal):
    def make_sound(self):
        return "Trumpettt!"

    def info(self):
        return f"Gajah bernama {self.get_name()} berusia {self.get_age()} tahun."

# Subclass Monkey mewarisi Animal
class Monkey(Animal):
    def make_sound(self):
        return "Ooh ooh aah aah!"

    def info(self):
        return f"Monyet bernama {self.get_name()} berusia {self.get_age()} tahun."

# Kelas Zoo untuk manajemen kebun binatang
class Zoo:
    def __init__(self):
        # Membuat list kosong untuk menyimpan hewan
        self.animals = []

    # Method untuk menambahkan hewan
    def add_animal(self, animal):
        # Validasi bahwa hanya instance dari Animal yang boleh ditambahkan
        if not isinstance(animal, Animal):
            raise TypeError("Hanya objek turunan Animal yang boleh ditambahkan.")
        self.animals.append(animal)
        print(f"Hewan {animal.get_name()} berhasil ditambahkan ke kebun binatang!")

    # Method untuk menampilkan semua hewan
    def show_animals(self):
        if not self.animals:
            print("Belum ada hewan di kebun binatang.")
        else:
            print("\nDaftar Hewan di Kebun Binatang:")
            for animal in self.animals:
                print(animal.info())
                print(f"Suara: {animal.make_sound()}\n")

# Fungsi utama untuk menjalankan program
def main():
    zoo = Zoo()  # Membuat objek Zoo

    while True:
        try:
            # Menampilkan menu utama
            print("\n=== Sistem Manajemen Kebun Binatang ===")
            print("1. Tambah Hewan")
            print("2. Tampilkan Daftar Hewan")
            print("3. Keluar")
            pilihan = input("Masukkan pilihan (1/2/3): ").strip()

            if pilihan == "1":
                # Tambah hewan baru
                print("\nPilih jenis hewan:")
                print("1. Singa")
                print("2. Gajah")
                print("3. Monyet")
                jenis = input("Masukkan pilihan jenis (1/2/3): ").strip()

                # Input nama dan umur hewan
                name = input("Masukkan nama hewan: ").strip()
                age = int(input("Masukkan umur hewan: "))

                # Membuat objek hewan sesuai pilihan
                if jenis == "1":
                    animal = Lion(name, age)
                elif jenis == "2":
                    animal = Elephant(name, age)
                elif jenis == "3":
                    animal = Monkey(name, age)
                else:
                    print("Jenis hewan tidak valid.")
                    continue  # Kembali ke menu

                # Menambahkan hewan ke kebun binatang
                zoo.add_animal(animal)

            elif pilihan == "2":
                # Menampilkan semua hewan di kebun binatang
                zoo.show_animals()

            elif pilihan == "3":
                # Keluar dari program
                print("Keluar dari program. Sampai jumpa!")
                break

            else:
                # Jika input pilihan tidak valid
                print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")

        # Menangani kesalahan input nilai
        except ValueError as ve:
            print(f"Input tidak valid: {ve}")

        # Menangani kesalahan tipe data
        except TypeError as te:
            print(f"Error tipe data: {te}")

        # Menangani semua error tidak terduga lainnya
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

# Menjalankan fungsi main
if __name__ == "__main__":
    main()
