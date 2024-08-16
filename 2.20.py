def configuraracion(**kwargs):
    configuraciones = {
        "modo_oscuro": False,
        "idioma": "en",
        "notificaciones": True
    }
    
    configuraciones.update(kwargs)
    
    return configuraciones

configuracionAplicada = configuraracion(modoOscuro=True, idioma="es", notificaciones=False)

print(configuracionAplicada)
