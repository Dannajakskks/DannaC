estudiantes = []
def agregarestudiante():
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad: "))
    grado = int(input("Grado: "))

    materias = {}
    cantidadmaterias = int(input("Cantidad de materias: "))
    for i in range(cantidadmaterias):
        materia = input("Nombre de la materia: ")
        cantidadnotas = int(input("Cantidad de notas para " + materia + ": "))
        notas = []
        for j in range(cantidadnotas):
            nota = float(input("Nota: "))
            notas.append(nota)
        promedio = sum(notas) / len(notas)
        materias[materia] = {"notas": notas, "promedio": promedio}

    estudiante = {"nombre": nombre, "edad": edad, "grado": grado, "materias": materias}
    estudiantes.append(estudiante)

def mejormateria(estudiante):
    mejormateria = None
    mejorpromedio = 0
    for materia in estudiante["materias"]:
        if estudiante["materias"][materia]["promedio"] > mejorpromedio:
            mejormateria = materia
            mejorpromedio = estudiante["materias"][materia]["promedio"]
    print(f"La mejor materia de {estudiante['nombre']} es {mejormateria} con un promedio de {mejorpromedio:.2f}")

def buscarestudiante(nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            return estudiante
    return None

def mostrarestudiantes():
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Grado: {estudiante['grado']}")
        print("Materias:")
        for materia in estudiante['materias']:
            print(f"  {materia}: {estudiante['materias'][materia]['promedio']:.2f}")

def combsort(estudiantes):
    gap = len(estudiantes)
    brecha = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / brecha)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(estudiantes):
            if estudiantes[i]['edad'] > estudiantes[i + gap]['edad']:
                estudiantes[i], estudiantes[i + gap] = estudiantes[i + gap], estudiantes[i]
                sorted = False
            i += 1

while True:
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Mostrar todos los estudiantes")
    print("4. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        agregarestudiante()
    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante a buscar: ")
        estudiante = buscarestudiante(nombre)
        if estudiante:
            mejormateria(estudiante)
        else:
            print("Estudiante no encontrado.")
    elif opcion == "3":
        print("ESTUDIANTES")
        mostrarestudiantes()
        print("ESTUDIANTES DE MENOR A MAYOR")
        combsort(estudiantes)
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, {estudiante['edad']}")
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")
