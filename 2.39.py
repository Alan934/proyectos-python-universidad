def mercado(preciosDiarios, operaciones):
    beneficioTotal = 0
    accionesCompradas = 0
    precioCompra = 0
    
    for operacion, dia in operaciones:
        precio = preciosDiarios[dia]
        
        if operacion == "compra":
            precioCompra = precio
            accionesCompradas += 1
            
        elif operacion == "venta":
            if accionesCompradas > 0:
                beneficioTotal += (precio - precioCompra)
                accionesCompradas -= 1
                
    return beneficioTotal

preciosDiarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

resultado = mercado(preciosDiarios, operaciones)

print(f"Beneficio o pérdida total: {resultado}")
