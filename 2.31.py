def publicar(nombre_usuario, texto_publicacion, etiquetas=[], **kwargs):
    publicacionDetalles = {
        "usuario": nombre_usuario,
        "texto": texto_publicacion,
        "etiquetas": etiquetas
    }
    
    publicacionDetalles.update(kwargs)
    
    return publicacionDetalles

publicacion = publicar(
    "Juan", 
    "Mi primer post!", 
    etiquetas=["#hola", "#primerPost"], 
    visibilidad="publica", 
    likes=100
)

print(publicacion)
