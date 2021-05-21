### SEMINAR REPORT 21-05-2021

1. Read client server communication UDP
2. Read TFTP protocol

3. Practical part:
    - Implemented Client server communication in UDP
    - Pre-shared key suing Diffie hellman
    - File transfer using UDP

#### Server code
``` python
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
        server.sendto(str(myPublicKey).encode("utf-8"), addr)
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
```

#### client code:

```python
import socket
import math
import random
global prime, root

if __name__ == "__main__":
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
    while True:

        data = input("Enter your input: ")
        # filename = data

        if data == "!EXIT":
            data = data.encode("utf-8")
            client.sendto(data, addr)
            print("Disconneted from the server.")
            client.close()
            exit()

        data = data.encode("utf-8")
        client.sendto(data, addr)

        data, addr = client.recvfrom(1024)
        data = data.decode("utf-8")
        print(f"{data}")
        # calculateSharedKey(f"{data}")
             
        # if(data[:3]=='KEY'):
            
        #     calculateSharedKey(f"{data}")
        if(data[:6]=='EXISTS'):
            filesize = int(data[6:])
            print(filesize, "filesize")
            f = open('new_'+data, 'wb')
            data,addr = client.recvfrom(1024)
            # data = data.decode("utf-8")
            totalRecv = len(data)
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

```



> Updated code on github: https://github.com/shashihacks/python-file-transfer-udp


4. Currently working on
    - Compression techniques
    - AES Encryption usning pycrypto
    - Resolving unexpected server crashes for large files