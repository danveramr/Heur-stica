import time
inicio = time.time()

# Puzle Lineal con busqueda en amplitud
from arbol import Nodo

def en_orden(hijo, solucion):
    e_o = 0  
    for i, elemento in enumerate(hijo):  
        if elemento == solucion[i]:
            e_o += 1  
    return e_o


def b_s_b(e0, solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[]
    nodoInicial = Nodo(e0)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera)!=0:
        nodo=nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            # solucion encontrada
            solucionado=True
            return nodo
        else:
            # expandir nodos hijo
            d_n = nodo.get_datos()
            # operador izquierdo
            hijo=[d_n[1], d_n[0], d_n[2], d_n[3]]
            ordenados_izq = en_orden(hijo, solucion)
            #print(ordenados_izq)
            hijo_izq = Nodo(hijo)
            
            # operador central
            hijo=[d_n[0], d_n[2], d_n[1], d_n[3]]
            ordenados_centro = en_orden(hijo, solucion)
            #print(ordenados_centro)
            hijo_centro = Nodo(hijo)
            
            # operador derecho
            hijo = [d_n[0], d_n[1], d_n[3], d_n[2]]
            ordenados_der = en_orden(hijo, solucion)
            #print(ordenados_der)
            hijo_der = Nodo(hijo)
            
            
            if ordenados_izq <= ordenados_centro and ordenados_izq<= ordenados_der:
                if ordenados_centro <= ordenados_der:
                    if not hijo_der.en_lista(nodos_visitados) and not hijo_der.en_lista(nodos_frontera):
                        nodos_frontera.append(hijo_der)
                        nodo.set_hijos([hijo_der])
                    else:
                        nodos_frontera.append(hijo_centro)
                        nodo.set_hijos([hijo_centro])
                else:
                    if not hijo_centro.en_lista(nodos_visitados) and not hijo_centro.en_lista(nodos_frontera):
                        nodos_frontera.append(hijo_centro)
                        nodo.set_hijos([hijo_centro])
                    else:
                        nodos_frontera.append(hijo_der)
                        nodo.set_hijos([hijo_der])
            else:
               if not hijo_izq.en_lista(nodos_visitados) and not hijo_izq.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo_izq)
                    nodo.set_hijos([hijo_izq])
               else:
                    nodos_frontera.append(hijo_centro)
                    nodo.set_hijos([hijo_centro])     
            
            
if __name__ == "__main__":
    e0 = [4, 1, 3, 2]
    solucion = [1, 2, 3, 4]
    nodo_solucion = b_s_b(e0, solucion)
    #print(nodo_solucion.get_padre())
    # mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        #print(resultado)
        nodo = nodo.get_padre()

    resultado.append(e0)
    resultado.reverse()
    print(resultado)
    time.sleep(1)

    fin = time.time()
print("\nTiempo de ejecución: " + str(fin - inicio) + "s")
