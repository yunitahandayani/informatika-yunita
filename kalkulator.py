 # Mulai
# Deklarasi variabel
a = 50
b = 30
op = input("Masukkan operator (+, -, *, /): ")

# Proses berdasarkan operator
if op == '+':
    hasil = a + b
elif op == '-':
    hasil = a - b
elif op == '*':
    hasil = a * b
elif op == '/':
    if b != 0:
        hasil = a / b
    else:
        hasil = "Error: Pembagian dengan nol!"
else:
    hasil = "Operator tidak dikenali."

# Output
print("Hasil:", hasil)
# Selesai
        