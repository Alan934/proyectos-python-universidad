puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def ordenarPuntuacion(puntuaciones):
    puntuacionesOrdenadas = sorted(puntuaciones, key=lambda x: x[1], reverse=True)
    
    return puntuacionesOrdenadas

puntuacionesOrdenadas = ordenarPuntuacion(puntuaciones)
print(puntuacionesOrdenadas)
