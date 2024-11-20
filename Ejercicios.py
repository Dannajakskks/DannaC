#Ejercicio 1
# Sistema de registro de estudiantes
def menu():
    print("\nSistema de Registro de Estudiantes")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Mostrar lista")
    print("4. Salir")
    return int(input("Seleccione una opción: "))

def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    matricula = input("Ingrese el número de matrícula: ")
    if matricula in [e['matricula'] for e in estudiantes]:
        print("Matrícula ya registrada. Intente con otra.")
    else:
        estudiantes.append({"nombre": nombre, "matricula": matricula})
        print("Estudiante agregado con éxito.")

def eliminar_estudiante(estudiantes):
    matricula = input("Ingrese el número de matrícula del estudiante a eliminar: ")
    for estudiante in estudiantes:
        if estudiante["matricula"] == matricula:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado con éxito.")
            return
    print("Matrícula no encontrada.")

def mostrar_lista(estudiantes):
    if not estudiantes:
        print("La lista de estudiantes está vacía.")
    else:
        print("\nLista de estudiantes:")
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Matrícula: {estudiante['matricula']}")

# Programa principal
estudiantes = []
while True:
    opcion = menu()
    if opcion == 1:
        agregar_estudiante(estudiantes)
    elif opcion == 2:
        eliminar_estudiante(estudiantes)
    elif opcion == 3:
        mostrar_lista(estudiantes)
    elif opcion == 4:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

#Ejercicio 2
#Inventario de productos

def opciones    