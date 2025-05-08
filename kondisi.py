# Contoh kondisi (percabangan) dalam Python
# Oleh: Yunita

# Input nilai siswa
nilai = 75

# Mengecek kondisi dengan if, elif, else
print("Penilaian Siswa:")
if nilai >= 85:
    print("Nilai Anda A (Sangat Baik)")
elif nilai >= 70:
    print("Nilai Anda B (Baik)")
elif nilai >= 55:
    print("Nilai Anda C (Cukup)")
elif nilai >= 40:
    print("Nilai Anda D (Kurang)")
else:
    print("Nilai Anda E (Sangat Kurang)")

# Contoh kondisi lain: menentukan bilangan genap atau ganjil
angka = 7
print("\nPengecekan Bilangan:")
if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")
