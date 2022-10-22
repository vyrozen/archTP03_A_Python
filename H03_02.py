nLampu, nTekan, x = int(input(f"Masukkan banyak lampu: ")), int(input(f"Masukkan berapa kali Tuan Kil menekan tombol: ")), ""
stateLampu = [0 for i in range(nLampu)]
for i in range (nTekan):
    act = int(input(f"Tombol yang ditekan ke {i+1}: ")) - 1
    if (0<act<nLampu-1):
        if stateLampu[act-1] == 0 : stateLampu[act-1] = 1
        else: stateLampu[act-1] = 0
        if stateLampu[act] == 0 : stateLampu[act] = 1
        else: stateLampu[act] = 0
        if stateLampu[act+1] == 0 : stateLampu[act+1] = 1
        else: stateLampu[act+1] = 0
    if (act == 0):
        if stateLampu[act] == 0 : stateLampu[act] = 1
        else: stateLampu[act] = 0
        if stateLampu[act+1] == 0 : stateLampu[act+1] = 1
        else: stateLampu[act+1] = 0
    if act == nLampu-1:
        if stateLampu[act] == 0 : stateLampu[act] = 1
        else: stateLampu[act] = 0
        if stateLampu[act-1] == 0 : stateLampu[act-1] = 1
        else: stateLampu[act-1] = 0

for i in range (nLampu):
    x = x + str(stateLampu[i])
print(f"Keadaan akhir rangkaian lampu adalah {x}.")
