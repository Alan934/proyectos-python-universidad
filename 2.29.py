notasEstudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def calcularPromedioNotas(notasEstudiantes):
    promedios = {}
    
    for estudiante, notas in notasEstudiantes:
        promedio = sum(notas) / len(notas)
        promedios[estudiante] = promedio
    
    return promedios

promediosEstudiantes = calcularPromedioNotas(notasEstudiantes)
print(promediosEstudiantes)
