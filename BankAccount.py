class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nama, nim): 
        self.nama = nama
        self.nim = nim

mhs = Mahasiswa("Anggi", "14022500022")
print(mhs.nama)
print(mhs.nim)

class BankAccount:
    no = ""
    balance = 0
    active = "Benar"

    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance

    @classmethod
    def disabled(cls, no, balance=0):
        result = cls(no, balance)
        result.active = "salah"
        return result

bank_account1 = BankAccount("1", 10000)
bank_account2 = BankAccount.disabled("2")
print(f"Bank account {bank_account1.no} has balance {bank_account1.balance} and status {bank_account1.active}")
print(f"Bank account {bank_account2.no} has balance {bank_account2.balance} and status {bank_account2.active}")
