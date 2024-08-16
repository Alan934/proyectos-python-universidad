from collections import Counter

hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def analizarTendencias(hashtags, tendencias):
    frecuenciaHashtags = Counter(hashtags)
    print("Frecuencia de hashtags:", frecuenciaHashtags)
    
    # Convertir la lista de tuplas en un diccionario
    frecuenciasTendencias = dict(tendencias)
    print("Frecuencias de tendencias:", frecuenciasTendencias)
    
    hashtagsRelevantes = []
    for hashtag, umbral in frecuenciasTendencias.items():
        if frecuenciaHashtags.get(hashtag, 0) > umbral:
            hashtagsRelevantes.append(hashtag)
    
    return hashtagsRelevantes

resultados = analizarTendencias(hashtags, tendencias)

print("Hashtags relevantes:", resultados)
