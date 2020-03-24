class MhsTif(object):
    def __init__(self,nama,nim,kota,uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTif("bambang", 10, "kudus", 280000)
c1 = MhsTif("hanan", 51, "klaten", 290000)
c2 = MhsTif("dimas", 2, "Surakarta", 270000)
c3 = MhsTif("jaky", 18, "Surakarta", 235000)
c4 = MhsTif("ilham", 4, "yogya", 240000)
c5 = MhsTif("Alip", 31, "Salatiga", 250000)
c6 = MhsTif("pras", 13, "Klaten", 245000)
c7 = MhsTif("Iqbal", 5, "Wonogiri", 245000)
c8 = MhsTif("boy", 23, "jepara", 245000)
c9 = MhsTif("paijo", 64, "Karanganyar", 270000)
c10 = MhsTif("paijem", 29, "Purwodadi", 265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

#NOMER 5
class node(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

    def cari(self, dicari):
        cur = self
        while cur is not None:
            if cur.next != None:
                if cur.data != dicari:
                    cur = cur.next
                else:
                    print ("Data", dicari, "ada dalam Linked List")
                    break
            elif cur.next == None:
                print ("Data", dicari, "tidak ada dalam Linked List")
                break
a = node(17)
menu = a
a.next = node (19)
a = a.next
a.next = node (45)
a = a.next
a.next = node (24)
a = a.next
menu.cari(45)
menu.cari(23)
