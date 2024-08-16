empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

def empleadosMayorSalario(empleados, salario_limite):
    empleadosFiltrados = {}
    
    for idEmpleado, infoEmpleados in empleados.items():
        nombre, edad, salario = infoEmpleados
        
        if salario > salario_limite:
            empleadosFiltrados[idEmpleado] = infoEmpleados
    
    return empleadosFiltrados

resultado = empleadosMayorSalario(empleados, 3000)

print(resultado)
