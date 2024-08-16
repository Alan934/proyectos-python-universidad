estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

def promedioCalificaciones(registroEstudiantes, matricula):
    calificaciones = registroEstudiantes[matricula]["calificaciones"].values()
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio

matricula = 101
promedio = promedioCalificaciones(estudiantes, matricula)
print(f"El promedio de calificaciones del estudiante con matrícula {matricula} es: {promedio}")