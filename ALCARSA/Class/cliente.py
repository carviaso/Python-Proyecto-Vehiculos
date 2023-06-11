import pickle
import os

# Esta es la clase cliente pretente crear , modificar ,cargar ,guardar y imprimir los arhivos.
class cliente:

    def __init__(self,identificacion,nombre,profession, puesto,direccion_de_casa,lugar_de_trabajo,usuario,contraseña):
        self.identificacion= identificacion
        self.nombre= nombre
        self.profesion= profesion
        self.puesto = puesto
        self.direccion_de_casa = direccion_de_casa
        self.lugar_de_trabajo= lugar_de_trabajo
        self.usuario=usuario
        self.contraseña=contraseña

     # Esta funcion retorna el objeto para guardarlo de tipo lista
    def imprimir(self):
        return self.identificacion, self.nombre, self.profesion,self.puesto, self.direccion_de_casa, self.lugar_de_trabajo, self.usuario, self.contraseña

     # Esta funcion guarda los datos en archivo .pickle
    def guardar_archivo(self):
        #print(self.imprimir(self))
        self.obj = self.imprimir(self)

        with open("cliente.pickle", "ab") as f:
            pickle.dump(self.obj, f)

    # Esta funcion permite cargar el archivo cliente.pickle
    def cargar_archivo(self):

        self.lista_clientes= []
        self.objetos = []
        Contador=int(0)
        carga = True
        try:
            (open("cliente.pickle", "rb"))

        except:
            carga = False

        if (carga):
            with (open("cliente.pickle", "rb")) as openfile:
                while True:
                    try:
                        self.objetos.append(pickle.load(openfile))
                    except EOFError:
                        break
        self.lista_clientes= self.objetos

        return self.lista_clientes

     # Esta funcion permite modificar los datos de la clase cliente
    def modificar(self, identificacion, nombre, profesion,puesto,direccion_de_casa, lugar_de_trabajo, nombre_usuario, contraseña):

        carlos = cliente
        carlos.cargar_archivo(carlos)
        contador = 0

        while (contador < len(self.lista_clientes)):
            if (self.lista_clientes[contador][0] == identificacion):
                self.lista_clientes.remove(self.lista_clientes[contador])

                self.lista_clientes.insert(contador, (identificacion, nombre, profesion,puesto,direccion_de_casa, lugar_de_trabajo, nombre_usuario, contraseña))

                break
            else:
                contador = contador + 1;
        #print(self.objetos)
        carlos.reescribir_archivo(carlos)

    # ESta funcion permite reescribir un archivo existente por otro
    def reescribir_archivo(self):
            reingreso = cliente
            contador = 0

            while (contador < len(self.lista_clientes)):
                reingreso.identificacion = self.lista_clientes[contador][0]
                reingreso.nombre = self.lista_clientes[contador][1]
                reingreso.profesion = self.lista_clientes[contador][2]
                reingreso.puesto = self.lista_clientes[contador][3]
                reingreso.direccion_de_casa = self.lista_clientes[contador][4]
                reingreso.lugar_de_trabajo = self.lista_clientes[contador][5]
                reingreso.usuario = self.lista_clientes[contador][6]
                reingreso.contraseña = self.lista_clientes[contador][7]
                if (contador == 0):
                    
                    self.obj = (reingreso.imprimir(reingreso))
                    os.remove("cliente.pickle")
                    with open("cliente.pickle", "ab") as f:
                        pickle.dump(self.obj, f)
                    contador = contador + 1
                else:

                    self.obj = reingreso.imprimir(reingreso)
                    with open("cliente.pickle", "ab") as f:
                        pickle.dump(self.obj, f)
                    contador = contador + 1

    # Esta funcion permite buscar el cliente por medio del objeto indentificacion
    def buscar_cliente(self, identificacion):
        self.cargar_archivo(self)
        contador=0

        while (contador < len(self.lista_clientes)):
               if((self.lista_clientes[contador][0])== identificacion):
                    variable_carga= cliente
                    variable_carga= self.lista_clientes[contador]
                    return variable_carga
                    break
               else:
                    contador= contador + 1

    # Esa funcion permite devolver la lista cliente
    def devuelve_lista(self):
        self.objetos = []

        carga = True
        try:
            (open("cliente.pickle", "rb"))

        except:
            carga = False

        if (carga):
            with (open("cliente.pickle", "rb")) as openfile:
                while True:
                    try:
                        self.objetos.append(pickle.load(openfile))
                    except EOFError:
                        break
        return self.objetos

    # Esta funcion permite verificar si el objeto identificacion es correcto
    def verificar_cedula(self, identificacion):
         Cliente = cliente
         Cliente.cargar_archivo(Cliente)
         contador = 0
         ingreso = True

         while (contador < len(self.objetos)):
           if ((self.objetos[contador][0] == identificacion)):
                   ingreso = False
                   break
           else:
                contador = contador + 1

         if (ingreso):
             return ingreso

         else:
             return ingreso


    # Esta funcion permite virificar el acceso al sistema mediante los objetos usuario y contraseña
    def verificar_acceso(self, usuario=str(), contraseña=str()):
        carlos = cliente
        carlos.cargar_archivo(carlos)
        contador = 0
        ingreso = False

        while (contador < len(self.objetos)):
            if ((self.objetos[contador][6] == usuario) and (self.objetos[contador][7] == contraseña)):
                ingreso = True
                break
            else:
                contador = contador + 1;

        if (ingreso):
            return self.objetos[contador]
        else:
            return []


"""carlos=cliente
#brandon.guardar_archivo(brandon)
carlos.identificacion = 208150532
carlos.nombre = "qwqwqwwqwqqwqwqw"
carlos.profesion = "Ing electronica"
carlos.direccion_de_casa = "100m al norte"
carlos.lugar_de_trabajo = "Oficinna"
carlos.usuario="goldenexperience"
carlos.contraseña="xxxxxx"""
#print(brandon.lugar_de_trabajo,brandon.nombre)
#carlos.guardar_archivo(carlos)
#carlos.modificar(carlos, 208150532, "BRANDON", "ING ELECTRONICA", "100", "ESTUDIANTE", "asdasd","dssdss")
#carlos.cargar_archivo(carlos)
#carlos.buscar_cliente(carlos, 208150532)
#carlos.verificar_acceso(carlos,"goldenexperience", "xxxxxxx")