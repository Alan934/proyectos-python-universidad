def analizarFinanzas(**kwargs):
    balanceFinal = 0
    
    for i, monto in kwargs.items():
        balanceFinal += monto
    
    return balanceFinal

balance = analizarFinanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)

print(f"El balance final es: {balance}")
