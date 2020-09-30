#-----------------------
#-------Ejderhan--------
#-----------------------

sesliharf = ["a","e","ı","i","u","ü","o","ö"] #Sesli harfler tanimlandi
from time import sleep as sl

def yaz(yazi, sure = 0.01): #Yazı yazdırmak için
    for i in str(yazi): #yazi nin icindeki her harf i
        sl(sure) #sleep 0.01 (default)
        print(str(i), sep = "", end="", flush=True)

def encode(yazi, encodeharf = "g"): #encode icin
    harfler = []
    encoded = ""

    for i in str(yazi):
        harfler.append(i) #Harfleri ayirdim

        #kus dili >>> ku-"gu"-s di-"gi"-li-"gi"

    for i in harfler: #Her harfler in icindeki i
        if i in sesliharf: #Eger i sesli ise
            decoded = decoded + str(i + encodeharf + i) #k-"u"-"gu"-s
        else: #Degilse
            decoded = decoded + i #Ekleme yapmadan yaz

    return str(encoded) #String cikis alacagiz
