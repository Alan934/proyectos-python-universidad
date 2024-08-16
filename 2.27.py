ventasMensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def calcularVentas(ventas):
    totalVentas = sum(ventas)
    promedioMensual = totalVentas / len(ventas)
    mesMayoresVentas = ventas.index(max(ventas)) + 1
    
    estadisticas = {
        "totalVentas": totalVentas,
        "promedioMensual": promedioMensual,
        "mesMayoresVentas": mesMayoresVentas
    }
    
    return estadisticas

estadisticasVentas = calcularVentas(ventasMensuales)
print(estadisticasVentas)
