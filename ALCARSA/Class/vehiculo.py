import pickle
import os

class vehiculo():

    # Esta funcion es para incializar la clase de tipo vehiculo
    def __init__(self,placa,modelo,marca,color,cantidad_pasajeros, valor_alquiler,en_uso):
        self.placa=placa
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self.cantidad_pasajeros=cantidad_pasajeros
        self.valor_alquiler= valor_alquiler
        self.en_uso=en_uso #SI / NO

    # Esta funcion recibe un objeto de tipo vehiculo y devuelve los valores guardados del objeto
    def imprimir(self):
        return self.placa,self.modelo,self.marca,self.color,self.cantidad_pasajeros, self.valor_alquiler,self.en_uso

    # Esta funcion recibe un objeto de tipo vehiculo y lo guarda en archivo
    def guardar_archivo(self):
        self.objeto = self.imprimir(self)
        with open ("vehiculo.pickle","ab") as f:
            pickle.dump(self.objeto,f)

    #esta funcion carga el archivo
    def cargar_archivo(self):
        self.lista_vehiculo=[]
        self.objeto = []
        contador = int(0)
        carga = True
        try:
            (open("vehiculo.pickle","rb"))
        except:
            carga=False

        if (carga):
            with (open("vehiculo.pickle","rb")) as openfile:
                while True:
                    try:
                        self.objeto.append(pickle.load(openfile))
                    except EOFError:
                        break
        self.lista_vehiculo=self.objeto

        return  self.lista_vehiculo

    # Esta funcion permite modificar los objetos de la clase vehiculo
    def modificar(self,placa,modelo,marca,color,cantidad_de_pasajeros,valor_alquiler,en_uso):

        Carros = vehiculo
        Carros.cargar_archivo(Carros)
        contador = 0
        while (contador < len(self.lista_vehiculo) ):
            if (self.lista_vehiculo[contador][0]==placa):
                self.lista_vehiculo.remove(self.lista_vehiculo[contador])
                self.lista_vehiculo.insert(contador,(placa,modelo,marca,color,cantidad_de_pasajeros,valor_alquiler,en_uso))
                break

            else:
                 contador = contador + 1
        #print(self.objetos)
        Carros.reescribir_archivo(Carros)

    # ESta funcion permite reeescribir los archivos de la lista de vehiculo
    def reescribir_archivo(self):
             reingreso = vehiculo
             contador = 0

             while (contador < len(self.lista_vehiculo)):
                 reingreso.placa=self.lista_vehiculo[contador][0]
                 reingreso.modelo=self.lista_vehiculo[contador][1]
                 reingreso.marca=self.lista_vehiculo[contador][2]
                 reingreso.color=self.lista_vehiculo[contador][3]
                 reingreso.cantidad_pasajeros=self.lista_vehiculo[contador][4]
                 reingreso.valor_alquiler= self.lista_vehiculo[contador][5]
                 reingreso.en_uso=self.lista_vehiculo[contador][6]
                 if(contador == 0):

                     self.objeto = reingreso.imprimir(reingreso)
                     os.remove("vehiculo.pickle")
                     with open("vehiculo.pickle","ab")as f:
                         pickle.dump(self.objeto,f)
                     contador = contador + 1
                 else:
                     self.objeto=reingreso.imprimir(reingreso)
                     with  open("vehiculo.pickle","ab")as f:
                         pickle.dump(self.objeto,f)
                     contador =contador + 1
    
    # Esta funcion verifica el string del obejto placa de la clase vehiculo con el archivo carros
    def verificar_placa(self, placa=str()):
        Carros = vehiculo
        Carros.cargar_archivo(Carros)
        contador = 0
        ingreso = True

        while (contador < len(self.lista_vehiculo)):
              if ((self.lista_vehiculo[contador][0] == placa)):
                      ingreso = False
                      break
              else:
                     contador = contador + 1

        return ingreso
    
    # Esta funcion busca la placa en la lista vehiculo  
    def busca_vehiculo(self, placa):
        Carros = vehiculo
        Carros.cargar_archivo(Carros)
        contador = 0
        while (contador < len(self.lista_vehiculo)):
            if (self.lista_vehiculo[contador][0] == placa):
                if(self.lista_vehiculo[contador][6])!= "SI":
                       return self.lista_vehiculo[contador]
                       break
                else:
                    return []

            else:
                contador = contador + 1
    
    # Devuelve la lista de vehiculos .pickle
    def devuelve_lista(self):
        self.objetos = []

        carga = True
        try:
            (open("vehiculo.pickle", "rb"))

        except:
            carga = False

        if (carga):
            with (open("vehiculo.pickle", "rb")) as openfile:
                while True:
                    try:
                        self.objetos.append(pickle.load(openfile))
                    except EOFError:
                        break
        return self.objetos
     
    # Esta funcion de vehiculo alquilado busca la placa en la lista auxiliar
    def vehiculo_alquilado(self, placa):
           lista_auxiliar= []
           lista_auxiliar= self.busca_vehiculo(self, placa)
           if(lista_auxiliar != []):
                  self.modificar(self,lista_auxiliar[0], lista_auxiliar[1], lista_auxiliar[2], lista_auxiliar[3],lista_auxiliar[4],lista_auxiliar[5], "SI")
                  lista_auxiliar=(lista_auxiliar[0],lista_auxiliar[1],lista_auxiliar[2],lista_auxiliar[3],lista_auxiliar[4],lista_auxiliar[5],"SI")
                  return lista_auxiliar
           else:
                  return lista_auxiliar








