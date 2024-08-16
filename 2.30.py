usuarios = ["Ana", "Luis", "María"]

def configurarPerfiles(usuarios, **kwargs):
    perfilesConfigurados = {}
    
    for usuario in usuarios:
        perfilesConfigurados[usuario] = list(kwargs.values())
    
    return perfilesConfigurados

perfiles = configurarPerfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)

print(perfiles)
