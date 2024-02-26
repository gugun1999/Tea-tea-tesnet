class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Berhasil mendepositkan {amount} koin ke wallet Anda.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Berhasil menarik {amount} koin dari wallet Anda.")
        else:
            print("Saldo tidak mencukupi.")

    def check_balance(self):
        print(f"Saldo Anda adalah {self.balance} koin.")

# Contoh penggunaan:
my_wallet = Wallet()
my_wallet.check_balance()
my_wallet.deposit(50)
my_wallet.check_balance()
my_wallet.withdraw(20)
my_wallet.check_balance()
