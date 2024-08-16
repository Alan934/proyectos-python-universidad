temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def analizarTemperaturas(temperaturas):
    temperaturaMedia = sum(temperaturas) / len(temperaturas)
    
    temperaturaMaxima = max(temperaturas)
    temperaturaMinima = min(temperaturas)
    
    return temperaturaMedia, temperaturaMaxima, temperaturaMinima

temperaturaMedia, temperaturaMaxima, temperaturaMinima = analizarTemperaturas(temperaturas)
print(f"Temperatura media: {temperaturaMedia:.2f}°C")
print(f"Temperatura máxima: {temperaturaMaxima}°C")
print(f"Temperatura mínima: {temperaturaMinima}°C")
