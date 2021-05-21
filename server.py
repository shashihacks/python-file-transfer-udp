import socket
import os
import math
import random
global prime, root
# from Crypto.Cipher import AES

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455
    addr = (host, port)
    """ Creating the UDP socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    """ Bind the host address with the port """
    server.bind((host, port))

    def secretNumber ():
        secret = int(random.randint(0,100))
        return secret

    # key information
    clientPublicKey = 1 #bob
    prime = 17
    root =3
    mySecretNumber = 89
    myPublicKey = 14

    # calculateSharedKey
    mySharedKey = (clientPublicKey ** mySecretNumber) % prime
    print("server shared Key", mySharedKey)

    def retriveFile(filename):
        print(filename, "exists")
        server.sendto(("EXISTS " +str(os.path.getsize(filename))).encode("utf-8"), addr)
        with open(filename, 'rb') as f:
            bytesToSend = f.read(1024)
            server.sendto(bytesToSend, addr)
            while(bytesToSend):
                print("sending", bytesToSend)
                bytesToSend = f.read(1024)
                server.sendto(bytesToSend, addr)
            f.close()
                
        # print("closing") 
        # server.close()

    def sendPublicKey():
        print("Sending Public key")
        keyInfo = 'KEY ' + str(myPublicKey)
        server.sendto(keyInfo.encode("utf-8"), addr)
    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        print(data)

        if data == "!EXIT":
            print("Client disconnected.")
            break

        print(f"Client: {data}")
        data = f"{data}"
        print(data)

        # deffie hellman

        if(data=="KEY"):
            sendPublicKey()
        else:

        # File retrive and send
            retriveFile(data)
        # server.close()
