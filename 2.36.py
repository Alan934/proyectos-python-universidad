inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

def actualizarInventario(**kwargs):
    nombreTienda = kwargs.pop("tienda", None)
    
    if nombreTienda is None:
        return "No se especificó el nombre de la tienda."
    
    if nombreTienda not in inventario:
        return f"La tienda '{nombreTienda}' no existe en el inventario."
    
    tiendaInventario = inventario[nombreTienda]
    
    for producto, cantidad in kwargs.items():
        if producto in tiendaInventario:
            tiendaInventario[producto] += cantidad
        else:
            return f"El producto '{producto}' no existe en la tienda '{nombreTienda}'."
    
    return inventario

resultado = actualizarInventario(tienda="Tienda A", producto_1=10, producto_2=-5)

print(resultado)
