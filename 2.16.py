def crearUsuario(nombre, edad, email, **kwargs):
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "email": email
    }
    
    perfil.update(kwargs)
    
    return perfil

usuario = crearUsuario(nombre="Alan Sanjurjo", edad=22, email="sanjurjoalan77@gmail.com", localidad="Lavalle", ocupacion="Estudiante", estadoCivil=("Soltero"))

print(usuario)
