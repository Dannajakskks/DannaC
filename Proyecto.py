estudiantes = []

def agregarestudiante():
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad: "))
    grado = int(input("Grado: "))

    materias = {}
    cantidadmaterias = int(input("Cantidad de materias: "))
    for i in range(cantidadmaterias):
        materia = input("Nombre de la materia: ")
        cantidadnotas = int(input(f"Cantidad de notas para {materia}: "))
        notas = []
        for j in range(cantidadnotas):
            nota = float(input("Nota: "))
            notas.append(nota)
        promedio = sum(notas) / len(notas)
        materias[materia] = {"notas": notas, "promedio": promedio}

    estudiante = {"nombre": nombre, "edad": edad, "grado": grado, "materias": materias}
    estudiantes.append(estudiante)

def mejormateria(estudiante):
    mejor_materia = None
    mejor_promedio = 0
    for materia in estudiante["materias"]:
        if estudiante["materias"][materia]["promedio"] > mejor_promedio:
            mejor_materia = materia
            mejor_promedio = estudiante["materias"][materia]["promedio"]
    print(f"La mejor materia de {estudiante['nombre']} es {mejor_materia} con un promedio de {mejor_promedio:.2f}")

def buscarestudiante(nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            return estudiante
    return None

def mostrarestudiantes():
    for estudiante in estudiantes:
        print(f"\nNombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Grado: {estudiante['grado']}")
        print("Materias:")
        for materia, detalles in estudiante['materias'].items():
            print(f"  {materia}: Promedio {detalles['promedio']:.2f}")

def combsort(estudiantes):
    gap = len(estudiantes)
    brecha = 1.3
    ordenado = False

    while not ordenado:
        gap = int(gap / brecha)
        if gap <= 1:
            gap = 1
            ordenado = True

        i = 0
        while i + gap < len(estudiantes):
            if estudiantes[i]['edad'] > estudiantes[i + gap]['edad']:
                estudiantes[i], estudiantes[i + gap] = estudiantes[i + gap], estudiantes[i]
                ordenado = False
            i += 1

def eliminarest():
    nombre = input("Ingrese el nombre completo del estudiante a eliminar: ")
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado con éxito.")
            return
    print("Estudiante no encontrado/a.")

# Menú principal
while True:
    print("\n1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Mostrar todos los estudiantes")
    print("4. Eliminar estudiante")
    print("5. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        agregarestudiante()
    elif opcion == 2:
        nombre = input("Ingrese el nombre del estudiante a buscar: ")
        estudiante = buscarestudiante(nombre)
        if estudiante:
            mejormateria(estudiante)
        else:
            print("Estudiante no encontrado.")
    elif opcion == 3:
        print("\nEstudiantes:")
        mostrarestudiantes()
        print("\nOrdenados de menor a mayor edad:")
        combsort(estudiantes)
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")
    elif opcion == 4:
        eliminarest()
    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
