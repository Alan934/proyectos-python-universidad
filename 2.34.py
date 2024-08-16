from collections import Counter

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

def calcularFrecuencias(encuestas):
    resultadosFrecuencias = {}
    
    for pregunta, respuestas in encuestas.items():
        frecuencias = Counter(respuestas)
        resultadosFrecuencias[pregunta] = dict(frecuencias)
    
    return resultadosFrecuencias

frecuencias = calcularFrecuencias(encuestas)

print(frecuencias)
