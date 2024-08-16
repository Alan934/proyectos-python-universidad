resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def calcularGoles(resultados):
    totalGolesAnotados = 0
    totalGolesRecibidos = 0
    
    for equipo, (goles_anotados, goles_recibidos) in resultados.items():
        totalGolesAnotados += goles_anotados
        totalGolesRecibidos += goles_recibidos
    
    return totalGolesAnotados, totalGolesRecibidos

totalAnotados, totalRecibidos = calcularGoles(resultados)
print(f"Total de goles anotados: {totalAnotados}")
print(f"Total de goles recibidos: {totalRecibidos}")
