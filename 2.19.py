resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def calcularGoles(resultados):
    totalGoles_anotados = 0
    totalGoles_recibidos = 0
    
    for equipo, (goles_anotados, goles_recibidos) in resultados.items():
        totalGoles_anotados += goles_anotados
        totalGoles_recibidos += goles_recibidos
    
    return totalGoles_anotados, totalGoles_recibidos

totalAnotados, totalRecibidos = calcularGoles(resultados)
print(f"Total de goles anotados: {totalAnotados}")
print(f"Total de goles recibidos: {totalRecibidos}")
