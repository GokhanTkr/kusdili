#-----------------------
#-------Ejderhan--------
#-----------------------
#04/09/2020 | UTC3 21.45

sesliharf = ["a","e","ı","i","u","ü","o","ö"] #Sesli harfler tanimlandi
from time import sleep as sl

def yaz(yazi, sure = 0.01):
    for i in str(yazi):
        sl(sure)
        print(str(i), sep = "", end="", flush=True)

def yardim():
    yaz("Kus Dili Ceviriciye hosgeldiniz!")
    sl(1)
    yaz("\nKullanabileceğiniz komutlar şunlardır:")
    sl(1)
    yaz("""
    cikis, c : yazilimi durdurmak icin kullanilir.
    decode, d: sifrelemek icin kullanılır.
    encode, e: sifreli yaziyi cozmek icin kullanılır. (Aktif degil)
    yardim, y: yardim yazisini gosterir.
    """)

yardim()

while True: #Dongu baslangaci


    komut = input("\n>>> ")


    if komut in ["cikis", "c"]:
        break

    elif komut in ["decode", "d"]:
        yazi = input("Cevrilecek olan yazı: ")
        harfler = []
        decoded = ""

        for i in yazi:
            harfler.append(i)

            #kus dili >>> ku-"gu"-s di-"gi"-li-"gi"

        for i in harfler:
            if i in sesliharf:
                decoded = decoded + str(i + "g" + i)
            else:
                decoded = decoded + i

        yaz("\n"+decoded)


    elif komut in ["encode", "e"]:
        yaz("komut kullanilabilir durumda degil!\n")

    elif komut in ["yardim", "y"]:
        yardim()

    else:
        yaz("\nVar olan bir komutu yazmadınız.\n")
