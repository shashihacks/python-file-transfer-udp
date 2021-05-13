import socket
import os
if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455

    """ Creating the UDP socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    """ Bind the host address with the port """
    server.bind((host, port))
    def retriveFile(filename):
        print(filename, "exists")
        server.sendto(("EXISTS " +str(os.path.getsize(filename))).encode("utf-8"), addr)

        with open(filename, 'rb') as f:
            bytesToSend = f.read(1024)
            server.sendto(bytesToSend, addr)
            while bytesToSend != "":
                bytesToSend = f.read(1024)
                server.sendto(bytesToSend, addr)
        server.close()
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
        retriveFile(data)
        # data = data.upper()
        # data = data.encode("utf-8")
        # server.sendto(data, addr)