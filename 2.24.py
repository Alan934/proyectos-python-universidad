def organizarEventos(*args):
    for i, evento in enumerate(args, start=1):
        print(f"{i}. {evento}")

organizarEventos("Concierto", "Exposición de arte", "Conferencia")
