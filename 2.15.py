def calcularPromedio(*args):
    promedio = sum(args) / len(args)
    return promedio

resultado = calcularPromedio(10, 7, 5, 8)
print(f"El promedio de las notas es: {resultado:.2f}")
