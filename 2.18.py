ventasDiarias = [200, 450, 300, 400, 350, 500, 600]

def procesarVentas(ventas):
    totalVentas = sum(ventas)
    
    promedioVentas = totalVentas / len(ventas) if len(ventas) > 0 else 0
    
    return totalVentas, promedioVentas

totalVentas, promedioVentas = procesarVentas(ventasDiarias)
print(f"Total de ventas: {totalVentas}")
print(f"Promedio de ventas por día: {promedioVentas:.2f}")
