from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña

    @abstractmethod
    def __str__(self):
        return f"Hola, me llamo: {self.nombre} {self.apellido}"

    @abstractmethod
    def validarCredenciales(self, email, contraseña):
        pass


class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str, legajo: int, añoInscripcion: int):
        super().__init__(nombre, apellido, email, contraseña)
        self.legajo = legajo
        self.añoInscripcion = añoInscripcion
        self.misCursos = []

    def __str__(self) -> str:
        return f"Hola, soy un estudiante y me llamo: {self.nombre} {self.apellido}"

    def validarCredenciales(self, email, contraseña) -> bool:
        for estudiante in listaEstudiantes:
            if email == estudiante.email and contraseña == estudiante.contraseña:
                return True
        return False

    def matricularCurso(self, curso):
        encontrado = False

        for cursos in listaCursos:
            if str(curso) == str(cursos.nombre) and str(curso) not in self.misCursos:
                contraseña = input("Ingrese la clave de matriculación: ")
                if contraseña == cursos.contraseñaMatriculacion:
                    self.misCursos.append(curso)
                    print("Se añadió con éxito!")
                    encontrado = True
        if not encontrado:
            print("Contraseña incorrecta o no existe un curso con ese nombre.")

    def mostrarCursos(self):
        resultado = f"{sep}Listado de cursos{sep}\n\n{sep}\n"
        i = 1
        for cursos in self.misCursos:
            resultado += f"{i}. {cursos}\n{sep}\n"
            i += 1
        return resultado


class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contraseña, titulo, añoEsgreso):
        super().__init__(nombre, apellido, email, contraseña)
        self.titulo = titulo
        self.añoEsgreso = añoEsgreso
        self.misCursos = []

    def __str__(self) -> str:
        return f"Hola, soy un profesor y me llamo: {self.nombre} {self.apellido}, Título: {self.titulo}"

    def validarCredenciales(self, email, contraseña):
        for profesor in listaProfesores:
            if email == profesor.email and contraseña == profesor.contraseña:
                return True
        print("No hay ningún profesor registrado con ese correo.")
        return False

    def dictarCurso(self, curso):
        nuevoCurso = Curso(curso)
        nuevoCurso.generarContraseña()
        self.misCursos.append(nuevoCurso)
        listaCursos.append(nuevoCurso)
        print("El curso fue añadido con éxito!")

    def mostrarCursos(self):
        resultado = f"{sep}Listado de cursos{sep}\n\n{sep}\n"
        i = 1
        for cursos in self.misCursos:
            resultado += f"{i}. {cursos}\n{sep}\n"
            i += 1
        print(resultado)


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contraseñaMatriculacion = None

    def __str__(self):
        return f"Materia: {self.nombre}\nClave: {self.contraseñaMatriculacion}\n"

    def generarContraseña(self):
        contraseña = input("Ingrese la contraseña del curso: ")
        self.contraseñaMatriculacion = contraseña


listaEstudiantes = []
listaProfesores = []
listaCursos = []

sep = "---" * 15


profesorJuan = Profesor("Juan", "Perez", "juan@gmail.com",
                        "juan123", "Docente universitario", 2014)
profesorPepe = Profesor("Pepe", "Sanchez", "pepe@gmail.com",
                        "pepe123", "Docente primario", 2018)
profesorMartin = Profesor(
    "Martin", "Josema", "martin@gmail.com", "martin123", "Medico", 2007)

listaProfesores.append(profesorPepe)
listaProfesores.append(profesorMartin)
listaProfesores.append(profesorJuan)

estudianteNacho = Estudiante(
    "Nacho", "Bastianelli", "nacho@gmail.com", "nacho123", 12345, 2023)
estudianteDani = Estudiante(
    "Danilo", "Mercado", "dani@gmail.com", "dani123", 11223, 2023)
estudianteAgus = Estudiante("Agustin", "Olbinsky",
                            "agus@gmail.com", "agus123", 54321, 2023)

listaEstudiantes.append(estudianteDani)
listaEstudiantes.append(estudianteAgus)
listaEstudiantes.append(estudianteNacho)


def buscar_estudiante(email):
    for estudiante in listaEstudiantes:
        if email == estudiante.email:
            return estudiante
    return None


def registro():  # Todavia no tiene un llamado, hay que probar si funciona...

    while True:
        print(f"{sep}Sistema de registros{sep}")
        print("""
1- Registrar un alumno
2- Registrar un profesor
3- Volver al menu principal               
              """)
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            print("Registro de estudiante")
            nombre = str(input("Nombre:"))
            apellido = str(input("Apellido: "))
            email = str(input("Email: "))
            contraseña = str(input("Contraseña: "))
            legajo = int(input("Legajo: "))
            añoIngreso = int(input("Año de ingreso: "))
            estudiante = Estudiante(
                nombre, apellido, email, contraseña, legajo, añoIngreso)
            listaEstudiantes.append(estudiante)

        elif opcion == 2:
            print("Registro de profesor")
            nombre = str(input("Nombre:"))
            apellido = str(input("Apellido: "))
            email = str(input("Email: "))
            contraseña = str(input("Contraseña: "))
            titulo = str(input("Titulo: "))
            añoEsgreso = input("Año de esgreso: ")
            profesor = Profesor(nombre, apellido, email,
                                contraseña, titulo, añoEsgreso)
            listaProfesores.append(profesor)

        elif opcion == 3:
            print("Volviendo al menu principal...")
            break

        else:
            print("Opcion invalida (1-3). Intentelo de nuevo...\n")


def menu():
    while True:
        print("""
1- Ingresar como alumno
2- Ingresar como profesor
3- Ver cursos
4- Salir del programa
        """)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            estudiante = buscar_estudiante(email)
            if estudiante and estudiante.validarCredenciales(email, contraseña):
                menuAlumnos(email)
            else:
                print("Credenciales inválidas o estudiante no registrado.")
        elif opcion == 2:
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            profesor = buscar_profesor(email)
            if profesor:
                if profesor.validarCredenciales(email, contraseña):
                    menuProfesores(email)
                else:
                    print("Credenciales inválidas")
            else:
                print("No se encontró un profesor registrado con ese correo")
        elif opcion == 3:
            if not listaCursos:
                print("Aún no hay cursos disponibles :(")
            else:
                listaOrdenada = sorted(
                    listaCursos, key=lambda curso: curso.nombre)
                for cursos in listaOrdenada:
                    print(
                        f"Materia: {cursos.nombre}\t\tCarrera: Tecnicatura Universitaria en Programación")
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Seleccionó una opción incorrecta :( ")


def menuAlumnos(email):
    while True:
        print(f"{sep}Menu alumnos{sep}")
        print("""
1- Matricularse a un curso
2- Ver cursos
3- Volver al menú principal
        """)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            if not listaCursos:
                print("Aún no hay cursos disponibles :(")
            else:
                i = 1
                for cursos in listaCursos:
                    print(f"{i}. {cursos.nombre}")
                    i += 1
                eleccion = int(input("Seleccione una de las opciones: "))
                if 1 <= eleccion <= len(listaCursos):
                    cursoEleccion = listaCursos[eleccion - 1].nombre
                    print(f"El curso elegido es: {cursoEleccion}")
                    for estudiante in listaEstudiantes:
                        if estudiante.email == email:
                            estudiante.matricularCurso(cursoEleccion)
        elif opcion == 2:
            estudiante = buscar_estudiante(email)
            if estudiante:
                resultado = estudiante.mostrarCursos()
                print(resultado)
        elif opcion == 3:
            print("Volviendo al menú principal...")
            break
        else:
            print("Ingresó una opción incorrecta (1-3). Inténtelo de nuevo")


def menuProfesores(email):
    while True:
        print(f"{sep}Menu profesores{sep}")
        print("""
1- Dictar cursos
2- Ver cursos
3- Volver al menú principal
        """)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            profesor = buscar_profesor(email)
            if profesor:
                curso = input("Ingrese el nombre del curso: ")
                if curso:
                    profesor.dictarCurso(curso)
                else:
                    print("El curso debe contener un nombre.")
        elif opcion == 2:
            profesor = buscar_profesor(email)
            if profesor:
                profesor.mostrarCursos()
        elif opcion == 3:
            print("Volviendo al menú principal...")
            break
        else:
            print("Ingresó una opción incorrecta (1-3). Inténtelo de nuevo")


def buscar_estudiante(email):
    for estudiante in listaEstudiantes:
        if estudiante.email == email:
            return estudiante
    return None


def buscar_profesor(email):
    for profesor in listaProfesores:
        if profesor.email == email:
            return profesor
    return None


menu()
