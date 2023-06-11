import pickle
import os

#Clase para guardar, consultar, modificar, etc todos los datos de los administradores del sistema
class asistente(object):

    #Funcion principal, esta crea el objeto de tipo administrador
    def __init__(self, identificacion, nombre, correo, puesto,nombre_usuario, contraseña):
        self.identificacion= identificacion
        self.nombre= nombre
        self.correo= correo
        self.puesto= puesto
        self.nombre_usuario= nombre_usuario
        self.contraseña= contraseña

    # Funcion que imprime el objeto consultado
    def imprimir(self):
        return self.identificacion, self.nombre, self.correo, self.puesto, self.nombre_usuario, self.contraseña

    #Esta funcion carga los datos guardados en el archivo de administradores
    def cargar_archivo(self):
            self.objetos = []
            carga= True
            try:
                (open("asistentes.pickle", "rb"))

            except:
                   carga= False


            if(carga):
                with (open("asistentes.pickle", "rb")) as openfile:
                    while True:
                        try:
                            self.objetos.append(pickle.load(openfile))
                        except EOFError:
                               break


            return self.objetos

    # Esta funcion devuelve la lista de los asistentes guardados en archivo
    def devuelve_lista(self):
        self.objetos = []

        carga = True
        try:
            (open("asistentes.pickle", "rb"))

        except:
            carga = False

        if (carga):
            with (open("asistentes.pickle", "rb")) as openfile:
                while True:
                    try:
                        self.objetos.append(pickle.load(openfile))
                    except EOFError:
                        break
        return self.objetos

    #Esta funcion guarda los datos de los administradores que se van ingresando
    def guardar_archivo(self):
            self.obj= self.imprimir(self)
            with open("asistentes.pickle", "ab") as f:
                    pickle.dump(self.obj, f)

 

    # Esta funcion reestructura el archivo para guardar los nuevos datos modificados
    def reescribir_archivo(self):
            reingreso = asistente
            contador = 0

            while(contador < len(self.objetos)):
                reingreso.identificacion = self.objetos[contador][0]
                reingreso.nombre= self.objetos[contador][1]
                reingreso.correo= self.objetos[contador][2]
                reingreso.puesto= self.objetos[contador][3]
                reingreso.nombre_usuario= self.objetos[contador][4]
                reingreso.contraseña= self.objetos[contador][5]
                if(contador==0):

                      self.obj = reingreso.imprimir(reingreso)
                      os.remove("asistentes.pickle")
                      with open("asistentes.pickle", "ab") as f:
                                 pickle.dump(self.obj, f)
                      contador = contador + 1
                else:

                    self.obj = reingreso.imprimir(reingreso)
                    with open("asistentes.pickle", "ab") as f:
                        pickle.dump(self.obj, f)
                    contador =  contador + 1


    # Esta busca y modifica los datos del administrador que se desea modificar
    def modificar(self, identificacion, nombre, correo, puesto, nombre_usuario, contraseña):

        carlos = asistente
        carlos.cargar_archivo(carlos)
        contador = 0

        while (contador < len(self.objetos)):
            if (self.objetos[contador][0] == identificacion):
                self.objetos.remove(self.objetos[contador])
                self.objetos.insert(contador, (identificacion, nombre, correo, puesto, nombre_usuario, contraseña))

                break
            else:
                contador = contador + 1;
        #print(self.objetos)
        carlos.reescribir_archivo(carlos)
    
    # Esta funcion verifica el objeto cedula si es valido o invalido 
    def verificar_cedula(self, cedula =str()):
            carlos= asistente
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
            carlos= asistente
            carlos.cargar_archivo(carlos)
            contador=0
            ingreso= False

            while(contador < len(self.objetos)):
                if((self.objetos[contador][4]== usuario) and (self.objetos[contador][5]== contraseña)):
                                    ingreso= True
                                    break
                else:
                     contador = contador + 1;

            if(ingreso):
                 return self.objetos[contador]
            else:
                 return []


