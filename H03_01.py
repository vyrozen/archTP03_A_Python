banyakBarang = int(input(f"Masukkan banyak barang: "))
x,y,z = "", "", 0
for i in range (banyakBarang):
    priceKeI = int(input(f"Masukkan harga awal barang ke-{i+1}: "))
    x = x + str(priceKeI) + "#"
for i in range (banyakBarang):
    diskonKeI = int(input(f"Masukkan besar diskon (dalam persen) barang ke-{i+1}: "))
    y = y + str(diskonKeI) + "#"
diskonList = y.split("#")
priceList = x.split("#")
for i in range (banyakBarang):
    hargaAkhir = ((int(diskonList[i]))/100)*int(priceList[i])
    if hargaAkhir>z :
        z = hargaAkhir
        HighestIndex = i
print(f"Barang {HighestIndex+1} meimiliki diskon paling besar yaitu {((int(diskonList[HighestIndex]))/100)*int(priceList[HighestIndex])}")
