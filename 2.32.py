def simularVentas(*args):
    totalIngresos = 0
    
    for venta in args:
        producto, cantidad, precioUnidad = venta
        totalIngresos += cantidad * precioUnidad
    
    return totalIngresos

total = simularVentas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
)

print(f"Total de ingresos: ${total:.2f}")
