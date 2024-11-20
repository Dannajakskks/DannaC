estudiantes = []

class Estudiante:
    def __init__(self, nombre, edad, grado, id, materias):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.id = id
        self.materias = materias

def aggestudiante():
    nombre = input("Ingrese el nombre completo del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    grado = int(input("Ingrese el grado del estudiante: "))
    id = int(input("Ingrese el documento del estudiante: "))

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
    
    est = Estudiante(nombre, edad, grado, id, materias)
    estudiantes.append(est)

def mejormateria(estudiante):
    mejormateria = None
    mejorpromedio = 0
    for materia, datos in estudiante.materias.items():
        if datos["promedio"] > mejorpromedio:
            mejormateria = materia
            mejorpromedio = datos["promedio"]
    print(f"La mejor materia de {estudiante.nombre} es {mejormateria} con un promedio de {mejorpromedio:.2f}")

def buscarestudiante(nombre):
    for estudiante in estudiantes:
        if estudiante.nombre == nombre:
            return estudiante
    return None

def mostrarestudiantes(ordenar=False):
    if ordenar:
        combsort(estudiantes)

    print("Lista de estudiantes:")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante.nombre}")
        print(f"Edad: {estudiante.edad}")
        print(f"Grado: {estudiante.grado}")
        print(f"Identificación: {estudiante.id}")
        print("Materias:")
        for materia, datos in estudiante.materias.items():
            print(f"  {materia}: {datos['promedio']:.2f}")
    print("-" * 40)

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
            if estudiantes[i].edad > estudiantes[i + gap].edad:
                estudiantes[i], estudiantes[i + gap] = estudiantes[i + gap], estudiantes[i]
                sorted = False
            i += 1

def eliminarestudiante():
    id_estudiante = int(input("Ingrese el ID del estudiante a eliminar: "))
    for estudiante in estudiantes:
        if estudiante.id == id_estudiante:
            estudiantes.remove(estudiante)
            print(f"Estudiante con ID {id_estudiante} eliminado con éxito.")
            return
    print("Estudiante no encontrado.")

while True:
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Mostrar todos los estudiantes")
    print("4. Eliminar estudiante")
    print("5. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        aggestudiante()
    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante a buscar: ")
        estudiante = buscarestudiante(nombre)
        if estudiante:
            mejormateria(estudiante)
        else:
            print("Estudiante no encontrado.")
    elif opcion == "3":
        print("ESTUDIANTES ORDENADOS POR EDAD:")
        mostrarestudiantes(ordenar=True)
    elif opcion == "4":
        eliminarestudiante()
    elif opcion == "5":
        print("Has salido del programa :(")
        break
    else:
        print("Opción inválida.")
