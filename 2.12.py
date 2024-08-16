productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]

def masCaro(productos):
    productoCaro = max(productos, key=lambda producto: producto[1])
    return productoCaro

resultado = masCaro(productos)
print("El producto más caro es:", resultado)