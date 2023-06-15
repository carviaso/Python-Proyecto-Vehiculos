#Se ejecuta intento de trabajar ventanas en HD, solo disponible en Windows (por eso el "try-except")
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

#Se crea clase principal (tk.Tk), la cual es la encargada de manejar los Frames
class APP(tk.Tk):
    def __init__(self,*args,**kwargs):
                #Se inicializa ademas, con la herencia de tk.Tk, para tener todas estas disponibilidades en "self"
        super().__init__(*args,**kwargs)

        #Se agrega fondo a ventana principal (la que va a contener el contenedor y a su vez, los frames)
        self.configure(bg = "black")

        #Cambiar "font" por defecto a todo (ojo con forma de importar libreria arriba)
        font.nametofont("TkDefaultFont").configure(size = 12, underline = True)

        #Se aprovecha que "self" ya es la ventana principal y se agrega titulo respectivo
        self.title("TKINTER CON FRAME Y POO")
        
        #Se busca que Ventana se mantenga central y correcta independiente del tamanno y expansiones realizadas:
        self.columnconfigure( 0, weight = 1 )
        self.rowconfigure(0, weight = 1)

        #OJO: Se crea el "CONTENEDOR PRINCIPAL", el cual es un Frame en donde se llamaran a los otros Frames de las otras clases...
        #...esto nos permitira tener el efecto de multiples ventanas segun la que se necesita (osea el frame respectivo)
        contenedor_principal = tk.Frame( self ,bg = "yellow")
        contenedor_principal.grid( padx = 5, pady = 5 , sticky = "nsew")
        
        #IMPORTANTISIMO (CREACION DE DICCIONARIO CON FRAMES A UTILIZAR EN APP --> TODAS LAS FRAMES QUE SE TENGAN):
        #Recordar que este diccionario, almacena los frames y juega un papel esencial en indicar cual de todos mostrar.
        #Ademas, se vuelve util con metodo especial para acceder a otros frames (ver mas abajo)
        self.todos_los_frames = dict()
                
        #PARTE INDISPENSABLE DE TRABAJO CON MULTIPAGINAS (MULTIPLES FRAMES):
        #Se debe crear cada una de las clases de los frames (TODAS), de tal forma que se agregen al diccionario de estas...
        #...esto es fundamental, porque asi identificaremos a cual frame ir, segun algo interactivo para el usuario
        #OJO: se pasan TODAS las clases asociadas a las paginas con las que trabajaremos, y se agregan correctamente...
        #RECORDERIS: Se recorre tupla, de todas las clases (forma de ahorrar lineas de codigo)
        for F in (Frame_1, Frame_2, Frame_Login, Frame_Administrador):
            #Se ejecuta la labor de llamar a todas las clases asociadas a Frames_N (una a una)
            #NOTA: ver que se almacenan momentaneamente en frame, para simplificar labor
            #OJO: NECESARIO: Parametro "self", como encargado de ser el "controller", la razon es porque...
            #... desde TODAS las otras clases (Frames), se debe poder acceder a metododo "show_frame", y si...
            #...NO se pasa esta, implica que NO habra acceso a los metodos de la APP principal. Por esto se pasa self.
            frame = F( contenedor_principal , self)
            #Se agrega a diccionario de todos los frames la llave y su respectivo correspondiente:
            #LLAVE = "F"    ---> Cada llave es cada clase de Frame_1, Frame_2, etc...
            #OBJETO = frame, que es :"F(contenedor_principal)"   ---> Cada objeto es Frame_1(contenedor_principal), etc...
            self.todos_los_frames[F] = frame
            #Ahora, se agrega correctamente cada una de las Frames recorridas en la tupla de frames
            #NOTA: FUNDAMENTAL crear frames con sticky = "nsew", para que no aparezcan cosas de otros frames indeseadas
            frame.grid(row = 0, column = 0, sticky = "nsew")
                
        #OJO: luego se debe llamar al metodo "show_frame", creado por nosotros, para mostrar un frame deseado...
        #...en esencia, permite traer al primer plano, un frame del vector "self.todos+los_frames"
        self.show_frame( Frame_Login )
    
        
    #METODO PARA MOSTRAR UNICAMENTE FRAME DESEADO (controller = Clase que queremos obtener de diccionario de frames)
    def show_frame(self, contenedor_llamado):
        #Se selecciona el frame requerido por el controller, desde el diccionario de frames ya creado anteriormente
        #Recordemos que el controller, es simplemente el valor por defecto de la clase asociada a cada Frame...
        #...estos keys se crearon arriba al recorrer tupla de los frames de la app
        frame = self.todos_los_frames[contenedor_llamado]

        #Se agrega funcionalidad al presionar "ENTER" y "ENTER NUMERICO"
        #OJO: Estos "bind" SOLAMENTE se pueden agregar aqui, y debe generalizarse su funcion, pues no hay otra forma de...
        #... diferenciar en que ventana hace efecto el enter
        self.bind( "<Return>", frame.saludarme )
        self.bind( "<KP_Enter>", frame.saludarme )

        #Se elimina lo escrito en el label del frame respectivo (asociado al saludo)
        frame.L_3.configure( text = "" )
        frame.entrada_usuario.set( "" )
        frame.E_1.focus()
        
        #Ahora se llama a funcion de tkinter heredada desde clase APP, la cual permite traer frame indicada a primer plano
        frame.tkraise()


#OJO( CREACION DE FRAMES):
#Se crean como clases con herencia de tk.Frame (para acceder inmediatamente a las clases Frames respectivas)
#NOTA: Si bien creamos Frames, recordemos que hace falta "llamarlos", de lo contrario, no se crea ni se hacen efectivos
class Frame_1(tk.Frame):
    #Se inicializan, recibiendo de parametro self, parent y controller.
    #self es para manejo de clase interna
    #container es para indicar el frame o root, en donde se ubicara el frame (en este caso en APP principal)
    #controller es indicador interno para manejo correcto de cambio de frames 
    # (es decir, podra acceder a app principal y a sus metodos, de tal forma que se permita cambio)
    #Recordemos que este container sera entonces un parametro que debemos incluir, al llamar a clase.
    #Se pueden incluir los *args y **kwargs, como parametros extra disponibles
    def __init__(self, container, controller,*args, **kwargs):
        #Para inicializar Frame y que se entienda la clase como un Frame, tambien se inicializa desde la herencia:
        #NOTA: NO olvidar pasar el parametro tambien, de lo contrario, no se comprende donde localizar el Frame creado
        #Luego de hacer esto, recordar que "self" es equivalente a decir el Frame_1, que es en donde agregaremos widgets
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "yellow")

        #Agregamos Widgets, con la ventaja de poder agregarlos en "self"(Frame_1)-->tk.Frame , que a su vez, estara en root(APP)-->tk.Tk
        #Variable para texto del usuario, el objetivo es poder obtener la info de Entry (E_1)
        self.entrada_usuario = tk.StringVar()

        L_1 = tk.Label( self, text = "MI PRIMER FRAME CON POO Y TKINTER", font = ("Times New Roman",14,"bold"),bg = "yellow",fg = "blue" )
        L_1.grid(row = 0, column = 0, columnspan = 4, sticky = "n")
        L_2 = tk.Label( self, text = "Ingrese Nombre: ", font = ("Times New Roman",12),bg = "yellow" )
        L_2.grid(row = 1, column = 0, sticky = "w")

        #Notar que entry debe tener como variable, la definida como "self.entrada_usuario". Se crea con "self", para acceder a ella en metodos
        self.E_1 = ttk.Entry( self, textvariable = self.entrada_usuario )
        self.E_1.focus()
        self.E_1.grid(row = 1, column = 1, columnspan = 2, padx = (0,10))


        #OJO: mirar B_1, es boton, que su command activa un metodo interno de la clase. Esto es maravilloso.
        #esto nos permitira acceder a metodos en clases, al interactuar con widgets. Es mas organizado segun clase (Frame)
        B_1 = ttk.Button( self, text = "SALUDARME" , command = self.saludarme )
        B_1.grid(row = 1, column = 3, sticky = "e")

 
        #OJO: este label es variable, por lo que lo creamos con "self.", para poder acceder a el con metodos de la clase
        self.L_3 = tk.Label( self, textvariable = "", font = ("Times New Roman",12,"bold"),bg = "yellow" )
        self.L_3.grid(row = 2, column = 0, columnspan = 4, sticky = "nsew")


        #Crear boton para cambio de paginas entre Frames:
        #NOTA: como se debe acceder a metodo "show_frame" desde otra clase, por eso se debe pasar "controller"
        B_2 = ttk.Button( self, text = "ingles", command = lambda:controller.show_frame( Frame_2 ) )
        B_2.grid(row = 3, column = 0)



    #OJO: Se debe agregar "*args", porque esta funcion ademas puede ser llamada a traves de darle "enter" al teclado...
    #...para lograr esto, se requiere pasar funcion con parametros a traves de "bind" (ver self.bind() en clase principal)
    def saludarme(self, *args):
        self.L_3.configure( text = "Buenos Dias : {}.".format( self.entrada_usuario.get() ) )


#Se crea Frame_2 (similar a primera, pero con idioma ingles)
class Frame_2(tk.Frame):
    #Se inicializan, recibiendo de parametro self, parent y controller.
    #self es para manejo de clase interna
    #parent es para indicar el frame o root, en donde se ubicara el frame (en este caso en APP principal)
    #controller es indicador interno para manejo correcto de cambio entre frames.
    # (es decir, podra acceder a app principal y a sus metodos, de tal forma que se permita cambio)
    def __init__(self, container,controller,*args, **kwargs):
        #Para inicializar Frame y que se entienda la clase como un Frame, tambien se inicializa desde la herencia:
        #NOTA: NO olvidar pasar el parametro tambien, de lo contrario, no se comprende donde localizar el Frame creado
        #Luego de hacer esto, recordar que "self" es equivalente a decir el Frame_1, que es en donde agregaremos widgets
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "yellow")

        #Agregamos Widgets, con la ventaja de poder agregarlos en "self"(Frame_1)-->tk.Frame , que a su vez, estara en root(APP)-->tk.Tk
        #Variable para texto del usuario, el objetivo es poder obtener la info de Entry (E_1)
        self.entrada_usuario = tk.StringVar()

        L_1 = tk.Label( self, text = "MI FIRST FRAME WITH OOP AND TKINTER", font = ("Times New Roman",14,"bold"),bg = "yellow",fg = "blue" )
        L_1.grid(row = 0, column = 0, columnspan = 4, sticky = "n")
        L_2 = tk.Label( self, text = "Entry name: ", font = ("Times New Roman",12),bg = "yellow" )
        L_2.grid(row = 1, column = 0, sticky = "w")

        #Notar que entry debe tener como variable, la definida como "self.entrada_usuario". Se crea con "self", para acceder a ella en metodos
        self.E_1 = ttk.Entry( self, textvariable = self.entrada_usuario )
        self.E_1.focus()
        self.E_1.grid(row = 1, column = 1, columnspan = 2, padx = (0,10))


        #OJO: mirar B_1, es boton, que su command activa un metodo interno de la clase. Esto es maravilloso.
        #esto nos permitira acceder a metodos en clases, al interactuar con widgets. Es mas organizado segun clase (Frame)
        B_1 = ttk.Button( self, text = "SAY HI" , command = self.saludarme )
        B_1.grid(row = 1, column = 3, sticky = "e")

 
        #OJO: este label es variable, por lo que lo creamos con "self.", para poder acceder a el con metodos de la clase
        self.L_3 = tk.Label( self, textvariable = "", font = ("Times New Roman",12,"bold"),bg = "yellow" )
        self.L_3.grid(row = 2, column = 0, columnspan = 4, sticky = "nsew")

        #Crear boton para cambio de paginas entre Frames:
        #NOTA: como se debe acceder a metodo "show_frame" desde otra clase, por eso se debe pasar "controller"
        B_2 = ttk.Button( self, text = "espannol", command = lambda:controller.show_frame( Frame_1 ) )
        B_2.grid(row = 3, column = 0)
    


    #OJO: Se debe agregar "*args", porque esta funcion ademas puede ser llamada a traves de darle "enter" al teclado...
    #...para lograr esto, se requiere pasar funcion con parametros a traves de "bind" (ver self.bind() en clase principal)
    def saludarme(self, *args):
        self.L_3.configure( text = "Good Morning, {}.".format( self.entrada_usuario.get() ) )


#Se crea Frame_Login (similar a primera, pero con idioma ingles)
class Frame_Login(tk.Frame):
    #Se inicializan, recibiendo de parametro self, parent y controller.
    #self es para manejo de clase interna
    #parent es para indicar el frame o root, en donde se ubicara el frame (en este caso en APP principal)
    #controller es indicador interno para manejo correcto de cambio entre frames.
    # (es decir, podra acceder a app principal y a sus metodos, de tal forma que se permita cambio)
    def __init__(self, container, controller, *args, **kwargs):
        #Para inicializar Frame y que se entienda la clase como un Frame, tambien se inicializa desde la herencia:
        #NOTA: NO olvidar pasar el parametro tambien, de lo contrario, no se comprende donde localizar el Frame creado
        #Luego de hacer esto, recordar que "self" es equivalente a decir el Frame_1, que es en donde agregaremos widgets
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "steelblue")

        #Agregamos Widgets, con la ventaja de poder agregarlos en "self"(Frame_1)-->tk.Frame , que a su vez, estara en root(APP)-->tk.Tk
        #Variable para texto del usuario, el objetivo es poder obtener la info de Entry (E_1)
        self.entrada_usuario = tk.StringVar()
        
        #Variable para guardar el nombre del usuario que va ha ingresar, y creacion del area de texto donde se va ingresar
        self.usuario = tk.StringVar()
        
        #Area donde se recibe la contraseña
        self.contraseña = tk.StringVar()
        
        controller.title('Login')

        # row 0, col 0
        # -----------------------------------------------------
        L_1 = tk.Label( self, text = "MENU DE INGRESO A SU SISTEMA ALCARSA", font = ("Times New Roman",14,"bold"), bg = "white",fg = "blue" )
        L_1.grid(row = 0, column = 0, columnspan = 4, sticky = "n")
        
        # row 1, col 0
        # -----------------------------------------------------
        L_2 = tk.Label( self, text = "Usuario: ", font = ("Times New Roman",12), bg = "steelblue", fg = "white" )
        L_2.grid(row = 1, column = 0, sticky = "w")
        
        #Notar que entry debe tener como variable, la definida como "self.entrada_usuario". Se crea con "self", para acceder a ella en metodos
        self.E_1 = ttk.Entry( self, textvariable = self.usuario )
        self.E_1.focus()
        self.E_1.grid(row = 1, column = 1, columnspan = 4, padx = (0,10))
        
        # row 2, col 0
        # -----------------------------------------------------
        L_4 = tk.Label( self, text = "Contraseña: ", font = ("Times New Roman", 12), bg = "steelblue", fg = "white" )
        L_4.grid(row = 2, column = 0, sticky = "w")
        
        #Notar que entry debe tener como variable, la definida como "self.entrada_usuario". Se crea con "self", para acceder a ella en metodos
        self.E_2 = ttk.Entry( self, textvariable = self.contraseña, show="*" )
        #self.E_1.focus()
        self.E_2.grid(row = 2, column = 1, columnspan = 4, padx = (0,10))
        
        # row 3, col 3
        # -----------------------------------------------------
        #OJO: mirar B_1, es boton, que su command activa un metodo interno de la clase. Esto es maravilloso.
        #esto nos permitira acceder a metodos en clases, al interactuar con widgets. Es mas organizado segun clase (Frame)
        B_1 = ttk.Button( self, text = "SAY HI" , command = self.saludarme )
        B_1.grid(row = 3, column = 2, sticky = "e")

        #Crear boton para cambio de paginas entre Frames:
        #NOTA: como se debe acceder a metodo "show_frame" desde otra clase, por eso se debe pasar "controller"
        B_2 = ttk.Button( self, text = "espannol", command = lambda:controller.show_frame( Frame_Administrador ) )
        B_2.grid(row = 3, column = 0)
        
        # row 4, col 0
        # -----------------------------------------------------
        #OJO: este label es variable, por lo que lo creamos con "self.", para poder acceder a el con metodos de la clase
        self.L_3 = tk.Label( self, textvariable = "", font = ("Times New Roman", 10, "bold"), bg = "yellow" )
        self.L_3.grid(row = 5, column = 0, columnspan = 4, sticky = "nsew")


    #OJO: Se debe agregar "*args", porque esta funcion ademas puede ser llamada a traves de darle "enter" al teclado...
    #...para lograr esto, se requiere pasar funcion con parametros a traves de "bind" (ver self.bind() en clase principal)
    def saludarme(self, *args):
        self.L_3.configure( text = "Good Morning, {}.".format( self.entrada_usuario.get() ) )


#Se crea Frame_Login (similar a primera, pero con idioma ingles)
class Frame_Administrador(tk.Frame):
    #Se inicializan, recibiendo de parametro self, parent y controller.
    #self es para manejo de clase interna
    #parent es para indicar el frame o root, en donde se ubicara el frame (en este caso en APP principal)
    #controller es indicador interno para manejo correcto de cambio entre frames.
    # (es decir, podra acceder a app principal y a sus metodos, de tal forma que se permita cambio)
    def __init__(self, container, controller, *args, **kwargs):
        #Para inicializar Frame y que se entienda la clase como un Frame, tambien se inicializa desde la herencia:
        #NOTA: NO olvidar pasar el parametro tambien, de lo contrario, no se comprende donde localizar el Frame creado
        #Luego de hacer esto, recordar que "self" es equivalente a decir el Frame_1, que es en donde agregaremos widgets
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "steelblue")
        
        #self.resizable(0,0)
                
        menubar = tk.Menu(self)
        
    
    #OJO: Se debe agregar "*args", porque esta funcion ademas puede ser llamada a traves de darle "enter" al teclado...
    #...para lograr esto, se requiere pasar funcion con parametros a traves de "bind" (ver self.bind() en clase principal)
    def saludarme(self, *args):
        self.L_3.configure( text = "Good Morning, {}.".format( self.entrada_usuario.get() ) )

#Se crea APP como tal (aprovechandonos de la clase creada)
root = APP()

#Se ejecuta la ventana principal, creada a traves de POO con las clases respectivas
root.mainloop()
