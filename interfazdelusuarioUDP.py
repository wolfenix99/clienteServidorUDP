#un modulo es objeto de Python con atributos con nombres arbitrarios, no es otra cosa mas que un archivo con .py
from tkinter import *#Carga módulo tk (widgets estándar)
import tkinter as ttk # Carga ttk (para widgets nuevos 8.5+)importa el modulo y le asigna otro nombre en este caso ttk
import socket #importa el modulo socket
import threading#importa los modulos de threading

serverAddressPort   = ("127.0.0.1", 30061) #define la tupla donde indica la direccion y el puerto donde se envia la informacion
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)#en esta parte crea un objeto mediante el constructor socket

class Aplicacion():
    def __init__(self):     
         
        # En el ejemplo se utiliza el prefijo 'self' para
        # declarar algunas variables asociadas al objeto 
        # ('mi_app')  de la clase 'Aplicacion'. Su uso es 
        # imprescindible para que se pueda acceder a sus
        # valores desde otros métodos:
        self.raiz = Tk() #se crea la ventana principal
        self.raiz.geometry('500x400') #asigna las medidas a la ventana principal
        self.raiz.title('usuario') #le asigna el titulo de la ventana
        self.raiz.configure(bg="white") #le asigna el fondo de la ventana
        #-------------------------------------------------------------
        self.text = StringVar() #variables a utilizar
        self.var = StringVar()
        #-------------------------------------------------------------
        self.en = ttk.Entry(self.raiz,textvariable=self.text,width=10)# Define el widget Entry para ingresar datos
        self.en.pack(side=TOP, fill=BOTH,padx=2, pady=5,ipadx=5,ipady=5)#esto es para asignarle el espacio dentro de la ventana y difentes caracteristicas 
        #-------------------------------------------------------------      
        self.et1 = ttk.Label(self.raiz,bg="red",textvariable=self.var)#Define el widget etiqueta que enviara ala variable var
        self.et1.pack(side=TOP,fill=BOTH,padx=2,pady=2,ipadx=5,ipady=5)#esto es para asignarle el espacio dentro de la ventana y difentes caracteristicas
        #-------------------------------------------------------------
        self.binfo = ttk.Button(self.raiz, text='enviar',command=self.conexion) #Define el widget de boton que enviara ala funcion conexion                               
        self.binfo.pack(padx=5,pady=1,ipadx=5,ipady=5)
        #-------------------------------------------------------------
        self.bsalir = ttk.Button(self.raiz, text='Salir',command=self.raiz.destroy) #Define el widget de boton donde cierra la ventana                            
        self.bsalir.pack(padx=5,pady=20,ipadx=5,ipady=5)

        self.raiz.mainloop()#crea el hilo principal de la ventana tkinter donde se mantiene a la espera de un evento

    def recibir_server(self):

        while True:                
            msgFromServer = UDPClientSocket.recvfrom(1024) #este metodo de la clase socket recibe el mensaje o envia el mensaje.
            message = msgFromServer[0]#separa la primer parte de la tupla donde tiene la informacion
            self.var.set(message.decode("utf-8"))#decodofica el mensaje y se lo envia ala variable var para que el widget muestre la informacion
       
        
    def conexion(self):

         bytesToSend = str.encode(self.text.get())
         UDPClientSocket.sendto(bytesToSend, serverAddressPort)
         t = threading.Thread(target=self.recibir_server)  
         t.start()
        
def main(): #define el metodo principal 
    mi_app = Aplicacion()#instancia el objeto de la clase aplicacion 
    return 0

if __name__ == '__main__':
    main()