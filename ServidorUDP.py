#un modulo es objeto de Python con atributos con nombres arbitrarios, no es otra cosa mas que un archivo con .py
import socket
import threading
localIP     = "127.0.0.1" #define la direccion ip
localPort   = 20004 #define el puerto donde estara a la escucha
bufferSize  = 1024 #define el numero de bytes 
c=4 #inicia la variable de control con un numero diferente de cero
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #define el puerto y la direccion ip donde se mantendra ala escucha
UDPServerSocket.bind((localIP, localPort)) #Tenemos ahora que indicar en qué puerto se va a mantener a la escucha 
#nuestro servidor utilizando el método bind. 
#UDPServerSocket.listen(10)
def request():
    global c #define la variable global para ocuparla en cualquier funcion 
    #>ojo< si igualas una variable global dentro de una funcion la conviertes en variable local
    print("porfavor ingrese el dato a enviar ")
    while True:
        if c==0:
            bytesToSend= input("-> ")
            ms=str.encode(bytesToSend)
            UDPServerSocket.sendto(ms,address)
            if ms.decode("utf-8") != "":
                c=4
   
def main():
    global address
    global c
    while True:
        if c>0:
            print("UDP server up and listening")           
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
            message = bytesAddressPair[0]
            address= bytesAddressPair[1]
            h1=address[0]
            mes=message.decode("utf-8")
            print(mes)
            if mes== "quit":
                break
            else:
                h = threading.Thread(target=request)
                h.start()
                c=0
    print("adios")
    UDPServerSocket.close() #cancela la 
    c=0

if __name__ == "__main__":
    main()
