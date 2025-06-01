import networkx as nx
import time
RESULTADOS = []

def construir_grafo(distancias, D, b, k):
    n = len(distancias)
    G = nx.DiGraph()
    fuente = 'S'
    sumidero = 'T'

    G.add_node(fuente)
    G.add_node(sumidero)

    for i in range(n):
        entrada = f'in_{i}'
        salida = f'out_{i}'
        G.add_node(entrada)
        G.add_node(salida)
        G.add_edge(fuente, entrada, capacity=k)
        G.add_edge(salida, sumidero, capacity=b)

    for i in range(n):
        for j in range(n):
            if i != j and distancias[i][j] < D:
                G.add_edge(f'in_{i}', f'out_{j}', capacity=1)

    return G

def asignar_respaldo(distancias, D, b, k):
    t1 = time.time()
    G = construir_grafo(distancias, D, b, k)
    flujo_total, flujo = nx.maximum_flow(G, 'S', 'T')
    n = len(distancias)

    if flujo_total < n * k:
        return None

    resultado = [[] for _ in range(n)]
    for i in range(n):
        entrada = f'in_{i}'
        for j in range(n):
            if i != j and distancias[i][j] < D:
                salida = f'out_{j}'
                if flujo[entrada].get(salida, 0) == 1:
                    resultado[i].append(j)
    print(resultado)
    t2 = time.time()
    print(t1-t2)
    return resultado




def leer_datos_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    D, k, b, N = map(int, lineas[0].strip().split())
    matriz = [list(map(int, line.strip().split())) for line in lineas[1:N+1]]
    return matriz, D, b, k

def escribir_resultados(nombre_salida):
    with open(nombre_salida, 'w') as archivo:
        for idx, resultado in enumerate(RESULTADOS, start=2):  # Comienza en 2 por set_redes_2.txt
            archivo.write(f"Set {idx}:\n")
            if resultado is None:
                archivo.write("No existe solución\n")
            else:
                for i, respaldos in enumerate(resultado):
                    archivo.write(f"  Nodo {i} respaldado por: {respaldos}\n")
            archivo.write("\n")

if __name__ == "__main__":
    archivo2 = "set_redes_2.txt"
    archivo3 = "set_redes_3.txt"
    archivo4 = "set_redes_4.txt"
    archivo5 = "set_redes_5.txt"
    archivo6 = "set_redes_6.txt"


    matriz2, D2, b2, k2 = leer_datos_desde_archivo(archivo2)
    resultado2 = asignar_respaldo(matriz2, D2, b2, k2)
    RESULTADOS.append(resultado2)

    matriz3, D3, b3, k3 = leer_datos_desde_archivo(archivo3)
    resultado3 = asignar_respaldo(matriz3, D3, b3, k3)
    RESULTADOS.append(resultado3)

    matriz4, D4, b4, k4 = leer_datos_desde_archivo(archivo4)
    resultado4 = asignar_respaldo(matriz4, D4, b4, k4)
    RESULTADOS.append(resultado4)

    matriz5, D5, b5, k5 = leer_datos_desde_archivo(archivo5)
    resultado5 = asignar_respaldo(matriz5, D5, b5, k5)
    RESULTADOS.append(resultado5)

    matriz6, D6, b6, k6 = leer_datos_desde_archivo(archivo6)
    resultado6 = asignar_respaldo(matriz6, D6, b6, k6)
    RESULTADOS.append(resultado6)

    escribir_resultados("resultados.txt")
    
