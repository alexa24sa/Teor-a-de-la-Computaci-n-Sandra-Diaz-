from tkinter import * 
from PIL import Image, ImageTk
import os

#colocamos la raíz de la siguiente manera
raiz = Tk()
raiz.config(bg="#5C5C5D")
raiz.title("Máquina expendedora:")
miFrame = Frame(raiz, width = 1080, height=1920, bg="#5C5C5D")
miFrame.pack()


#cuadroTexto = Entry (miFrame)
#cuadroTexto.grid(row= 0, column=0, columnspan=)
#definimos las variables usadas en la lógica del programa
#producto = IntVar()
#nombreProducto = StringVar["Papas Sol Naturales", "Papas Sol Adobadas", "Papas Sol Limón",
#                           "Papas Sol Extremas", "Papas Sol Queso", "Jugo del Valle Naranja", 
#                            "Jugo del Valle Guayaba", "Jugo del Valle Mango", "Galletas María",
#                             "Galletas Cremax Chocolate", "Galletas Cremax Fresa", "Galletas Cremax Vainilla" ]
#dinero = IntVar()
#precioProducto = IntVar()
# Variables
numeroPantalla = StringVar()  # Para mostrar el producto elegido
saldo = IntVar(value=0)  # Para manejar el saldo acumulado
saldoPantalla = StringVar(value="$0")  # Para mostrar el saldo en la pantalla

# Pantalla de texto para elegir productos
pantallaProducto = Entry(miFrame, fg="#11FCB2", font=("DS-DIGITAL", 16), bg="#323232", textvariable=numeroPantalla)
pantallaProducto.grid(row=2, column=6, rowspan=4, columnspan=4, padx=5, pady=5)
pantallaProducto.config(justify="center")

# Pantalla de texto para mostrar el saldo
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
    if nuevo_saldo > 0:
        numeroPantalla.set("Elige tu producto")

# Función para añadir monto al saldo
def agregarMoneda(monto):
    actualizarSaldo(monto)


#-----------Pulsasiones teclado-----------------

def numeroPulsado(num): #la función recibe el parámetro num
    numeroPantalla.set(numeroPantalla.get() + num)





#colocamos un espacio para que la primera columna no se ocupe:
Label1 = Label(miFrame, bg="#5C5C5D")
Label1.grid(row= 0, column= 0, columnspan= 11, padx= 10, pady=10)
Label2 = Label(miFrame, bg="#5C5C5D")
Label2.grid(row= 0, column= 0, rowspan=24, padx=10, pady=10)
Label3 = Label(miFrame, bg="#5C5C5D")
Label3.grid(row= 10, column= 10, rowspan=24, padx=10, pady=10)
Label4 = Label(miFrame, bg="#5C5C5D")
Label4.grid(row= 24, column= 24, columnspan= 11, padx= 10, pady=10)
Label5 = Label(miFrame, bg="#5C5C5D")
Label5.grid(row= 0, column= 5, rowspan= 24, padx= 10, pady=10)

#Agregamos las imagenes:



#------------------LABEL DEL CÓDIGO DE CADA PRODUCTO:----------------------------
#Agregamos los label de texto:
texto1 = Label(miFrame, text="(1)", font=("SF Pro Display", 14), bg="#3B3B49")
texto1.grid(row= 6, column= 1, padx= 10, pady=10)
texto1.config(justify="center")
texto2 = Label(miFrame, text="(2)", font=("SF Pro Display", 14), bg="#3B3B49")
texto2.grid(row= 6, column= 2, padx= 10, pady=10)
texto2.config(justify="center")
texto3 = Label(miFrame, text="(3)", font=("SF Pro Display", 14), bg="#3B3B49")
texto3.grid(row= 6, column= 3, padx= 10, pady=10)
texto3.config(justify="center")
texto4 = Label(miFrame, text="(4)", font=("SF Pro Display", 14), bg="#3B3B49")
texto4.grid(row= 6, column= 4, padx= 10, pady=10)
texto4.config(justify="center")
texto5 = Label(miFrame, text="(5)", font=("SF Pro Display", 14), bg="#3B3B49")
texto5.grid(row= 12, column= 1, padx= 10, pady=10)
texto5.config(justify="center")
texto6 = Label(miFrame, text="(6)", font=("SF Pro Display", 14), bg="#3B3B49")
texto6.grid(row= 12, column= 2, padx= 10, pady=10)
texto6.config(justify="center")
texto7 = Label(miFrame, text="(7)", font=("SF Pro Display", 14), bg="#3B3B49")
texto7.grid(row= 12, column= 3, padx= 10, pady=10)
texto7.config(justify="center")
texto8 = Label(miFrame, text="(8)", font=("SF Pro Display", 14), bg="#3B3B49")
texto8.grid(row= 12, column= 4, padx= 10, pady=10)
texto8.config(justify="center")
texto9 = Label(miFrame, text="(9)", font=("SF Pro Display", 14), bg="#3B3B49")
texto9.grid(row= 18, column= 1, padx= 10, pady=10)
texto9.config(justify="center")
texto10 = Label(miFrame, text="(10)", font=("SF Pro Display", 14), bg="#3B3B49")
texto10.grid(row= 18, column= 2, padx= 10, pady=10)
texto10.config(justify="center")
texto11 = Label(miFrame, text="(11)", font=("SF Pro Display", 14), bg="#3B3B49")
texto11.grid(row= 18, column= 3, padx= 10, pady=10)
texto11.config(justify="center")
texto12 = Label(miFrame, text="(12)", font=("SF Pro Display", 14), bg="#3B3B49")
texto12.grid(row= 18, column= 4, padx= 10, pady=10)
texto12.config(justify="center")

#Se crea la función antes de los botones que lee los números insertados mediante el teclado:
#recuerda que el valor máximo que deja insertar la máquina es de 18 pesos, los productos son los siguientes
# Papas sol - $18, sabores (naturales, adobadas, limón, extremas y queso)
# Jugos del Valle - $15 sabores (naranja, guayaba, mango)
# Galletas - $12 sabores (María, Chocolate, Fresa, Vainila)
#def leerProducto:
#    if (dinero == 18):
#        producto.set("Ha elegido el producto" + nombreProducto)
#        #caso papas: se puede comprar todo, incluso papas que cuestan 18
#        dinero = dinero - precioProducto
#    else if (dinero >= 15 && dinero < 18):
#        #caso jugos: el costo de los jugos es de 15 
#        producto.set("Ha elegido el producto" + nombreProducto) #ya no puede elegir papas sol ya que cuestan 18
#        dinero = dinero - precioProducto
#    else if (dinero>= 12 && dinero < 15):
#        #caso galletas: el costo de las galletas es de 12
#        producto.set("Ha elegido el producto" + nombreProducto) #ya no se pueden elegir jugos del Valle, ya que cuestan 15

#-------------------SECCIÓN DE IMAGENES DE PRODUCTOS------------------------------------------
papasSolNaturales = Image.open("productos/papas1.png")
resized_papas1 = papasSolNaturales.resize((150, 200), Image.LANCZOS)
papa_1 = ImageTk.PhotoImage(resized_papas1)
image1 = Label(miFrame, image=papa_1, bg="#494B4A")
image1.grid(row=1, column=1, rowspan=5, columnspan=1)

papasSolLimon = Image.open("productos/papas2.png")
resized_papas2 = papasSolLimon.resize((150, 200), Image.LANCZOS)
papa_2 = ImageTk.PhotoImage(resized_papas2)
image2 = Label(miFrame, image=papa_2, bg="#494B4A")
image2.grid(row=1, column=2, rowspan=5, columnspan=1)

papasSolAdobadas = Image.open("productos/papas3.png")
resized_papas3 = papasSolAdobadas.resize((150, 200), Image.LANCZOS)
papa_3 = ImageTk.PhotoImage(resized_papas3)
image3 = Label(miFrame, image=papa_3, bg="#494B4A")
image3.grid(row=1, column=3, rowspan=5, columnspan=1)

papasSolExtremas = Image.open("productos/papas4.png")
resized_papas4 = papasSolExtremas.resize((150, 200), Image.LANCZOS)
papa_4 = ImageTk.PhotoImage(resized_papas4)
image4 = Label(miFrame, image=papa_4, bg="#494B4A")
image4.grid(row=1, column=4, rowspan=5, columnspan=1)

papasSolQueso = Image.open("productos/papas5.png")
resized_papas5 = papasSolQueso.resize((150, 200), Image.LANCZOS)
papa_5 = ImageTk.PhotoImage(resized_papas5)
image5 = Label(miFrame, image=papa_5, bg="#494B4A")
image5.grid(row=7, column=1, rowspan=5, columnspan=1)

jugoValleMango = Image.open("productos/jugo1.png")
resized_jugo1 = jugoValleMango.resize((150, 200), Image.LANCZOS)
jugo_1 = ImageTk.PhotoImage(resized_jugo1)
image6 = Label(miFrame, image=jugo_1, bg="#494B4A")
image6.grid(row=7, column=2, rowspan=5, columnspan=1)

jugoValleGuayaba = Image.open("productos/jugo2.png")
resized_jugo2 = jugoValleGuayaba.resize((150, 200), Image.LANCZOS)
jugo_2 = ImageTk.PhotoImage(resized_jugo2)
image7 = Label(miFrame, image=jugo_2, bg="#494B4A")
image7.grid(row=7, column=3, rowspan=5, columnspan=1)

jugoValleNaranja = Image.open("productos/jugo3.png")
resized_jugo3 = jugoValleNaranja.resize((150, 200), Image.LANCZOS)
jugo_3 = ImageTk.PhotoImage(resized_jugo3)
image8 = Label(miFrame, image=jugo_3, bg="#494B4A")
image8.grid(row=7, column=4, rowspan=5, columnspan=1)

galletasMaria = Image.open("productos/galletas1.png")
resized_galletas1 = galletasMaria.resize((150, 150), Image.LANCZOS)
galletas_1 = ImageTk.PhotoImage(resized_galletas1)
image9 = Label(miFrame, image=galletas_1, bg="#494B4A")
image9.grid(row=13, column=1, rowspan=5, columnspan=1)

galletasCremaxChocolate = Image.open("productos/galletas2.png")
resized_galletas2 = galletasCremaxChocolate.resize((150, 150), Image.LANCZOS)
galletas_2 = ImageTk.PhotoImage(resized_galletas2)
image10 = Label(miFrame, image=galletas_2, bg="#494B4A")
image10.grid(row=13, column=2, rowspan=5, columnspan=1)

galletasCremaxFresa = Image.open("productos/galletas3.png")
resized_galletas3 = galletasCremaxFresa.resize((150, 150), Image.LANCZOS)
galletas_3 = ImageTk.PhotoImage(resized_galletas3)
image11 = Label(miFrame, image=galletas_3, bg="#494B4A")
image11.grid(row=13, column=3, rowspan=5, columnspan=1)

galletasCremaxVainila = Image.open("productos/galletas4.png")
resized_galletas4 = galletasCremaxVainila.resize((150, 150), Image.LANCZOS)
galletas_4 = ImageTk.PhotoImage(resized_galletas4)
image12 = Label(miFrame, image=galletas_4, bg="#494B4A")
image12.grid(row=13, column=4, rowspan=5, columnspan=1)

#-------------------SECCIÓN DE BOTONES DE SELECCIÓN DE PRODUCTO---------------------------------
#Se colocan los botones para la selección de productos:
boton1 = Button(miFrame, text="1", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("1"))
boton1.grid(row= 8, column=6, padx=10, pady=10)
boton2 = Button(miFrame, text="2", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("2"))
boton2.grid(row= 8, column=7, padx=10, pady=10)
boton3 = Button(miFrame, text="3", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("3"))
boton3.grid(row= 8, column=8, padx=10, pady=10)
boton4 = Button(miFrame, text="4", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("4"))
boton4.grid(row= 8, column=9, padx=10, pady=10)
boton5 = Button(miFrame, text="5", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("5"))
boton5.grid(row= 9, column=6, padx=10, pady=10)
boton6 = Button(miFrame, text="6", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("6"))
boton6.grid(row= 9, column=7, padx=10, pady=10)
boton7 = Button(miFrame, text="7", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("7"))
boton7.grid(row= 9, column=8, padx=10, pady=10)
boton8 = Button(miFrame, text="8", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("8"))
boton8.grid(row= 9, column=9, padx=10, pady=10)
boton9 = Button(miFrame, text="9", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("9"))
boton9.grid(row= 10, column=6, padx=10, pady=10)
boton10 = Button(miFrame, text="0", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("0"))
boton10.grid(row= 10, column=7, padx=10, pady=10)
boton11 = Button(miFrame, text="✔", fg="#FFFFFF", font=("SF Pro Display", 14), bg="#323232", command= lambda: numeroPulsado("11"))
boton11.grid(row= 10, column=8, padx=10, pady=10)

#-------------------------SECCIÓN DE BOTONES PARA LA INSERCIÓN DE MONEDAS--------------------------------






# Cargar y redimensionar la primera imagen
peso1 = Image.open("peso1.png")
resized_peso1 = peso1.resize((50, 50), Image.LANCZOS)
moneda_1 = ImageTk.PhotoImage(resized_peso1)
moneda1 = Button(miFrame, image=moneda_1, borderwidth=0, highlightthickness=0, bg="#5C5C5D", command=lambda: agregarMoneda(1))
moneda1.grid(row=15, column=6)
moneda1.image = moneda_1  # Guardar referencia de la imagen

# Cargar y redimensionar la segunda imagen
peso2 = Image.open("peso2.png")
resized_peso2 = peso2.resize((50, 50), Image.LANCZOS)
moneda_2 = ImageTk.PhotoImage(resized_peso2)
moneda2 = Button(miFrame, image=moneda_2, borderwidth=0, highlightthickness=0, bg="#5C5C5D", command=lambda: agregarMoneda(2))
moneda2.grid(row=15, column=7)
moneda2.image = moneda_2  # Guardar referencia de la imagen

# Cargar y redimensionar la tercera imagen
peso5 = Image.open("peso5.png")
resized_peso5 = peso5.resize((50, 50), Image.LANCZOS)
moneda_5 = ImageTk.PhotoImage(resized_peso5)
moneda5 = Button(miFrame, image=moneda_5, borderwidth=0, highlightthickness=0, bg="#5C5C5D", command=lambda: agregarMoneda(5))
moneda5.grid(row=15, column=8)
moneda5.image = moneda_5  # Guardar referencia de la imagen

# Cargar y redimensionar la cuarta imagen
peso10 = Image.open("peso10.png")
resized_peso10 = peso10.resize((50, 50), Image.LANCZOS)
moneda_10 = ImageTk.PhotoImage(resized_peso10)
moneda10 = Button(miFrame, image=moneda_10, borderwidth=0, highlightthickness=0, bg="#5C5C5D", command=lambda: agregarMoneda(10))
moneda10.grid(row=15, column=9)
moneda10.image = moneda_10  # Guardar referencia de la imagen
#nombreLabel = Label(miFrame, text = "PANTALLA:")
#nombreLabel.place()



#siempre se coloca en loop la apertura del main hasta el final
raiz.mainloop()
