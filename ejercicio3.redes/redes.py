import networkx as nx

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
    return resultado
