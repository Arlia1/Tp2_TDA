import time
import random
import string

def min_palindromos(palabra):
    t1 = time.time()
    n = len(palabra)
    palabra = palabra.upper()

    opt = [float('inf')] * (n + 1)
    opt[n] = 0

    es_palindromo = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if palabra[i] == palabra[j] and (j - i <= 1 or es_palindromo[i + 1][j - 1]):
                es_palindromo[i][j] = True

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if es_palindromo[i][j]:
                opt[i] = min(opt[i], 1 + opt[j + 1])
    
    t2 = time.time()

    print(opt[0])
    print("Tiempo de ejecución:", t2 - t1)
    print("\n\n")
    return opt[0]


if __name__ == "__main__":

    archivo_lectura = "set_datos_1.txt"
    archivo_escritura = "resultados.txt"

    with open(archivo_lectura, 'r') as f:
        with open(archivo_escritura, 'w') as fw:
            for linea in f:
                palabra = linea.strip()
                resultado = min_palindromos(palabra)
                fw.write(f"{palabra}: {resultado}\n")

