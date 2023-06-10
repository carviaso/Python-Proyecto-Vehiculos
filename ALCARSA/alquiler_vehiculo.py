import pickle
import os
from vehiculo import vehiculo
from cliente import cliente
import datetime

class alquiler_vehiculo:
    #cliente_alquila= cliente
    #vehiculo_alquilado= vehiculo
    def __init__(self, factura, cliente_alquila, vehiculo_alquilado, fecha_salida,fecha_de_regreso,valor_por_dia,n_card_credit,vencimiento, estado, monto_factura):
        self.factura= factura
        self.cliente_alquila= cliente_alquila
        self.vehiculo_alquilado= vehiculo_alquilado
        self.fecha_salida= fecha_salida
        self.fecha_de_regreso= fecha_de_regreso
        self.valor_por_dia= valor_por_dia
        self.n_card_credit= n_card_credit
        self.vencimiento= vencimiento
        self.estado= estado #Preparado, Activo, Devuelto
        self.monto_factura= monto_factura
    # Esta funcion retorna los objetos de la clase alquiler vehiculo
    def imprimir(self):
        return self.factura,  self.cliente_alquila, self.vehiculo_alquilado, self.fecha_salida, self.fecha_de_regreso, self.valor_por_dia, self.n_card_credit, self.vencimiento, self.estado, self.monto_factura

    #Esta funcion permite guardar el archivo en .pickle
    def guardar_archivo(self):
        self.obj = self.imprimir(self)

        with open("alquiler_vehiculo.pickle", "ab") as f:
            pickle.dump(self.obj, f)

    # Esta funcion permite cargar la lista del archivo .pickle
    def cargar_archivo(self):

        self.lista_vehiculos_alquilados= []
        self.objetos = []
        Contador=int(0)
        carga = True
        try:
            (open("alquiler_vehiculo.pickle", "rb"))

        except:
            carga = False

        if (carga):
            with (open("alquiler_vehiculo.pickle", "rb")) as openfile:
                while True:
                    try:
                        self.objetos.append(pickle.load(openfile))
                    except EOFError:
                        break
        self.lista_vehiculos_alquilados= self.objetos

        return self.lista_vehiculos_alquilados

    # Esta fucnion permitemodificar los objetos de la lista alquier vehiculo
    def modificar(self, factura, cliente_alquila, vehiculo_alquilado, fecha_salida,fecha_de_regreso,valor_por_dia,n_card_credit,vencimiento, estado, monto_factura):

        Carga = alquiler_vehiculo
        Carga.cargar_archivo(Carga)
        contador = 0
        while (contador < len(self.lista_vehiculos_alquilados)):
            if (self.lista_vehiculos_alquilados[contador][0] == factura):
                self.lista_vehiculos_alquilados.remove(self.lista_vehiculos_alquilados[contador])
                self.lista_vehiculos_alquilados.insert(contador,(factura, cliente_alquila, vehiculo_alquilado, fecha_salida,fecha_de_regreso,valor_por_dia,n_card_credit,vencimiento, estado, monto_factura) )
                break

            else:
                contador = contador + 1
        # print(self.objetos)
        Carga.reescribir_archivo(Carga)

    # Esta funcion permite reescribir el archivo .pickle
    def reescribir_archivo(self):
        reingreso = alquiler_vehiculo
        contador = 0

        while (contador < len(self.lista_vehiculos_alquilados)):
            reingreso.factura = self.lista_vehiculos_alquilados[contador][0]
            reingreso.cliente_alquila = self.lista_vehiculos_alquilados[contador][1]
            reingreso.vehiculo_alquilado = self.lista_vehiculos_alquilados[contador][2]
            reingreso.fecha_salida = self.lista_vehiculos_alquilados[contador][3]
            reingreso.fecha_de_regreso = self.lista_vehiculos_alquilados[contador][4]
            reingreso.valor_por_dia = self.lista_vehiculos_alquilados[contador][5]
            reingreso.n_card_credit= self.lista_vehiculos_alquilados[contador][6]
            reingreso.vencimiento= self.lista_vehiculos_alquilados[contador][7]
            reingreso.estado=self.lista_vehiculos_alquilados[contador][8]
            reingreso.monto_factura= self.lista_vehiculos_alquilados[contador][9]
            if (contador == 0):

                self.objeto = reingreso.imprimir(reingreso)
                os.remove("alquiler_vehiculo.pickle")
                with open("alquiler_vehiculo.pickle", "ab")as f:
                    pickle.dump(self.objeto, f)
                contador = contador + 1
            else:
                self.objeto = reingreso.imprimir(reingreso)
                with  open("alquiler_vehiculo.pickle", "ab")as f:
                    pickle.dump(self.objeto, f)
                contador = contador + 1




