def registrar_mascota():
    print("--- Registro de Mascota (Programación Tradicional) ---")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (ej. Perro, Gato): ")
    edad = int(input("Ingrese la edad de la mascota: "))
    
    return {"nombre": nombre, "especie": especie, "edad": edad}

def mostrar_informacion(mascota):
    print("\n--- Información de la Mascota ---")
    print(f"Nombre: {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad: {mascota['edad']} años")

if __name__ == "__main__":
    datos_mascota = registrar_mascota()
    mostrar_informacion(datos_mascota)