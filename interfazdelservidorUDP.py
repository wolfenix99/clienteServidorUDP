#un modulo es objeto de Python con atributos con nombres arbitrarios, no es otra cosa mas que un archivo con .py
from tkinter import * #Carga módulo tk (widgets estándar)
import tkinter as ttk # Carga ttk (para widgets nuevos 8.5+)importa el modulo y le asigna otro nombre en este caso ttk
import socket         #importa el modulo socket
import threading      #importa los modulos de threading
localIP     = "127.0.0.1" #define la direccion ip
localPort   = 30061 #define el puerto donde se va a comunicar
bufferSize  = 1024  #define el numero de bytes que envia
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #en esta parte crea un objeto mediante el constructor socket y le asigna 
# la familia y el tipo
# puede haber socket de flujo o TCP(socket.SOCK_STREAM) y socket de datagramas UDP (socket.SOCK_DGRAM)
# los sockets se pueden clasificar en familia en este caso UNIX socket.AF_UNIX O en ficheros sockets socket.AF_INET 
# tambien existen los socket.AF_INET6 para IPv6
# Para crear un socket se utiliza el constructor socket.socket() que puede tomar como parámetros opcionales la familia,
# el tipo y el protocolo. Por defecto se utiliza la familia AF_INET y el tipo SOCK_STREAM.

class Aplicacion():

    def __init__(self):     

        # En el ejemplo se utiliza el prefijo 'self' para
        # declarar algunas variables asociadas al objeto 
        # ('mi_app')  de la clase 'Aplicacion'. Su uso es 
        # imprescindible para que se pueda acceder a sus
        # valores desde otros métodos:
        self.raiz = Tk()  #se crea la ventana principal
        self.raiz.geometry('500x400') #asigna las medidas a la ventana principal
        self.raiz.title('servidor')   #le asigna el titulo de la ventana
        self.raiz.configure(bg="black") #le asigna el fondo de la ventana
        #variables a utilizar
        self.text = StringVar()    #para tkinter se utiliza Stringvar para declarar variables tipo cadena e IntVar() para entero
        self.var = StringVar()
        #-------------------------------------------------------------
        self.en = ttk.Entry(self.raiz,textvariable=self.text,width=10) # Define el widget Entry para ingresar datos
        self.en.pack(side=TOP,fill=BOTH,padx=0, pady=2,ipadx=5,ipady=5) #esto es para asignarle el espacio dentro de la ventana y difentes caracteristicas
        #-------------------------------------------------------------  
        self.et1 = ttk.Label(self.raiz,bg="red",textvariable=self.var) #Define el widget etiqueta que enviara ala variable var  
        self.et1.pack(side=TOP,fill=BOTH,padx=2,pady=2,ipadx=5,ipady=5)#esto es para asignarle el espacio dentro de la ventana y difentes caracteristicas
        #-------------------------------------------------------------   
        self.bsalir = ttk.Button(self.raiz, text='enviar',command=self.enviar) #Define el widget de boton que envia ala funcion enviar donde envia los datos
        self.bsalir.pack(padx=5,pady=20,ipadx=5,ipady=5) #Define la posicion del boton dentro de la pantalla
        #-------------------------------------------------------------
        self.bsalir = ttk.Button(self.raiz, text='Salir',command=self.raiz.destroy) #Define el widget de boton donde cierra la ventana                             
        self.bsalir.pack(padx=5,pady=20,ipadx=5,ipady=5)
        #------------------------------------------------------------- 
        UDPServerSocket.bind((localIP, localPort)) # define el puerto y la direccion ip donde se mantendra ala escucha
        #-------------------------------------------------------------
        self.t = threading.Thread(target=self.iniciar_server)  #crea un objeto del modulo threading con el constructor Thread donde manda a llamar un metodo
        #de la clase aplicacion
        self.t.start() #inicializa el objeto para poder correrlo como hilo paralelo
        self.raiz.mainloop() #crea el hilo principal de la ventana tkinter donde se mantiene a la espera de un evento
        

    def enviar (self):
        bytesToSend = str.encode(self.text.get()) #codifica el mensaje que se encuentra en el widget entry
        UDPServerSocket.sendto(bytesToSend,self.address) #envia el mensaje codificado a la direccion que recibio del cliente

    def iniciar_server(self):
      while True :
        bytesAddressPair = UDPServerSocket.recvfrom(1024) #este metodo de la clase socket recibe el mensaje o envia el mensaje. donde lo recibe en forma de tupla
        message = bytesAddressPair[0] #separa la primer parte de la tupla donde tiene la informacion
        self.address = bytesAddressPair[1] #crea la variable de direccion en forma global self
        self.var.set(message.decode("utf-8")) #decodofica el mensaje y se lo envia ala variable var para que el widget muestre la informacion

def main():            #define el metodo principal 
    mi_app = Aplicacion() #instancia el objeto de la clase aplicacion 
    return 0

if __name__ == '__main__': 
    main()