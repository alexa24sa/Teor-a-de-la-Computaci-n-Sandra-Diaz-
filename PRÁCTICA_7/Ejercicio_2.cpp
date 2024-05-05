/*Ejercicio 2: Diseña un programa similar al anterior, pero ahora para el lenguaje L= { w*w^I | w pertenece {a,b}* }
donde w^I es la cadena inversa de w. Por ejemplo, la cadena abba sí pertenece al lenguaje, pero la cadena ababaa
no pertenece*/
//DECLARACIÓN DE LIBRERÍAS
#include<iostream>
//#include<conio.h>
#include<string>
#include <chrono>
#include <thread> //para usar sleep

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
	char dato;
	string cadena;
	bool valido=true;
	int i=0, tam=0;
	
	cout<<"Digite un elemento de su cadena completa, en caso de ser cadena vac"<<char(161)<<"a inserte E: ";
	cin >> cadena;
	
	tam = cadena.length();
	char aux;
	
	if (cadena =="E" || cadena =="e"){
	    cout<<"\nLa cadena w insertada, pertenece Lenjuage y es la siguiente "<< char(157)<< endl;
		return 0;
	}
	
	if((tam%2)!=0){
	    cout<<"La cadena "<<cadena<<" NO es v"<<char(160)<<"lida.";
	    return 0;
	}
	valido= true;
	
	for(i = 0; i <= ((tam/2) - 1); i++){
	    agregarPila(pila, cadena[i]);
	}
	// Revisión de la lógica de comparación para asegurarnos de que es correcta
    for(i = tam/2; i < tam; i++){
        sacarPila(pila, dato);
        if(dato != cadena[i]){ // Esto compara el último caracter de la primera mitad con el primer caracter de la segunda mitad, y así sucesivamente.
            valido = false;
            break;
        }
    }

 
	
	if (valido == true){
	    cout<< "La cadena w insertada SI es v"<<char(160)<<"lida.\n";
	}else {
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
	
	//cout <<"\tel elemento en la cima es: "<<pila->dato<<endl;
	//cout <<"\t Elemento "<<n<<" ha sido agregado a la pila correctamente\n"; //línea usada para comprobar funcionamiento	
}


void sacarPila(Nodo *&pila, char &n){
    //Recordemos de la pila tiene una lógica de programación siguiente: LIFO
    Nodo *aux = pila; //a la variable auxiliar se le asigna el valor de la cima de la pila
    n = aux-> dato; /*"a la variable n se le asignará el último valor específico contenido dentro de "dato"
    es decir, que se le asigna la cima de la pila*/
    pila = aux -> siguiente; /*ahora a pila se le asigna el valor de la siguiente dirección de memoria
    , es decir irémos avanzando entre los elementos de la pila, y ahora pila se encontrará en la penúltima 
    posición*/
    //cout <<"\tel elemento en la cima es: "<<pila->dato<<endl;
    //cout <<"\t Elemento "<<n<<" ha sacado de la pila correctamente\n"; //solo se usa esta línea para comprobar funcionamiento
    //this_thread::sleep_for(chrono::seconds(3));//se queda en espera por 1s antes de ejecutar la siguiente instrucción
    delete aux; //eliminamos lo contenido dentro de la variable auxiliar 
}
