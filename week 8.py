# Nomor 1
def profil(nama, alamat, gender, umur, hoby):
    print("nama saya :", nama)
    print("alamat saya :", alamat)
    print("gender saya :", gender)
    print("umur saya :", umur)
    print("hoby saya :", hoby)
  
profil("Muhamad Tolib", "Cibinong Bogor", "Laki-Laki", "21", "Maen Game")

#Nomor 2
def hasil(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 < nilai <= 70:
        return "Baik"
    elif 71 < nilai <= 80:
        return "Sangat Baik"
    elif 81 < nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"
    
nilai_mahasiswa = float(input("Masukan nilai mahasiswa :"))
hasil = hasil(nilai_mahasiswa)
print(f"mahasiswa ini {hasil}.")

#Nomor 3
def nilai_ganjil(n):
    for n in range(1, n + 1, 2):
        print(n, end='  ')


nilai_ganjil(100)