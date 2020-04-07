import socket
print('================================================')
print('Programi: FIEK-TCP Clienti')
print('================================================')


serverName = input("Shenoni emrin e serverit (apo lini zbrazet per vlere te nenkuptuar): ")
port = input("Shenoni portin e serverit (apo lini zbrazet per vlere te nenkuptuar): ")
if (serverName == ''):
    serverName = 'localhost'
if (port == ''):
    port = 13000
else:
    try:
        port = int(port)
    except:
        print("Nuk keni japur numer valid per port")

print("Jeni lidhur ne serverin ",serverName," ne portin ",port)
print("============================================\n")

# MENYJA e programit 
print("""Jeni te lidhur me serverin!
       Cilat nga keto metoda deshironi ti perdorni: 
               
       1.IPADDRESS                        - Percakton dhe kthen IP adresen e klientit
               
       2.PORT                       - Percakton dhe kthen portin e klientit
               
       3.COUNT {hapesire} teksti      - Merr si parameter nje tekst dhe kthen numrin e zanoreve dhe bashtingelloreve 
                                        ne ate tekst
               
       4.REVERSE {hapesire} teksti      - Merr si parameter nje tekst dhe kthen fjaline e shtypur dhe 
                                         te formatuar ne anen e kundert
      
       5.PALINDROME {hapesire} teksti  - E merr tekstin e shikon a eshte palindrome apo jo
               
       6.TIME                          - Kthen kohen aktuale ne server
               
       7.GAME                          - Kthen vargun e 5 numrave "random" te rangut [1,35]
               
       8.GCF {hapesire} numri {hapesire} numri    - Gjen numrin GCF si rezultat i parametrit 
                                                    te dhene

       9.CONVERT {hapesire} opcioni {hapesire} vlera    - Kthen si rezultat konvertimin e parametrit hyres sipaste 
                                                         opcionit  te dhene
                                                                 cmToFeet
                                                                 FeetToCm
                                                                 kmToMiles
                                                                 MileToKm
               
       10.SYPTREKENDESHIT {hapesire} vleraA {hapesire} vleraH   - Merr si parameter vlerat e brinjes A dhe lartesite H
                                
      
       11.ROLLTHEDICE                  - Kthen dy vlera "random" te dy zareve te gjuajtura
               
               Sheno quit per te dalur nga programi!
========================================================================================================================================              
               """)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((serverName, port))
    while True:
        try:
            request = input("Shenoni kerkesen per serverin apo shenoni quit per te dalur nga programi: ")
            if (request == "quit"):
                break
            elif (len(request.encode()) > 128):
                print("Keni japur kerkese me te madhe se 128 bajt")
                continue
            elif (request == ""):
                continue
            s.sendall(str.encode(request))
            response = s.recv(128).decode()
            print('Pergjigja: ', repr(response))
        except:
            print("Ka ndodhur nje gabim, ju lutem provoni perseri")