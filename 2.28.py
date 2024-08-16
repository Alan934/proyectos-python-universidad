biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

def libroPublicados(biblioteca):
    librosRecientes = []
    
    for titulo, info in biblioteca.items():
        if info["año"] > 2000:
            librosRecientes.append(titulo)
    
    return librosRecientes

librosRecientes = libroPublicados(biblioteca)
print(librosRecientes)
