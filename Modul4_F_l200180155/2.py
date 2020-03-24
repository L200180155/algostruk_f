class MhsTif(object):
    def __init__(self,nama,nim,kota,uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTif("bambang", 10, "kudus", 280000)
c1 = MhsTif("hanan", 51, "klaten", 290000)
c2 = MhsTif("dimas", 2, "Surakarta", 270000)
c3 = MhsTif("jaky", 18, "Surakarta", 230000)
c4 = MhsTif("ilham", 4, "yogya", 240000)
c5 = MhsTif("Alip", 31, "Salatiga", 250000)
c6 = MhsTif("pras", 13, "Klaten", 245000)
c7 = MhsTif("Iqbal", 5, "Wonogiri", 245000)
c8 = MhsTif("boy", 23, "jepara", 245000)
c9 = MhsTif("paijo", 64, "Karanganyar", 270000)
c10 = MhsTif("paijem", 29, "Purwodadi", 265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]


#NOMER 2
def cariUangSakuTerkecil(list):
    car = list[0].uangSaku
    for i in list[1:]:
        if i.uangSaku < car:
            car = i.uangSaku
    return car

a = cariUangSakuTerkecil(Daftar)
print(a)


