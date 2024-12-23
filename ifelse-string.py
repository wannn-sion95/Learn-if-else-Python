nama = input("Masukkan nama anda: ").strip().title()
umur = int(input("Masukkan umur anda: "))

if nama == "Wannn Sion" and umur == 19:
    print("------------------")
    print("Data diri anda:")
    print(f"Nama: {nama}\nUmur: {umur}" + " tahun")
    print("------------------")
else:
    print("Data tidak valid!.")
