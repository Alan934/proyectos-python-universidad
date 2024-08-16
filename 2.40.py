def calcularPromedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def rankingEstudiantes(estudiantes):
    promedios = {}
    
    for estudianteId, materias in estudiantes.items():
        totalCalificaciones = []
        
        for calificaciones in materias.values():
            totalCalificaciones.extend(calificaciones)
        
        promedioGeneral = calcularPromedio(totalCalificaciones)
        promedios[estudianteId] = promedioGeneral
    
    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    
    return ranking

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

resultadoRanking = rankingEstudiantes(estudiantes)

for estudianteId, promedio in resultadoRanking:
    print(f"ID Estudiante: {estudianteId}, Promedio General: {promedio:.2f}")
