# Cuenta Nequi
import time
import platform #Nos ayuda a reconocer cuál es el sistema operativo que estemos usando en la computadora
import os #Nos sirve para invocar el comando de limpieza en pantalla
from getpass import getpass

Empezar = True
Usuario = []
Password = []
Telefono = []
Cap = []
Ahorro = []

def Main(count):

    print("------------------ NEQUI ------------------")

    while not Empezar != True:
        print("-------- Menú App --------\n")
        print("1.Crear\n2.Ingresar")
        Preguntar = input("Digita la opción deseada: ")

        if Preguntar == "1" or Preguntar == "Crear" or Preguntar == "crear":
            count += 1
            if count == 2:
                Usuario.pop(0)
                Cap.pop(0)
                Ahorro.pop(0)
                count = 0 
            Crear()
        else:
            Cuenta_Creada()

class Crear():

    def __init__(self):
        self.Telefono = 0
        self.Nombre = " "
        self.Clave = 0
        self.Crear_Cuenta()
    
    def Crear_Cuenta(self):
        self.Limpiar()
        self.Telefono = int(input("Digita el número del celular: +57 "))
        self.Nombre = input("Digita el nombre: ")
        self.Clave = getpass("Digita una nueva clave: ")
        self.Guardar()
        self.Limpiar()
    
    def Guardar(self):
        Telefono.append(self.Telefono)
        Usuario.append(self.Nombre)
        Password.append(self.Clave)
        # print(Telefono[0])
    
    def Limpiar(self):
        time.sleep(1)

        if platform.system() == 'Windows':
            # print("Espere unos instante...")
            time.sleep(1)
            os.system('cls')
        else:
            os.system('clear')

class Cuenta_Creada(Crear):
    
    def __init__(self):
        self.Contador = 3
        self.Iniciar_Sesion()
    
    def Iniciar_Sesion(self):
        self.Limpiar()
        self.Telefono = int(input("Digita el teléfono: "))
        # self.Clave = int(input("Digita la clave: "))
        self.Clave = getpass("Digita la clave: ")

        if self.Telefono in Telefono:
            if self.Clave in Password:
                self.Limpiar()
                self.Cuenta_Ingresada()

        elif self.Telefono != Telefono:
            if self.Clave != Password:
                self.Limpiar()
                print("Ingreso invalido, por favor vuelva a intentar")
                self.Contador = self.Contador - 1
                if self.Contador == 0:
                    print("El sistema se bloqueo, espera unos segundos!!")
                    time.sleep(5)
                    self.Iniciar_Sesion()
            self.Iniciar_Sesion()

    def Cuenta_Ingresada(self):
        Proceso()

class Proceso(Cuenta_Creada):

    def __init__(self):
        self.acumulador = 0
        self.acumuladorA = 0
        self.Capital = 0
        self.Ahorro = 0
        print("\tBienvenido",Usuario[0],"\n")
        print("Estado Actual:\nCantidad: $",Cap,"\nAhorro: $",Ahorro)
        self.Capital_()

    def Capital_(self):
        print("-------- Menú Principal -------")
        print("1. Consignar\n2. Retirar\n3. Comenzar ahorro\n4. Salir")
        Op = int(input("Digita tu opción: "))

        while Op != 5:

            if Op == 1:
                self.Capital = float(input("Digita la cantidad a consignar a tu cuenta: $ "))
                self.acumulador = self.acumulador + self.Capital
                self.Limpiar()
                self.Actualizar_Datos()

            if Op  == 2:
                self.Retirar = input("Deseas retirar de tu cuenta actual o tu ahorro? ")

                if self.Retirar == "Cuenta" or self.Retirar == "cuenta":
                    self.Capital = float(input("Digita la cantidad a retirar de tu cuenta: $"))
                    self.acumulador -= self.Capital
                    self.Limpiar()
                    self.Actualizar_Datos()
                
                else:
                    self.Capital = float(input("Digita la cantidad a retirar de tu ahorro: $"))
                    self.acumuladorA -= self.Capital
                    self.Ahorro = self.acumuladorA
                    self.Limpiar()
                    self.Actualizar_Datos()

            if Op == 3:
                self.Capital = float(input("Digita la cantidad que deseas ahorrar: $"))
                self.acumulador -= self.Capital
                self.acumuladorA += self.Capital
                self.Ahorro =  self.acumuladorA 
                self.Limpiar()
                self.Actualizar_Datos()
            
            if Op == 4:
                Cap.append(self.acumulador)
                Ahorro.append(self.Ahorro)
                print("Saliendo de tu cuenta...")
                self.Limpiar()
                Main(count=1)
    
    def Actualizar_Datos(self):
        print("\tBienvenido",Usuario[0],"\n")
        print(f"Estado Actual:\nCantidad: ${self.acumulador:.0f}\nAhorro ${self.Ahorro:.0f}")
        self.Capital_()

contador = 0
Main(contador)
