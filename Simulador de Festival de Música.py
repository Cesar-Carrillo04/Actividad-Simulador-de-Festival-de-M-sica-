
class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f" Hola, soy {self.nombre}, interpreto música de género {self.genero} "
              f"y mi popularidad es {self.popularidad}/100.")

    def actuar(self):
        print(f"{self.nombre} está actuando en el escenario...")

    def despedirse(self):
        print(f" {self.nombre} se despide del público con una gran sonrisa.\n")


# Subclase: Cantante
class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f" {self.nombre} canta su éxito '{self.cancion_mas_popular}' con gran energía.")


# Subclase: DJ
class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f" El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")


# Subclase: Banda
class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f" La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")



def iniciar_festival(lista_artistas):
    print("\n ¡Comienza el Festival Musical! \n")
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print(" Fin de la actuación \n")
    print(" ¡El festival ha terminado! Gracias por asistir ")


if __name__ == "__main__":
    lista_artistas = []
    n = int(input("¿Cuántos artistas se presentarán en el festival? "))

    for i in range(n):
        print(f"\n--- Artista #{i+1} ---")
        tipo = input("Tipo de artista (Cantante, DJ o Banda): ").strip().lower()
        nombre = input("Nombre del artista: ")
        genero = input("Género musical: ")
        popularidad = int(input("Nivel de popularidad (1-100): "))

        if tipo == "cantante":
            cancion = input("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)
        elif tipo == "dj":
            estilo = input("Estilo musical del DJ: ")
            artista = DJ(nombre, genero, popularidad, estilo)
        elif tipo == "banda":
            integrantes = int(input("Número de integrantes: "))
            artista = Banda(nombre, genero, popularidad, integrantes)
        else:
            print(" Tipo de artista no válido. Intenta de nuevo.")
            continue

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)
