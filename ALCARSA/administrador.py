import pickle
import os

#Clase para guardar, consultar, modificar, etc todos los datos de los administradores del sistema
class administrador(object):

    #Funcion principal, esta crea el objeto de tipo administrador
    def __init__(self, identificacion, nombre, puesto,nombre_usuario, contraseña):
        self.identificacion= identificacion
        self.nombre= nombre
        self.puesto= puesto
        self.nombre_usuario= nombre_usuario
        self.contraseña= contraseña

    # Funcion que imprime el objeto consultado
    def imprimir(self):
        return self.identificacion, self.nombre, self.puesto, self.nombre_usuario, self.contraseña

    #Esta funcion carga los datos guardados en el archivo de administradores
    def cargar_archivo(self):
            self.objetos = []
            carga= True
            try:
                (open("obj.pickle", "rb"))

            except:
                   carga= False

            if(carga):
                with (open("obj.pickle", "rb")) as openfile:
                    while True:
                        try:
                            self.objetos.append(pickle.load(openfile))
                        except EOFError:
                               break



    # Esta funcion devuelve la lista .pickle 
    def devuelve_lista(self):
        self.objetos = []

        carga = True
        try:
            (open("obj.pickle", "rb"))

        except:
            carga = False

        if (carga):
            with (open("obj.pickle", "rb")) as openfile:
                while True:
                    try:
                        self.objetos.append(pickle.load(openfile))
                    except EOFError:
                        break
        return self.objetos
 
    #Esta funcion guarda los datos de los administradores que se van ingresando
    def guardar_archivo(self):
            self.obj= self.imprimir(self)
            with open("obj.pickle", "ab") as f:
                    pickle.dump(self.obj, f)

    # Esta funcion reestructura el archivo para guardar los nuevos datos modificados
    def reescribir_archivo(self):
            reingreso = administrador
            contador = 0

            while(contador < len(self.objetos)):
                reingreso.identificacion = self.objetos[contador][0]
                reingreso.nombre= self.objetos[contador][1]
                reingreso.puesto= self.objetos[contador][2]
                reingreso.nombre_usuario= self.objetos[contador][3]
                reingreso.contraseña= self.objetos[contador][4]
                if(contador==0):

                      self.obj = reingreso.imprimir(reingreso)
                      os.remove("obj.pickle")
                      with open("obj.pickle", "ab") as f:
                                 pickle.dump(self.obj, f)
                      contador = contador + 1
                else:

                    self.obj = reingreso.imprimir(reingreso)
                    with open("obj.pickle", "ab") as f:
                        pickle.dump(self.obj, f)
                    contador =  contador + 1


    # Esta busca y modifica los datos del administrador que se desea modificar
    def modificar(self, identificacion, nombre, puesto, nombre_usuario, contraseña):

        carlos = administrador
        carlos.cargar_archivo(carlos)
        contador = 0

        while (contador < len(self.objetos)):
            if (self.objetos[contador][0] == identificacion):
                self.objetos.remove(self.objetos[contador])
                self.objetos.insert(contador, (identificacion, nombre, puesto, nombre_usuario, contraseña))

                break
            else:
                contador = contador + 1;
        carlos.reescribir_archivo(carlos)

    # Esta funcion permite verificar la cedula de la lista administrador
    def verificar_cedula(self, cedula =str()):
            carlos= administrador
            carlos.cargar_archivo(carlos)
            contador=0
            ingreso= True

            while(contador < len(self.objetos)):
                if(int(self.objetos[contador][0])== int(cedula)):
                                    ingreso= False
                                    break
                else:
                     contador = contador + 1;

            if(ingreso):
                 return ingreso
            else:
                 return ingreso

    # Esta funcion se encarga de verificar que el usuario y la contraseña ingresados pertenescan a algun administrador
    def verificar_acceso(self, usuario =str(), contraseña= str()):
            carlos= administrador
            carlos.cargar_archivo(carlos)
            contador=0
            ingreso= False

            while(contador < len(self.objetos)):
                if((self.objetos[contador][3]== usuario) and (self.objetos[contador][4]== contraseña)):
                                    ingreso= True
                                    break
                else:
                     contador = contador + 1;

            if(ingreso):
                return self.objetos[contador]

            else:
                return []


