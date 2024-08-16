rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distanciasMax = [600, 400, 500]

def filtrarRutas(rutas, distanciasMax):
    rutasFiltradas = []
    
    if len(rutas) != len(distanciasMax):
        return "La cantidad de distancias máximas no coincide con la cantidad de rutas."
    
    for ruta, distanciaMax in zip(rutas, distanciasMax):
        origen, destino, distancia = ruta
        if distancia <= distanciaMax:
            rutasFiltradas.append(ruta)
    
    return rutasFiltradas

rutasOptimizadas = filtrarRutas(rutas, distanciasMax)

print(rutasOptimizadas)
