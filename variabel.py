# Contoh 1: Menyimpan nama
yunita = "Yunita"
print("Halo, namaku", yunita)

# Contoh 2: Menyimpan umur
yunita = 16
print("Umur Yunita adalah", yunita, "tahun")

# Contoh 3: Menyimpan data dalam bentuk dictionary
yunita = {
    "nama": "Yunita",
    "umur": 16,
    "hobi": ["coding", "membaca", "bermimpi besar"]
}
print("Data Yunita:")
print("Nama:", yunita["nama"])
print("Umur:", yunita["umur"])
print("Hobi:", ", ".join(yunita["hobi"]))