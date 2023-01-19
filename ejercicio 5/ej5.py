#n elemenos, w peso maximo, val valores, weight pesos

def mochila(n, w, val, weight):
    if n == 0 or w == 0:
        return 0
    if weight[n-1] > w:
        return mochila(n-1, w, val, weight)
    else:
        return max(val[n-1] + mochila(n-1, w-weight[n-1], val, weight), mochila(n-1, w, val, weight))

def main():
    precio = [103, 60, 70, 5, 15]
    pesos = [12, 23, 11, 15, 7]
    peso_maximo = 100
    n = len(precio)
    valor_maximo = mochila(n, peso_maximo, precio, pesos)
    print(valor_maximo)
