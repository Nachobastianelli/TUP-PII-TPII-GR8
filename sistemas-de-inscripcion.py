from abc import ABC, abstractmethod
import random
import string

listaEstudiantes = []
listaProfesores = []
listaCursos = []


class Persona(ABC):
    def __init__(self, nombre, apellido, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña

    @abstractmethod
    def __str__(self) -> str:
        return f"Hola, me llamo {self.nombre} {self.apellido}!"

    @abstractmethod
    def validar_credenciales(self, emailValidar=None, contraseñaValidar=None) -> bool:
        pass


class Estudiante(Persona):
    def __init__(self, nombre, apellido, email, contraseña, añoIngreso):
        legajo = self.generar_legajo()
        super().__init__(nombre, apellido, email, contraseña)
        self.legajo = legajo
        self.añoIngreso = añoIngreso
        self.misCursos = []

    def generar_legajo(self):
        return ''.join(random.choice('0123456789') for _ in range(5))

    def validar_credenciales(self, emailValidar=None, contraseñaValidar=None) -> bool:
        if emailValidar is not None and contraseñaValidar is not None:
            for estudiante in listaEstudiantes:
                if emailValidar == estudiante.email and contraseñaValidar == estudiante.contraseña:
                    print(
                        f"Inicio de sesión exitoso para el estudiante: {estudiante.nombre} {estudiante.apellido}, con el legajo: {estudiante.legajo}!")
                    return True
        return False

    def matricularse(self, curso):
        if curso in self.misCursos:
            print("Ya estás matriculado en el curso")
        else:
            claveMatricula = input(
                "Ingrese la clave de matriculación del curso:")
            if claveMatricula == curso.claveMatriculacion:
                self.misCursos.append(curso)
                print("Se ha inscrito con éxito!")
            else:
                print("Ingresó una contraseña incorrecta.")

    def mostrarCursos(self, email):
        resultado = "Lista de cursos:\n\n------------\n"
        i = 1
        for cursos in self.misCursos:
            resultado += f"{i}. {cursos}\n-----------\n"
            i += 1
        return resultado

    def __str__(self) -> str:
        return "Soy un estudiante"


class Profesor(Persona):
    def __init__(self, nombre, apellido, email, contraseña, titulo, añoEsgreso):
        super().__init__(nombre, apellido, email, contraseña)
        self.titulo = titulo
        self.añoEsgreso = añoEsgreso
        self.misCursos = []

    def validar_credenciales(self, emailValidar=None, contraseñaValidar=None) -> bool:
        if emailValidar is not None and contraseñaValidar is not None:
            for profesor in listaProfesores:
                if emailValidar == profesor.email and contraseñaValidar == profesor.contraseña:
                    print(
                        f"Bienvenido {profesor.nombre} {profesor.apellido}!")
                    return True
        return False

    def dictarCursos(self):
        nombreCurso = input("Ingrese el nombre del curso:")
        encontrado = next(
            (curso for curso in listaCursos if curso.nombre == nombreCurso), None)

        if encontrado is None:
            nuevoCurso = Curso(nombreCurso)
            nuevoCurso.contraseña()
            listaCursos.append(nuevoCurso)
            self.misCursos.append(nuevoCurso)
            print("Se agregó el curso con éxito")
        else:
            print(f"Ya tiene el curso {nombreCurso} cargado en el sistema")

    def mostrarCursos(self):
        resultado = "Lista de cursos:\n\n------------\n"
        i = 1
        for cursos in self.misCursos:
            resultado += f"{i}. {cursos}\n-----------\n"
            i += 1
        return resultado

    def __str__(self) -> str:
        return "Soy un profesor"


class Curso():
    def __init__(self, nombre):
        self.nombre = nombre
        self.claveMatriculacion = None

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nClave: {self.claveMatriculacion}"

    def contraseña(self):
        def generar_contraseña():
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        self.claveMatriculacion = generar_contraseña()


# Instanciamientos de clase: profesores
profesor1 = Profesor("jose luis", "cecarelli", "jose@gmail.com",
                     "jose123", "docente", "12/01/2019")
listaProfesores.append(profesor1)

# Estudiantes
estudiante1 = Estudiante("Ignacio", "Bastianelli",
                         "nacho@gmail.com", "nacho123", "28/06/2003")
listaEstudiantes.append(estudiante1)

estudiante2 = Estudiante(
    "ricardo", "fort", "ricky@gmail.com", "ricky123", "19/09/1999")
listaEstudiantes.append(estudiante2)


def menuAlumno():
    while True:
        print("""
1- Registrarse como estudiante
2- Ingresar como estudiante
3- Salir
        """)
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            print("Registro de estudiante:\n ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Correo electronico: ")

            if any(estudiante.email == email for estudiante in listaEstudiantes):
                print("Ya existe una cuenta asociada a ese correo.")
            else:
                contraseña = input("Contraseña: ")
                añoIngreso = input(
                    "Año de ingreso: ")

                estudiante = Estudiante(
                    nombre, apellido, email, contraseña, añoIngreso)
                listaEstudiantes.append(estudiante)
                print("Registro exitoso.")

        elif opcion == 2:
            print("Ingeso de alumno: \n")
            email = input("Correo electronico: ")
            contraseña = input("Contraseña: ")

            for estudiante in listaEstudiantes:
                if estudiante.validar_credenciales(email, contraseña):
                    opcionAlumno = 0
                    while opcionAlumno != 3:
                        print("""
1- Matricularse a un curso
2- Ver cursos
3- Volver al menú principal
                        """)
                        opcionAlumno = int(input("Seleccione una opción:\n"))
                        if opcionAlumno == 1:
                            if not listaCursos:
                                print("No hay cursos disponibles")
                            else:
                                i = 1
                                for curso in listaCursos:
                                    print(f"{i}. {curso}\n")
                                    i += 1
                                opcion = int(input("Seleccione un curso: "))
                                if opcion <= len(listaCursos):
                                    curso = listaCursos[opcion - 1]
                                    estudiante.matricularse(curso)
                                else:
                                    print(
                                        "Opción incorrecta. Inténtelo de nuevo...")
                        elif opcionAlumno == 2:
                            if not estudiante.misCursos:
                                print("No estás matriculado en ningún curso.")
                            else:

                                resultado = estudiante.mostrarCursos(
                                    estudiante.email)
                                print(resultado)
                        elif opcionAlumno == 3:
                            print("Volviendo al menú principal")
                        else:
                            print("Opción incorrecta. Inténtelo de nuevo...")

                    break
            else:
                print("Credenciales inválidas")

        elif opcion == 3:
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo\n")


def menuProfesor():
    while True:
        print("""
1- Registrarse como profesor
2- Ingresar como profesor
3- Salir
        """)
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            print("Registro de profesor:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Correo electrónico: ")

            if any(profesor.email == email for profesor in listaProfesores):
                print(
                    "Ya existe una cuenta con ese correo electrónico. Inténtelo de nuevo...")
            else:
                contraseña = input("Contraseña: ")
                titulo = input("Título universitario: ")
                añoEgreso = input("Ingrese su año de egreso: ")

                profesor = Profesor(nombre, apellido, email,
                                    contraseña, titulo, añoEgreso)
                listaProfesores.append(profesor)

        elif opcion == 2:
            print("Ingreso de profesor: \n")
            email = input("Correo electrónico: ")
            contraseña = input("Contraseña: ")

            for profesor in listaProfesores:
                if profesor.validar_credenciales(email, contraseña):
                    opcionProfesor = 0
                    while opcionProfesor != 3:
                        print("""
1- Dictar un curso
2- Ver cursos
3- Volver al menú principal
                        """)
                        opcionProfesor = int(input("Seleccione una opción:\n"))
                        if opcionProfesor == 1:
                            profesor.dictarCursos()
                        elif opcionProfesor == 2:
                            if not profesor.misCursos:
                                print("No tienes cursos disponibles.")
                            else:
                                resultado = profesor.mostrarCursos()
                                print(resultado)
                        elif opcionProfesor == 3:
                            print("Volviendo al menú principal")
                        else:
                            print("Opción incorrecta. Inténtelo de nuevo...\n")
                    break
            else:
                print("Credenciales inválidas")

        elif opcion == 3:
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo\n")


def menu():
    while True:
        print("""
1- Ingresar como alumno
2- Ingresar como profesor
3- Ver cursos
4- Salir del programa
        """)
        opcion = int(input("Seleccione una opción:\n"))

        if opcion == 1:
            menuAlumno()
        elif opcion == 2:
            menuProfesor()
        elif opcion == 3:
            if not listaCursos:
                print("Aún no hay cursos disponibles :(")
            else:
                print("Cursos: \n\n")
                for i, curso in enumerate(listaCursos, start=1):
                    print(f"{i}. {curso}")
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción incorrecta. Inténtelo de nuevo:\n")


menu()
