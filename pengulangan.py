# Contoh pengulangan (looping) dalam Python
# Oleh: Yunita

# 1. Pengulangan dengan for (mengulang 5 kali)
print("Pengulangan for:")
for i in range(5):
    print("Perulangan ke-", i + 1)

# 2. Pengulangan dengan for pada list
buah = ["apel", "jeruk", "mangga"]
print("\nDaftar buah:")
for b in buah:
    print("-", b)

# 3. Pengulangan dengan while
print("\nPengulangan while:")
hitung = 1
while hitung <= 5:
    print("Hitung:", hitung)
    hitung += 1

# 4. Pengulangan dengan break dan continue
print("\nPengulangan dengan break dan continue:")
for angka in range(1, 10):
    if angka == 7:
        print("Ditemukan angka 7, berhenti!")
        break
    if angka % 2 == 0:
        continue  # Lewati angka genap
    print("Angka ganjil:", angka)
