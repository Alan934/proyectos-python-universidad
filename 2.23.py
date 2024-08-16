inventario = [50, 30, 20, 10]

ventas = [5, 10, 5, 2]

def actualizarInventario(inventario, ventas):
    inventarioActualizado = []
    
    for cantidadDisponible, cantidadVendida in zip(inventario, ventas):
        inventarioActualizado.append(cantidadDisponible - cantidadVendida)
    
    return inventarioActualizado

inventarioActualizado = actualizarInventario(inventario, ventas)
print(inventarioActualizado)
