import socket
import threading
msgFromClient       = "Hello UDP Server"
serverAddressPort   = ("127.0.0.1", 20004)
bufferSize          = 1024
c=4
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
def request():
    print("escuchando al server ")
    global c #define la variable global para ocuparla en cualquier funcion 
    #>ojo< si igualas una variable global dentro de una funcion la conviertes en variable local
    while True:     
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        message = msgFromServer[0]
        print(message.decode("utf-8"))
        if message.decode("utf-8")!="":
            c=4
def main():
    global ms
    global c
    while True:
        if c >0:
            print("porfavor ingrese el dato a enviar ")
            bytesToSend= input("-> ")
            ms=str.encode(bytesToSend)
            UDPClientSocket.sendto(ms, serverAddressPort)
            if ms !="":
                h = threading.Thread(target=request)
                h.start()
                
                c=0

if __name__ == '__main__':
    main()