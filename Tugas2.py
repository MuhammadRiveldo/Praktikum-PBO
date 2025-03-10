# Muhammad Riveldo Hermawan Putra
# 122140037
# Tugas 2 Praktikum

import random  # Mengimpor library random untuk menentukan kemungkinan serangan

# Kelas Ninja merepresentasikan karakter dalam pertarungan
class Ninja:
    def __init__(self, name, hp, attack_power):
        self.name = name  # Nama ninja (Naruto atau Sasuke)
        self.hp = hp  # Jumlah HP (Health Points) atau nyawa karakter
        self.attack_power = attack_power  # Kekuatan serangan karakter
        self.defending = False  # Status bertahan (True jika bertahan, False jika tidak)
    
    # Metode untuk menyerang musuh
    def attack_enemy(self, enemy):
        if random.random() > 0.2:  # 80% kemungkinan serangan mengenai target
            damage = self.attack_power // 2 if enemy.defending else self.attack_power  # Jika musuh bertahan, damage berkurang setengah
            enemy.hp -= damage  # Mengurangi HP musuh
            
            # Menampilkan pesan berdasarkan siapa yang menyerang
            if self.name == "Naruto":
                print(f"🔥 {self.name} menggunakan Rasengan dan menyerang {enemy.name}, memberikan {damage} damage! 🔥")
            else:
                print(f"⚡ {self.name} melepaskan Chidori ke arah {enemy.name}, memberikan {damage} damage! ⚡")
        else:
            print(f"💨 {self.name} mencoba menyerang, tetapi {enemy.name} menghindar dengan kecepatan tinggi! 💨")
        enemy.defending = False  # Reset status bertahan setelah serangan
    
    # Metode untuk bertahan dari serangan musuh
    def defend(self):
        self.defending = True  # Mengaktifkan mode bertahan
        print(f"🛡️ {self.name} memasang posisi bertahan, siap menghadapi serangan! 🛡️")

# Kelas Battle untuk mengatur jalannya pertarungan
class Battle:
    def __init__(self, ninja1, ninja2):
        self.ninja1 = ninja1  # Ninja pertama dalam pertarungan
        self.ninja2 = ninja2  # Ninja kedua dalam pertarungan
    
    # Metode untuk memulai pertarungan
    def start_fight(self):
        round_num = 1  # Menentukan ronde awal
        while self.ninja1.hp > 0 and self.ninja2.hp > 0:  # Looping selama kedua ninja masih memiliki HP
            print(f"\n⚔️ Round-{round_num} ==========================================================")
            print(f"{self.ninja1.name} [{self.ninja1.hp} HP | {self.ninja1.attack_power} ATK]")  # Menampilkan status ninja 1
            print(f"{self.ninja2.name} [{self.ninja2.hp} HP | {self.ninja2.attack_power} ATK]")  # Menampilkan status ninja 2
            
            action1 = self.get_action(self.ninja1)  # Meminta aksi dari ninja pertama
            action2 = self.get_action(self.ninja2)  # Meminta aksi dari ninja kedua
            
            # Jika ninja pertama menyerah
            if action1 == '3':
                print(f"🏆 {self.ninja1.name} menyerah! {self.ninja2.name} adalah pemenang pertarungan ini! 🏆")
                break
            # Jika ninja kedua menyerah
            if action2 == '3':
                print(f"🏆 {self.ninja2.name} menyerah! {self.ninja1.name} adalah pemenang pertarungan ini! 🏆")
                break
            
            # Jika ninja pertama memilih menyerang
            if action1 == '1':
                self.ninja1.attack_enemy(self.ninja2)
            elif action1 == '2':  # Jika ninja pertama memilih bertahan
                self.ninja1.defend()
            
            # Jika HP ninja kedua habis setelah serangan ninja pertama, maka ninja pertama menang
            if self.ninja2.hp <= 0:
                print(f"🥇 {self.ninja1.name} telah memenangkan pertarungan! 🥇")
                break
            
            # Jika ninja kedua memilih menyerang
            if action2 == '1':
                self.ninja2.attack_enemy(self.ninja1)
            elif action2 == '2':  # Jika ninja kedua memilih bertahan
                self.ninja2.defend()
            
            # Jika HP ninja pertama habis setelah serangan ninja kedua, maka ninja kedua menang
            if self.ninja1.hp <= 0:
                print(f"🥇 {self.ninja2.name} telah memenangkan pertarungan! 🥇")
                break
            
            round_num += 1  # Menambah ronde pertarungan
    
    # Metode untuk mendapatkan aksi pemain
    def get_action(self, ninja):
        print("\n1. Attack     2. Defense     3. Give up")  # Menampilkan pilihan aksi
        return input(f"{ninja.name}, pilih aksi: ")  # Meminta input aksi dari pemain

# Inisialisasi karakter Naruto dan Sasuke dengan HP dan attack power mereka
naruto = Ninja("Naruto", 600, 12)  # Naruto memiliki 600 HP dan serangan 12
sasuke = Ninja("Sasuke", 550, 14)  # Sasuke memiliki 550 HP dan serangan 14

# Memulai pertarungan antara Naruto dan Sasuke
battle = Battle(naruto, sasuke)
battle.start_fight()
