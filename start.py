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
    decode, d: sifrelemek icin kullanılır.
    encode, e: sifreli yaziyi cozmek icin kullanılır. (Aktif degil)
    yardim, y: yardim yazisini gosterir.
    """)

yardim()

while True: #Dongu baslangaci
    komut = input("\n>>> ")


    if komut in ["cikis", "c"]:
        break

    elif komut in ["encode", "e"]:
        text = input("Cevrilecek olan yazı: ")
        modules.yaz(modules.encode(text))

    elif komut in ["encode", "e"]:
        modules.yaz("komut kullanilabilir durumda degil!\n")

    elif komut in ["yardim", "y"]:
        yardim()

    else:
        modules.yaz("\nVar olan bir komutu yazmadınız.\n")
