# Muhammad Riveldo Hermawan Putra
# 122140037
# Tugas 3-1 Agriculture: Smart Farming System dengan Abstraksi dan Polimorfisme
from abc import ABC, abstractmethod  # Mengimpor modul ABC untuk membuat kelas abstrak

# Kelas abstrak Plant
class Plant(ABC):
    def __init__(self, name, water_needs, fertilizer_needs):
        # Inisialisasi atribut dasar tanaman
        self.name = name  # Nama tanaman
        self.water_needs = water_needs  # Kebutuhan air dalam liter
        self.fertilizer_needs = fertilizer_needs  # Kebutuhan pupuk dalam kg
        
        # Menyimpan kebutuhan yang dapat disesuaikan berdasarkan kondisi cuaca
        self.adjusted_water_needs = water_needs
        self.adjusted_fertilizer_needs = fertilizer_needs

    @abstractmethod
    def grow(self):
        pass  # Metode abstrak yang harus diimplementasikan di subclass
        
    def calculate_needs(self, rainfall, soil_moisture):
        # Mengurangi kebutuhan air jika curah hujan lebih dari 5 mm
        if rainfall > 5:
            self.adjusted_water_needs = max(0, self.water_needs - (rainfall / 10))  # Penyesuaian kebutuhan air
        else:
            self.adjusted_water_needs = self.water_needs  # Jika tidak, tetap sama
        
        # Meningkatkan kebutuhan pupuk jika kelembapan tanah kurang dari 50%
        if soil_moisture < 50:
            self.adjusted_fertilizer_needs = self.fertilizer_needs * 1.2  # Peningkatan 20%
        else:
            self.adjusted_fertilizer_needs = self.fertilizer_needs  # Jika tidak, tetap sama

    def show_needs(self):
        # Menampilkan kebutuhan air dan pupuk yang telah disesuaikan
        print(f"Adjusted Water Needs: {self.adjusted_water_needs:.2f} liters")
        print(f"Adjusted Fertilizer Needs: {self.adjusted_fertilizer_needs:.2f} kg")

# Kelas turunan RicePlant (tanaman padi)
class RicePlant(Plant):
    def __init__(self):
        # Menginisialisasi tanaman padi dengan kebutuhan air dan pupuk bawaan
        super().__init__(name="Rice", water_needs=20, fertilizer_needs=5)

    def grow(self):
        # Implementasi metode grow untuk padi
        print("Rice is growing in the paddy field")

# Kelas turunan CornPlant (tanaman jagung)
class CornPlant(Plant):
    def __init__(self):
        # Menginisialisasi tanaman jagung dengan kebutuhan air dan pupuk bawaan
        super().__init__(name="Corn", water_needs=18, fertilizer_needs=7)

    def grow(self):
        # Implementasi metode grow untuk jagung
        print("Corn is growing in the farm")
        
# Simulasi kondisi cuaca
def simulate_weather(plant, rainfall, soil_moisture):
    plant.grow()  # Memanggil metode grow dari tanaman
    print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")  # Menampilkan kondisi cuaca
    plant.calculate_needs(rainfall, soil_moisture)  # Menyesuaikan kebutuhan berdasarkan cuaca
    plant.show_needs()  # Menampilkan hasil penyesuaian

# Contoh penggunaan
if __name__ == "__main__":
    rice = RicePlant()  # Membuat objek RicePlant
    corn = CornPlant()  # Membuat objek CornPlant

    # Simulasi cuaca untuk RicePlant
    simulate_weather(rice, rainfall=10, soil_moisture=75)
    print()  # Pemisah output

    # Simulasi cuaca untuk CornPlant
    simulate_weather(corn, rainfall=2, soil_moisture=40)
