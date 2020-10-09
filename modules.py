#-----------------------
#-------Ejderhan--------
#-----------------------

sesliharf = ["a","e","ı","i","u","ü","o","ö","A","E","I","İ","U","Ü","O","Ö"] #Sesli harfler tanimlandi
from time import sleep as sl

def yaz(yazi, sure = 0.005): #Yazı yazdırmak için
    for i in str(yazi): #yazi nin icindeki her harf i
        sl(sure) #sleep 0.01 (default)
        print(str(i), sep = "", end="", flush=True)

def encode(yazi, encodeharf = "g"): #encode icin
    harfler = []
    encoded = ""

    #kus dili >>> ku-"gu"-s di-"gi"-li-"gi"

    for i in str(yazi): #Her harfler in icindeki i
        if i in sesliharf: #Eger i sesli ise
            encoded = encoded + str(i + encodeharf + i) #k-"u"-"gu"-s
        else: #Degilse
            encoded = encoded + i #Ekleme yapmadan yaz

    return str(encoded) #String cikis alacagiz


###!!!CALISMIYOR!!!###
def decode(yazi, encodeharf = "g"): #decode icin
    decoded = ""

    for i in sesliharf:
        yazi.split(i+encodeharf)

    return decoded
###^^^^^^^^^^^^^^^^###

def bruteforce(yazi):
    pass
