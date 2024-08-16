reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

def hacerReserva(fecha, nombreHuesped, habitacion, precio):
    if fecha in reservas:
        for reserva in reservas[fecha]:
            _, habitacionReservada, _ = reserva
            if habitacionReservada == habitacion:
                return "La habitación ya está reservada para la fecha seleccionada."
    else:
        reservas[fecha] = []
    
    reservas[fecha].append((nombreHuesped, habitacion, precio))
    return "Reserva realizada con éxito."

resultado = hacerReserva("2024-08-15", "María", 103, 200)
print(resultado)

resultado = hacerReserva("2024-08-17", "Carlos", 101, 150)
print(resultado)

print(reservas)
