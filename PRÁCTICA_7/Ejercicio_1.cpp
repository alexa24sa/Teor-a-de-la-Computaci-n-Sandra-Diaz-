/*Ejercicio 1: Diseña un programa que acepte caracter a caracter una cadena w que determine si w pertenece
al lenguaje L= { a^n*b^n | n >= 0}. Para hacerlo deberás emplear una sola pila e ingresar o sacar de la 
pila, un caracter a la vez. Al finalizar la entrada de caracteres, tu programa debe imprimir un mensaje en
pantalla indicando si w pertenece o no a L*/
//DECLARACIÓN DE LIBRERÍAS
#include<iostream>
//#include<conio.h>
#include<string>
#include<cctype> // Para funciones de manejo de caracteres, como isalpha()

using namespace std;

//creamos una función global:
//realizamos la estrcutura de nodo:
	
	struct Nodo {
		char dato;//valor que estara contenido dentro del struct Nodo
		Nodo *siguiente; //apuntador al siguiente nodo
	};

void agregarPila(Nodo *&, char);//se le pasan los parámetros de nodo como puntero por referencia y el otro es el dato 
void sacarPila(Nodo *&, char &);

//Prototipo de Función
int main(){
	//llamamos al struct dentro del main principal para poderla usar como pila
	Nodo *pila  = NULL; //inicializamos un struct de tipo Nodo como apuntador de nombre pila con valor de cero
	int longitud_a, longitud_b; //variable auxiliar
	char dato;
	char rpt;
	string cadena_a, cadena_b;
	bool valido=true;
	
	do{
		cout<<"Digite un elemento de su cadena a/b, en caso de ser cadena vac"<<char(161)<<"a inserte E: ";
		cin>>dato;
		agregarPila(pila, dato);
		
		if(pila->dato == 'a'){
		    if (longitud_b > 0){
		        valido = false;
		    }
		    longitud_a++;
		}else if ((pila->dato) =='E'||(pila->dato) =='e'){
		    cout<<"\nLa cadena w insertada, pertenece Lenjuage y es la siguiente "<< char(157);
		}else if (pila->dato == 'b'){
		    longitud_b++;
		} else {
		    cout << "Carácter inválido. Solo se permiten 'a' o 'b'.\n";
		}
		
		cout<<"\n Deseas agregar otro elemento a PILA(s/n): ";
		cin>>rpt;
		
	}while(tolower(rpt) == 's');
	
	if ((longitud_b == longitud_a)&&(valido=true)){
		    cout << "La cadena w insertada SI es v"<<char(160)<<"lida.\n";
		} else {
		    cout << "La cadena w insertada NO es v"<<char(160)<<"lida.\n";
		}
	
	return 0;
}

void agregarPila(Nodo *&pila, char n){
	Nodo  *nuevoNodo = new Nodo(); //reservamos memoria para un nuevo nodo
	nuevoNodo -> dato = n; /*guardar un nuevo elemento de la pila dentro del dato. Posteriormente
	se apunta a la variable de tipo "dato" dentro del struct y se almacenará en esta el valor de 
	la variable "n"*/
	nuevoNodo -> siguiente = pila; /*se comienza desde la pila para agregar apuntdando a la variable
	de tipo puntero llamada "siguiente" a la cuál se le asignará el valor de "pila" */
	pila = nuevoNodo; /*finalmente a "pila" se le asignará la dirección de memoria de nuevoNodo
	ya que dentro pila ya habrá un nuevo espacio en el que almacenar valores*/
	
	cout <<"\t Elemento "<<n<<" ha sido agregado a la pila correctamente\n";	
}


void sacarPila(Nodo *&pila, char &n){
    //Recordemos de la pila tiene una lógica de programación siguiente: LIFO
    Nodo *aux = pila; //a la variable auxiliar se le asigna el valor de la cima de la pila
    n = aux-> dato; /*"a la variable n se le asignará el último valor específico contenido dentro de "dato"
    es decir, que se le asigna la cima de la pila*/
    pila = aux -> siguiente; /*ahora a pila se le asigna el valor de la siguiente dirección de memoria
    , es decir irémos avanzando entre los elementos de la pila, y ahora pila se encontrará en la penúltima 
    posición*/
    delete aux; //eliminamos lo contenido dentro de la variable auxiliar 
}

