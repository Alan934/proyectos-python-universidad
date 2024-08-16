paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

def calcularTotalPaquetes(paquetes):
    preciosTotales = {}
    
    for destino, precioDia, duracion in paquetes:
        precioTotal = precioDia * duracion
        preciosTotales[destino] = precioTotal
    
    return preciosTotales

precios_totales = calcularTotalPaquetes(paquetes)
print(precios_totales)
