teks = input("masukan nilai: ")
try:
    nilai = float(teks)
    print(f"Nilai = {nilai}")
except ValueError:
    print("input harus berupa angka.")