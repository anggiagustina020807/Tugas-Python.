class Teman:
    lokasi = "cafe pertigaan" # Class Attribute
    def __init__(self, nama):
        self.nama = nama # Instance Attribute
    def bicara(self, teks):
        print(f"{self.nama} : {teks}")

class Penjual:
    nama_toko = "Cafe Pertigaan" # Class Attribute
    def bicara(self, teks):
        print(f"Penjual : {teks}")

class Cewek:
    def __init__(self, nama):
        self.nama = nama # Instance Attribute
    def bicara(self, teks):
        print(f"{self.nama} : {teks}")

# Object
anggi = Teman("Anggi")
asep = Teman("Asep")
penjual = Penjual()
caca = Cewek("Caca")

# Harga
harga_americano = 18000
harga_goodday = 12000
total = harga_americano + harga_goodday # 30000

# Cerita
anggi.bicara("Sep anter ngopi yu")
asep.bicara("Kemana?")
anggi.bicara("Biasa ke cafe di pertigaan itu")
asep.bicara("Ngapain tiba-tiba ngajak ngopi")
anggi.bicara("Biasa aja nenangin diri")
asep.bicara("Ayo lah gasken")
anggi.bicara("Mesen dulu ayo")
asep.bicara("Gas")
anggi.bicara("Saya mau pesen minuman rasa Americano, tambahin gula sedikit aja bang")
anggi.bicara("Sep mau pesen apa?")
asep.bicara("Good Day satu")
anggi.bicara("Berapa bang semuanya?")
penjual.bicara(f"Americano nya Rp{harga_americano}, Good Day nya Rp{harga_goodday}, jadi totalnya Rp{total} bang")
anggi.bicara("Bang udah bayar ya QRIS")
penjual.bicara("Oke tunggu ya bang nanti di anterin kopinya")
anggi.bicara("Oke bang")
asep.bicara("Gini gini doang ngopi, ngapain kek")
anggi.bicara("Udah tunggu kopi dulu aja")
asep.bicara("Oke deh")
penjual.bicara("Bang nih kopinya")
anggi.bicara("Oke bang makasih")
anggi.bicara("Wih sep cewek tuh")
asep.bicara("Mana")
anggi.bicara("Itu yang pake kacamata cakep kan")
asep.bicara("Wih cakep emang kenalan geh")
anggi.bicara("Malu eyy")
asep.bicara("Bilang doang cakep gapunya nyali")
anggi.bicara("Oke otw samperin dah kalau begitumah")
anggi.bicara("Ekhemmmm kak")
caca.bicara("Ehhh iya kenapa kak")
anggi.bicara("Salam kenal saya Anggi")
anggi.bicara("Nama kamu siapa?")
caca.bicara("Aku Caca, ada apa ya")
anggi.bicara("Minta IG nya dong")
caca.bicara("Eh tiba-tiba banget minta IG")
anggi.bicara("Gapapa pengen kenal kamu aja, trus juga tadi beli Americano padahal udah pake gula tetep pait, pas ngeliat kamu ternyata ke ambil sama kamu manisnya ihihihihi")
caca.bicara("Bisa aja, yaudah boleh deh")
anggi.bicara("Nih hp nya ketik aja")
caca.bicara("Sini aku ketik ..........")
caca.bicara("Udah yaa")
anggi.bicara("Eeeeeeee...")
caca.bicara("Kenapa lagi")
anggi.bicara("Kamu lagi sibuk ga tangannya")
caca.bicara("Nggak kok emang kenapa")
anggi.bicara("Boleh follback dulu gaaaa ihihihi")
caca.bicara("Hmmm, udah tuh yaaa")
anggi.bicara("Oke deh makasih yaa kalau di IG bosen boleh ke WA aja yaa")
anggi.bicara("Babayyyy")
caca.bicara("Iya Babay juga")
