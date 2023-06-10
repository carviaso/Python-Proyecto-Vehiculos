import pickle
import os

#Clase para guardar, consultar, modificar, cargar y guardar todos los usuarios que ingresan al sistema
class bitacora(object):

    #Funcion principal, esta crea el objeto de tipo administrador
    def __init__(self, identificacion, nombre, puesto,nombre_usuario, contraseña):
        self.identificacion= identificacion
        self.nombre= nombre
        self.puesto= puesto
        self.nombre_usuario= nombre_usuario
    # Esta funcion permite imprimir los objetos de tipo administrador
    def imprimir(self):
        return self.identificacion, self.nombre, self.puesto, self.nombre_usuario
    # Esta funcion permite guardar los archivos en una encriptacion tipo pickle
    def guardar_archivo(self):
            self.obj= self.imprimir(self)
            with open("bitacora.pickle", "ab") as f:
                    pickle.dump(self.obj, f)
    # Esta funcion carga los archivos y los desencripta dentro de .pickle
    def cargar_archivo(self):
            self.objetos = []
            carga= True
            try:
                (open("bitacora.pickle", "rb"))

            except:
                   carga= False

            if(carga):
                with (open("bitacora.pickle", "rb")) as openfile:
                    while True:
                        try:
                            self.objetos.append(pickle.load(openfile))
                        except EOFError:
                               break

            return self.objetos
