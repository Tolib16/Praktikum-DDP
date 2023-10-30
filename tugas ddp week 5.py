print("tugas nomor 1")
Kendaraan =["Genio","motor","110cc","merah","dua"]
print(Kendaraan)
Kendaraan.append("19 Juta")
Kendaraan.append("matic")
Kendaraan.insert(2,"Genio")

print("tugas nomor 2")
pesan="""
menu:
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
pilih menu:
"""
pilihan=input(pesan)

match pilihan:
    case "1":
        print("anda memasukan angka 1 untuk menghitung luas persegi")
        sisi=int(input("masukan sisi:"))
        luas=sisi*sisi
        print("luas persegi dengan sisi",sisi,"adalah",luas)
    case "2":
        print("anda memasukan angka 2 untuk menghitung luas lingkaran")
        r = float(input("Masukkan jari-jari lingkaran: "))
        luas1 = 3.14 * (r * r)
        print("luas lingkaran dengan jari-jari",r,"adalah",luas1)
    case "3":
        print("anda memasukan angka 3 untuk menghitung luas segitiga")
        alas = int(input("Masukkan alas: "))
        tinggi = int(input("masukan tinggi: "))
        luas2 = 1/2*(alas*tinggi)
        print("luas segitiga dengan alas","dan tinggi",tinggi,"adalah",luas2)