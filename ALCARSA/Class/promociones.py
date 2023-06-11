import pickle
import os


class promociones:
    # Esta funcion es para incializar la clase de tipo promociones
    def __init__(self, fecha_inicio,fecha_final,marca, xdia):

        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.marca = marca
        self.xdia = xdia

    def imprimir(self):
        return self.fecha_inicio, self.fecha_final, self.marca,self.xdia

    def guardar_archivo(self):
        self.obj = self.imprimir(self)

        with open("promociones.pickle", "ab") as f:
            pickle.dump(self.obj, f)

    def cargar_archivo(self):

        self.lista_promociones= []
        self.objetos = []
        Contador=int(0)
        carga = True
        try:
            (open("promociones.pickle", "rb"))

        except:
            carga = False

        if (carga):
            with (open("promociones.pickle", "rb")) as openfile:
                while True:
                    try:
                        self.objetos.append(pickle.load(openfile))
                    except EOFError:
                        break
        self.lista_promociones= self.objetos
        return self.lista_promociones

