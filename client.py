import socket
import math
import random
global prime, root


host = "127.0.0.1"
port = 4455
addr = (host, port)

""" Creating the UDP socket """
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Key Information
def secretNumber ():
    secret = int(random.randint(0,100))
    return secret
mySecretKey = 96
root = 3 # agreed root
prime = 17
# server public key (variable) 
myPublicKey = 1
def calculateSharedKey(receivedPublicKey):
    print("calculating shared key")
    mySharedKey = (int(receivedPublicKey) ** mySecretKey) % prime
    print("client shared key" , mySharedKey)

# Request file 


askKey = "KEY".encode("utf-8")
client.sendto(askKey, addr)
data, addr = client.recvfrom(1024)
data = data.decode("utf-8")
if(data[:3]=='KEY'): 
    print(f"{data}")
    getKeyFromData = f"{data}"[4:]
    calculateSharedKey(getKeyFromData)

while True:

    data = input("Enter your input: ")
    filename = data

    if data == "exit":
        data = data.encode("utf-8")
        client.sendto(data, addr)
        print("Disconneted from the server.")
        client.close()
        exit()

    data = data.encode("utf-8")
    client.sendto(data, addr)

    data, addr = client.recvfrom(1024)
    data = data.decode("utf-8")

    if(data[:6]=='EXISTS'):
        filesize = int(data[6:])
        print(filesize, "filesize")
        f = open('new_'+filename, 'wb')
        data,addr = client.recvfrom(1024)
        totalRecv = len(data)
        print("writing data")
        f.write(data)
        while totalRecv < filesize:
            data,addr = client.recvfrom(1024)
            totalRecv+=len(data)
            f.write(data)
            # print("{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done")
        print("download complete !!")

        f.close()
        # client.close()
    else:
        print("file does'nt exist")
# client.close()

    