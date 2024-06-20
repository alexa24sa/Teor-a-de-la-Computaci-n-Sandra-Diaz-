from tkinter import *
from PIL import Image, ImageTk
from pygame import *

# Declaramos las librerías para el sonido:
# Inicializar Pygame
mixer.init()

# Cargar el sonido
coins = mixer.Sound("coin_sound.MP3")
dispensador = mixer.Sound("dispensador.MP3")
error_sound = mixer.Sound("error.MP3")

def reproducir_sonido(sonido):
    sonido.play()

# Colocamos la raíz de la siguiente manera
raiz = Tk()
raiz.config(bg="#5C5C5D")
raiz.title("Máquina expendedora:")
miFrame = Frame(raiz, width=1080, height=1920, bg="#5C5C5D")
miFrame.pack()

# Variables
numeroPantalla = StringVar()  # Para mostrar el producto elegido
saldo = IntVar(value=0)  # Para manejar el saldo acumulado
saldoPantalla = StringVar(value="$0")  # Para mostrar el saldo en la pantalla

# Pantalla de texto para elegir productos
pantallaProducto = Entry(miFrame, fg="#11FCB2", font=("DS-DIGITAL", 16), bg="#323232", textvariable=numeroPantalla)
pantallaProducto.grid(row=2, column=6, rowspan=4, columnspan=4, padx=5, pady=5)
pantallaProducto.config(justify="center")

# Pantalla de texto para mostrar el saldo
textoProducto = Label(miFrame, text="Inserte monto exacto:" , fg="#8CA0AB", font=("DS-DIGITAL", 15, "bold"), bg="#5C5C5D")
textoProducto.grid(row = 12, column= 6, columnspan=4)
pantallaSaldo = Entry(miFrame, fg="#11FCB2", font=("DS-DIGITAL", 16), bg="#323232", textvariable=saldoPantalla)
pantallaSaldo.grid(row=13, column=6, rowspan=2, columnspan=4, padx=5, pady=5)
pantallaSaldo.config(justify="center")

# Función para actualizar la pantalla del saldo
def actualizarSaldo(monto):
    nuevo_saldo = saldo.get() + monto
    if nuevo_saldo > 18:
        return  # No permite que el saldo exceda de 18
    saldo.set(nuevo_saldo)
    saldoPantalla.set(f"${nuevo_saldo}")
    if nuevo_saldo > 0 and pantallaProducto.get() == "0":
        numeroPantalla.set(" Elige tu producto ")

# Función para añadir monto al saldo
def agregarMoneda(monto):
    actualizarSaldo(monto)

# Función para manejar el evento de insertar moneda y reproducir sonido
def manejar_evento_moneda(monto, sonido):
    agregarMoneda(monto)
    reproducir_sonido(sonido)

# Pulsaciones del teclado
def numeroPulsado(num):  # La función recibe el parámetro num
    numeroPantalla.set(numeroPantalla.get() + num)

# Leer el número en la pantalla del monitor
def leerCodigo():
    dinero = saldo.get()
    codigo = numeroPantalla.get()
    if not codigo.isdigit():
        reproducir_sonido(error_sound)
        numeroPantalla.set(" CODIGO NO VALIDO... ")
        return

    productoActual = int(codigo)  # Obtener el producto actual como entero
    monto = int(dinero)  # Obtener el monto actual del saldo

    productos = {
        1: ("PAPAS SOL NATURALES ", 18),
        2: ("PAPAS SOL LIMON ", 18),
        3: ("PAPAS SOL ADOBADAS ", 18),
        4: ("PAPAS SOL EXTREMAS ", 18),
        5: ("PAPAS SOL QUESO ", 18),
        6: ("JUGO MANGO ", 15),
        7: ("JUGO GUAYABA ", 15),
        8: ("JUGO NARANJA ", 15),
        9: ("GALLETAS MARIA ", 12),
        10: ("GALLETAS CHOCOLATE ", 12),
        11: ("GALLETAS FRESA ", 12),
        12: ("GALLETAS VAINILLA ", 12),
    }

    if productoActual not in productos:
        reproducir_sonido(error_sound)
        numeroPantalla.set(" CODIGO NO VALIDO... ")
    else:
        nombreProducto, precioProducto = productos[productoActual]
        if monto >= precioProducto:
            reproducir_sonido(dispensador)
            numeroPantalla.set(f" ELIGIO {nombreProducto}")
            saldo.set(monto - precioProducto)
            saldoPantalla.set(f"${saldo.get()}")  # Actualizar pantalla de saldo
        else:
            numeroPantalla.set(" SALDO INSUFICIENTE ")
            reproducir_sonido(error_sound)



# Función para actualizar la marquesina
def actualizar_marquesina():
    texto = numeroPantalla.get()
    if len(texto) > 0:
        nuevo_texto = texto[1:] + texto[0]  # Mover el primer carácter al final
        numeroPantalla.set(nuevo_texto)
    raiz.after(200, actualizar_marquesina)  # Llamar a la función cada 200 ms

# Iniciar la marquesina
actualizar_marquesina()

# Colocamos un espacio para que la primera columna no se ocupe
Label1 = Label(miFrame, bg="#5C5C5D")
Label1.grid(row=0, column=0, columnspan=11, padx=10, pady=10)
Label2 = Label(miFrame, bg="#5C5C5D")
Label2.grid(row=0, column=0, rowspan=24, padx=10, pady=10)
Label3 = Label(miFrame, bg="#5C5C5D")
Label3.grid(row=10, column=10, rowspan=24, padx=10, pady=10)
Label4 = Label(miFrame, bg="#5C5C5D")
Label4.grid(row=24, column=24, columnspan=11, padx=10, pady=10)
Label5 = Label(miFrame, bg="#5C5C5D")
Label5.grid(row=0, column=5, rowspan=24, padx=10, pady=10)

# Agregamos los label de texto
for i, (text, row, column) in enumerate([
    ("(1)", 6, 1), ("(2)", 6, 2), ("(3)", 6, 3), ("(4)", 6, 4),
    ("(5)", 12, 1), ("(6)", 12, 2), ("(7)", 12, 3), ("(8)", 12, 4),
    ("(9)", 18, 1), ("(10)", 18, 2), ("(11)", 18, 3), ("(12)", 18, 4)
]):
    texto = Label(miFrame, text=text, font=("SF Pro Display", 14), bg="#3B3B49")
    texto.grid(row=row, column=column, padx=10, pady=10)
    texto.config(justify="center")

# Sección de imágenes de productos
productos_imagenes = [
    ("productos/papas1.png", 1, 1, 5, 1),
    ("productos/papas2.png", 1, 2, 5, 1),
    ("productos/papas3.png", 1, 3, 5, 1),
    ("productos/papas4.png", 1, 4, 5, 1),
    ("productos/papas5.png", 7, 1, 5, 1),
    ("productos/jugo1.png", 7, 2, 5, 1),
    ("productos/jugo2.png", 7, 3, 5, 1),
    ("productos/jugo3.png", 7, 4, 5, 1),
    ("productos/galletas1.png", 13, 1, 5, 1),
    ("productos/galletas2.png", 13, 2, 5, 1),
    ("productos/galletas3.png", 13, 3, 5, 1),
    ("productos/galletas4.png", 13, 4, 5, 1),
]

for path, row, column, rowspan, columnspan in productos_imagenes:
    img = Image.open(path)
    resized_img = img.resize((150, 200), Image.LANCZOS)
    tk_img = ImageTk.PhotoImage(resized_img)
    label_img = Label(miFrame, image=tk_img, bg="#494B4A")
    label_img.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
    label_img.image = tk_img  # Guardar referencia de la imagen

#-------------------SECCIÓN DE BOTONES DE SELECCIÓN DE PRODUCTO---------------------------------
# Se colocan los botones para la selección de productos:
boton1 = Button(miFrame, text="1", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPulsado("1"))
boton1.grid(row=8, column=6, padx=10, pady=10)
boton2 = Button(miFrame, text="2", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPulsado("2"))
boton2.grid(row=8, column=7, padx=10, pady=10)
boton3 = Button(miFrame, text="3", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPulsado("3"))
boton3.grid(row=8, column=8, padx=10, pady=10)
boton4 = Button(miFrame, text="4", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPulsado("4"))
boton4.grid(row=8, column=9, padx=10, pady=10)
boton5 = Button(miFrame, text="5", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPulsado("5"))
boton5.grid(row=9, column=6, padx=10, pady=10)
boton6 = Button(miFrame, text="6", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPulsado("6"))
boton6.grid(row=9, column=7, padx=10, pady=10)
boton7 = Button(miFrame, text="7", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPulsado("7"))
boton7.grid(row=9, column=8, padx=10, pady=10)
boton8 = Button(miFrame, text="8", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPulsado("8"))
boton8.grid(row=9, column=9, padx=10, pady=10)
boton9 = Button(miFrame, text="9", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPulsado("9"))
boton9.grid(row=10, column=6, padx=10, pady=10)
boton10 = Button(miFrame, text="0", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPulsado("0"))
boton10.grid(row=10, column=7, padx=10, pady=10)

botonEnter = Button(miFrame, text="✔", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=leerCodigo)
botonEnter.grid(row=10, column=8, padx=5, pady=5)
botonBorrar = Button(miFrame, text="X", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command=lambda: numeroPantalla.set(""))
botonBorrar.grid(row=10, column=9, padx=5, pady=5)

# Sección de botones para la inserción de monedas
# Cargar y redimensionar la primera imagen
peso1 = Image.open("peso1.png")
resized_peso1 = peso1.resize((50, 50), Image.LANCZOS)
moneda_1 = ImageTk.PhotoImage(resized_peso1)
moneda1 = Button(miFrame, image=moneda_1, borderwidth=0, highlightthickness=0, bg="#5C5C5D", command=lambda: manejar_evento_moneda(1, coins))
moneda1.grid(row=15, column=6)
moneda1.image = moneda_1  # Guardar referencia de la imagen

# Cargar y redimensionar la segunda imagen
peso2 = Image.open("peso2.png")
resized_peso2 = peso2.resize((50, 50), Image.LANCZOS)
moneda_2 = ImageTk.PhotoImage(resized_peso2)
moneda2 = Button(miFrame, image=moneda_2, borderwidth=0, highlightthickness=0, bg="#5C5C5D", command=lambda: manejar_evento_moneda(2, coins))
moneda2.grid(row=15, column=7)
moneda2.image = moneda_2  # Guardar referencia de la imagen

# Cargar y redimensionar la tercera imagen
peso5 = Image.open("peso5.png")
resized_peso5 = peso5.resize((50, 50), Image.LANCZOS)
moneda_5 = ImageTk.PhotoImage(resized_peso5)
moneda5 = Button(miFrame, image=moneda_5, borderwidth=0, highlightthickness=0, bg="#5C5C5D", command=lambda: manejar_evento_moneda(5, coins))
moneda5.grid(row=15, column=8)
moneda5.image = moneda_5  # Guardar referencia de la imagen

# Cargar y redimensionar la cuarta imagen
peso10 = Image.open("peso10.png")
resized_peso10 = peso10.resize((50, 50), Image.LANCZOS)
moneda_10 = ImageTk.PhotoImage(resized_peso10)
moneda10 = Button(miFrame, image=moneda_10, borderwidth=0, highlightthickness=0, bg="#5C5C5D", command=lambda: manejar_evento_moneda(10, coins))
moneda10.grid(row=15, column=9)
moneda10.image = moneda_10  # Guardar referencia de la imagen

# nombreLabel = Label(miFrame, text = "PANTALLA:")
# nombreLabel.place()


#--------------TEXTO PARA LOS PRECIOS:--------------------------
precio0 = Label(miFrame, text="LISTA PRECIOS", fg="#8CA0AB", font=("DS-DIGITAL", 14), bg="#3B3B49", width=20)
precio0.grid(row=16, column=6, columnspan=4)
precio1 = Label(miFrame, text="- PAPAS SOL $18", fg="#8CA0AB", anchor="w", font=("DS-DIGITAL", 14, "bold"), bg="#3B3B49", width=20)
precio1.grid(row=17, column=6, columnspan=4)
precio2 = Label(miFrame, text="- JUGOS DEL VALLE $15", fg="#8CA0AB", anchor="w", font=("DS-DIGITAL", 14, "bold"), bg="#3B3B49", width=20)
precio2.grid(row=18, column=6, columnspan=4)
precio3 = Label(miFrame, text="- GALLETAS $12", fg="#8CA0AB", anchor="w", font=("DS-DIGITAL", 14, "bold"), bg="#3B3B49", width=20)
precio3.grid(row=19, column=6, columnspan=4)


raiz.mainloop()

