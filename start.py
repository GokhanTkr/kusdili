#-----------------------
#-------Ejderhan--------
#-----------------------
#04/09/2020 | UTC3 21.45

import modules

def yardim():
    modules.yaz("Kus Dili Ceviriciye hosgeldiniz!")
    modules.yaz("\nKullanabileceğiniz komutlar şunlardır:")
    modules.yaz("""
    cikis, c : yazilimi durdurmak icin kullanilir.
    decode, d: sifreli yaziyi cozmek icin kullanılır. (Aktif degil)
    encode, e: sifrelemek icin kullanılır.
    yardim, y: yardim yazisini gosterir.
    """)

yardim()

while True: #Dongu baslangaci
    komut = input("\n>>> ")


    if komut in ["cikis", "c"]:
        break

    elif komut in ["encode", "e"]:
        text = input("Encode edilecek yazi: ")
        modules.yaz(modules.encode(text))

    elif komut in ["decode", "d"]:
        text = input("Decode edilecek yazi: ")
        modules.yaz(modules.decode(text))

    elif komut in ["yardim", "y"]:
        yardim()

    else:
        modules.yaz("\nVar olan bir komutu yazmadınız.\n")
