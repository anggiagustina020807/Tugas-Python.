class Sekolah:
    pass

class Siswa:
    pass

Kepala_sekolah = Sekolah()
Orang_tua = Siswa()

print(type(Kepala_sekolah))
print(type(Orang_tua))

Anggi = Sekolah()
Asep = Siswa()

print(type(Anggi))
print(type(Asep))

Kepala_sekolah = Sekolah()
Kepala_sekolah.umur = 26
Kepala_sekolah.nama = "Anggi"

print(Kepala_sekolah.umur)
print(Kepala_sekolah.nama)

Orang_tua = Siswa()
Orang_tua.umur = 59
Orang_tua.nama = "Asep"

print(Orang_tua.umur)
print(Orang_tua.nama)
