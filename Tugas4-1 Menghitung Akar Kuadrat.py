# Muhammad Riveldo Hermawan Putra
# 122140037
# Tugas 4 Praktikum Menghitung Akar Kuadra

import math  # Mengimpor modul math untuk menggunakan fungsi matematika seperti sqrt (akar kuadrat)

while True:  # Membuat loop tak terbatas, agar program terus meminta input sampai mendapat input yang valid
    try:
        # Meminta input dari pengguna
        user_input = input("Masukkan angka: ")
        
        # Mencoba mengonversi input menjadi float
        number = float(user_input)
        
        # Memeriksa apakah angka negatif atau nol
        if number < 0:
            print("Input tidak valid. Harap masukkan angka positif.")  
            # Angka negatif tidak diperbolehkan karena akar kuadrat bilangan negatif tidak real
        elif number == 0:
            print("Error: Akar kuadrat dari nol tidak diperbolehkan.")  
            # Spesifik di kasus ini, nol dianggap tidak valid (meskipun matematis sqrt(0) = 0)
        else:
            # Menghitung akar kuadrat jika input valid (> 0)
            result = math.sqrt(number)
            print(f"Akar kuadrat dari {number} adalah {result}.")
            break  # Keluar dari loop setelah berhasil menghitung
    except ValueError:
        # Menangani input yang bukan angka, misalnya huruf atau karakter khusus
        print("Input tidak valid. Harap masukkan angka yang valid.")
