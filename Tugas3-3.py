# Kelas BankAccount merepresentasikan rekening bank dengan fitur multi-mata uang dan kalkulasi bunga
class BankAccount:
    # Kurs konversi tetap antara mata uang
    exchange_rates = {
        ("EUR", "USD"): 1.1,  # 1 EUR = 1.1 USD
        ("USD", "EUR"): 0.91, # 1 USD = 0.91 EUR
        ("IDR", "USD"): 0.000065, # 1 IDR = 0.000065 USD
        ("USD", "IDR"): 15400  # 1 USD = 15,400 IDR
    }

    def __init__(self, account_holder, balance, currency):
        # Inisialisasi atribut akun bank
        self.account_holder = account_holder  # Menyimpan nama pemilik akun
        self.balance = balance  # Menyimpan jumlah saldo awal
        self.currency = currency  # Menyimpan jenis mata uang akun

    def apply_interest(self):
        """
        Menambahkan bunga tahunan ke saldo berdasarkan jumlah saldo:
        - 2% jika saldo >= 5000
        - 1% jika saldo < 5000
        """
        interest_rate = 0.02 if self.balance >= 5000 else 0.01  # Menentukan suku bunga berdasarkan saldo
        interest = self.balance * interest_rate  # Menghitung jumlah bunga
        self.balance += interest  # Menambahkan bunga ke saldo
        print(f"Applying interest... New Balance = {self.currency}{self.balance:.2f}")  # Menampilkan saldo setelah bunga

    def convert_currency(self, target_currency):
        # Metode untuk mengonversi mata uang
        if self.currency == target_currency:
            return self.balance  # Jika mata uang sama, tidak perlu konversi
        
        conversion_rate = self.exchange_rates.get((self.currency, target_currency))  # Mengambil kurs konversi
        if conversion_rate:
            return self.balance * conversion_rate  # Mengonversi saldo dengan kurs yang sesuai
        else:
            print("Currency conversion not supported!")  # Pesan jika kurs tidak tersedia
            return None

    def withdraw(self, amount, currency):
        # Konversi saldo ke mata uang penarikan jika berbeda
        converted_balance = self.convert_currency(currency)  # Mengonversi saldo akun ke mata uang yang diinginkan
        
        if converted_balance is not None and converted_balance >= amount:  # Mengecek apakah saldo cukup untuk ditarik
            if self.currency != currency:
                # Jika mata uang berbeda, lakukan konversi ke mata uang akun sebelum mengurangi saldo
                self.balance -= amount / self.exchange_rates[(self.currency, currency)]
            else:
                self.balance -= amount  # Jika mata uang sama, cukup kurangi saldo secara langsung
            print(f"Withdrawal successful! New Balance = {self.currency}{self.balance:.2f}")  # Menampilkan saldo setelah penarikan
        else:
            print("Insufficient balance for withdrawal!")  # Pesan jika saldo tidak mencukupi

    def __str__(self):
        
        #Mengembalikan representasi string dari rekening bank
        
        return f"{self.account_holder}'s Account: Balance = {self.currency}{self.balance:.2f}"  # Format tampilan akun


# Contoh skenario penggunaan
if __name__ == "__main__":
    # Membuat akun John dengan saldo awal $5000 (USD)
    john_account = BankAccount("John", 5000, "USD")
    print(f"{john_account.account_holder}'s Account: Initial Balance = ${john_account.balance}")  # Menampilkan saldo awal
    john_account.apply_interest()  # Menghitung dan menambahkan bunga ke saldo John
    print()  # Pemisah output

    # Membuat akun Emily dengan saldo awal €1000 (EUR)
    emily_account = BankAccount("Emily", 1000, "EUR")
    print(f"{emily_account.account_holder}'s Account: Initial Balance = €{emily_account.balance}")  # Menampilkan saldo awal Emily

    # Konversi saldo Emily ke USD
    converted_balance = emily_account.convert_currency("USD")  # Mengonversi saldo dari EUR ke USD
    print(f"Converted to USD: ${converted_balance:.2f}")  # Menampilkan saldo setelah konversi

    # Emily ingin menarik $1200 setelah konversi
    emily_account.withdraw(1200, "USD")  # Melakukan penarikan dana

    # Menampilkan saldo akhir Emily
    print(f"{emily_account.account_holder}'s Account: Balance remains at €{emily_account.balance:.2f}")  # Menampilkan saldo akhir
