#Soal_1
a=input('Masukkan angka 1:')
b=input('Masukkan angka 1:')

def proses_pembalik(a,b): 
    aaa = int(a[::-1]) #string akan dibalik kemudian baru dijadikan int dan di assign ke variabel baru
    bbb = int(b[::-1]) #string akan dibalik kemudian baru dijadikan int dan di assign ke variabel baru
    c = aaa + bbb #disini terjadi kalkulasi pertambahan
    cc = print((str(c))[::-1]) #hasil dari kalkulasi di balik kemudian di jadikan string lalu di print, semua proses ini di assign pada variabel cc
    return cc # yang kemudian cc akan di return untuk mengeluarkan value pada fungsi def

if a.isnumeric() and b.isnumeric():  # Line ini digunakan untuk mengidentifikasi input user apakah Int
    aa = int(a)
    bb = int(b)
    if aa >359999 or aa <0 or bb >359999 or bb <0: # Jika input user diluar 359999 atau minus maka akan invalid
        print(" Invalid Input!")
    else:
        proses_pembalik(a,b) #jika semua kondisi terpenuhi maka akan melanjutkan ke fungsi pada line 5
else: # Jika input user diluar int maka akan invalid
    print(" Invalid Input!")

