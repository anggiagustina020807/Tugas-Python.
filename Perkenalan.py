class Pegawai:
    npm = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

    def hello(self, nama):
        print(f"Halo {self.nama}, nama saya {nama}")

pegawai = Pegawai()
pegawai.nama = "Anggi"
pegawai.perkenalan()
pegawai.hello("Asep")
