# Muhammad Riveldo Hermawan Putra
# 122140037
# PBO RF

# Kelas Employee merepresentasikan seorang karyawan
class Employee:
    def __init__(self, name, role, hours_worked, task_completed):
        # Inisialisasi atribut karyawan
        self.name = name  # Nama karyawan
        self.role = role  # Peran atau jabatan karyawan
        self.hours_worked = hours_worked  # Jumlah jam kerja
        self.task_completed = task_completed  # Jumlah tugas yang diselesaikan

    def work(self):
        # Menampilkan pekerjaan yang sedang dilakukan karyawan
        print(f"{self.name} is working as a {self.role}.")

    def evaluate_performance(self):
        # Menghitung rasio produktivitas (tugas selesai per jam kerja)
        productivity_ratio = self.task_completed / self.hours_worked if self.hours_worked > 0 else 0
        return productivity_ratio

    def performance_rating(self):
        # Menilai kinerja berdasarkan rasio produktivitas
        productivity_ratio = self.evaluate_performance()
        if productivity_ratio >= 2:
            return "High Performance"
        elif productivity_ratio >= 1:
            return "Medium Performance"
        else:
            return "Low Performance"

# Kelas turunan SoftwareEngineer
class SoftwareEngineer(Employee):
    def __init__(self, name, hours_worked, task_completed):
        # Menginisialisasi karyawan dengan peran Software Engineer
        super().__init__(name, "Software Engineer", hours_worked, task_completed)

    def work(self):
        # Implementasi metode work untuk Software Engineer
        print(f"{self.name} is coding and developing software.")

# Kelas turunan DataScientist
class DataScientist(Employee):
    def __init__(self, name, hours_worked, task_completed):
        # Menginisialisasi karyawan dengan peran Data Scientist
        super().__init__(name, "Data Scientist", hours_worked, task_completed)

    def work(self):
        # Implementasi metode work untuk Data Scientist
        print(f"{self.name} is analyzing data and building models.")

# Kelas turunan ProductManager
class ProductManager(Employee):
    def __init__(self, name, hours_worked, task_completed):
        # Menginisialisasi karyawan dengan peran Product Manager
        super().__init__(name, "Product Manager", hours_worked, task_completed)

    def work(self):
        # Implementasi metode work untuk Product Manager
        print(f"{self.name} is managing product development and strategy.")

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek karyawan dengan berbagai peran
    emp1 = SoftwareEngineer("Alice", hours_worked=40, task_completed=80)
    emp2 = DataScientist("Bob", hours_worked=35, task_completed=20)
    emp3 = ProductManager("Charlie", hours_worked=30, task_completed=15)

    # Menampilkan informasi pekerjaan dan evaluasi karyawan
    for employee in [emp1, emp2, emp3]:
        employee.work()  # Memanggil metode work
        print(f"Performance Rating: {employee.performance_rating()}")  # Menampilkan penilaian kinerja
        print()  # Pemisah output
