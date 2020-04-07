

from socket import *
from datetime import *
import random
import sys
import threading
import cmath
from _thread import *


#Metodat

def IPADDRESS():
    return "Ip adresa juaj eshte %s" % addr[0]

   

def PORT():
    return "Porti juaj eshte %s" % addr[1]
  
def COUNT(text):
    fjalia = str(text)
    nr_zanoret=0
    nr_bashtingellore=0
    zanoret = set("aeiouAEIOU")
    bashtingelloret = set("BCDFGHJKLMNPQRSTVXZWbcdfghjklmnpqrstvxzw")
    for x in fjalia:
        if x in zanoret:
            nr_zanoret=nr_zanoret+1
        elif x in bashtingelloret:
            nr_bashtingellore=nr_bashtingellore+1


    text="Teksti permban " + str(nr_zanoret) + " zanore dhe " + str(nr_bashtingellore) + " bashtingellore."
 
    return text


def REVERSE(str):
  return "Fjalia e shtypur ne ekran: " + ' '.join(word[::-1] for word in str.split())

def PALINDROME(string):
    
    rev_string= string[::-1]
    if string == rev_string:
        return "The string is palindrome!"
    else:
      return "The string is not palindrome!"

def TIME():
    return "Koha aktuale eshte: " +  datetime.now().strftime("%H:%M:%S")

def GAME():
    return  str(random.sample(range(1, 35), 5))

def GCF(x, y): 
    
   x = float(x)
   y = float(y)
   while(y): 
       x, y = y, x % y 
  
   return "Faktori me i madh i perbashket i dy numrave eshte: "  + str(x)

def CONVERT(option,number):
    
    nr = float(number)
    if option == 'cmToFeet':
        return "% .2f " % (nr/30.48) + " Feet"
    elif option =='FeetToCm':
        return "% .2f" % (nr*30.48) + " Cm"
    elif option == 'kmToMiles':
        return "% .2f" % (nr*0.6214) + " Miles"
    elif option == 'MileToKm':
        return "% .2f" % (nr/0.6214) + " Km"
    else:
        return "Error - Konvertimi i kerkuar nuk ekziston"
   

#Metodat e shtuara
def SYPTREKENDESHIT(a, h):
    try:
        a=float(a)
        h=float(h)
    except:
        return "Argumentet e dhena nuk jane numra"
    if(a<0 or h<0):
        return "Keni dhene brinjen dhe lartesine negative"
    return "Syprina e trekendeshit eshte: " + str((a*h)/2)

def ROLLTHEDICE():
    min = 1
    max = 6
    kubi1 = str(random.randint(min, max))
    kubi2 = str(random.randint(min, max))
    pergjigja = str("Rolling the dice...        Vlerat e qelluara jane:   " + kubi1 + " dhe " + kubi2)
    return pergjigja

# te gjitha te dhenat qe dergohen te klienti kjo metode i printon edhe te serveri
def ShtypTeDhenat(teDhenat):
    print("\n----------------------------------------------------------------------------------------------")
    print("Te dhenat e derguara te klienti =>  ", teDhenat)
    return
 
def handle_request(data):
        request=data.split()
        response=""
        if request[0] == "IPADDRESS":
            response = IPADDRESS()
            ShtypTeDhenat(("IP adresa e klientit: "+IPADDRESS()))
        elif request[0] == "PORT":
            response = PORT()
            ShtypTeDhenat(("Porti i  klientit: "+PORT()))
        elif request[0] == "COUNT":
            response = str(COUNT(request[1]))
            ShtypTeDhenat(("Teksti kthen keto: "+COUNT(request[1])))
        elif request[0] == "REVERSE":
            response = str(REVERSE(request[1]))
            ShtypTeDhenat(("Teksti kthen:  "+REVERSE(request[1])))
        elif request[0] == "PALINDROME":
            response = PALINDROME(request[1])
            ShtypTeDhenat(("Teksti kthen:  "+PALINDROME(request[1])))
        elif request[0] == "TIME":
            response = TIME()
            ShtypTeDhenat(("Koha sot:  "+TIME()))
        elif request[0] == "GAME":
            response = GAME()
            ShtypTeDhenat(("Loja kthen 5 numra random: "+GAME()))
        elif request[0] == "GCF":
            response = str(GCF(request[1],request[2]))
            ShtypTeDhenat(str("Faktorin me te madh: "+GCF(request[1],request[2])))
        elif request[0] == "CONVERT":
            response = str(CONVERT(request[1],request[2]))
            ShtypTeDhenat(str("Teksti kthen: "+CONVERT(request[1],request[2])))
        elif request[0] == "SYPTREKENDESHIT":
            response = str(SYPTREKENDESHIT(request[1],request[2]))
            ShtypTeDhenat(str("Syprina:  "+SYPTREKENDESHIT(request[1],request[2])))
        elif request[0] == "ROLLTHEDICE":
            response = str(ROLLTHEDICE())
            ShtypTeDhenat(str(ROLLTHEDICE()))
        else:
            response = "Kerkesa invalide"
            ShtypTeDhenat("ERROR")
        return response
      


   
            
       

             

print('================================================')
print('Programi: FIEK-UDP Serveri')
print('================================================')

#Hosti per socketin e serverit:
host='localhost'

#Porti per socketin e serverit:
port=13000

#Krijimi i socketit,sipas TCP protokollit:
s = socket(AF_INET, SOCK_DGRAM)

#Hosti dhe Porti i serverit me socketin e krijuar:
s.bind((host,port))




print('Serveri eshte i gatshem te pranoj kerkesa...')

while True:
    msg, addr =s.recvfrom(128)
    response = handle_request(msg.decode())
    s.sendto(str.encode(response), addr)

s.close()










    