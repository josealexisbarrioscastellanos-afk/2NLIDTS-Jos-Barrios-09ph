class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
 
 
def direccion(nodo):
    # Equivalente a imprimir un apuntador en C++: direccion de memoria o nullptr
    return hex(id(nodo)) if nodo is not None else "None"
 
 
# Recorre la lista desde la cabeza hacia la cola
# Muestra tambien la direccion de memoria de cada nodo y sus enlaces
def ImprimirLista(cabeza):
    actual = cabeza
    while actual is not None:
        print(f"Dato: {actual.dato}"
              f" | Direccion: {direccion(actual)}"
              f" | Anterior: {direccion(actual.anterior)}"
              f" | Siguiente: {direccion(actual.siguiente)}")
        actual = actual.siguiente
    print()
 
 
# Recorre la lista desde la cola hacia la cabeza (usando el apuntador anterior)
def ImprimirListaReversa(cola):
    actual = cola
    while actual is not None:
        print(f"Dato: {actual.dato}"
              f" | Direccion: {direccion(actual)}"
              f" | Anterior: {direccion(actual.anterior)}"
              f" | Siguiente: {direccion(actual.siguiente)}")
        actual = actual.anterior
    print()
 
 
# En Python no hay delete ni paso por referencia: se desenlazan los nodos
# y la funcion devuelve (cabeza, cola) ya en None
def BorrarLista(cabeza, cola):
    contador = 0
    while cabeza is not None:
        siguiente = cabeza.siguiente
        contador += 1
        # Se imprime antes de desenlazar el nodo
        print(f"Elemento borrado {contador}"
              f" | Dato: {cabeza.dato}"
              f" | Direccion: {direccion(cabeza)}")
        # Se cortan los enlaces; el recolector de basura libera el nodo
        cabeza.siguiente = None
        cabeza.anterior = None
        cabeza = siguiente
    print(f"Total de elementos borrados: {contador}")
    cola = None
    return cabeza, cola
 
 
# Agrega un nodo al final; mantener la cola evita recorrer toda la lista
# Devuelve (cabeza, cola) porque Python no tiene paso por referencia
def agregarNodo(cabeza, cola, valor):
    nuevoNodo = Nodo(valor)  # Creando el nuevo elemento con sus apuntadores
 
    if cabeza is None:
        # Lista vacia: el nuevo nodo es cabeza y cola a la vez
        cabeza = nuevoNodo
        cola = nuevoNodo
    else:
        cola.siguiente = nuevoNodo  # El ultimo nodo apunta al nuevo
        nuevoNodo.anterior = cola   # El nuevo apunta de regreso al ultimo
        cola = nuevoNodo            # El nuevo pasa a ser la cola
    return cabeza, cola
 
 
def main():
    print("Actividad 08 - Lista Doblemente Enlazada")
    cabeza = None  # Apuntador al primer nodo
    cola = None    # Apuntador al ultimo nodo
 
    try:
        tamanoLista = int(input("Ingrese la cantidad de elementos de la lista enlazada: "))
    except ValueError:
        print("Cantidad de elementos no valida")
        return 1
    if tamanoLista <= 0:
        print("Cantidad de elementos no valida")
        return 1
 
    for i in range(tamanoLista):
        valor = int(input(f"Ingrese el dato {i + 1}: "))
        # Invocamos la funcion para agregar el Nodo
        cabeza, cola = agregarNodo(cabeza, cola, valor)
 
    print("\nImprimiendo lista (de inicio a fin):")
    ImprimirLista(cabeza)
 
    print("Imprimiendo lista (de fin a inicio):")
    ImprimirListaReversa(cola)
 
    print("\nBorrando lista de numeros")
    cabeza, cola = BorrarLista(cabeza, cola)
 
    return 0
 
 
if __name__ == "__main__":
    main()
