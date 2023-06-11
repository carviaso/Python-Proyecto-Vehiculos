import tkinter as tk
import calendar
import datetime
import sys
from tkinter import messagebox
from tkinter import *
#from tkinter import  scrolledtext
from tkinter import ttk
import os



#LLamado a las diferentes clases del programa
from administrador import administrador
from asistente import asistente
from cliente import cliente
from vehiculo import vehiculo
from promociones import promociones
from  alquiler_vehiculo import alquiler_vehiculo
from bitacora import bitacora






# Esta clase es para el diseño de la ventana que recibe los datos de entrada
# esto son el usuario y la contraseña con la cual el usuario ingresara al sistema
class Ventana_principal:

    #palabra= StringVar()
    # inicializador de la ventana principal aqui se definen todos lso parametros de la ventana
    # asi como las areas de texto y botones necesarios para el ingreso del sistema
    def __init__(self):

        self.vent_p = Tk()
        self.vent_p.geometry("400x200")
        self.vent_p.wm_title("ALCARSA")
        self.vent_p.configure(background='steelblue')
        self.vent_p.resizable(0,0)
        #self.vent_p.geometry("%dx%d+%d+%d" % (size + (x, y)))
        Ventana_principal.center(self.vent_p)
        usuario1= StringVar()

        Label(self.vent_p, text="MENU DE INGRESO A SU SISTEMA ALCARSA", bg="white", anchor= "center", width= 30).place_configure(x= 10, y= 10, width= 380, height= 20)
        Label(self.vent_p, text="Usuario:", bg= "white").place_configure(x= 10, y= 50, width= 90, height= 20)

        #Variable para guardar el nombre del usuario que va ha ingresar, y creacion del area de texto donde se va ingresar
        self.usuario= StringVar()
        self.usua_i=Entry(self.vent_p, bd=3, textvariable= self.usuario, bg="white")
        self.usua_i.place_configure(x= 110, y=50, width= 280, height=20)

        Label(self.vent_p, text="Contraseña:", bg="white").place_configure(x=10, y=100, width=90, height=20)

        #Area donde se recibe la contraseña
        self.contraseña= StringVar()
        self.cotra_i=Entry(self.vent_p, bd= 3,textvariable= self.contraseña, show= "*", bg="white")
        self.cotra_i.place_configure(x=110, y=100, width=280, height=20)

        botton1= Button(self.vent_p, text="Entrar", bg= "white", command= self.new_window).place_configure(x=75, y= 150, width= 100, height= 20)
        botton1

        botton2 = Button(self.vent_p, text="Salir", bg="white", command=self.cerrar).place_configure(x=225, y=150, width=100, height=20)
        botton2
        # ventana de mensaje para consultar si desea salir del sistema
        def on_closing():
            if messagebox.askokcancel("Salir", "Desea salir?"):
                self.vent_p.destroy()
                sys.exit()


        self.vent_p.protocol("WM_DELETE_WINDOW", on_closing)


        self.vent_p.mainloop()




    # ventana principal donde se agrega una barra de menu con todas las tareas que el usuario
    # puede realizar segun el tipo de usuario que ingreso (asistente,administrador,asistente,cliente)
    def ventana_admin(self):

        self.ventana_administracion= Toplevel()
        self.ventana_administracion.geometry("700x500")
        self.ventana_administracion.resizable(0,0)
        self.ventana_administracion.title("ADMINISTRACION")
        self.ventana_administracion.transient(master= self.vent_p)
        self.ventana_administracion.geometry("%dx%d+%d+%d" % ((600,300) + (483.0, 284.0)))
        self.ventana_administracion.configure(background='steelblue')
        self.image = tk.PhotoImage(file="guardar.gif")
        self.imagen = tk.PhotoImage(file="salir.gif")

        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario +": ", )
        self.nombre.insert(24, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=280, width=700, height=20)

        self.barramenu = Menu(self.ventana_administracion)
        self.ventana_administracion.config(menu=self.barramenu)
        self.opciones3 = tk.Menu(self.barramenu)
        self.opciones4 = tk.Menu(self.barramenu)
        self.opciones5 = tk.Menu(self.barramenu)
        self.opciones6 = tk.Menu(self.barramenu)
        self.opciones6.add_command(label="Preparar alquiler", command=self.agregar_alquiler)
        if(self.tipo_usuario== "ADMINISTRADOR"):
            self.opciones1 = tk.Menu(self.barramenu)
            self.opciones1.add_command(label="Ingresar nuevo administrador", command=self.agregar_admin)
            self.opciones1.add_command(label="Modificar administrador", command=self.modifica_admin)
            self.opciones1.add_command(label="Mostrar lista de administradores", command=self.muestra_lista_admin)
            self.opciones1.add_command(label="Reportes de ingresos de usuarios", command=self.muestra_ingreso_usuarios)
            self.barramenu.add_cascade(label="ADMINISTRADORES", menu=self.opciones1)

        if(self.tipo_usuario== "ASISTENTE") or (self.tipo_usuario=="ADMINISTRADOR"):
            self.opciones2 = tk.Menu(self.barramenu)
            self.opciones2.add_command(label="Ingresar nuevo asistente", command=self.agregar_asis)
            self.opciones2.add_command(label="Modificar Asistente", command=self.modifica_asis)
            self.opciones2.add_command(label="Mostrar lista de asistentes", command= self.muestra_lista_asis)
            self.barramenu.add_cascade(label="ASISTENTES", menu=self.opciones2)
            self.opciones3 = tk.Menu(self.barramenu)
            self.opciones3.add_command(label="Ingresar nuevo cliente", command=self.agregar_cliente)
            self.opciones3.add_command(label="Modificar cliente", command=self.modifica_cliente)
            self.opciones3.add_command(label="Mostrar lista de clientes", command=self.muestra_lista_cliente)
            self.barramenu.add_cascade(label="CLIENTES", menu=self.opciones3)
            self.opciones4.add_command(label="Ingresar nuevo Vehiculo", command=self.agregar_vehiculo)
            self.opciones4.add_command(label="Modificar Vehiculo", command=self.modifica_vehiculo)
            self.opciones5.add_command(label="Ingresar nueva promocion", command=self.agregar_promociones)
            self.opciones6.add_command(label="Activar alquiler", command=self.aplicar_alquiler)
            self.opciones6.add_command(label="Desactivar alquiler", command=self.desactivar_alquiler)

        self.opciones4.add_command(label="Mostrar lista de Vehiculos disponibles", command=self.muestra_lista_vehiculo)
        self.opciones4.add_command(label="Mostrar lista de Vehiculos en uso", command=self.muestra_lista_vehiculo_1)
        self.opciones4.add_command(label="Mostrar lista de Vehiculos completa", command=self.muestra_lista_vehiculo_2)
        self.barramenu.add_cascade(label="VEHICULOS", menu=self.opciones4)



        self.opciones5.add_command(label="Ver promociones existentes", command=self.ver_promociones)
        self.barramenu.add_cascade(label="PROMOCIONES", menu=self.opciones5)



        self.opciones6.add_command(label="Mostrar alquileres por cliente", command=self.mostrar_alquiler)
        self.barramenu.add_cascade(label="ALQUILER VEHICULO", menu=self.opciones6)
        #self.barramenu.add_cascade(label="CLIENTES", menu= self.opciones3)


        self.ventana_administracion.grab_set()
        self.vent_p.wait_window(self.ventana_administracion)

    # esta funcion es para crear la ventana administrador en el modo insertar administrador nuevo es
    # llamada desde la barra de menu pincipal
    def agregar_admin(self):
        self.ventana_administracion.geometry("400x300")
        self.ventana_administracion.configure(background= 'steelblue')
        self.barramenu.entryconfig(index= 1,state= 'disabled')
        self.barramenu.entryconfig(index=2, state= 'disabled')
        self.barramenu.entryconfig(index=3, state= 'disabled')
        self.barramenu.entryconfig(index=4, state= 'disabled')
        self.barramenu.entryconfig(index=5, state= 'disabled')
        self.barramenu.entryconfig(index=6, state= 'disabled')

        Label0 = Label(self.ventana_administracion, text="Ingresar todos los datos solicitados para\n agregar al nuevo administrador",bg="white").place_configure(x=10, y=10, width=260, height=50)
        Label1=Label(self.ventana_administracion, text="Inserte numero de identificación:", bg="white").place_configure(x=10, y=70, width=180, height=20)
        Label2=Label(self.ventana_administracion, text="Inserte nombre completo: ", bg="white").place_configure(x=10, y=110, width=180, height=20)
        Label3 = Label(self.ventana_administracion, text="Inserte nombre usuario: ", bg="white").place_configure(x=10, y=150,width=180, height=20)
        Label4 = Label(self.ventana_administracion, text="Inserte la contraseña:", bg="white").place_configure(x=10,y=190,width=180,height=20)
        Label5 = Label(self.ventana_administracion, text="Confirmacion de la contraseña:", bg="white").place_configure(x=10,y=230,width=180,height=20)
        #self.barramenu.entryconfig(index=1, state= 'normal')

        self.Numero_id= StringVar()
        self.id_numero=Entry(self.ventana_administracion,bd=3, textvariable=self.Numero_id, bg="white")
        self.id_numero.place_configure(x=200, y=70, width=190, height=20)

        self.Nombre= StringVar()
        self.nombre=Entry(self.ventana_administracion, bd=3, textvariable=self.Nombre, bg="white")
        self.nombre.place_configure(x=200, y=110, width=190, height=20)

        self.Usuario= StringVar()
        self.usu=Entry(self.ventana_administracion, bd=3, textvariable=self.Usuario, bg="white")
        self.usu.place_configure(x=200, y=150, width=190, height=20)

        self.Contraseña= StringVar()
        self.cont1=Entry(self.ventana_administracion, bd=3, textvariable=self.Contraseña, show="*", bg="white")
        self.cont1.place_configure(x=200, y=190, width=190, height=20)

        self.Contraseña2 = StringVar()
        self.cotra2=Entry(self.ventana_administracion, bd=3, textvariable=self.Contraseña2, show="*", bg="white")
        self.cotra2.place_configure(x=200, y=230,width=190, height=20)

        self.image= tk.PhotoImage(file="guardar.gif")
        #self.image.zoom(45,45)
        botton1 = Button(self.ventana_administracion, text="Guardar", image= self.image, command=self.guardar).place_configure(x=280, y=10, width=50, height=50)


        botton1
        self.imagen = tk.PhotoImage(file="salir.gif")
        botton2 = Button(self.ventana_administracion, text="Salir",image=self.imagen, command=self.salir).place_configure(x=340, y=10, width=50, height=50)
        botton2

    #Esta funcion se llama desde modificar administrador se ejecuta para modificar el administrador
    # se busca mediante su numero de cedula y se rellenan los campos que se desean modificar
    def modifica_admin(self):
        self.ventana_administracion.geometry("400x300")
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')

        Label0 = Label(self.ventana_administracion,text="Seleccione la cedula del administrador\n a modificar, luego rellenar los datos\nsolicitados y dar click sobre el check ", bg="white").place_configure(x=10, y=10, width=210, height=50)

        Label(self.ventana_administracion, text="Seleccione el administrador :", justify= "left", bg="white").place_configure(x=10, y=70, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte nombre completo: ", justify= "left", bg="white").place_configure(x=10, y=110,width=180,height=20)
        Label(self.ventana_administracion, text="Inserte nombre usuario: ", justify="left", bg="white").place_configure(x=10, y=150, width=180,height=20)
        Label(self.ventana_administracion, text="Inserte la contraseña:", justify="left", bg="white").place_configure(x=10,y=190, width=180, height=20)
        Label(self.ventana_administracion, text="Confirmacion de la contraseña:", justify="left", bg="white").place_configure(x=10, y=230, width=180, height=20)
        # self.barramenu.entryconfig(index=1, state= 'normal')

        #self.Numero_id = StringVar()
        #self.id_numero = Entry(self.ventana_administracion, textvariable=self.Numero_id, bg="green")
        #self.id_numero.place_configure(x=200, y=60, width=190, height=20)
        self.Combo= ttk.Combobox(self.ventana_administracion,state='readonly')
        self.Combo.place_configure(x=200, y=70, width=190, height=20)

        #listadmin.place_configure(x=200, y= 60, width=190, height=20)

        self.Nombre = StringVar()
        self.nombre = Entry(self.ventana_administracion, bd=3, textvariable=self.Nombre, bg="white")
        self.nombre.place_configure(x=200, y=110, width=190, height=20)

        self.Usuario = StringVar()
        self.usu = Entry(self.ventana_administracion, bd=3, textvariable=self.Usuario, bg="white")
        self.usu.place_configure(x=200, y=150, width=190, height=20)

        self.Contraseña = StringVar()
        self.cont1 = Entry(self.ventana_administracion, bd=3, textvariable=self.Contraseña, show="*", bg="white")
        self.cont1.place_configure(x=200, y=190, width=190, height=20)

        self.Contraseña2 = StringVar()
        self.cotra2 = Entry(self.ventana_administracion, bd=3, textvariable=self.Contraseña2, show="*", bg="white")
        self.cotra2.place_configure(x=200, y=230, width=190, height=20)

        #self.botton1 = Button(self.ventana_administracion, text="Buscar", bg="green", command=self.buscar)
        #self.botton1.place_configure(x=225, y=0, width=50, height=50)

        #self.image = tk.PhotoImage(file="guardar.gif")
        self.botton11 = Button(self.ventana_administracion, text="Guardar", image= self.image, command=self.llama_modificar_admin)
        self.botton11.place_configure(x=285, y=10, width=50, height=50)

        #self.imagen = tk.PhotoImage(file="salir.gif")
        botton2 = Button(self.ventana_administracion, text="Salir", image= self.imagen, command=self.salir)
        botton2.place_configure(x=340, y=10, width=50, height=50)
        cargar_archivo = administrador
        self.lista = []
        self.lista = cargar_archivo.devuelve_lista(cargar_archivo)
        self.lista2 = []
        contador = 0

        while (contador < len(self.lista)):
            self.lista2.append(self.lista[contador][0])
            contador = contador + 1

        self.seleccion = str()
        self.Combo['values'] = self.lista2
        #self.seleccion = self.Combo.get()
        #print(self.seleccion)
        self.Combo.bind("<<ComboboxSelected>>", self.buscar)



    # Esta funcion sirve para mostrar la lista de administradores registrados
    def muestra_lista_admin(self):

        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')

        self.ventana_administracion.geometry("300x400")
        Label(self.ventana_administracion, text="Lista de administradores registrados", justify="center", width=10, height=3,
              bg="steelblue").grid(row=0, column=0, columnspan=2, ipadx=190)
        self.imagen = tk.PhotoImage(file="salir.gif")
        #botton2 = Button(self.ventana_administracion, text="Salir", image= self.imagen, command=self.salir)
        botton2 = Button(self.ventana_administracion, text="Salir", image= self.imagen, justify="left", width= 10,height=60,
                         command=self.salir).grid(row=0, column=2, ipadx=30)
        botton2

        # dezpla= tk.Canvas(self.ventana_administracion, bg="blue", height=380, width= 600)
        # dezpla.pack()

        Administrador = administrador
        lista_administrador = Administrador.devuelve_lista(Administrador)
        height = len(lista_administrador)
        width = 3
        b = Entry(self.ventana_administracion, width=40, text="")
        b.insert(0, "Identificacion del administrador")
        b.grid(row=2, column=0)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=40, text="")
        b.insert(0, "Nombre del administrador")
        b.grid(row=2, column=1)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=40, text="")
        b.insert(0, "Usuario del administrador")
        b.grid(row=2, column=2)
        b.config(state='readonly')


        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = Entry(self.ventana_administracion, width=40, text="")

                if (j >= 2):
                    b.insert(0, lista_administrador[i][(j + 1)])
                else:
                    b.insert(0, lista_administrador[i][j])
                b.grid(row=(i + 3), column=j)
                b.config(state='readonly')

        self.ventana_administracion.geometry("650" + "x" + str(((len(lista_administrador) + 2) * 20) + 60))
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0,self.tipo_usuario + ": ", )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=(((len(lista_administrador) + 2) * 20) + 40), width=650, height=20)

    # Esta funcion sirve para mostar la lista de asistentes registrados en la clase asistente
    def muestra_ingreso_usuarios(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x600")
        Label(self.ventana_administracion, text="Lista de asistentes registrados", justify="center", width=22, height=4,
              bg="steelblue").grid(row=0, column=0, columnspan=3, ipadx=140)
        #self.imagen = tk.PhotoImage(file="salir.gif")
        botton2 = Button(self.ventana_administracion, text="Salir",bg="white", image= self.imagen, justify="left", height=60,
                         command=self.salir).grid(row=0, column=3, columnspan=5, ipadx=10)
        botton2

        # dezpla= tk.Canvas(self.ventana_administracion, bg="blue", height=380, width= 600)
        # dezpla.pack()

        Bitacora = bitacora
        lista_bitacora = Bitacora.cargar_archivo(Bitacora)
        height = len(lista_bitacora)
        width = 4
        b = Entry(self.ventana_administracion, width=26, text="")
        b.insert(0, "Numero de identificacion")
        b.grid(row=2, column=0)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=26, text="")
        b.insert(0, "Nombre de la persona")
        b.grid(row=2, column=1)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=26, text="")
        b.insert(0, "Tipo de usuario")
        b.grid(row=2, column=2)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=26, text="")
        b.insert(0, "Nombre del usuario")
        b.grid(row=2, column=3)
        b.config(state='readonly')

        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = Entry(self.ventana_administracion, width=26, text="")
                b.insert(0, lista_bitacora[i][j])
                b.grid(row=(i + 3), column=j)
                b.config(state='readonly')

        self.ventana_administracion.geometry("600" + "x" + str(((len(lista_bitacora) + 2) * 20) + 70))
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario)
        self.nombre.insert(22, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=(((len(lista_bitacora) + 2) * 20) + 50), width=650, height=20)

    # Esta funcion permite ingresar un cliente mediante la clase cliente
    def agregar_cliente(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x400")

        Label0 = Label(self.ventana_administracion,
                       text="Ingresar todos los datos solicitados para\n agregar al nuevo cliente",
                       bg="white").place_configure(x=10, y=10, width=260, height=50)
        Label1 = Label(self.ventana_administracion, text="Inserte numero de identificación:",
                       bg="white").place_configure(x=10, y=70, width=180, height=20)
        Label2 = Label(self.ventana_administracion, text="Inserte nombre completo: ", bg="white").place_configure(x=10,
        y=110,width=180,height=20)
        Label6 = Label(self.ventana_administracion, text="Inserte la profesion: ", bg="white").place_configure(x=10, y=150,
        width=180,height=20)
        Label7 = Label(self.ventana_administracion, text="Inserte la dirreccion de casa: ", bg="white").place_configure(x=10,
        y=190,width=180,height=20)
        Label8 = Label(self.ventana_administracion, text="Lugar de trabajo: ", bg="white").place_configure(x=10,y=230,
        width=180,height=20)


        Label3 = Label(self.ventana_administracion, text="Inserte nombre usuario: ", bg="white").place_configure(x=10,
        y=270,width=180,height=20)
        Label4 = Label(self.ventana_administracion, text="Inserte la contraseña:", bg="white").place_configure(x=10,
        y=310,width=180,height=20)
        Label5 = Label(self.ventana_administracion, text="Confirmacion de la contraseña:", bg="white").place_configure(
        x=10,y=350, width=180, height=20)

        # self.barramenu.entryconfig(index=1, state= 'normal')
        self.nombre.config(state=tk.NORMAL)
        self.nombre.delete(0, END)
        self.nombre.insert(0, self.tipo_usuario)
        self.nombre.insert(22, ": ")
        self.nombre.insert(25, self.usuario.get())
        self.nombre.place_configure(x=0, y=380, width=400, height=20)
        self.nombre.config(state= tk.DISABLED)

        self.Numero_id = StringVar()
        self.id_numero = Entry(self.ventana_administracion, textvariable=self.Numero_id, bg="white")
        self.id_numero.place_configure(x=200, y=70, width=190, height=20)

        self.Nombre = StringVar()
        self.nombre = Entry(self.ventana_administracion, textvariable=self.Nombre, bg="white")
        self.nombre.place_configure(x=200, y=110, width=190, height=20)

        self.Profesion = StringVar()
        self.profesion = Entry(self.ventana_administracion, textvariable=self.Profesion, bg="white")
        self.profesion.place_configure(x=200, y=150, width=190, height=20)

        self.Casa = StringVar()
        self.casa = Entry(self.ventana_administracion, textvariable=self.Casa, bg="white")
        self.casa.place_configure(x=200, y=190, width=190, height=20)

        self.Trabajo = StringVar()
        self.trabajo = Entry(self.ventana_administracion, textvariable=self.Trabajo, bg="white")
        self.trabajo.place_configure(x=200, y=230, width=190, height=20)

        self.Usuario = StringVar()
        self.usu = Entry(self.ventana_administracion, textvariable=self.Usuario, bg="white")
        self.usu.place_configure(x=200, y=270, width=190, height=20)

        self.Contraseña = StringVar()
        self.cont1 = Entry(self.ventana_administracion, textvariable=self.Contraseña, show="*", bg="white")
        self.cont1.place_configure(x=200, y=310, width=190, height=20)

        self.Contraseña2 = StringVar()
        self.cotra2 = Entry(self.ventana_administracion, textvariable=self.Contraseña2, show="*", bg="white")
        self.cotra2.place_configure(x=200, y=350, width=190, height=20)

        #self.image = tk.PhotoImage(file="guardar.gif")
        botton1 = Button(self.ventana_administracion, text="Guardar", image= self.image,
                         command=self.guardar_cliente).place_configure(x=280, y=10, width=50, height=50)
        botton1
        #self.imagen = tk.PhotoImage(file="salir.gif")
        botton2 = Button(self.ventana_administracion, text="Salir", image= self.imagen, command=self.salir).place_configure(
            x=340, y=10, width=50, height=50)
        botton2


    # Esta funcion permite guardar un cliente en la clase cliente
    # ademas de verificar si el cliente es guardado es correcto o incorrecto
    def guardar_cliente(self):
        if (self.Contraseña.get() == self.Contraseña2.get()) and (self.Contraseña.get() != "") and (
                self.Nombre.get() != "") and (self.Profesion.get() != "") and (self.Casa.get() != "" ) and (self.Trabajo.get()!="") and  (self.Usuario.get() != "") and (
                self.Numero_id.get() != ""):

            cedula_correcta = True
            try:
                int(self.Numero_id.get())
            except:
                cedula_correcta = False

            if (cedula_correcta):
                Nuevo_cliente = cliente
                if (Nuevo_cliente.verificar_cedula(Nuevo_cliente, int(self.Numero_id.get()))):
                    Nuevo_cliente.identificacion = int(self.Numero_id.get())
                    Nuevo_cliente.nombre = self.Nombre.get()
                    Nuevo_cliente.profesion = self.Profesion.get()
                    Nuevo_cliente.puesto = "Cliente"
                    Nuevo_cliente.direccion_de_casa = self.Casa.get()
                    Nuevo_cliente.lugar_de_trabajo = self.Trabajo.get()
                    Nuevo_cliente.usuario = self.Usuario.get()
                    Nuevo_cliente.contraseña = self.Contraseña.get()

                    Nuevo_cliente.guardar_archivo(Nuevo_cliente)
                    Nuevo_cliente.cargar_archivo(Nuevo_cliente)
                    self.id_numero.delete(0, tk.END)
                    self.nombre.delete(0, tk.END)
                    self.profesion.delete(0, tk.END)
                    self.casa.delete(0,tk.END)
                    self.trabajo.delete(0,tk.END)
                    self.usu.delete(0, tk.END)
                    self.cont1.delete(0, tk.END)
                    self.cotra2.delete(0, tk.END)
                    messagebox.showinfo("Ingreso correcto", "El cliente se guardo correctamente")
                else:
                    messagebox.showinfo("Ingreso incorreco", "El cliente ya existe, con esa cedula")
            else:
                messagebox.showinfo("Ingreso inorrecto", "El numero identificacion no tiene validez")
            # print(Nuevo_administrador.identificacion, " ", Nuevo_administrador.nombre, Nuevo_administrador.puesto, " ", Nuevo_administrador.usuario," ", Nuevo_administrador.contraseña)
        else:
            if (self.Contraseña.get() == self.Contraseña2.get()) and (self.Contraseña.get() != ""):
                messagebox.showinfo("Error de ingreso", "Todos los datos deben de ser ingresados")
                self.id_numero.delete(0, tk.END)
                self.nombre.delete(0, tk.END)
                self.profesion.delete(0,tk.END)
                self.casa.delete(0, tk.END)
                self.trabajo.delete(0, tk.END)
                self.usu.delete(0, tk.END)
                self.cont1.delete(0, tk.END)
                self.cotra2.delete(0, tk.END)
            else:
                messagebox.showinfo("Error de ingreso", "Las contraseñas no coinciden")
                self.cont1.delete(0, tk.END)
                self.cotra2.delete(0, tk.END)

    # Esta clase permite modificar la clase cliente desde la la barra del menu
    # Despliega un ventana el cual puede modificar los datos
    def modifica_cliente(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x400")
        self.nombre.destroy()
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(23, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=380, width=400, height=20)

        Label0 = Label(self.ventana_administracion,
                       text="Seleccione la cedula del cliente\n a modificar, luego rellenar los datos\nsolicitados y dar click sobre el check ",
                       bg="white").place_configure(x=10, y=10, width=210, height=50)

        Label(self.ventana_administracion, text="Seleccione el cliente :", justify="left",bg="white").place_configure(x=10, y=70, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte nombre completo: ", justify="left",bg="white").place_configure(x=10, y=110, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte nombre de la profesion: ", justify="left", bg="white").place_configure( x=10, y=150, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte la direccion de la casa: ", justify="left",bg="white").place_configure( x=10, y=190, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte el lugar de trabajo: ", justify="left",bg="white").place_configure(x=10, y=230, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte el nombre del usuario: ", justify="left",bg="white").place_configure(x=10, y=270, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte la contraseña:", justify="left", bg="white").place_configure(x=10, y=310, width=180, height=20)
        Label(self.ventana_administracion, text="Confirmacion de la contraseña:", justify="left",
              bg="white").place_configure(x=10, y=350, width=180, height=20)
        # self.barramenu.entryconfig(index=1, state= 'normal')

        # self.Numero_id = StringVar()
        # self.id_numero = Entry(self.ventana_administracion, textvariable=self.Numero_id, bg="green")
        # self.id_numero.place_configure(x=200, y=60, width=190, height=20)
        self.Combo = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo.place_configure(x=200, y=70, width=190, height=20)

        cargar_archivo = cliente
        self.lista = []
        self.lista = cargar_archivo.devuelve_lista(cargar_archivo)
        self.lista2 = []
        contador = 0

        while (contador < len(self.lista)):
            self.lista2.append(self.lista[contador][0])
            contador = contador + 1

        self.seleccion = str()
        self.Combo['values'] = self.lista2
        self.Combo.bind("<<ComboboxSelected>>", self.buscar_cliente)
        #55sd5w

        self.seleccion = self.Combo.get()

        # listadmin.place_configure(x=200, y= 60, width=190, height=20)

        self.Nombre = StringVar()
        self.nombre = Entry(self.ventana_administracion,bd= 3, textvariable=self.Nombre, bg="white")
        self.nombre.place_configure(x=200, y=110, width=190, height=20)

        self.Profesion = StringVar()
        self.profesion = Entry(self.ventana_administracion, bd=3, textvariable=self.Profesion, bg="white")
        self.profesion.place_configure(x=200, y=150, width=190, height=20)

        self.Direccion_de_casa = StringVar()
        self.direccion_de_casa = Entry(self.ventana_administracion,bd=3, textvariable=self.Direccion_de_casa, bg="white")
        self.direccion_de_casa.place_configure(x=200, y=190, width=190, height=20)

        self.Lugar_de_trabajo = StringVar()
        self.lugar_de_trabajo = Entry(self.ventana_administracion,bd=3, textvariable=self.Lugar_de_trabajo, bg="white")
        self.lugar_de_trabajo.place_configure(x=200, y=230, width=190, height=20)

        self.Usuario_u = StringVar()
        self.usu = Entry(self.ventana_administracion,bd=3, textvariable=self.Usuario_u, bg="white")
        self.usu.place_configure(x=200, y=270, width=190, height=20)

        self.Contraseña = StringVar()
        self.cont1 = Entry(self.ventana_administracion,bd=3, textvariable=self.Contraseña, show="*", bg="white")
        self.cont1.place_configure(x=200, y=310, width=190, height=20)

        self.Contraseña2 = StringVar()
        self.cotra2 = Entry(self.ventana_administracion, bd=3, textvariable=self.Contraseña2, show="*", bg="white")
        self.cotra2.place_configure(x=200, y=350, width=190, height=20)

        #self.botton1 = Button(self.ventana_administracion, text="Buscar", bg="green", command=self.buscar_cliente)
        #self.botton1.place_configure(x=225, y=0, width=50, height=50)

        self.botton11 = Button(self.ventana_administracion, image=self.image, text="Guardar",command=self.llama_modificar_cliente)
        self.botton11.place_configure(x=285, y=10, width=50, height=50)

        botton2 = Button(self.ventana_administracion, image= self.imagen, text="Salir", command=self.salir)
        botton2.place_configure(x=340, y=10, width=50, height=50)

        #self.ventana_administracion.geometry("650" + "x" + str(((len(lista_clientes) + 2) * 20) + 60))

    # esta funcion se encarga de buscar dentro de la clase cliente
    # comparando los datos de la clase cliente segun su principio de busqueda
    def buscar_cliente(self, event):
        self.nombre.delete(0,END)
        self.profesion.delete(0,END)
        self.direccion_de_casa.delete(0,END)
        self.lugar_de_trabajo.delete(0, END)
        self.usu.delete(0, END)
        self.cont1.delete(0, END)
        self.cotra2.delete(0,END)
        #self.botton1.destroy()
        self.seleccion= self.Combo.get()

        conta_aux=0
        if(self.seleccion != ""):
             while(conta_aux < len(self.lista)):
                 if(int(self.seleccion)== int(self.lista[conta_aux][0])):
                     self.nombre.insert(0, self.lista[conta_aux][1])
                     self.profesion.insert(0, self.lista[conta_aux][2])
                     self.direccion_de_casa.insert(0, self.lista[conta_aux][4])
                     self.lugar_de_trabajo.insert(0, self.lista[conta_aux][5])
                     self.usu.insert(0, self.lista[conta_aux][6])
                     self.cont1.insert(0, self.lista[conta_aux][7])
                     self.cotra2.insert(0, self.lista[conta_aux][7])
                     conta_aux= conta_aux + 1
                 else:
                     conta_aux=conta_aux + 1
        else:
            messagebox.showinfo("Error de identificacion", "No se ha selecionado ningun administrador")
    # esta funcion llama a modificar cliente dentro de la clase cliente
    # esta remueve el cliente anterior para modificarlo por el cliente nuevo
    def llama_modificar_cliente(self):
        if(self.Combo.get()!="")and(self.Nombre.get() != "") and (self.Profesion.get()!= "")and(self.Direccion_de_casa.get()!="") and(self.Lugar_de_trabajo.get()!="") and (self.Usuario_u.get()!= "") and (self.Contraseña.get()!="") and (self.Contraseña2.get()!=""):
            if(self.Contraseña.get() == self.Contraseña2.get()):
                Conexion_client= cliente
                Conexion_client.cargar_archivo(Conexion_client)
                print(self.Usuario_u.get())
                Conexion_client.modificar(Conexion_client, int(self.Combo.get()), self.Nombre.get(),self.Profesion.get(),"CLIENTE", self.Direccion_de_casa.get(), self.Lugar_de_trabajo.get(), self.Usuario_u.get(), self.Contraseña.get())
                self.lista = Conexion_client.devuelve_lista(Conexion_client)
                contador=0
                self.lista2=[]
                while (contador < len(self.lista)):
                    self.lista2.append(self.lista[contador][0])
                    contador = contador + 1

                self.Combo.delete(0, len(self.lista)-1)
                self.Combo['values'] = self.lista2
                messagebox.showinfo("Actualizacion completada", "Los datos fueron actualizados")


            else:
                messagebox.showinfo("Error de autenticicacion", "Las contraseñas no coinciden")
        else:
            messagebox.showinfo("Error de carga", "Los datos se encuentran incompletos")

    # esta funcion ejecuta la clase cliente llamando la lista cliente
    # mostrando la lista de clientes disponibles
    def muestra_lista_cliente(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x600")
        Label(self.ventana_administracion, text="Lista de clientes registrados", justify="center", width=22, height=4,
              bg="steelblue").grid(row=0, column=0, columnspan=5, ipadx=245)
        botton2 = Button(self.ventana_administracion, image= self.imagen, text="Salir", bg="white", justify="left", height=60,command=self.salir).grid(row=0, column=5)
        botton2


        #dezpla= tk.Canvas(self.ventana_administracion, bg="blue", height=380, width= 600)
        #dezpla.pack()

        Cliente = cliente
        lista_clientes = Cliente.cargar_archivo(Cliente)
        height = len(lista_clientes)
        width =7
        b=Entry(self.ventana_administracion, width=22, text="")
        b.insert(0,"Identificacion")
        b.grid(row=2, column=0)
        b.config(state='readonly')
        b=Entry(self.ventana_administracion, width=22,text="")
        b.insert(0, "Nombre")
        b.grid(row=2, column=1)
        b.config(state='readonly')
        b=Entry(self.ventana_administracion, width=22,text="")
        b.insert(0, "Profesion")
        b.grid(row=2, column=2)
        b.config(state='readonly')
        b=Entry(self.ventana_administracion, width=22, text="")
        b.insert(0, "Direccion")
        b.grid(row=2, column=3)
        b.config(state='readonly')
        b=Entry(self.ventana_administracion, width=22,text="")
        b.insert(0, "Lugar de trabajo")
        b.grid(row=2, column=4)
        b.config(state='readonly')
        b=Entry(self.ventana_administracion, width=22,text="")
        b.insert(0, "Usuario")
        b.grid(row= 2, column=5)
        b.config(state='readonly')


        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = Entry(self.ventana_administracion, width= 22, text="")

                if(j>=3):
                    b.insert(0, lista_clientes[i][(j+1)])
                else:
                    b.insert(0, lista_clientes[i][j])
                b.grid(row=(i+3), column=j)
                b.config(state='readonly')

        self.ventana_administracion.geometry("800"+"x"+str(((len(lista_clientes)+2)*20) + 80))
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(24, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=(((len(lista_clientes)+2)*20) + 60), width=800, height=20)
        #dezpla.pack()

        """ ventana_lista = tk()
        ventana_lista
        ventana_lista.geometry("400x360")
        ventana_lista.resizable(0, 0)
        ventana_lista.title("ADMINISTRACION")
        ventana_lista.transient(master=self.ventana_administracion)
        ventana_lista.geometry("%dx%d+%d+%d" % ((400, 300) + (483.0, 284.0)))
        ventana_lista.
        ventana_l= ttk.Treeview()
        #ventana_lista.mainloop()
        #root.mainloop()"""

    # esta funcion ejecuta la clase asistente mostrando una lista
    # en esta se ingresan los datos para registrar el asistente
    def agregar_asis(self):
        self.ventana_administracion.geometry("400x320")
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')

        self.nombre.destroy()
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(23, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=300, width=400, height=20)

        Label0 = Label(self.ventana_administracion,text="Ingresar todos los datos solicitados para\n agregar al nuevo asistente",bg="white").place_configure(x=10, y=10, width=260, height=50)
        Label1 = Label(self.ventana_administracion, text="Inserte numero de identificación:",bg="white").place_configure(x=10, y=70, width=180, height=20)
        Label2 = Label(self.ventana_administracion, text="Inserte nombre completo: ", bg="white").place_configure(x=10, y=110,width=180,height=20)
        Label6 = Label(self.ventana_administracion, text="Inserte el correo: ", bg="white").place_configure(x=10,y=150,width=180,height=20)
        Label3 = Label(self.ventana_administracion, text="Inserte nombre usuario: ", bg="white").place_configure(x=10, y=190, width=180,height=20)
        Label4 = Label(self.ventana_administracion, text="Inserte la contraseña:", bg="white").place_configure(x=10,   y=230, width=180,height=20)
        Label5 = Label(self.ventana_administracion, text="Confirmacion de la contraseña:", bg="white").place_configure(x=10, y=270, width=180, height=20)
        # self.barramenu.entryconfig(index=1, state= 'normal')

        self.Numero_id = StringVar()
        self.id_numero = Entry(self.ventana_administracion, bd=3, textvariable=self.Numero_id, bg="white")
        self.id_numero.place_configure(x=200, y=70, width=190, height=20)

        self.Nombre = StringVar()
        self.nombre = Entry(self.ventana_administracion, bd=3, textvariable=self.Nombre, bg="white")
        self.nombre.place_configure(x=200, y=110, width=190, height=20)

        self.Correo = StringVar()
        self.correo = Entry(self.ventana_administracion,bd=3, textvariable=self.Correo, bg="white")
        self.correo.place_configure(x=200, y=150, width=190, height=20)

        self.Usuario = StringVar()
        self.usu = Entry(self.ventana_administracion, textvariable=self.Usuario, bg="white")
        self.usu.place_configure(x=200, y=190, width=190, height=20)

        self.Contraseña = StringVar()
        self.cont1 = Entry(self.ventana_administracion,bd=3, textvariable=self.Contraseña, show="*", bg="white")
        self.cont1.place_configure(x=200, y=230, width=190, height=20)

        self.Contraseña2 = StringVar()
        self.cotra2 = Entry(self.ventana_administracion, bd=3, textvariable=self.Contraseña2, show="*", bg="white")
        self.cotra2.place_configure(x=200, y=270, width=190, height=20)

        botton1 = Button(self.ventana_administracion, image=self.image, text="Guardar", command=self.guardar_asist).place_configure(x=280, y=10, width=50, height=50)
        botton1
        #self.voll = PhotoImage(file="C:\Michael\Desktop\Carrera\Arquitectura")
        botton2 = Button(self.ventana_administracion, image= self.imagen,text="Salir", command=self.salir).place_configure(x=340, y=10, width=50, height=50)
        botton2

    # su funcion es modificar los asistentes existentes remplazando uno por otro
    def modifica_asis(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x320")

        self.nombre.destroy()
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(23, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=300, width=400, height=20)

        Label0 = Label(self.ventana_administracion,
                       text="Seleccione la cedula del asistente a\n modificar y luego rellene los datos\n solicitados, luego dar click en el check",
                       bg="white").place_configure(x=10, y=10, width=210, height=50)

        Label(self.ventana_administracion, text="Seleccione el administrador :", justify="left",
              bg="white").place_configure(x=10, y=70, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte nombre completo: ", justify="left",
              bg="white").place_configure(x=10, y=110, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte el correo: ", justify="left",
              bg="white").place_configure(x=10, y=150, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte nombre usuario: ", justify="left", bg="white").place_configure(
            x=10, y=190, width=180, height=20)
        Label(self.ventana_administracion, text="Inserte la contraseña:", justify="left", bg="white").place_configure(
            x=10, y=230, width=180, height=20)
        Label(self.ventana_administracion, text="Confirmacion de la contraseña:", justify="left",
              bg="white").place_configure(x=10, y=270, width=180, height=20)
        # self.barramenu.entryconfig(index=1, state= 'normal')

        # self.Numero_id = StringVar()
        # self.id_numero = Entry(self.ventana_administracion, textvariable=self.Numero_id, bg="green")
        # self.id_numero.place_configure(x=200, y=60, width=190, height=20)
        self.Combo = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo.place_configure(x=200, y=70, width=190, height=20)

        cargar_archivo1 = asistente
        self.lista = []
        self.lista = cargar_archivo1.devuelve_lista(cargar_archivo1)
        self.lista2 = []
        contador = 0

        while (contador < len(self.lista)):
            self.lista2.append(self.lista[contador][0])
            contador = contador + 1

        self.seleccion = str()
        self.Combo['values'] = self.lista2
        self.Combo.bind("<<ComboboxSelected>>", self.buscar_asist)
        self.seleccion = self.Combo.get()


        # listadmin.place_configure(x=200, y= 60, width=190, height=20)

        self.Nombre = StringVar()
        self.nombre = Entry(self.ventana_administracion,bd=3, textvariable=self.Nombre, bg="white")
        self.nombre.place_configure(x=200, y=110, width=190, height=20)

        self.Correo = StringVar()
        self.correo = Entry(self.ventana_administracion, bd=3, textvariable=self.Correo, bg="white")
        self.correo.place_configure(x=200, y=150, width=190, height=20)

        self.Usuario = StringVar()
        self.usu = Entry(self.ventana_administracion, bd=3, textvariable=self.Usuario, bg="white")
        self.usu.place_configure(x=200, y=190, width=190, height=20)

        self.Contraseña = StringVar()
        self.cont1 = Entry(self.ventana_administracion, bd=3, textvariable=self.Contraseña, show="*", bg="white")
        self.cont1.place_configure(x=200, y=230, width=190, height=20)

        self.Contraseña2 = StringVar()
        self.cotra2 = Entry(self.ventana_administracion, bd=3, textvariable=self.Contraseña2, show="*", bg="white")
        self.cotra2.place_configure(x=200, y=270, width=190, height=20)

        #self.botton1 = Button(self.ventana_administracion, text="Buscar", bg="green", command=self.buscar_asist)
        #self.botton1.place_configure(x=225, y=0, width=50, height=50)

        self.botton11 = Button(self.ventana_administracion, image=self.image, text="Guardar",
                               command=self.llama_modificar_asist)
        self.botton11.place_configure(x=285, y=10, width=50, height=50)

        botton2 = Button(self.ventana_administracion, image=self.imagen,text="Salir", command=self.salir)
        botton2.place_configure(x=340, y=10, width=50, height=50)

     # Esta funcion muestra la lista de asistentes
    def muestra_lista_asis(self):
        # Esta parte de la funcion sirve para ajustar los botones de la lista de asistentes.
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x600")
        Label(self.ventana_administracion, text="Lista de asistentes registrados", justify="center", width=22, height=4,
              bg="steelblue").grid(row=0, column=0, columnspan=3, ipadx=140)
        botton2 = Button(self.ventana_administracion, image= self.imagen, text="Salir", justify="left", height=60,
                         command=self.salir).grid(row=0, column=3, columnspan=15, ipadx=20)
        botton2

        # dezpla= tk.Canvas(self.ventana_administracion, bg="blue", height=380, width= 600)
        # dezpla.pack()

        # Esta parte carga la lista de asistentes y muestra sus respectivos resultados
        Asistente = asistente
        lista_asistente = Asistente.cargar_archivo(Asistente)
        height = len(lista_asistente)
        width = 4
        b = Entry(self.ventana_administracion, width=26, text="")
        b.insert(0, "Numero de identificacion")
        b.grid(row=2, column=0)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=26, text="")
        b.insert(0, "Nombre del asistente")
        b.grid(row=2, column=1)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=26, text="")
        b.insert(0, "Correo del asistente")
        b.grid(row=2, column=2)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=26, text="")
        b.insert(0, "Usuario del asistente")
        b.grid(row=2, column=3)
        b.config(state='readonly')

        # Esta parte es para los parametros para la Fila y Columna
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = Entry(self.ventana_administracion, width=26, text="")

                if (j >= 3):
                    b.insert(0, lista_asistente[i][(j + 1)])
                else:
                    b.insert(0, lista_asistente[i][j])
                b.grid(row=(i + 3), column=j)
                b.config(state='readonly')

        self.ventana_administracion.geometry("600" + "x" + str(((len(lista_asistente) + 2) * 20) + 80))
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, "Administrador: ", )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=(((len(lista_asistente) + 2) * 20) + 60), width=650, height=20)

       # Esta funcion verifica la contraseña
       # Si esta es valida se guarda en caso de no serlo mostrara error
    def guardar(self):
        if(self.Contraseña.get()== self.Contraseña2.get()) and (self.Contraseña.get() != "") and(self.Nombre.get() !="") and (self.Usuario.get()!="") and (self.Numero_id.get() != ""):

         cedula_correcta= True
         try:
             int(self.Numero_id.get())
         except:
             cedula_correcta=False

         if(cedula_correcta):
                Nuevo_administrador= administrador
                if(Nuevo_administrador.verificar_cedula(Nuevo_administrador,int(self.Numero_id.get()))):
                    Nuevo_administrador.identificacion= int(self.Numero_id.get())
                    Nuevo_administrador.nombre= self.Nombre.get()
                    Nuevo_administrador.puesto= "Administrador"
                    Nuevo_administrador.nombre_usuario= self.Usuario.get()
                    Nuevo_administrador.contraseña= self.Contraseña.get()
                    Nuevo_administrador.guardar_archivo(Nuevo_administrador)
                    Nuevo_administrador.cargar_archivo(Nuevo_administrador)
                    self.id_numero.delete(0, tk.END)
                    self.nombre.delete(0, tk.END)
                    self.usu.delete(0, tk.END)
                    self.cont1.delete(0, tk.END)
                    self.cotra2.delete(0, tk.END)
                    messagebox.showinfo("Ingreso correcto", "El administrador se guardo correctamente")
                else:
                    messagebox.showinfo("Ingreso incorreco", "El administrador ya existe, con esa cedula")
         else:
                messagebox.showinfo("Ingreso inorrecto", "El numero identificacion no tiene validez")
         #print(Nuevo_administrador.identificacion, " ", Nuevo_administrador.nombre, Nuevo_administrador.puesto, " ", Nuevo_administrador.usuario," ", Nuevo_administrador.contraseña)
        else:
            if(self.Contraseña.get()== self.Contraseña2.get()) and (self.Contraseña.get()!= ""):
                messagebox.showinfo("Error de ingreso",  "Todos los datos deven de ser ingresados")
                self.id_numero.delete(0, tk.END)
                self.nombre.delete(0, tk.END)
                self.usu.delete(0, tk.END)
                self.cont1.delete(0, tk.END)
                self.cotra2.delete(0, tk.END)
            else:
                messagebox.showinfo("Error de ingreso", "Las contraseñas no coinciden")
                self.cont1.delete(0,tk.END)
                self.cotra2.delete(0, tk.END)

    # Esta funcion sirve para salir
    def salir(self):
        self.ventana_administracion.destroy()
        self.ventana_admin()

    # Esta funcion sirve para buscar en las listas
    # Muestra los resultados de la lista
    def buscar(self, event):
        self.nombre.delete(0,END)
        self.usu.delete(0, END)
        self.cont1.delete(0, END)
        self.cotra2.delete(0,END)
        #self.botton1.destroy()
        self.seleccion= self.Combo.get()

        conta_aux=0
        if(self.seleccion != ""):
             while(conta_aux < len(self.lista)):
                 if(int(self.seleccion)== int(self.lista[conta_aux][0])):
                     self.nombre.insert(0, self.lista[conta_aux][1])
                     self.usu.insert(0, self.lista[conta_aux][3])
                     self.cont1.insert(0, self.lista[conta_aux][4])
                     self.cotra2.insert(0, self.lista[conta_aux][4])
                     conta_aux= conta_aux + 1
                 else:
                     conta_aux=conta_aux + 1
        else:
            messagebox.showinfo("Error de identificacion", "No se ha selecionado ningun administrador")

    #Esta funcion permite guardar la lsita de asistentes en la clase asistentes
    #Ademas de comprobar la lista de asistentes
    def guardar_asist(self):
        if(self.Contraseña.get()== self.Contraseña2.get()) and (self.Contraseña.get() != "") and(self.Nombre.get() !="") and (self.Correo.get()!="") and (self.Usuario.get()!="") and (self.Numero_id.get() != ""):

         cedula_correcta= True
         try:
             int(self.Numero_id.get())
         except:
             cedula_correcta=False

         if(cedula_correcta):
                Nuevo_asistente= asistente
                if(Nuevo_asistente.verificar_cedula(Nuevo_asistente,int(self.Numero_id.get()))):
                    Nuevo_asistente.identificacion= int(self.Numero_id.get())
                    Nuevo_asistente.nombre= self.Nombre.get()
                    Nuevo_asistente.correo = self.Correo.get()
                    Nuevo_asistente.puesto= "Asistente"
                    Nuevo_asistente.nombre_usuario= self.Usuario.get()
                    Nuevo_asistente.contraseña= self.Contraseña.get()
                    Nuevo_asistente.guardar_archivo(Nuevo_asistente)
                    Nuevo_asistente.cargar_archivo(Nuevo_asistente)
                    self.id_numero.delete(0, tk.END)
                    self.nombre.delete(0, tk.END)
                    self.correo.delete(0,tk.END)
                    self.usu.delete(0, tk.END)
                    self.cont1.delete(0, tk.END)
                    self.cotra2.delete(0, tk.END)
                    messagebox.showinfo("Ingreso correcto", "El asistente se guardo correctamente")
                else:
                    messagebox.showinfo("Ingreso incorreco", "El asistente ya existe, con esa cedula")
         else:
                messagebox.showinfo("Ingreso inorrecto", "El numero identificacion no tiene validez")
         #print(Nuevo_administrador.identificacion, " ", Nuevo_administrador.nombre, Nuevo_administrador.puesto, " ", Nuevo_administrador.usuario," ", Nuevo_administrador.contraseña)
        else:
            if(self.Contraseña.get()== self.Contraseña2.get()) and (self.Contraseña.get()!= ""):
                messagebox.showinfo("Error de ingreso",  "Todos los datos deben de ser ingresados")
                self.id_numero.delete(0, tk.END)
                self.nombre.delete(0, tk.END)
                self.usu.delete(0, tk.END)
                self.cont1.delete(0, tk.END)
                self.cotra2.delete(0, tk.END)
            else:
                messagebox.showinfo("Error de ingreso", "Las contraseñas no coinciden")
                self.cont1.delete(0,tk.END)
                self.cotra2.delete(0, tk.END)
    # Esta funcion busca los asistentes de la clase asistentes
    def buscar_asist(self, event):
        self.nombre.delete(0,END)
        self.correo.delete(0, END)
        self.usu.delete(0, END)
        self.cont1.delete(0, END)
        self.cotra2.delete(0,END)
        #self.botton1.destroy()
        self.seleccion= self.Combo.get()
        conta_aux=0
        if(self.seleccion != ""):
             while(conta_aux < len(self.lista)):
                 if(int(self.seleccion)== int(self.lista[conta_aux][0])):
                     self.nombre.insert(0, self.lista[conta_aux][1])
                     self.correo.insert(0, self.lista[conta_aux][2])
                     self.usu.insert(0, self.lista[conta_aux][4])
                     self.cont1.insert(0, self.lista[conta_aux][5])
                     self.cotra2.insert(0, self.lista[conta_aux][5])
                     conta_aux= conta_aux + 1
                 else:
                     conta_aux=conta_aux + 1
        else:
            messagebox.showinfo("Error de identificacion", "No se ha selecionado ningun asistente")

    # Esta funcion sirve para modificar la lista de asistentes
    def llama_modificar_asist(self):
        if(self.Combo.get()!="")and(self.Nombre.get() != "") and (self.Correo.get()!= "") and (self.Usuario.get()!= "") and (self.Contraseña.get()!="") and (self.Contraseña2.get()!=""):
            if(self.Contraseña.get() == self.Contraseña2.get()):
                Conexion_asist= asistente
                Conexion_asist.modificar(Conexion_asist, int(self.Combo.get()), self.Nombre.get(),self.Correo.get(),"ASISTENTE", self.Usuario.get(), self.Contraseña.get())
                self.lista = Conexion_asist.devuelve_lista(Conexion_asist)
                contador=0
                self.lista2=[]
                while (contador < len(self.lista)):
                    self.lista2.append(self.lista[contador][0])
                    contador = contador + 1

                self.Combo.delete(0, len(self.lista)-1)
                self.Combo['values'] = self.lista2
                messagebox.showinfo("Actualizacion completada", "Los datos fueron actualizados")


            else:
                messagebox.showinfo("Error de autenticicacion", "Las contraseñas no coinciden")
        else:
            messagebox.showinfo("Error de carga", "Los datos se encuentran incompletos")
    # Funcion para modificar la lista de administrador
    def llama_modificar_admin(self):
        if(self.Combo.get()!="")and(self.Nombre.get() != "") and(self.Usuario.get()!= "") and (self.Contraseña.get()!="") and (self.Contraseña2.get()!=""):
            if(self.Contraseña.get() == self.Contraseña2.get()):
                Conexion_admin= administrador
                Conexion_admin.modificar(Conexion_admin, int(self.Combo.get()), self.Nombre.get(),"ADMINISTRADOR", self.Usuario.get(), self.Contraseña.get())
                self.lista = Conexion_admin.devuelve_lista(Conexion_admin)
                contador=0
                self.lista2=[]
                while (contador < len(self.lista)):
                    self.lista2.append(self.lista[contador][0])
                    contador = contador + 1

                self.Combo.delete(0, len(self.lista)-1)
                self.Combo['values'] = self.lista2
                messagebox.showinfo("Actualizacion completada", "Los datos fueron actualizados")


            else:
                messagebox.showinfo("Error de autenticicacion", "Las contraseñas no coinciden")
        else:
            messagebox.showinfo("Error de carga", "Los datos se encuentran incompletos")

    # Esta funcion permite agregar u vehiculo a la lista vehiculo
    def agregar_vehiculo(self):
        self.ventana_administracion.geometry("400x320")
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.nombre.destroy()
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ":", )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=300, width=400, height=20)

        Label0 = Label(self.ventana_administracion,
                       text="Ingresar todos los datos solicitados para\n agregar el nuevo vehiculo",
                       bg="white").place_configure(x=10, y=10, width=260, height=50)
        Label1 = Label(self.ventana_administracion, text="Inserte el numero de placa:",
                       bg="white").place_configure(x=10, y=70, width=180, height=20)
        Label2 = Label(self.ventana_administracion, text="Inserte el modelo: ", bg="white").place_configure(x=10,
                                                                                                                  y=110,
                                                                                                                  width=180,
                                                                                                                  height=20)
        Label6 = Label(self.ventana_administracion, text="Inserte la marca: ", bg="white").place_configure(x=10, y=150,
                                                                                                            width=180,
                                                                                                            height=20)
        Label3 = Label(self.ventana_administracion, text="Inserte el color: ", bg="white").place_configure(x=10,
                                                                                                                 y=190,
                                                                                                                 width=180,
                                                                                                                 height=20)
        Label4 = Label(self.ventana_administracion, text="Inserte la cantidad de pasajeros:", bg="white").place_configure(x=10,
                                                                                                               y=230,
                                                                                                               width=180,
                                                                                                               height=20)
        Label4 = Label(self.ventana_administracion, text="Valor del alquiler por dia:",
                       bg="white").place_configure(x=10,
                                                   y=270,
                                                   width=180,
                                                   height=20)


        self.Numero_placa = StringVar()
        self.id_placa = Entry(self.ventana_administracion, bd=3, textvariable=self.Numero_placa, bg="white")
        self.id_placa.place_configure(x=200, y=70, width=190, height=20)

        self.Modelo = StringVar()
        self.modelo = Entry(self.ventana_administracion, bd=3, textvariable=self.Modelo, bg="white")
        self.modelo.place_configure(x=200, y=110, width=190, height=20)

        self.Marca = StringVar()
        self.marca = Entry(self.ventana_administracion, bd=3, textvariable=self.Marca, bg="white")
        self.marca.place_configure(x=200, y=150, width=190, height=20)

        self.Color = StringVar()
        self.color = Entry(self.ventana_administracion, bd=3, textvariable=self.Color, bg="white")
        self.color.place_configure(x=200, y=190, width=190, height=20)

        self.Num_pasageros = StringVar()
        self.num_pasageros = Entry(self.ventana_administracion, bd=3, textvariable=self.Num_pasageros, bg="white")
        self.num_pasageros.place_configure(x=200, y=230, width=190, height=20)

        self.Valor_dia = StringVar()
        self.valor_dia = Entry(self.ventana_administracion, bd=3, textvariable=self.Valor_dia, bg="white")
        self.valor_dia.place_configure(x=200, y=270, width=190, height=20)


        botton1 = Button(self.ventana_administracion,image= self.image, text="Guardar",
                         command=self.guardar_vehiculo).place_configure(x=280, y=10, width=50, height=50)
        botton1
        # self.voll = PhotoImage(file="C:\Michael\Desktop\Carrera\Arquitectura")
        botton2 = Button(self.ventana_administracion,image= self.imagen, text="Salir", command=self.salir).place_configure(
            x=340, y=10, width=50, height=50)
        botton2

    #Esta funcion permite guardar una vehiculo en la lista vehiculo
    def guardar_vehiculo(self):
        if (self.Numero_placa.get()!="") and (self.Modelo.get()!= "") and (self.Marca.get() != "") and(self.Color.get()!="")and (self.Num_pasageros.get() != ""):

            placa_correcta = True
            try:
                int(self.Numero_placa.get())
            except:
                placa_correcta= False

            pasageros_correcto= True
            try:
                int(self.Num_pasageros.get())
            except:
                pasageros_correcto= False
            valor_correcto= True
            try:
                int(self.Valor_dia.get())
            except:
                valor_correcto= False

            if (placa_correcta and pasageros_correcto and valor_correcto):
                Nuevo_vehiculo = vehiculo
                if (Nuevo_vehiculo.verificar_placa(Nuevo_vehiculo, int(self.Numero_placa.get()))):
                    Nuevo_vehiculo.placa = int(self.Numero_placa.get())
                    Nuevo_vehiculo.modelo = self.Modelo.get()
                    Nuevo_vehiculo.marca = self.Marca.get()
                    Nuevo_vehiculo.color = self.Color.get()
                    Nuevo_vehiculo.cantidad_pasajeros = self.Num_pasageros.get()
                    Nuevo_vehiculo.valor_alquiler= self.Valor_dia.get()
                    Nuevo_vehiculo.en_uso= "NO"
                    Nuevo_vehiculo.guardar_archivo(Nuevo_vehiculo)
                    Nuevo_vehiculo.cargar_archivo(Nuevo_vehiculo)
                    self.id_placa.delete(0, tk.END)
                    self.modelo.delete(0, tk.END)
                    self.marca.delete(0, tk.END)
                    self.color.delete(0, tk.END)
                    self.num_pasageros.delete(0, tk.END)
                    self.valor_dia.delete(0, tk.END)
                    messagebox.showinfo("Ingreso correcto", "El vehiculo se guardo correctamente")
                else:
                    self.id_placa.delete(0, tk.END)
                    self.modelo.delete(0, tk.END)
                    self.marca.delete(0, tk.END)
                    self.color.delete(0, tk.END)
                    self.num_pasageros.delete(0, tk.END)
                    self.valor_dia.delete(0, tk.END)
                    messagebox.showinfo("Ingreso incorreco", "El vehiculo ya existe con esa placa")
            else:
                messagebox.showinfo("Ingreso inorrecto", "El numero de placa,la cantidad de pasajeros y valor por dia tienen que ser valores numericos")
            # print(Nuevo_administrador.identificacion, " ", Nuevo_administrador.nombre, Nuevo_administrador.puesto, " ", Nuevo_administrador.usuario," ", Nuevo_administrador.contraseña)
        else:
                messagebox.showinfo("Error de ingreso", "Todos los datos deben de ser ingresados")
                self.id_placa.delete(0, tk.END)
                self.modelo.delete(0, tk.END)
                self.marca.delete(0, tk.END)
                self.color.delete(0, tk.END)
                self.num_pasageros.delete(0, tk.END)
                self.valor_dia.delete(0, tk.END)

     #Esta funcion permite modificar un vehiculo de la lista vehiculo
    def modifica_vehiculo(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x320")
        self.nombre.destroy()
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ":", )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=300, width=400, height=20)


        Label0 = Label(self.ventana_administracion,
                       text="Seleccione la placa del vehiculo\n a modificar, luego rellenar los datos\nsolicitados y dar click sobre el check ",
                       bg="white").place_configure(x=10, y=10, width=210, height=50)

        Label(self.ventana_administracion, text="Seleccione el numero de placa:", justify="left",
              bg="white").place_configure(x=10, y=70, width=180, height=20)
        Label2 = Label(self.ventana_administracion, text="Inserte el modelo: ", bg="white").place_configure(x=10,
                                                                                                            y=110,
                                                                                                            width=180,
                                                                                                            height=20)
        Label6 = Label(self.ventana_administracion, text="Inserte la marca: ", bg="white").place_configure(x=10, y=150,
                                                                                                           width=180,
                                                                                                           height=20)
        Label3 = Label(self.ventana_administracion, text="Inserte el color: ", bg="white").place_configure(x=10,
                                                                                                           y=190,
                                                                                                           width=180,
                                                                                                           height=20)
        Label4 = Label(self.ventana_administracion, text="Inserte la cantidad de pasajeros:",
                       bg="white").place_configure(x=10,
                                                   y=230,
                                                   width=180,
                                                   height=20)
        Label4 = Label(self.ventana_administracion, text="Valor del alquiler por dia:",
                       bg="white").place_configure(x=10,
                                                   y=270,
                                                   width=180,
                                                   height=20)
        # self.barramenu.entryconfig(index=1, state= 'normal')

        # self.Numero_id = StringVar()
        # self.id_numero = Entry(self.ventana_administracion, textvariable=self.Numero_id, bg="green")
        # self.id_numero.place_configure(x=200, y=60, width=190, height=20)
        self.Combo = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo.place_configure(x=200, y=70, width=190, height=20)

        cargar_archivo1 = vehiculo
        self.lista = []
        self.lista = cargar_archivo1.devuelve_lista(cargar_archivo1)
        self.lista2 = []
        contador = 0

        while (contador < len(self.lista)):
            if(self.lista[contador][6]=="NO") or (self.lista[contador][6]=="no"):
               self.lista2.append(self.lista[contador][0])
            contador = contador + 1

        self.seleccion = str()
        self.Combo['values'] = self.lista2

        self.seleccion = self.Combo.get()
        self.Combo.bind("<<ComboboxSelected>>", self.buscar_vehiculo)

        # listadmin.place_configure(x=200, y= 60, width=190, height=20)

        self.Modelo = StringVar()
        self.modelo = Entry(self.ventana_administracion,bd=3, textvariable=self.Modelo, bg="white")
        self.modelo.place_configure(x=200, y=110, width=190, height=20)

        self.Marca = StringVar()
        self.marca = Entry(self.ventana_administracion, bd=3, textvariable=self.Marca, bg="white")
        self.marca.place_configure(x=200, y=150, width=190, height=20)

        self.Color = StringVar()
        self.color = Entry(self.ventana_administracion, bd=3, textvariable=self.Color, bg="white")
        self.color.place_configure(x=200, y=190, width=190, height=20)

        self.Num_pasageros = StringVar()
        self.num_pasageros = Entry(self.ventana_administracion, bd=3, textvariable=self.Num_pasageros, bg="white")
        self.num_pasageros.place_configure(x=200, y=230, width=190, height=20)

        self.Valor_dia = StringVar()
        self.valor_dia = Entry(self.ventana_administracion, bd=3, textvariable=self.Valor_dia, bg="white")
        self.valor_dia.place_configure(x=200, y=270, width=190, height=20)

        #self.botton1 = Button(self.ventana_administracion, text="Buscar", bg="green", command=self.buscar_vehiculo)
        #self.botton1.place_configure(x=225, y=0, width=50, height=50)

        self.botton11 = Button(self.ventana_administracion, image=self.image, text="Guardar",
                               command=self.llama_modificar_vehiculo)
        self.botton11.place_configure(x=285, y=10, width=50, height=50)

        botton2 = Button(self.ventana_administracion, image=self.imagen, text="Salir", command=self.salir)
        botton2.place_configure(x=340, y=10, width=50, height=50)

    # Esta funcion permite buscar un vehiculo de la clase vehiculo en la clase vehiculo
    def buscar_vehiculo(self, event):
        #self.id_placa.delete(0, tk.END)
        self.modelo.delete(0, tk.END)
        self.marca.delete(0, tk.END)
        self.color.delete(0, tk.END)
        self.num_pasageros.delete(0, tk.END)
        self.valor_dia.delete(0, tk.END)
        # self.botton1.destroy()
        self.seleccion = self.Combo.get()
        conta_aux = 0
        if (self.seleccion != ""):
            while (conta_aux < len(self.lista)):
                if (int(self.seleccion) == int(self.lista[conta_aux][0])):
                    self.modelo.insert(0, self.lista[conta_aux][1])
                    self.marca.insert(0, self.lista[conta_aux][2])
                    self.color.insert(0, self.lista[conta_aux][3])
                    self.num_pasageros.insert(0, self.lista[conta_aux][4])
                    self.valor_dia.insert(0, self.lista[conta_aux][5])
                    conta_aux = conta_aux + 1
                else:
                    conta_aux = conta_aux + 1
        else:
            messagebox.showinfo("Error de identificacion", "No se ha selecionado ninguna placa")

    # Esta funcion permite modificar un vehiculo de la clase vehiculo
    def llama_modificar_vehiculo(self):
        if (self.Combo.get()!="")and(self.Modelo.get() != "") and (self.Marca.get() != "") and (self.Color.get() != "") and (self.Num_pasageros.get() != "") and(self.Valor_dia.get()!=""):
            pasageros_correcto = True
            try:
                int(self.Num_pasageros.get())
            except:
                pasageros_correcto = False

            valor_correcto = True
            try:
                int(self.Valor_dia.get())
            except:
                valor_correcto = False

            if(pasageros_correcto) and (valor_correcto):
                Conexion_vehiculo = vehiculo
                Conexion_vehiculo.modificar(Conexion_vehiculo, int(self.Combo.get()), self.Modelo.get(), self.Marca.get(),
                                          self.Color.get(), self.Num_pasageros.get(), self.Valor_dia.get(), "NO")
                self.lista = Conexion_vehiculo.devuelve_lista(Conexion_vehiculo)
                contador = 0
                self.lista2 = []
                while (contador < len(self.lista)):
                    self.lista2.append(self.lista[contador][0])
                    contador = contador + 1

                self.Combo.delete(0, len(self.lista) - 1)
                self.Combo['values'] = self.lista2
                messagebox.showinfo("Actualizacion completada", "Los datos fueron actualizados")

            else:
                messagebox.showinfo("Error de ingreso", "La cantidad de pasajeros tiene que ser numerica")
        else:
            messagebox.showinfo("Error de ingreso", "Debe selecconar el numero de placa y todos los espacios tienen que ser completados")

    # Esta funcion muestra un vehiculo de la lista vehiculo
    def muestra_lista_vehiculo(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x600")
        Label(self.ventana_administracion, text="Lista de vehiculos disponibles", justify="center", width=22, height=4,
              bg="steelblue").grid(row=0, column=0, columnspan=5, ipadx=290)
        botton2 = Button(self.ventana_administracion, image= self.imagen, text="Salir", justify="left", height=60,
                         command=self.salir).grid(row=0, column=5, ipadx=20)
        botton2

        # dezpla= tk.Canvas(self.ventana_administracion, bg="blue", height=380, width= 600)
        # dezpla.pack()

        Vehiculo = vehiculo
        lista_vehiculos = Vehiculo.cargar_archivo(Vehiculo)
        height = len(lista_vehiculos)
        width = 7
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Placa")
        b.grid(row=2, column=0)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Modelo")
        b.grid(row=2, column=1)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Marca")
        b.grid(row=2, column=2)
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Color")
        b.grid(row=2, column=3)
        b.config(state='readonly')
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Numero de pasajeros")
        b.grid(row=2, column=4)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Valor por dia")
        b.grid(row=2, column=5)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "En uso")
        b.grid(row=2, column=6)
        b.config(state='readonly')


        lista_aux=[]
        contador=0

        while contador< len(lista_vehiculos):
                if(lista_vehiculos[contador][6]=="NO"):
                    lista_aux.append(lista_vehiculos[contador])
                contador= contador + 1

        lista_vehiculos= lista_aux
        height = len(lista_vehiculos)

        for i in range(height):  # Rows
                for j in range(width):  # Columns
                    b = Entry(self.ventana_administracion, width=25, text="")
                    b.insert(0, lista_vehiculos[i][j])
                    b.grid(row=(i + 3), column=j)
                    b.config(state='readonly')

        self.ventana_administracion.geometry("900" + "x" + str(((len(lista_vehiculos) + 2) * 20) + 90))
        self.ventana_administracion.geometry("%dx%d+%d+%d" % ((900, int(((len(lista_vehiculos) + 2) * 20) + 90)) + (-500, -500)))
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=(((len(lista_vehiculos) + 2) * 20) + 70), width=900, height=20)

    # Esta funcion muestra la lista vehiculo en un uso
    def muestra_lista_vehiculo_1(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x600")
        Label(self.ventana_administracion, text="Lista de vehiculos en uso", justify="center", width=22, height=4,
          bg="steelblue").grid(row=0, column=0, columnspan=5, ipadx=290)
        botton2 = Button(self.ventana_administracion,image= self.imagen, text="Salir", justify="left", height=60,
                     command=self.salir).grid(row=0, column=5, ipadx=20)
        botton2

    # dezpla= tk.Canvas(self.ventana_administracion, bg="blue", height=380, width= 600)
    # dezpla.pack()

        Vehiculo = vehiculo
        lista_vehiculos = Vehiculo.cargar_archivo(Vehiculo)
        height = len(lista_vehiculos)
        width = 6
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Placa")
        b.grid(row=2, column=0)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Modelo")
        b.grid(row=2, column=1)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Marca")
        b.grid(row=2, column=2)
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Color")
        b.grid(row=2, column=3)
        b.config(state='readonly')
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Numero de pasajeros")
        b.grid(row=2, column=4)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Valor por dia")
        b.grid(row=2, column=5)
        b.config(state='readonly')

        lista_aux = []
        contador = 0

        while contador < len(lista_vehiculos):
            if (lista_vehiculos[contador][6] == "SI"):
                lista_aux.append(lista_vehiculos[contador])
            contador = contador + 1

        lista_vehiculos = lista_aux
        height = len(lista_vehiculos)

        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = Entry(self.ventana_administracion, width=25, text="")
                b.insert(0, lista_vehiculos[i][j])
                b.grid(row=(i + 3), column=j)
                b.config(state='readonly')


        self.ventana_administracion.geometry(
        "%dx%d+%d+%d" % ((900, int(((len(lista_vehiculos) + 2) * 20) + 90)) + (-500, -500)))
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=(((len(lista_vehiculos) + 2) * 20) + 70), width=900, height=20)

    # Esta funcion permite mostrar la lista de vehiculos registrados
    def muestra_lista_vehiculo_2(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x600")
        Label(self.ventana_administracion, text="Lista de vehiculos registrados", justify="center", width=22, height=4,
              bg="steelblue").grid(row=0, column=0, columnspan=5, ipadx=290)
        botton2 = Button(self.ventana_administracion, image= self.imagen, text="Salir", justify="left", height=60,
                         command=self.salir).grid(row=0, column=5, ipadx=20)
        botton2

        # dezpla= tk.Canvas(self.ventana_administracion, bg="blue", height=380, width= 600)
        # dezpla.pack()

        Vehiculo = vehiculo
        lista_vehiculos = Vehiculo.cargar_archivo(Vehiculo)
        height = len(lista_vehiculos)
        width = 6
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Placa")
        b.grid(row=2, column=0)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Modelo")
        b.grid(row=2, column=1)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Marca")
        b.grid(row=2, column=2)
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Color")
        b.grid(row=2, column=3)
        b.config(state='readonly')
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Numero de pasajeros")
        b.grid(row=2, column=4)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=25, text="")
        b.insert(0, "Valor por dia")
        b.grid(row=2, column=5)
        b.config(state='readonly')

        for i in range(height):  # Rows
                for j in range(width):  # Columns
                    b = Entry(self.ventana_administracion, width=25, text="")
                    b.insert(0, lista_vehiculos[i][j])
                    b.grid(row=(i + 3), column=j)
                    b.config(state='readonly')


        self.ventana_administracion.geometry(
            "%dx%d+%d+%d" % ((900, int(((len(lista_vehiculos) + 2) * 20) + 90)) + (-500, -500)))
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=(((len(lista_vehiculos) + 2) * 20) + 70), width=900, height=20)


     # Esta funcion permite agregar promociones
    def agregar_promociones(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("%dx%d+%d+%d" % ((500, 300) + (483.0, 284.0)))
        self.ano = datetime.date.today().year
        self.mes = datetime.date.today().month

        self.label= tk.Label(self.ventana_administracion, text= "Seleccione la fecha inicio de la oferta(año/mes/dia)", justify= tk.LEFT, bg='white')
        self.label.place_configure(x= 220, y= 70, width= 270, height= 20)

        self.label = tk.Label(self.ventana_administracion, text="Ingrese los datos que \n requiere para la oferta",
                              justify=tk.CENTER, bg= 'white')
        self.label.place_configure(x=220, y=10, width=140, height=50)

        self.label = tk.Label(self.ventana_administracion, text="Seleccione la fecha fin de la oferta (año/mes/dia)", bg= 'white',
                              justify=tk.LEFT)
        self.label.place_configure(x=220, y=130, width=270, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Seleccione la marca del vehiculo",
                              justify=tk.LEFT, bg= 'white')
        self.label.place_configure(x=220, y=195, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Ingrese el valor por dia",
                              justify=tk.LEFT, bg= 'white')
        self.label.place_configure(x=220, y=230, width=180, height=20)

        self.Valorxdia= StringVar()
        self.valorxdia = Entry(self.ventana_administracion, textvariable=self.Valorxdia, bg="white")
        self.valorxdia.place_configure(x=420, y=230, width=70, height=20)


        self.label1 = tk.Label(self.ventana_administracion, text="", font=('courier', 10, 'bold'), bg='white', justify=tk.LEFT)

        self.label1.place_configure(x= 10, y=10 , width= 200 , height = 200)

        self.anterior = tk.Button(self.ventana_administracion, text="Anterior", bg= 'white', command=self.mesAnterior)
        self.anterior.place_configure(x= 10, y = 230, width= 50, height= 20)

        self.siguiente = tk.Button(self.ventana_administracion, text="Siguiente",bg= 'white', command=self.mesSiguiente)
        self.siguiente.place_configure(x=155, y=230, width=55, height=20)

        botton1 = Button(self.ventana_administracion, image= self.image, text="Guardar",
                         command=self.guardar_promocion).place_configure(x=380, y=10, width=50, height=50)
        botton1

        botton2 = Button(self.ventana_administracion, image= self.imagen, text="Salir", command=self.salir).place_configure(
            x=440, y=10, width=50, height=50)
        botton2

        self.Combo_año = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_mes = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_fecha = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_año.place_configure(x=220, y=100, width=75, height=20)
        self.Combo_mes.place_configure(x=320, y=100, width=75, height=20)
        self.Combo_fecha.place_configure(x=420, y=100, width=70, height=20)

        self.Combo_año_fin = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_mes_fin = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_fecha_fin = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_año_fin.place_configure(x=220, y=160, width=75, height=20)
        self.Combo_mes_fin.place_configure(x=320, y=160, width=75, height=20)
        self.Combo_fecha_fin.place_configure(x=420, y=160, width=70, height=20)

        self.Combo_marca= ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_marca.place_configure(x=420, y=195, width=70, height=20)

        cargar = vehiculo
        lista = cargar.cargar_archivo(cargar)
        listaaux= []
        contador = 0
        while contador < len(lista ):
            listaaux.append(lista[contador][2])
            contador = contador + 1

        self.Combo_marca['values']= listaaux





        self.writeCalendar(self.ano, self.mes)

    # Esta funcion permite guardar promociones en la clase promociones
    def guardar_promocion(self):

        if(self.Combo_año.get()!= "") and (self.Combo_mes.get()!="") and (self.Combo_fecha.get()!="") and (self.Combo_año_fin.get()!="") and (self.Combo_mes_fin.get()!= "") and(self.Combo_fecha_fin!="") and (self.Combo_marca.get()!="") and(self.Valorxdia.get()!= ""):
            monto = True
            try:
                int(self.Valorxdia.get())
            except:
                monto = False

            if(monto):
                    Cargar = promociones

                    lista= Cargar.cargar_archivo(Cargar)
                    contador= 0
                    ingreso = True


                    while(contador < len(lista)):

                        if (lista [contador][0] == (self.Combo_fecha.get() +"/" + self.Combo_mes.get()+ "/" +self.Combo_año.get())) and (lista[contador][1]==self.Combo_fecha_fin.get() + "/" + self.Combo_mes_fin.get() + "/" + self.Combo_año_fin.get()) and (lista [contador][2] == self.Combo_marca.get()):
                            ingreso= False
                        contador = contador + 1

                    if (ingreso):

                        if(self.Combo_año_fin.get()> self.Combo_año.get()):
                           Cargar.fecha_inicio = self.Combo_fecha.get() + "/" + self.Combo_mes.get() + "/" + self.Combo_año.get()
                           Cargar.fecha_final = self.Combo_fecha_fin.get() + "/" + self.Combo_mes_fin.get() + "/" + self.Combo_año_fin.get()
                           Cargar.marca = self.Combo_marca.get()
                           Cargar.xdia = self.Valorxdia.get()
                           Cargar.guardar_archivo(Cargar)
                           messagebox.showinfo("Actualizacion Completada", "Los datos fueron actualizados")
                           self.ventana_administracion
                           self.agregar_promociones()
                        elif(self.mes_a_numero(self.Combo_mes.get()) < self.mes_a_numero(self.Combo_mes_fin.get())) and(self.Combo_año.get()== self.Combo_año_fin.get()):
                            Cargar.fecha_inicio = self.Combo_fecha.get() + "/" + self.Combo_mes.get() + "/" + self.Combo_año.get()
                            Cargar.fecha_final = self.Combo_fecha_fin.get() + "/" + self.Combo_mes_fin.get() + "/" + self.Combo_año_fin.get()
                            Cargar.marca = self.Combo_marca.get()
                            Cargar.xdia = self.Valorxdia.get()
                            Cargar.guardar_archivo(Cargar)
                            messagebox.showinfo("Actualizacion Completada", "Los datos fueron actualizados")
                            self.ventana_administracion
                            self.agregar_promociones()

                        elif(self.mes_a_numero(self.Combo_mes.get()) == self.mes_a_numero(self.Combo_mes_fin.get())) and (self.Combo_fecha.get() <= self.Combo_fecha_fin.get() ):
                            Cargar.fecha_inicio = self.Combo_fecha.get() + "/" + self.Combo_mes.get() + "/" + self.Combo_año.get()
                            Cargar.fecha_final = self.Combo_fecha_fin.get() + "/" + self.Combo_mes_fin.get() + "/" + self.Combo_año_fin.get()
                            Cargar.marca = self.Combo_marca.get()
                            Cargar.xdia = self.Valorxdia.get()
                            Cargar.guardar_archivo(Cargar)
                            messagebox.showinfo("Actualizacion Completada", "Los datos fueron actualizados")
                            self.ventana_administracion
                            self.agregar_promociones()
                        else:
                            messagebox.showinfo("Error de actualizacion", "La fecha de fin no puede ser mayor que la fecha de inicio")

                    else:
                        messagebox.showinfo("Error de ingreso", "La oferta ya esta ingresada")



            else:
                    messagebox.showinfo("Error de ingreso", "El valor debe de ser numerico")

        else:
            messagebox.showinfo("Error de ingreso", "Todos los datos deben de ser ingresados")

    # Esta funcion sirve para visualizar la lista de promociones realizadas de la clase promociones
    def ver_promociones(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("400x550")
        Label(self.ventana_administracion, text="Lista de promociones realizadas", justify="center", width=22, height=4,
              bg="steelblue").grid(row=0, column=0, columnspan=3, ipadx=185)
        botton2 = Button(self.ventana_administracion, image= self.imagen, text="Salir", justify="left", height=60,
                         command=self.salir).grid(row=0, column=3, columnspan=1, ipadx=30)
        botton2

        # dezpla= tk.Canvas(self.ventana_administracion, bg="blue", height=380, width= 600)
        # dezpla.pack()

        Promociones = promociones
        lista_promociones = Promociones.cargar_archivo(Promociones)
        height = len(lista_promociones)
        width = 4
        b = Entry(self.ventana_administracion, width=30, text="")
        b.insert(0, "Marca del vehiculo en promocion")
        b.grid(row=2, column=2)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=30, text="")
        b.insert(0, "Fecha de inicio de la promocion")
        b.grid(row=2, column=0)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=30, text="")
        b.insert(0, "Fecha final de la promocion")
        b.grid(row=2, column=1)
        b.config(state='readonly')
        b = Entry(self.ventana_administracion, width=30, text="")
        b.insert(0, "Valor por dia en la promocion")
        b.grid(row=2, column=3)
        b.config(state='readonly')

        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = Entry(self.ventana_administracion, width=30, text="")
                b.insert(0, lista_promociones[i][j])
                b.grid(row=(i + 3), column=j)
                b.config(state='readonly')

        self.ventana_administracion.geometry("710" + "x" + str(((len(lista_promociones) + 2) * 20) + 90))
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(24, self.usuario.get())
        self.nombre.config(state=tk.DISABLED)
        self.nombre.place_configure(x=0, y=(((len(lista_promociones) + 2) * 20) + 70), width=710, height=20)

    # Esta funcion sirve para agregar el alquiler a la lista alquiler vehiculo
    def agregar_alquiler(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("%dx%d+%d+%d" % ((500, 570) + (483.0, 284.0)))
        self.ano = datetime.date.today().year
        self.mes = datetime.date.today().month

        self.label = tk.Label(self.ventana_administracion, text="Seleccione la fecha inicio de la oferta(año/mes/dia)",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=70, width=270, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Ingrese los datos requeridos para el alquiler\n del vehiculo",
                              justify=tk.CENTER, bg='white')
        self.label.place_configure(x=10, y=10, width=270, height=50)

        self.label = tk.Label(self.ventana_administracion, text="Seleccione la fecha fin de la oferta (año/mes/dia)",
                              bg='white',
                              justify=tk.LEFT)
        self.label.place_configure(x=10, y=130, width=270, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Seleccione la placa del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=195, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Marca del vehiculo seleccionado",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=225, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Modelo del vehiculo seleccionado",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=255, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Cantidad de pasajeros",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=285, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Seleccione la cedula del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=315, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Nombre del cliente seleccionado",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=345, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Profesion del cliente seleccionado",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=375, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Direccion de la casa de residencia",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=405, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Lugar de trabajo del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=435, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Numero de alquiler",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=465, width=180, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Ingrese el valor por dia",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=290, y=315, width=200, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Ingrese el numero de tarjeta",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=290, y=375, width=200, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Fecha de vencimiento(MM/AAAA)",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=290, y=435, width=200, height=20)


        self.label = tk.Label(self.ventana_administracion, text="TOTAL FACTURA",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=0, y=490, width=500, height=20)

        self.Valorxdia = StringVar()
        self.valorxdia = Entry(self.ventana_administracion,bd=3, textvariable=self.Valorxdia, bg="white")
        self.valorxdia.place_configure(x=290, y=345, width=200, height=20)
        self.valorxdia.insert(0,0)
        self.valorxdia.config(state= 'readonly')

        self.Tarjeta = StringVar()
        self.targeta = Entry(self.ventana_administracion, bd=3, textvariable=self.Tarjeta, bg="white")
        self.targeta.place_configure(x=290, y=405, width=200, height=20)


        self.Marca = StringVar()
        self.marca = Entry(self.ventana_administracion, bd=3, textvariable=self.Marca, bg="white")
        self.marca.place_configure(x=210, y=225, width=70, height=20)

        self.Modelo = StringVar()
        self.modelo = Entry(self.ventana_administracion, bd=3, textvariable=self.Modelo, bg="white")
        self.modelo.place_configure(x=210, y=255, width=70, height=20)

        self.Nombre_cliente = StringVar()
        self.nombre_cliente = Entry(self.ventana_administracion, bd=3, textvariable=self.Nombre_cliente, bg="white")
        self.nombre_cliente.place_configure(x=210, y=345, width=70, height=20)

        self.Profesion = StringVar()
        self.profesion = Entry(self.ventana_administracion, bd=3, textvariable=self.Profesion, bg="white")
        self.profesion.place_configure(x=210, y=375, width=70, height=20)

        self.Direccion_casa = StringVar()
        self.direccion_casa = Entry(self.ventana_administracion,bd=3, textvariable=self.Direccion_casa, bg="white")
        self.direccion_casa.place_configure(x=210, y=405, width=70, height=20)

        self.Lugar_trabajo = StringVar()
        self.lugar_trabajo = Entry(self.ventana_administracion, bd=3, textvariable=self.Lugar_trabajo, bg="white")
        self.lugar_trabajo.place_configure(x=210, y=435, width=70, height=20)

        self.Cantidad_pasajeros = StringVar()
        self.cantidad_pasajeros = Entry(self.ventana_administracion, bd=3, textvariable=self.Cantidad_pasajeros, bg="white")
        self.cantidad_pasajeros.place_configure(x=210, y=285, width=70, height=20)

        self.Numero_alquiler= StringVar()
        self.numero_alquiler= Entry(self.ventana_administracion, bd=3, textvariable= self.Numero_alquiler, bg='white')
        self.numero_alquiler.place_configure(x=210, y=465, width=70, height=20)


        self.Monto_fac= StringVar()
        self.monto_fac= Entry(self.ventana_administracion, bd=3, font=('courier', 26, 'bold'), textvariable= self.Monto_fac, bg='yellow', justify="center")
        self.monto_fac.place_configure(x=125, y=515, width=250, height=30)

        #self.monto_fac.insert(0, "Bola")
        #self.monto_fac.config(state='readonly')

        self.label1 = tk.Label(self.ventana_administracion, text="", font=('courier', 10, 'bold'), bd=3, bg='white',
                               justify=tk.LEFT)

        self.label1.place_configure(x=290, y=70, width=200, height=205)
        self.anterior = tk.Button(self.ventana_administracion, text="Anterior", bg='white', command=self.mesAnterior)
        self.anterior.place_configure(x=290, y=285, width=50, height=20)

        self.siguiente = tk.Button(self.ventana_administracion, text="Siguiente", bg='white', command=self.mesSiguiente)
        self.siguiente.place_configure(x=435, y=285, width=55, height=20)

        botton1 = Button(self.ventana_administracion, image= self.image, text="Guardar",
                         command=self.guardar_alquiler_preparado).place_configure(x=370, y=10, width=50, height=50)
        botton1

        botton2 = Button(self.ventana_administracion, image= self.imagen, text="Salir", command=self.salir).place_configure(
            x=440, y=10, width=50, height=50)
        botton2

       # botton3 = Button(self.ventana_administracion, text="Buscar", bg="green", command=self.buscar_en_alquiler).place_configure(
        #    x=290, y=0, width=50, height=50)
        #botton3

        self.Combo_año = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_mes = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_fecha = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_año.place_configure(x=10, y=100, width=70, height=20)
        self.Combo_mes.place_configure(x=110, y=100, width=70, height=20)
        self.Combo_fecha.place_configure(x=210, y=100, width=70, height=20)

        self.Combo_año_fin = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_mes_fin = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_fecha_fin = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_año_fin.place_configure(x=10, y=160, width=70, height=20)
        self.Combo_mes_fin.place_configure(x=110, y=160, width=70, height=20)
        self.Combo_fecha_fin.place_configure(x=210, y=160, width=70, height=20)

        self.Combo_marca = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_marca.place_configure(x=210, y=195, width=70, height=20)

        self.Combo_cliente = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_cliente.place_configure(x=210, y=315, width=70, height=20)

        self.Combo_vencimiento_mes= ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_vencimiento_mes.place_configure(x=290, y=465, width=89, height=20)
        self.Combo_vencimiento_mes['values']= (1,2,3,4,5,6,7,8,9,10,11,12)

        self.Combo_vencimiento_año = ttk.Combobox(self.ventana_administracion, state='readonly')
        self.Combo_vencimiento_año.place_configure(x=400, y=465, width=89, height=20)



        self.nombre.destroy()
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.place_configure(x=0, y=550, width=500, height=20)
        self.nombre.config(state=tk.DISABLED)

        cargar_archivo1 = vehiculo
        self.lista = []
        self.lista = cargar_archivo1.devuelve_lista(cargar_archivo1)
        self.lista2 = []
        contador = 0

        while (contador < len(self.lista)):
            if (self.lista[contador][6] == "NO") or (self.lista[contador][6] == "no"):
                self.lista2.append(self.lista[contador][0])
            contador = contador + 1

        self.Combo_marca['values']= self.lista2
        self.Combo_marca.bind("<<ComboboxSelected>>", self.buscar_en_alquiler)



        cargar = cliente
        lista = cargar.cargar_archivo(cargar)
        listaaux = []
        contador = 0
        while contador < len(lista):
            listaaux.append(lista[contador][0])
            contador = contador + 1

        self.Combo_cliente['values'] = listaaux
        if(self.tipo_usuario=="CLIENTE"):
            self.Combo_cliente['values']= self.id_usuario
        self.Combo_cliente.bind("<<ComboboxSelected>>", self.buscar_en_alquiler)


        self.writeCalendar(self.ano, self.mes)
        año_aux = int(self.año_seleccion)
        lista_aux = []
        año_aux = año_aux - 20
        contador_aux = 0
        while (contador_aux < 100):
            lista_aux.append(año_aux)
            año_aux = año_aux + 1
            contador_aux = contador_aux + 1

        self.Combo_vencimiento_año['values'] = lista_aux
    # Esta funcion sirve para buscar dentro de la clase alquiler vehiculo
    def buscar_en_alquiler(self, event):
        if(self.Combo_marca.get()!="") and (self.Combo_año.get() != "") and (self.Combo_mes.get() != "") and (self.Combo_fecha.get() != "") and (
            self.Combo_año_fin.get() != "") and (self.Combo_mes_fin.get() != "") and (self.Combo_fecha_fin != ""
            ) and int(self.cantidad_dias_alquiler(int(self.Combo_fecha.get()), self.mes_a_numero(self.Combo_mes.get()),
                                                int(self.Combo_año.get()), int(self.Combo_fecha_fin.get()),
                                                self.mes_a_numero(self.Combo_mes_fin.get()),
                                                int(self.Combo_año_fin.get()))) >0 :
            self.marca.config(state='normal')
            self.modelo.config(state='normal')
            self.cantidad_pasajeros.config(state='normal')
            self.valorxdia.config(state='normal')
            self.monto_fac.config(state='normal')
            self.marca.delete(0, tk.END)
            self.modelo.delete(0, tk.END)
            self.cantidad_pasajeros.delete(0, tk.END)
            self.valorxdia.delete(0, tk.END)
            self.monto_fac.delete(0, tk.END)
            #print(self.cantidad_dias_alquiler(int(self.Combo_fecha.get()),self.mes_a_numero(self.Combo_mes.get()),int(self.Combo_año.get()), int(self.Combo_fecha_fin.get()), self.mes_a_numero(self.Combo_mes_fin.get()), int(self.Combo_año_fin.get())))

            cargar2= vehiculo
            lista_vehiculo = cargar2.busca_vehiculo(cargar2, int(self.Combo_marca.get()))
            self.lista_vehiculo_global= lista_vehiculo

            self.marca.insert(0, lista_vehiculo[2])
            self.marca.config(state= 'readonly')
            self.modelo.insert(0, lista_vehiculo[1])
            self.modelo.config(state= 'readonly')
            self.cantidad_pasajeros.insert(0, lista_vehiculo[3])
            self.cantidad_pasajeros.config(state= 'readonly')
            self.valorxdia.insert(0, lista_vehiculo[5])
            self.valorxdia.config(state= 'readonly')
            self.Monto_fac.set(
                int(self.cantidad_dias_alquiler(int(self.Combo_fecha.get()), self.mes_a_numero(self.Combo_mes.get()),
                                                int(self.Combo_año.get()), int(self.Combo_fecha_fin.get()),
                                                self.mes_a_numero(self.Combo_mes_fin.get()),
                                                int(self.Combo_año_fin.get()))) * int(self.Valorxdia.get()))
            self.monto_fac.config(state= 'readonly')
            self.Combo_fecha.config(state= 'disable')
            self.Combo_mes.config(state='disable')
            self.Combo_año.config(state='disable')
            self.Combo_fecha_fin.config(state='disable')
            self.Combo_mes_fin.config(state= 'disable')
            self.Combo_año_fin.config(state= 'disable')
        if(self.Combo_cliente.get()!="") :
            self.nombre_cliente.config(state='normal')
            self.profesion.config(state='normal')
            self.direccion_casa.config(state='normal')
            self.lugar_trabajo.config(state='normal')
            self.numero_alquiler.config(state='normal')
            self.monto_fac.config(state='normal')
            self.nombre_cliente.delete(0, tk.END)
            self.profesion.delete(0, tk.END)
            self.direccion_casa.delete(0, tk.END)
            self.lugar_trabajo.delete(0, tk.END)
            self.numero_alquiler.delete(0, tk.END)
            self.monto_fac.delete(0, tk.END)

            cargar = cliente
            lista_cliente = cargar.buscar_cliente(cargar, int(self.Combo_cliente.get()))
            self.lista_cliente_global = lista_cliente

            cargar3 = alquiler_vehiculo
            lista_alquiler_vehiculo = cargar3.cargar_archivo(cargar3)

            self.nombre_cliente.insert(0, lista_cliente[1])
            self.nombre_cliente.config(state='readonly')
            self.profesion.insert(0, lista_cliente[2])
            self.profesion.config(state='readonly')
            self.direccion_casa.insert(0, lista_cliente[4])
            self.direccion_casa.config(state='readonly')
            self.lugar_trabajo.insert(0, lista_cliente[5])
            self.lugar_trabajo.config(state='readonly')
            self.numero_alquiler.insert(0, (len(lista_alquiler_vehiculo) + 1))
            self.numero_alquiler.config(state='readonly')
            if(self.Combo_marca.get()!="") and (self.Combo_año.get() != "") and (self.Combo_mes.get() != "") and (self.Combo_fecha.get() != "") and (
            self.Combo_año_fin.get() != "") and (self.Combo_mes_fin.get() != "") and (self.Combo_fecha_fin != ""
            ) and int(self.cantidad_dias_alquiler(int(self.Combo_fecha.get()), self.mes_a_numero(self.Combo_mes.get()),
                                                int(self.Combo_año.get()), int(self.Combo_fecha_fin.get()),
                                                self.mes_a_numero(self.Combo_mes_fin.get()),
                                                int(self.Combo_año_fin.get()))) >0:
                self.Monto_fac.set(
                    int(self.cantidad_dias_alquiler(int(self.Combo_fecha.get()),
                                                    self.mes_a_numero(self.Combo_mes.get()),
                                                    int(self.Combo_año.get()), int(self.Combo_fecha_fin.get()),
                                                    self.mes_a_numero(self.Combo_mes_fin.get()),
                                                    int(self.Combo_año_fin.get()))) * int(self.Valorxdia.get()))
            self.monto_fac.config(state= 'readonly')
            #self.Monto_fac.set(int(self.cantidad_dias_alquiler(int(self.Combo_fecha.get()), self.mes_a_numero(self.Combo_mes.get()),
             #                           int(self.Combo_año.get()), int(self.Combo_fecha_fin.get()),
              #                          self.mes_a_numero(self.Combo_mes_fin.get()), int(self.Combo_año_fin.get()))) * int(self.Valorxdia.get()))
        if(self.Combo_cliente.get()!= "") or(self.Combo_marca.get()!=""):
            return

        else:
            messagebox.showinfo("Error de busqueda", "Debe de estar seleccionado el numero de identicacion del cliente y el numero de placa del vehiculo")

    # Esta funcion sirve para guardar el alquiler en la clase alquiler
    def guardar_alquiler_preparado(self):

        self.valorxdia.config(state="normal")
        self.targeta.config(state="normal")
        self.numero_alquiler.config(state="normal")



        if (self.Combo_año.get() != "") and (self.Combo_mes.get() != "") and (self.Combo_fecha.get() != "") and (
            self.Combo_año_fin.get() != "") and (self.Combo_mes_fin.get() != "") and (self.Combo_fecha_fin != ""
            ) and (self.Combo_marca.get() != "") and(self.Combo_cliente.get()!="") and (self.Valorxdia.get() != ""
            ) and (self.Tarjeta.get()!= "") and(self.Combo_vencimiento_mes.get()!="") and(self.Combo_vencimiento_año.get()!=""
            )and(self.Numero_alquiler.get()!=""):
            monto = True
            try:
                int(self.Valorxdia.get())
            except:
                monto = False

            card= True

            try:
                int(self.Tarjeta.get())
            except:
                card = False


            if (monto and card):
                Cargar = alquiler_vehiculo
                Vehiculo= vehiculo


                if (self.Combo_año_fin.get() > self.Combo_año.get()):
                        Cargar.factura= int(self.Numero_alquiler.get())
                        Cargar.cliente_alquila= self.lista_cliente_global
                        Cargar.vehiculo_alquilado= Vehiculo.vehiculo_alquilado(Vehiculo, int(self.Combo_marca.get()))
                        contador= 0
                        fecha_i =int(self.Combo_fecha.get())
                        largo_mes= len(self.Combo_fecha.get())
                        while(fecha_i <= largo_mes):
                              contador= contador +1;
                              fecha_i= fecha_i + 1

                        Cargar.fecha_salida = self.Combo_fecha.get() + "/" + self.Combo_mes.get() + "/" + self.Combo_año.get()
                        Cargar.fecha_de_regreso = self.Combo_fecha_fin.get() + "/" + self.Combo_mes_fin.get() + "/" + self.Combo_año_fin.get()
                        Cargar.valor_por_dia = self.Valorxdia.get()
                        Cargar.n_card_credit= self.Tarjeta.get()
                        Cargar.vencimiento= str(self.Combo_vencimiento_mes.get()+"/"+self.Combo_vencimiento_año.get())
                        Cargar.estado="Preparado"
                        Cargar.monto_factura= int(self.Monto_fac.get())
                        Cargar.guardar_archivo(Cargar)
                        Cargar.cargar_archivo(Cargar)
                        messagebox.showinfo("Alquiler preparado", "El numero de orden para para aplicar el alquiler es el " + self.Numero_alquiler.get())
                        self.ventana_administracion
                        self.agregar_alquiler()
                elif (self.mes_a_numero(self.Combo_mes.get()) < self.mes_a_numero(self.Combo_mes_fin.get())) and (
                            self.Combo_año.get() == self.Combo_año_fin.get()):
                        Cargar.factura = int(self.Numero_alquiler.get())
                        Cargar.cliente_alquila = self.lista_cliente_global
                        Cargar.vehiculo_alquilado = Vehiculo.vehiculo_alquilado(Vehiculo, int(self.Combo_marca.get()))
                        Cargar.fecha_salida = self.Combo_fecha.get() + "/" + self.Combo_mes.get() + "/" + self.Combo_año.get()
                        Cargar.fecha_de_regreso = self.Combo_fecha_fin.get() + "/" + self.Combo_mes_fin.get() + "/" + self.Combo_año_fin.get()
                        Cargar.valor_por_dia = self.Valorxdia.get()
                        Cargar.n_card_credit = self.Tarjeta.get()
                        Cargar.vencimiento = str(self.Combo_vencimiento_mes.get() + "/" + self.Combo_vencimiento_año.get())
                        Cargar.estado = "Preparado"
                        Cargar.guardar_archivo(Cargar)
                        Cargar.cargar_archivo(Cargar)
                        messagebox.showinfo("Alquiler preparado","El numero de orden para para aplicar el alquiler es el " + self.Numero_alquiler.get())
                        self.ventana_administracion
                        self.agregar_alquiler()

                elif (self.mes_a_numero(self.Combo_mes.get()) == self.mes_a_numero(self.Combo_mes_fin.get())) and (
                            int(self.Combo_fecha.get()) <= int(self.Combo_fecha_fin.get())):
                        Cargar.factura = int(self.Numero_alquiler.get())
                        Cargar.cliente_alquila = self.lista_cliente_global
                        Cargar.vehiculo_alquilado = Vehiculo.vehiculo_alquilado(Vehiculo, int(self.Combo_marca.get()))
                        Cargar.fecha_salida = self.Combo_fecha.get() + "/" + self.Combo_mes.get() + "/" + self.Combo_año.get()
                        Cargar.fecha_de_regreso = self.Combo_fecha_fin.get() + "/" + self.Combo_mes_fin.get() + "/" + self.Combo_año_fin.get()
                        Cargar.valor_por_dia = self.Valorxdia.get()
                        Cargar.n_card_credit = self.Tarjeta.get()
                        Cargar.vencimiento = str(self.Combo_vencimiento_mes.get() + "/" + self.Combo_vencimiento_año.get())
                        Cargar.estado = "Preparado"
                        Cargar.monto_factura= int(self.Monto_fac.get())
                        Cargar.guardar_archivo(Cargar)
                        Cargar.cargar_archivo(Cargar)
                        messagebox.showinfo("Alquiler preparado","El numero de orden para para aplicar el alquiler es el " + self.Numero_alquiler.get())
                        self.ventana_administracion
                        self.agregar_alquiler()
                else:
                        messagebox.showinfo("Error al preparar alquiler",
                                            "La fecha de fin no puede ser mayor que la fecha de inicio")



            else:
                messagebox.showinfo("Error al preparar alquiler", "Los valores de valor por dia y el numero de targeta deben de ser numericos")

        else:
            messagebox.showinfo("Error al preparar alquiler", "Todos los datos deben de ser ingresados")

    #Esta funcion sirve para aplicar el alquier
    # Con su respectivos modulos , orden y valor
    def aplicar_alquiler(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("%dx%d+%d+%d" % ((600, 340) + (483.0, 284.0)))
        self.ventana_administracion.geometry("%dx%d+%d+%d" % ((600, 420) + (483.0, 284.0)))
        self.label = tk.Label(self.ventana_administracion, text="TOTAL FACTURA",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=0, y=320, width=600, height=20)
        self.Monto_fac = StringVar()
        self.monto_fac = Entry(self.ventana_administracion, bd=3, font=('courier', 30, 'bold'),
                               textvariable=self.Monto_fac, bg='yellow', justify="center")
        self.monto_fac.place_configure(x=175, y=350, width=250, height=40)
        self.label = tk.Label(self.ventana_administracion,
                              text="Bienvenido  al modulo aplicacion del alquiler, seleccionar la orden\n y luego dar click sobre el check para aplicarla, para salir dar click en la puerta  ",
                              justify=tk.CENTER, bg='white')
        self.label.place_configure(x=10, y=10, width=450, height=50)


        botton1 = Button(self.ventana_administracion, image= self.image, text="Guardar",
                         command=self.guardar_alquiler_activo).place_configure(x=480, y=10, width=50, height=50)
        botton1

        botton2 = Button(self.ventana_administracion, image= self.imagen, text="Salir", command=self.salir).place_configure(
            x=540, y=10, width=50, height=50)
        botton2

        self.label = tk.Label(self.ventana_administracion, text="Seleccione la de orden para aplicar",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=70, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Placa del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=70, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Numero de factura",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=100, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Marca del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=100, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Cedula del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=130, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Modelo del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=130, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Nombre del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=160, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Color del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=160, width=170, height=20)


        self.label = tk.Label(self.ventana_administracion, text="Profesion del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=190, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Cantidad de pasageros",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=190, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Direccion de casa",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=220, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Fecha del alquiler",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=220, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Lugar de trabajo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=250, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Fecha para devolucion",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=250, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Valor por dia",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=285, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Numero de targeta",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=285, width=190, height=20)



        self.Combo_numero_orden = ttk.Combobox(self.ventana_administracion, state='readonly',)
        self.Combo_numero_orden.place_configure(x=210, y=70, width=90, height=20)

        self.Numero_placa = StringVar()
        self.numero_placa = Entry(self.ventana_administracion, bd=3, textvariable=self.Numero_placa, bg="white")
        self.numero_placa.place_configure(x=490, y=70, width=100, height=20)

        self.Marca = StringVar()
        self.marca = Entry(self.ventana_administracion,bd=3, textvariable=self.Marca, bg="white")
        self.marca.place_configure(x=490, y=100, width=100, height=20)

        self.Modelo = StringVar()
        self.modelo = Entry(self.ventana_administracion, bd=3, textvariable=self.Modelo, bg="white")
        self.modelo.place_configure(x=490, y=130, width=100, height=20)

        self.Color = StringVar()
        self.color = Entry(self.ventana_administracion, bd=3, textvariable=self.Color, bg="white")
        self.color.place_configure(x=490, y=160, width=100, height=20)

        self.Cantidad_pasajeros = StringVar()
        self.cantidad_pasajeros = Entry(self.ventana_administracion,bd=3, textvariable=self.Cantidad_pasajeros, bg="white")
        self.cantidad_pasajeros.place_configure(x=490, y=190, width=100, height=20)

        self.Fecha = StringVar()
        self.fecha = Entry(self.ventana_administracion, bd=3, textvariable=self.Fecha, bg="white")
        self.fecha.place_configure(x=490, y=220, width=100, height=20)

        self.Fecha_fin = StringVar()
        self.fecha_fin = Entry(self.ventana_administracion, bd=3, textvariable=self.Fecha_fin, bg="white")
        self.fecha_fin.place_configure(x=490, y=250, width=100, height=20)

        self.Valorxdia = StringVar()
        self.valorxdia = Entry(self.ventana_administracion, bd=3, textvariable=self.Valorxdia, bg="white")
        self.valorxdia.place_configure(x=490, y=285, width=100, height=20)

        self.Numero_factura = StringVar()
        self.numero_factura = Entry(self.ventana_administracion, bd=3, textvariable=self.Numero_factura, bg="white")
        self.numero_factura.place_configure(x=210, y=100, width=90, height=20)

        self.Cedula_cliente = StringVar()
        self.cedula_cliente = Entry(self.ventana_administracion,bd=3, textvariable=self.Cedula_cliente, bg="white")
        self.cedula_cliente.place_configure(x=210, y=130, width=90, height=20)

        self.Nombre_cliente = StringVar()
        self.nombre_cliente = Entry(self.ventana_administracion, bd=3, textvariable=self.Nombre_cliente, bg="white")
        self.nombre_cliente.place_configure(x=210, y=160, width=90, height=20)

        self.Profesion = StringVar()
        self.profesion = Entry(self.ventana_administracion, bd=3, textvariable=self.Profesion, bg="white")
        self.profesion.place_configure(x=210, y=190, width=90, height=20)

        self.Direccion_casa = StringVar()
        self.direccion_casa = Entry(self.ventana_administracion, bd=3, textvariable=self.Direccion_casa, bg="white")
        self.direccion_casa.place_configure(x=210, y=220, width=90, height=20)

        self.Lugar_trabajo = StringVar()
        self.lugar_trabajo = Entry(self.ventana_administracion, bd=3, textvariable=self.Lugar_trabajo, bg="white")
        self.lugar_trabajo.place_configure(x=210, y=250, width=90, height=20)

        self.Tarjeta = StringVar()
        self.targeta = Entry(self.ventana_administracion, bd=3, textvariable=self.Tarjeta, bg="white")
        self.targeta.place_configure(x=210, y=285, width=90, height=20)


        Cargar= alquiler_vehiculo
        self.lista_alquiler_vehiculo=Cargar.cargar_archivo(Cargar)
        lista_aux=[]
        contador=0
        while(contador < len(self.lista_alquiler_vehiculo)):

            if(self.lista_alquiler_vehiculo[contador][8]== 'Preparado'):
               lista_aux.append(self.lista_alquiler_vehiculo[contador][0])
            contador= contador +1
        self.Combo_numero_orden['values']= lista_aux

        #self.Combo_numero_orden.bind("<<ComboboxSelected>>", self.callbackFunc)
        self.Combo_numero_orden.bind("<<ComboboxSelected>>", self.mostrar_datos_orden)
        self.nombre.destroy()
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.place_configure(x=0, y=400, width=600, height=20)
        self.nombre.config(state=tk.DISABLED)

     # Esta funcion carga los datos de alquiler vehiculo
    def mostrar_datos_orden(self, event):
        self.numero_factura.config(state='normal')
        self.cedula_cliente.config(state='normal')
        self.nombre_cliente.config(state='normal')
        self.profesion.config(state='normal')
        self.direccion_casa.config(state='normal')
        self.lugar_trabajo.config(state='normal')

        self.numero_placa.config(state='normal')
        self.marca.config(state='normal')
        self.modelo.config(state='normal')
        self.color.config(state='normal')
        self.cantidad_pasajeros.config(state='normal')

        self.fecha.config(state='normal')
        self.fecha_fin.config(state='normal')
        self.targeta.config(state='normal')
        self.valorxdia.config(state='normal')
        self.monto_fac.config(state='normal')

        self.numero_factura.delete(0, END)
        self.cedula_cliente.delete(0, END)
        self.nombre_cliente.delete(0, END)
        self.profesion.delete(0, END)
        self.direccion_casa.delete(0, END)
        self.lugar_trabajo.delete(0, END)

        self.numero_placa.delete(0, END)
        self.marca.delete(0, END)
        self.modelo.delete(0, END)
        self.color.delete(0, END)
        self.cantidad_pasajeros.delete(0,END)

        self.fecha.delete(0, END)
        self.fecha_fin.delete(0, END)

        self.targeta.delete(0,END)
        self.valorxdia.delete(0, END)
        self.monto_fac.delete(0, END)

        lista_aux=[]
        contador=0
        x=int
        Cargar = alquiler_vehiculo
        self.lista_alquiler_vehiculo = Cargar.cargar_archivo(Cargar)
        while(contador< len(self.lista_alquiler_vehiculo)):
            if(self.lista_alquiler_vehiculo[contador][0]==int(self.Combo_numero_orden.get())):
                lista_aux= self.lista_alquiler_vehiculo[contador]
            contador= contador + 1

        self.numero_factura.insert(0, lista_aux[0])
        self.cedula_cliente.insert(0, lista_aux[1][0])
        self.nombre_cliente.insert(0, lista_aux[1][1])
        self.profesion.insert(0, lista_aux[1][2])
        self.direccion_casa.insert(0, lista_aux[1][4])
        self.lugar_trabajo.insert(0, lista_aux[1][5])

        self.numero_placa.insert(0,lista_aux[2][0])
        self.marca.insert(0, lista_aux[2][1])
        self.modelo.insert(0, lista_aux[2][2])
        self.color.insert(0, lista_aux[2][3])
        self.cantidad_pasajeros.insert(0, lista_aux[2][4])

        self.fecha.insert(0, lista_aux[3])
        self.fecha_fin.insert(0, lista_aux[4])
        self.targeta.insert(0, lista_aux[6])
        self.valorxdia.insert(0, lista_aux[5])
        self.monto_fac.insert(0, lista_aux[9])

        self.numero_factura.config(state= 'readonly')
        self.cedula_cliente.config(state= 'readonly')
        self.nombre_cliente.config(state= 'readonly')
        self.profesion.config(state= 'readonly')
        self.direccion_casa.config(state= 'readonly')
        self.lugar_trabajo.config(state= 'readonly')

        self.numero_placa.config(state= 'readonly')
        self.marca.config(state= 'readonly')
        self.modelo.config(state= 'readonly')
        self.color.config(state= 'readonly')
        self.cantidad_pasajeros.config(state= 'readonly')

        self.fecha.config(state= 'readonly')
        self.fecha_fin.config(state= 'readonly')
        self.targeta.config(state= 'readonly')
        self.monto_fac.config(state= 'readonly')
        self.valorxdia.config(state= 'readonly')
        self.lista_alquiler_vehiculo= lista_aux

        Cargar = alquiler_vehiculo
        self.lista_alquiler_vehiculo = Cargar.cargar_archivo(Cargar)
        lista_aux2 = []
        contador = 0
        while (contador < len(self.lista_alquiler_vehiculo)):

            if (self.lista_alquiler_vehiculo[contador][8] == 'Preparado'):
                lista_aux2.append(self.lista_alquiler_vehiculo[contador][0])
            contador = contador + 1
        self.Combo_numero_orden['values'] = lista_aux2
        self.lista_alquiler_vehiculo= lista_aux

    # Esta funcion carga los datos de devolucion de la clase alquier vehiculo
    def mostrar_datos_devolucion(self, event):
        self.numero_factura.config(state='normal')
        self.cedula_cliente.config(state='normal')
        self.nombre_cliente.config(state='normal')
        self.profesion.config(state='normal')
        self.direccion_casa.config(state='normal')
        self.lugar_trabajo.config(state='normal')

        self.numero_placa.config(state='normal')
        self.marca.config(state='normal')
        self.modelo.config(state='normal')
        self.color.config(state='normal')
        self.cantidad_pasajeros.config(state='normal')

        self.fecha.config(state='normal')
        self.fecha_fin.config(state='normal')
        self.targeta.config(state='normal')
        self.valorxdia.config(state='normal')

        self.numero_factura.delete(0, END)
        self.cedula_cliente.delete(0, END)
        self.nombre_cliente.delete(0, END)
        self.profesion.delete(0, END)
        self.direccion_casa.delete(0, END)
        self.lugar_trabajo.delete(0, END)

        self.numero_placa.delete(0, END)
        self.marca.delete(0, END)
        self.modelo.delete(0, END)
        self.color.delete(0, END)
        self.cantidad_pasajeros.delete(0,END)

        self.fecha.delete(0, END)
        self.fecha_fin.delete(0, END)

        self.targeta.delete(0,END)
        self.valorxdia.delete(0, END)


        lista_aux=[]
        contador=0
        x=int
        Cargar = alquiler_vehiculo
        self.lista_alquiler_vehiculo = Cargar.cargar_archivo(Cargar)
        while(contador< len(self.lista_alquiler_vehiculo)):
            if(self.lista_alquiler_vehiculo[contador][0]==int(self.Combo_numero_orden.get())):
                lista_aux= self.lista_alquiler_vehiculo[contador]
            contador= contador + 1

        self.numero_factura.insert(0, lista_aux[0])
        self.cedula_cliente.insert(0, lista_aux[1][0])
        self.nombre_cliente.insert(0, lista_aux[1][1])
        self.profesion.insert(0, lista_aux[1][2])
        self.direccion_casa.insert(0, lista_aux[1][4])
        self.lugar_trabajo.insert(0, lista_aux[1][5])

        self.numero_placa.insert(0,lista_aux[2][0])
        self.marca.insert(0, lista_aux[2][1])
        self.modelo.insert(0, lista_aux[2][2])
        self.color.insert(0, lista_aux[2][3])
        self.cantidad_pasajeros.insert(0, lista_aux[2][4])

        self.fecha.insert(0, lista_aux[3])
        self.fecha_fin.insert(0, lista_aux[4])
        self.targeta.insert(0, lista_aux[6])
        self.valorxdia.insert(0, lista_aux[5])

        self.numero_factura.config(state= 'readonly')
        self.cedula_cliente.config(state= 'readonly')
        self.nombre_cliente.config(state= 'readonly')
        self.profesion.config(state= 'readonly')
        self.direccion_casa.config(state= 'readonly')
        self.lugar_trabajo.config(state= 'readonly')

        self.numero_placa.config(state= 'readonly')
        self.marca.config(state= 'readonly')
        self.modelo.config(state= 'readonly')
        self.color.config(state= 'readonly')
        self.cantidad_pasajeros.config(state= 'readonly')

        self.fecha.config(state= 'readonly')
        self.fecha_fin.config(state= 'readonly')
        self.targeta.config(state= 'readonly')
        self.valorxdia.config(state= 'readonly')
        self.lista_alquiler_vehiculo= lista_aux

        Cargar = alquiler_vehiculo
        self.lista_alquiler_vehiculo = Cargar.cargar_archivo(Cargar)
        lista_aux2 = []
        contador = 0
        while (contador < len(self.lista_alquiler_vehiculo)):

            if (self.lista_alquiler_vehiculo[contador][8] == 'Activo'):
                lista_aux2.append(self.lista_alquiler_vehiculo[contador][0])
            contador = contador + 1
        self.Combo_numero_orden['values'] = lista_aux2
        self.lista_alquiler_vehiculo= lista_aux

    # Esta funcion permite guardar los datos de la alquiler vehiculo
    def guardar_alquiler_activo(self):

        monto = True
        try:
            int(self.Valorxdia.get())
        except:
            monto = False


        if(self.Combo_numero_orden.get()!="") and(monto) :
            Cargar= alquiler_vehiculo
            Cargar.modificar(Cargar, self.lista_alquiler_vehiculo[0], self.lista_alquiler_vehiculo[1], self.lista_alquiler_vehiculo[2
            ], self.lista_alquiler_vehiculo[3], self.lista_alquiler_vehiculo[4], self.Valorxdia.get(), self.lista_alquiler_vehiculo[6
            ], self.lista_alquiler_vehiculo[7], "Activo", self.lista_alquiler_vehiculo[9])
            messagebox.showinfo("Proceso completado", "Ya puede retirar el vehiculo su fatura es la numero: " + str(self.lista_alquiler_vehiculo[0]))
            #self.ventana_administracion.destroy()
            self.ventana_administracion
            self.aplicar_alquiler()
        else:
            messagebox.showinfo("Error de seleccion","No ha seleccionado ninguna orden, o el precio por dia no esta ingresado")

    # Esta funcion fue implementada para desabilitar el vehiculo de la clase alquiler
    def desactivar_alquiler(self):


        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')
        self.ventana_administracion.geometry("%dx%d+%d+%d" % ((600, 340) + (483.0, 284.0)))

        self.label = tk.Label(self.ventana_administracion,
                              text="Bienvenido  a su sistema Alcarsa, en el modulo devolucion del alquiler,seleccionar\n la factura y luego dar click sobre el check, para salir dar click sobre la puerta  ",
                              justify=tk.CENTER, bg='white')
        self.label.place_configure(x=10, y=10, width=450, height=50)

        botton1 = Button(self.ventana_administracion, image=self.image, text="Guardar", bg="white",
                         command=self.guardar_alquiler_desactivo).place_configure(x=480, y=10, width=50, height=50)
        botton1

        botton2 = Button(self.ventana_administracion, image= self.imagen, text="Salir", bg="white", command=self.salir).place_configure(
            x=540, y=10, width=50, height=50)
        botton2


        self.label = tk.Label(self.ventana_administracion, text="Seleccione la factura a devolver",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=70, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Placa del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=70, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Numero de factura",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=100, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Marca del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=100, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Cedula del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=130, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Modelo del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=130, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Nombre del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=160, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Color del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=160, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Profesion del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=190, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Cantidad de pasageros",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=190, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Direccion de casa",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=220, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Fecha del alquiler",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=220, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Lugar de trabajo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=250, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Fecha para devolucion",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=250, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Valor por dia",
                              justify=tk.LEFT, bg='yellow')
        self.label.place_configure(x=310, y=285, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Numero de targeta",
                              justify=tk.LEFT, bg='yellow')
        self.label.place_configure(x=10, y=285, width=190, height=20)

        self.Combo_numero_orden = ttk.Combobox(self.ventana_administracion, state='readonly', )
        self.Combo_numero_orden.place_configure(x=210, y=70, width=90, height=20)

        self.Numero_placa = StringVar()
        self.numero_placa = Entry(self.ventana_administracion, bd=3, textvariable=self.Numero_placa, bg="white")
        self.numero_placa.place_configure(x=490, y=70, width=100, height=20)

        self.Marca = StringVar()
        self.marca = Entry(self.ventana_administracion, bd=3, textvariable=self.Marca, bg="white")
        self.marca.place_configure(x=490, y=100, width=100, height=20)

        self.Modelo = StringVar()
        self.modelo = Entry(self.ventana_administracion, bd=3, textvariable=self.Modelo, bg="white")
        self.modelo.place_configure(x=490, y=130, width=100, height=20)

        self.Color = StringVar()
        self.color = Entry(self.ventana_administracion, bd=3, textvariable=self.Color, bg="white")
        self.color.place_configure(x=490, y=160, width=100, height=20)

        self.Cantidad_pasajeros = StringVar()
        self.cantidad_pasajeros = Entry(self.ventana_administracion, bd=3, textvariable=self.Cantidad_pasajeros,
                                        bg="white")
        self.cantidad_pasajeros.place_configure(x=490, y=190, width=100, height=20)

        self.Fecha = StringVar()
        self.fecha = Entry(self.ventana_administracion, bd=3, textvariable=self.Fecha, bg="white")
        self.fecha.place_configure(x=490, y=220, width=100, height=20)

        self.Fecha_fin = StringVar()
        self.fecha_fin = Entry(self.ventana_administracion, bd=3, textvariable=self.Fecha_fin, bg="white")
        self.fecha_fin.place_configure(x=490, y=250, width=100, height=20)

        self.Valorxdia = StringVar()
        self.valorxdia = Entry(self.ventana_administracion, bd=3, textvariable=self.Valorxdia, bg="yellow")
        self.valorxdia.place_configure(x=490, y=285, width=100, height=20)

        self.Numero_factura = StringVar()
        self.numero_factura = Entry(self.ventana_administracion, bd=3, textvariable=self.Numero_factura, bg="white")
        self.numero_factura.place_configure(x=210, y=100, width=90, height=20)

        self.Cedula_cliente = StringVar()
        self.cedula_cliente = Entry(self.ventana_administracion, bd=3, textvariable=self.Cedula_cliente, bg="white")
        self.cedula_cliente.place_configure(x=210, y=130, width=90, height=20)

        self.Nombre_cliente = StringVar()
        self.nombre_cliente = Entry(self.ventana_administracion, bd=3, textvariable=self.Nombre_cliente, bg="white")
        self.nombre_cliente.place_configure(x=210, y=160, width=90, height=20)

        self.Profesion = StringVar()
        self.profesion = Entry(self.ventana_administracion, bd=3, textvariable=self.Profesion, bg="white")
        self.profesion.place_configure(x=210, y=190, width=90, height=20)

        self.Direccion_casa = StringVar()
        self.direccion_casa = Entry(self.ventana_administracion, bd=3, textvariable=self.Direccion_casa, bg="white")
        self.direccion_casa.place_configure(x=210, y=220, width=90, height=20)

        self.Lugar_trabajo = StringVar()
        self.lugar_trabajo = Entry(self.ventana_administracion, bd=3, textvariable=self.Lugar_trabajo, bg="white")
        self.lugar_trabajo.place_configure(x=210, y=250, width=90, height=20)

        self.Tarjeta = StringVar()
        self.targeta = Entry(self.ventana_administracion, bd=3, textvariable=self.Tarjeta, bg="yellow")
        self.targeta.place_configure(x=210, y=285, width=90, height=20)

        Cargar = alquiler_vehiculo
        self.lista_alquiler_vehiculo = Cargar.cargar_archivo(Cargar)
        lista_aux = []
        contador = 0
        while (contador < len(self.lista_alquiler_vehiculo)):

            if (self.lista_alquiler_vehiculo[contador][8] == 'Activo'):
                lista_aux.append(self.lista_alquiler_vehiculo[contador][0])
            contador = contador + 1
        self.Combo_numero_orden['values'] = lista_aux

        # self.Combo_numero_orden.bind("<<ComboboxSelected>>", self.callbackFunc)
        self.Combo_numero_orden.bind("<<ComboboxSelected>>", self.mostrar_datos_devolucion)
        self.nombre.destroy()
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ",  )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.place_configure(x=0, y=320, width=600, height=20)
        self.nombre.config(state=tk.DISABLED)

    # esta funcion permite mostrar el estado de el alquiler
    def mostrar_alquiler(self):
        self.ventana_administracion.configure(background='steelblue')
        self.barramenu.entryconfig(index=1, state='disabled')
        self.barramenu.entryconfig(index=2, state='disabled')
        self.barramenu.entryconfig(index=3, state='disabled')
        self.barramenu.entryconfig(index=4, state='disabled')
        self.barramenu.entryconfig(index=5, state='disabled')
        self.barramenu.entryconfig(index=6, state='disabled')

        self.ventana_administracion.geometry("%dx%d+%d+%d" % ((600, 340) + (483.0, 284.0)))
        self.label = tk.Label(self.ventana_administracion,
                              text="Consulta de alquileres realizados por los clientes, selecionar el numero de cedula\n del cliente para que se despliegue la informacion, para ver \nel siguiente alquiler, precionar el boton siguiente",
                              justify=tk.CENTER, bg='white')
        self.label.place_configure(x=10, y=10, width=450, height=50)

        botton1 = Button(self.ventana_administracion, text="Siguiente", bg="white",
                         command=self.siguiente_alquiler).place_configure(x=480, y=10, width=50, height=50)
        botton1

        botton2 = Button(self.ventana_administracion,image= self.imagen, text="Salir", command=self.salir).place_configure(
            x=540, y=10, width=50, height=50)
        botton2

        self.label = tk.Label(self.ventana_administracion, text="Seleccione la cedula del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=70, width=190, height=20)
        self.label = tk.Label(self.ventana_administracion, text="   Placa del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=70, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Numero de factura",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=100, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Marca del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=100, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Estado del alquiler",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=130, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Modelo del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=130, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Nombre del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=160, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Color del vehiculo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=160, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Profesion del cliente",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=190, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Cantidad de pasageros",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=190, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Direccion de casa",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=220, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Fecha del alquiler",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=220, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Lugar de trabajo",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=10, y=250, width=190, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Fecha para devolucion",
                              justify=tk.LEFT, bg='white')
        self.label.place_configure(x=310, y=250, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Valor por dia",
                              justify=tk.LEFT, bg='yellow')
        self.label.place_configure(x=310, y=285, width=170, height=20)

        self.label = tk.Label(self.ventana_administracion, text="Numero de targeta",
                              justify=tk.LEFT, bg='yellow')
        self.label.place_configure(x=10, y=285, width=190, height=20)

        self.Combo_numero_orden = ttk.Combobox(self.ventana_administracion, state='readonly', )
        self.Combo_numero_orden.place_configure(x=210, y=70, width=90, height=20)

        self.Numero_placa = StringVar()
        self.numero_placa = Entry(self.ventana_administracion, bd=3, textvariable=self.Numero_placa, bg="white")
        self.numero_placa.place_configure(x=490, y=70, width=100, height=20)

        self.Marca = StringVar()
        self.marca = Entry(self.ventana_administracion, bd=3, textvariable=self.Marca, bg="white")
        self.marca.place_configure(x=490, y=100, width=100, height=20)

        self.Modelo = StringVar()
        self.modelo = Entry(self.ventana_administracion, bd=3, textvariable=self.Modelo, bg="white")
        self.modelo.place_configure(x=490, y=130, width=100, height=20)

        self.Color = StringVar()
        self.color = Entry(self.ventana_administracion, bd=3, textvariable=self.Color, bg="white")
        self.color.place_configure(x=490, y=160, width=100, height=20)

        self.Cantidad_pasajeros = StringVar()
        self.cantidad_pasajeros = Entry(self.ventana_administracion, bd=3, textvariable=self.Cantidad_pasajeros,
                                        bg="white")
        self.cantidad_pasajeros.place_configure(x=490, y=190, width=100, height=20)

        self.Fecha = StringVar()
        self.fecha = Entry(self.ventana_administracion, bd=3, textvariable=self.Fecha, bg="white")
        self.fecha.place_configure(x=490, y=220, width=100, height=20)

        self.Fecha_fin = StringVar()
        self.fecha_fin = Entry(self.ventana_administracion, bd=3, textvariable=self.Fecha_fin, bg="white")
        self.fecha_fin.place_configure(x=490, y=250, width=100, height=20)

        self.Valorxdia = StringVar()
        self.valorxdia = Entry(self.ventana_administracion, bd=3, textvariable=self.Valorxdia, bg="yellow")
        self.valorxdia.place_configure(x=490, y=285, width=100, height=20)

        self.Numero_factura = StringVar()
        self.numero_factura = Entry(self.ventana_administracion, bd=3, textvariable=self.Numero_factura, bg="white")
        self.numero_factura.place_configure(x=210, y=100, width=90, height=20)

        self.Cedula_cliente = StringVar()
        self.cedula_cliente = Entry(self.ventana_administracion, bd=3, textvariable=self.Cedula_cliente, bg="white")
        self.cedula_cliente.place_configure(x=210, y=130, width=90, height=20)

        self.Nombre_cliente = StringVar()
        self.nombre_cliente = Entry(self.ventana_administracion, bd=3, textvariable=self.Nombre_cliente, bg="white")
        self.nombre_cliente.place_configure(x=210, y=160, width=90, height=20)

        self.Profesion = StringVar()
        self.profesion = Entry(self.ventana_administracion, bd=3, textvariable=self.Profesion, bg="white")
        self.profesion.place_configure(x=210, y=190, width=90, height=20)

        self.Direccion_casa = StringVar()
        self.direccion_casa = Entry(self.ventana_administracion, bd=3, textvariable=self.Direccion_casa, bg="white")
        self.direccion_casa.place_configure(x=210, y=220, width=90, height=20)

        self.Lugar_trabajo = StringVar()
        self.lugar_trabajo = Entry(self.ventana_administracion, bd=3, textvariable=self.Lugar_trabajo, bg="white")
        self.lugar_trabajo.place_configure(x=210, y=250, width=90, height=20)

        self.Tarjeta = StringVar()
        self.targeta = Entry(self.ventana_administracion, bd=3, textvariable=self.Tarjeta, bg="yellow")
        self.targeta.place_configure(x=210, y=285, width=90, height=20)

        Cargar = alquiler_vehiculo
        self.lista_alquiler_vehiculo = Cargar.cargar_archivo(Cargar)
        lista_aux = []
        contador = 0
        while (contador < len(self.lista_alquiler_vehiculo)):

            contador_aux=0
            verificador= True
            while(contador_aux< len(lista_aux)):
                if(self.lista_alquiler_vehiculo[contador][1][0]== lista_aux[contador_aux]):
                    verificador= False
                contador_aux= contador_aux + 1
            if(verificador):
               lista_aux.append(self.lista_alquiler_vehiculo[contador][1][0])

            contador = contador + 1
        self.Combo_numero_orden['values'] = lista_aux

        if (self.tipo_usuario == "CLIENTE"):
            self.Combo_numero_orden['values'] = self.id_usuario
        #self.Combo_cliente.bind("<<ComboboxSelected>>", self.buscar_en_alquiler)

        # self.Combo_numero_orden.bind("<<ComboboxSelected>>", self.callbackFunc)
        self.Combo_numero_orden.bind("<<ComboboxSelected>>", self.mostrar_alquileres)
        self.nombre.destroy()
        self.nombre = Entry(self.ventana_administracion, width=10)
        self.nombre.insert(0, self.tipo_usuario + ": ", )
        self.nombre.insert(22, self.usuario.get())
        self.nombre.place_configure(x=0, y=320, width=600, height=20)
        self.nombre.config(state=tk.DISABLED)

    # Esta funcion permite carga el alquiler y lo muestra
    def mostrar_alquileres(self, event):
        Cargar = alquiler_vehiculo
        self.lista_alquiler_vehiculo = Cargar.cargar_archivo(Cargar)
        self.lista_alquiler_vehiculo_auxiliar=[]
        contador=0

        while(contador< len(self.lista_alquiler_vehiculo)) and self.Combo_numero_orden.get()!="":
            if(self.lista_alquiler_vehiculo[contador][1][0]==int(self.Combo_numero_orden.get())):
                self.lista_alquiler_vehiculo_auxiliar.append(self.lista_alquiler_vehiculo[contador])
            contador= contador + 1

        if(len(self.lista_alquiler_vehiculo_auxiliar)>0):
            self.numero_factura.config(state='normal')
            self.cedula_cliente.config(state='normal')
            self.nombre_cliente.config(state='normal')
            self.profesion.config(state='normal')
            self.direccion_casa.config(state='normal')
            self.lugar_trabajo.config(state='normal')

            self.numero_placa.config(state='normal')
            self.marca.config(state='normal')
            self.modelo.config(state='normal')
            self.color.config(state='normal')
            self.cantidad_pasajeros.config(state='normal')

            self.fecha.config(state='normal')
            self.fecha_fin.config(state='normal')
            self.targeta.config(state='normal')
            self.valorxdia.config(state='normal')

            self.numero_factura.delete(0, END)
            self.cedula_cliente.delete(0, END)
            self.nombre_cliente.delete(0, END)
            self.profesion.delete(0, END)
            self.direccion_casa.delete(0, END)
            self.lugar_trabajo.delete(0, END)

            self.numero_placa.delete(0, END)
            self.marca.delete(0, END)
            self.modelo.delete(0, END)
            self.color.delete(0, END)
            self.cantidad_pasajeros.delete(0, END)

            self.fecha.delete(0, END)
            self.fecha_fin.delete(0, END)

            self.targeta.delete(0, END)
            self.valorxdia.delete(0, END)



            self.numero_factura.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][0])
            self.cedula_cliente.insert(0,self.lista_alquiler_vehiculo_auxiliar[0][8])
            self.nombre_cliente.insert(0,self.lista_alquiler_vehiculo_auxiliar[0][1][1])
            self.profesion.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][1][2])
            self.direccion_casa.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][1][4])
            self.lugar_trabajo.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][1][5])

            self.numero_placa.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][2][0])
            self.marca.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][2][1])
            self.modelo.insert(0,self.lista_alquiler_vehiculo_auxiliar[0][2][2] )
            self.color.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][2][3])
            self.cantidad_pasajeros.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][2][4])

            self.fecha.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][3])
            self.fecha_fin.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][4])
            self.targeta.insert(0, self.lista_alquiler_vehiculo_auxiliar[0][6])
            self.valorxdia.insert(0,self.lista_alquiler_vehiculo_auxiliar[0][5] )

            self.numero_factura.config(state='readonly')
            self.cedula_cliente.config(state='readonly')
            self.nombre_cliente.config(state='readonly')
            self.profesion.config(state='readonly')
            self.direccion_casa.config(state='readonly')
            self.lugar_trabajo.config(state='readonly')

            self.numero_placa.config(state='readonly')
            self.marca.config(state='readonly')
            self.modelo.config(state='readonly')
            self.color.config(state='readonly')
            self.cantidad_pasajeros.config(state='readonly')

            self.fecha.config(state='readonly')
            self.fecha_fin.config(state='readonly')
            self.targeta.config(state='readonly')
            self.valorxdia.config(state='readonly')
            self.contador=1

    # Esta funcion permite mostrar el siguiente alquiler
    def siguiente_alquiler(self):
        if(self.Combo_numero_orden.get()!=""):
           if (self.contador< len(self.lista_alquiler_vehiculo_auxiliar)):
               self.numero_factura.config(state='normal')
               self.cedula_cliente.config(state='normal')
               self.nombre_cliente.config(state='normal')
               self.profesion.config(state='normal')
               self.direccion_casa.config(state='normal')
               self.lugar_trabajo.config(state='normal')

               self.numero_placa.config(state='normal')
               self.marca.config(state='normal')
               self.modelo.config(state='normal')
               self.color.config(state='normal')
               self.cantidad_pasajeros.config(state='normal')

               self.fecha.config(state='normal')
               self.fecha_fin.config(state='normal')
               self.targeta.config(state='normal')
               self.valorxdia.config(state='normal')

               self.numero_factura.delete(0, END)
               self.cedula_cliente.delete(0, END)
               self.nombre_cliente.delete(0, END)
               self.profesion.delete(0, END)
               self.direccion_casa.delete(0, END)
               self.lugar_trabajo.delete(0, END)

               self.numero_placa.delete(0, END)
               self.marca.delete(0, END)
               self.modelo.delete(0, END)
               self.color.delete(0, END)
               self.cantidad_pasajeros.delete(0, END)

               self.fecha.delete(0, END)
               self.fecha_fin.delete(0, END)

               self.targeta.delete(0, END)
               self.valorxdia.delete(0, END)

               self.numero_factura.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][0])
               self.cedula_cliente.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][8])
               self.nombre_cliente.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][1][1])
               self.profesion.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][1][2])
               self.direccion_casa.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][1][4])
               self.lugar_trabajo.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][1][5])

               self.numero_placa.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][2][0])
               self.marca.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][2][1])
               self.modelo.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][2][2])
               self.color.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][2][3])
               self.cantidad_pasajeros.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][2][4])

               self.fecha.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][3])
               self.fecha_fin.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][4])
               self.targeta.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][6])
               self.valorxdia.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][5])

               self.numero_factura.config(state='readonly')
               self.cedula_cliente.config(state='readonly')
               self.nombre_cliente.config(state='readonly')
               self.profesion.config(state='readonly')
               self.direccion_casa.config(state='readonly')
               self.lugar_trabajo.config(state='readonly')

               self.numero_placa.config(state='readonly')
               self.marca.config(state='readonly')
               self.modelo.config(state='readonly')
               self.color.config(state='readonly')
               self.cantidad_pasajeros.config(state='readonly')

               self.fecha.config(state='readonly')
               self.fecha_fin.config(state='readonly')
               self.targeta.config(state='readonly')
               self.valorxdia.config(state='readonly')
               self.contador= self.contador + 1
           else:
               self.contador=0
               self.numero_factura.config(state='normal')
               self.cedula_cliente.config(state='normal')
               self.nombre_cliente.config(state='normal')
               self.profesion.config(state='normal')
               self.direccion_casa.config(state='normal')
               self.lugar_trabajo.config(state='normal')

               self.numero_placa.config(state='normal')
               self.marca.config(state='normal')
               self.modelo.config(state='normal')
               self.color.config(state='normal')
               self.cantidad_pasajeros.config(state='normal')

               self.fecha.config(state='normal')
               self.fecha_fin.config(state='normal')
               self.targeta.config(state='normal')
               self.valorxdia.config(state='normal')

               self.numero_factura.delete(0, END)
               self.cedula_cliente.delete(0, END)
               self.nombre_cliente.delete(0, END)
               self.profesion.delete(0, END)
               self.direccion_casa.delete(0, END)
               self.lugar_trabajo.delete(0, END)

               self.numero_placa.delete(0, END)
               self.marca.delete(0, END)
               self.modelo.delete(0, END)
               self.color.delete(0, END)
               self.cantidad_pasajeros.delete(0, END)

               self.fecha.delete(0, END)
               self.fecha_fin.delete(0, END)

               self.targeta.delete(0, END)
               self.valorxdia.delete(0, END)

               self.numero_factura.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][0])
               self.cedula_cliente.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][8])
               self.nombre_cliente.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][1][1])
               self.profesion.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][1][2])
               self.direccion_casa.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][1][4])
               self.lugar_trabajo.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][1][5])

               self.numero_placa.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][2][0])
               self.marca.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][2][1])
               self.modelo.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][2][2])
               self.color.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][2][3])
               self.cantidad_pasajeros.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][2][4])

               self.fecha.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][3])
               self.fecha_fin.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][4])
               self.targeta.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][6])
               self.valorxdia.insert(0, self.lista_alquiler_vehiculo_auxiliar[self.contador][5])

               self.numero_factura.config(state='readonly')
               self.cedula_cliente.config(state='readonly')
               self.nombre_cliente.config(state='readonly')
               self.profesion.config(state='readonly')
               self.direccion_casa.config(state='readonly')
               self.lugar_trabajo.config(state='readonly')

               self.numero_placa.config(state='readonly')
               self.marca.config(state='readonly')
               self.modelo.config(state='readonly')
               self.color.config(state='readonly')
               self.cantidad_pasajeros.config(state='readonly')

               self.fecha.config(state='readonly')
               self.fecha_fin.config(state='readonly')
               self.targeta.config(state='readonly')
               self.valorxdia.config(state='readonly')
               self.contador= self.contador + 1
        else:
             messagebox.showinfo("Error de seleccion", "No ha seleccionado ningun numero de cedula de los usuarios")




     # Esta funcion permite guardar un alquiler desactivado
    def guardar_alquiler_desactivo(self):
        if (self.Combo_numero_orden.get() != ""):
             Cargar= alquiler_vehiculo
             Cargar2= vehiculo
             Cargar2.modificar(Cargar2, self.lista_alquiler_vehiculo[2][0], self.lista_alquiler_vehiculo[2][1],
                           self.lista_alquiler_vehiculo[2][2], self.lista_alquiler_vehiculo[2][3],self.lista_alquiler_vehiculo[2][4],
                           self.lista_alquiler_vehiculo[2][5], "NO")

             Cargar.modificar(Cargar, self.lista_alquiler_vehiculo[0], self.lista_alquiler_vehiculo[1], self.lista_alquiler_vehiculo[2
             ], self.lista_alquiler_vehiculo[3], self.lista_alquiler_vehiculo[4], self.lista_alquiler_vehiculo[5], self.lista_alquiler_vehiculo[6
             ], self.lista_alquiler_vehiculo[7], "Devuelto", self.lista_alquiler_vehiculo[9])

             #self.ventana_administracion.destroy()
             messagebox.showinfo("Proceso completado", "La devolucion del vehiculo placa " + str(
             self.lista_alquiler_vehiculo[2][0]) + " fue realizado correctamente")
             self.ventana_administracion
             self.desactivar_alquiler()
        else:
            messagebox.showinfo("Error de seleccion","No ha seleccionado ninguna orden")

    # Esta funcion tiene las variables del calendario
    def mes_a_numero(self, mes):
        num_mes=0
        if mes == "January":
            num_mes=1
        if mes == "February":
            num_mes=2
        if mes == "March":
            num_mes = 3
        if mes == "April":
            num_mes = 4
        if mes == "May":
            num_mes = 5
        if mes == "June":
            num_mes = 6
        if mes == "July":
            num_mes = 7
        if mes == "August":
            num_mes = 8
        if mes == "September":
            num_mes = 9
        if mes == "October":
            num_mes = 10
        if mes == "November":
            num_mes = 11
        if mes == "December":
            num_mes = 12
        return num_mes
    # Algoritmo para el calculo de valor por dia en que se evaluan el dia, mes y año.
    def cantidad_dias_alquiler(self,dia_ini, mes_ini, año_ini,dia_fin, mes_fin, año_fin):
            #mes_i= self.mes_a_numero(mes_inicio)
            #mes_f= self.mes_a_numero(mes_fin)
            total_dias=0

            if(año_fin> año_ini):

                if(mes_ini==1):
                        total_dias= 31 - dia_ini + 1
                        total_dias= total_dias +334
                        año_ini =año_ini + 1
                        mes_ini=1
                if(mes_ini == 2):
                        total_dias = 28 - dia_ini + 1
                        total_dias = total_dias + 307
                        año_ini = año_ini + 1
                        mes_ini=1
                if (mes_ini == 3):
                        total_dias = 31 - dia_ini + 1
                        total_dias = total_dias + 275
                        año_ini = año_ini + 1
                        mes_ini=1
                if (mes_ini == 4):
                        total_dias = 30 - dia_ini + 1
                        total_dias = total_dias + 245
                        año_ini = año_ini + 1
                        mes_ini=1
                if (mes_ini == 5):
                        total_dias = 31 - dia_ini + 1
                        total_dias = total_dias + 214
                        año_ini = año_ini + 1
                        mes_ini=1
                if (mes_ini == 6):
                        total_dias = 30 - dia_ini + 1
                        total_dias = total_dias + 184
                        año_ini = año_ini + 1
                        mes_ini= 1
                if (mes_ini == 7):
                        total_dias = 31 - dia_ini + 1
                        total_dias = total_dias + 153
                        año_ini = año_ini + 1
                        mes_ini=1
                if (mes_ini == 8):
                        total_dias = 31 - dia_ini + 1
                        total_dias = total_dias + 122
                        año_ini = año_ini + 1
                        mes_ini=1

                if (mes_ini == 9):
                        total_dias = 30 - dia_ini + 1
                        total_dias = total_dias + 92
                        año_ini = año_ini + 1
                        mes_ini= 1
                if (mes_ini == 10):
                        total_dias = 31 - dia_ini + 1
                        total_dias = total_dias + 61
                        año_ini = año_ini + 1
                        mes_ini= 1
                if (mes_ini == 11):
                        total_dias = 30 - dia_ini +1
                        total_dias = total_dias + 31
                        año_ini = año_ini + 1
                        mes_ini=1
                if (mes_ini == 12):
                        total_dias = 31 - dia_ini +1
                        año_ini = año_ini + 1
                        mes_ini=1

                while(año_fin> año_ini):
                        total_dias= total_dias + 365
                        año_ini= año_ini + 1

                if(año_fin == año_ini):
                        while(mes_fin>mes_ini):
                            if (mes_ini == 1):
                                total_dias = total_dias+ 31
                                mes_ini = mes_ini + 1
                            elif (mes_ini == 2):
                                total_dias = total_dias + 28
                                mes_ini = mes_ini + 1
                            elif (mes_ini == 3):
                                total_dias = total_dias + 31
                                mes_ini = mes_ini + 1
                            elif (mes_ini == 4):
                                total_dias = total_dias + 30
                                mes_ini = mes_ini + 1
                            elif (mes_ini == 5):
                                total_dias = total_dias + 31
                                mes_ini = mes_ini + 1
                            elif (mes_ini == 6):
                                total_dias = total_dias + 30
                                mes_ini = mes_ini + 1
                            elif (mes_ini == 7):
                                total_dias = total_dias + 31
                                mes_ini = mes_ini + 1
                            elif (mes_ini == 8):
                                total_dias = total_dias + 31
                                mes_ini = mes_ini + 1
                            elif (mes_ini == 9):
                                total_dias = total_dias + 30
                                mes_ini = mes_ini + 1
                            elif (mes_ini == 10):
                                total_dias = total_dias + 31
                                mes_ini = mes_ini + 1
                            elif (mes_ini == 11):
                                total_dias = total_dias + 30
                                mes_ini = mes_ini + 1
                        if(mes_ini==mes_fin):
                            total_dias = total_dias + dia_fin

            elif(año_ini==año_fin) and (mes_fin>mes_ini):
                    if(mes_ini== 1):
                        total_dias = 31 -dia_ini
                    if (mes_ini == 2):
                        total_dias = 28 - dia_ini
                    if (mes_ini == 3):
                        total_dias = 31 - dia_ini
                    if (mes_ini == 4):
                        total_dias = 30 - dia_ini
                    if (mes_ini == 5):
                        total_dias = 31 - dia_ini
                    if (mes_ini == 6):
                        total_dias = 30 - dia_ini
                    if (mes_ini == 7):
                        total_dias = 31 - dia_ini
                    if (mes_ini == 8):
                        total_dias = 31 - dia_ini
                    if (mes_ini == 9):
                        total_dias = 30 - dia_ini
                    if (mes_ini == 10):
                        total_dias = 31 - dia_ini
                    if (mes_ini == 11):
                        total_dias = 30 - dia_ini
                    if (mes_ini == 12):
                        total_dias = 31 - dia_ini

                    mes_ini= mes_ini + 1

                    while (mes_fin > mes_ini):
                        if (mes_ini == 1):
                            total_dias = total_dias + 31
                            mes_ini = mes_ini + 1
                        elif (mes_ini == 2):
                            total_dias = total_dias + 28
                            mes_ini = mes_ini + 1
                        elif (mes_ini == 3):
                            total_dias = total_dias + 31
                            mes_ini = mes_ini + 1
                        elif (mes_ini == 4):
                            total_dias = total_dias + 30
                            mes_ini = mes_ini + 1
                        elif (mes_ini == 5):
                            total_dias = total_dias + 31
                            mes_ini = mes_ini + 1
                        elif(mes_ini == 6):
                            total_dias = total_dias + 30
                            mes_ini = mes_ini + 1
                        elif (mes_ini == 7):
                            total_dias = total_dias + 31
                            mes_ini = mes_ini + 1
                        elif (mes_ini == 8):
                            total_dias = total_dias + 31
                            mes_ini = mes_ini + 1
                        elif (mes_ini == 9):
                            total_dias = total_dias + 30
                            mes_ini = mes_ini + 1
                        elif (mes_ini == 10):
                            total_dias = total_dias + 31
                            mes_ini = mes_ini + 1
                        elif (mes_ini == 11):
                            total_dias = total_dias + 30
                            mes_ini = mes_ini + 1
                    if (mes_ini == mes_fin):
                        total_dias = total_dias + dia_fin
            elif(año_fin==año_ini) and (mes_ini==mes_fin):
                 total_dias= dia_fin - dia_ini
                 total_dias= total_dias + 1


            return  total_dias














    # Esta funcion carga los datos del calendario y los muestra en pantalla
    def writeCalendar(self, ano, mes):
        # Asignamos el año y mes al calendario

        self.str1 = calendar.month(ano, mes)
        self.mes_seleccion = ""
        self.año_seleccion = ""
        self.dia_seleccion= ""
        largo=0
        largo_aux=0
        contador= 0
        while(largo< len(self.str1)):

            if(self.str1[largo].isspace()):
                largo= largo + 1

            elif((self.str1[largo].isspace()!= True) and (contador < 16)):
                while((self.str1[largo].isspace()!= True) and contador==0 and (largo< len(self.str1))) :
                      self.mes_seleccion= str(self.mes_seleccion) + str(self.str1[largo])
                      largo= largo + 1

                while ((self.str1[largo].isspace() != True) and contador == 1):
                    self.año_seleccion = self.año_seleccion + self.str1[largo]
                    largo = largo + 1
                if(contador > 1):
                    largo= largo +1

                contador= contador + 1
            elif contador>=16:
                while (largo < len(self.str1)):
                    self.dia_seleccion = self.dia_seleccion + self.str1[largo]
                    largo = largo + 1
            else:
                largo= largo + 1





        if(self.Combo_año.get()== "") or (self.Combo_mes.get()== "") or(self.Combo_año.get()==""):
           self.Combo_año['values'] = self.año_seleccion
           self.Combo_mes['values'] = self.mes_seleccion
           self.Combo_fecha['values']= self.dia_seleccion


        self.Combo_año_fin['values'] = self.año_seleccion
        self.Combo_mes_fin['values'] = self.mes_seleccion
        self.Combo_fecha_fin['values'] = self.dia_seleccion

        self.label1.configure(text=self.str1)

    # Esta funicon permite seleccionar el mes anterior
    def mesAnterior(self):
        #global mes, ano
        self.mes -= 1

        if self.mes == 0:
            self.mes = 12
            self.ano -= 1

        # ano -= 1
        self.writeCalendar(self.ano, self.mes)

    # Esta funcion permite seleccionar el mes siguiente
    def mesSiguiente(self):

        self.mes += 1

        if self.mes == 13:
            self.mes = 1
            self.ano += 1

        self.writeCalendar(self.ano,self.mes)

    # Esta funcion permite abrir una ventana secundaria despues de ingresar la clave
    def new_window(self):
        #self.ventana2()
       Enlace = administrador
       usuario=[]
       administrador_vacio=[]
       administrador_vacio= Enlace.devuelve_lista(Enlace)
       usuario= Enlace.verificar_acceso(Enlace,self.usuario.get(), self.contraseña.get())
       if(len(administrador_vacio)>0):
        if(usuario==[]):
            Enlace = asistente
            usuario = []
            usuario = Enlace.verificar_acceso(Enlace, self.usuario.get(), self.contraseña.get())

            if(usuario==[]):
                Enlace = cliente
                usuario = []
                usuario = Enlace.verificar_acceso(Enlace, self.usuario.get(), self.contraseña.get())
                if(usuario==[]):
                    messagebox.showinfo("Error de autentificacion", "El usuario no existe")
                else:
                    Bitacora = bitacora
                    Bitacora.identificacion = usuario[0]
                    Bitacora.nombre = usuario[1]
                    Bitacora.puesto = usuario[3]
                    Bitacora.nombre_usuario = usuario[6]
                    Bitacora.guardar_archivo(Bitacora)
                    self.nombre_usuario = self.usuario.get()
                    self.tipo_usuario = "CLIENTE"
                    self.id_usuario= usuario[0]
                    self.ventana_admin()
                    self.usua_i.delete(0, tk.END)
                    self.cotra_i.delete(0, tk.END)

            else:
                Bitacora = bitacora
                Bitacora.identificacion = usuario[0]
                Bitacora.nombre = usuario[1]
                Bitacora.puesto = usuario[3]
                Bitacora.nombre_usuario = usuario[4]
                Bitacora.guardar_archivo(Bitacora)
                self.nombre_usuario = self.usuario.get()
                self.tipo_usuario = "ASISTENTE"
                self.id_usuario = usuario[0]
                self.ventana_admin()
                self.usua_i.delete(0, tk.END)
                self.cotra_i.delete(0, tk.END)


        #self.Numero_id.set()
        else:
            Bitacora= bitacora
            Bitacora.identificacion= usuario[0]
            Bitacora.nombre= usuario[1]
            Bitacora.puesto = usuario[2]
            Bitacora.nombre_usuario = usuario[3]
            Bitacora.guardar_archivo(Bitacora)
            self.nombre_usuario= self.usuario.get()
            self.tipo_usuario= "ADMINISTRADOR"
            self.id_usuario = usuario[0]
            self.ventana_admin()
            self.usua_i.delete(0, tk.END)
            self.cotra_i.delete(0, tk.END)
       else:
           messagebox.showinfo("Primer ingreso", "El usuario es admin y la contraseña es admin")
           try:
                os.remove("bitacora.pickle")
           except:
               x=0
           try:
                os.remove("asistentes.pickle")
           except:
               x=0
           try:
                os.remove("cliente.pickle")
           except:
               x=0
           try:
                os.remove("vehiculo.pickle")
           except:
               x=0
           try:
                os.remove("promociones.pickle")
           except:
               x=0
           try:
                os.remove("alquiler_vehiculo.pickle")
           except:
               x=0

           Nuevo_administrador= administrador
           Nuevo_administrador.identificacion = int(00000000)
           Nuevo_administrador.nombre = "admin"
           Nuevo_administrador.puesto = "Administrador"
           Nuevo_administrador.nombre_usuario = "admin"
           Nuevo_administrador.contraseña = "admin"
           Nuevo_administrador.guardar_archivo(Nuevo_administrador)
           #Nuevo_administrador.cargar_archivo(Nuevo_administrador)




    # Esta funcion permite salir del programa
    def cerrar(self):

        sys.exit()


    # Esta funcion permite ajustar el tamaño
    def center(toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))









# Esta funcion llama a la ventana principal

def main():
  Ventana_principal()

if __name__ == '__main__':
    main()


