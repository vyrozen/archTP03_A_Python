nString1 = int(input(f"Masukkan panjang string 1: ")) #Dapat diabaikan
iString1 = str(input(f"Masukkan string 1: ")) 
nString2 = int(input(f"Masukkan panjang string 2: ")) #Dapat diabaikan
iString2 = str(input(f"Masukkan string 2: "))
charString1, charString2, solved = "", "", 0

for i in iString1:
    charString1 = charString1 + i + "#"
for i in iString2:
    charString2 = charString2 + i + "#"
listString1,listString2 = charString1.split("#"), charString2.split("#")

for i in range (len(listString2)):
    calc = 0
    if i+len(listString1) > len(listString2) : break
    for j in range (len(listString1)):
        if (listString1[j]) == (listString2[i+j]):
            if not listString1[j] == "" : calc += 1
    if calc == len(listString1) - 1 : solved += 1
print(f"String 1 muncul sebanyak {solved} kali.")