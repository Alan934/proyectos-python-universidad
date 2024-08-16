def actualizarSuscripcion(suscripciones, usuario, suscripcion, **opciones):
    if usuario in suscripciones:
        if suscripcion not in suscripciones[usuario]:
            suscripciones[usuario].append(suscripcion)
    else:
        suscripciones[usuario] = [suscripcion]

    for clave, valor in opciones.items():
        print(f"Opción adicional para {usuario}: {clave} = {valor}")

    return suscripciones

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

estadoActualizado = actualizarSuscripcion(suscripciones, usuario="Luis", suscripcion="mensual", auto_renovacion=True)

print(estadoActualizado)
