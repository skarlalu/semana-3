class Mascota:
   
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre    # Atributo: nombre
        self.especie = especie  # Atributo: especie
        self.edad = edad        # Atributo: edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años")

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif self.especie.lower() == "gato":
            print(f"{self.nombre} dice: ¡Miau miau!")
        else:
            print(f"{self.nombre} hace un sonido nativo de su especie.")