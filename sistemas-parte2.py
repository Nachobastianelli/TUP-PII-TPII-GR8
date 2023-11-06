from abc import ABC, abstractmethod
from datetime import datetime
import random
import string


class Archivo:
    def __init__(self, nombre, formato, fecha):
        self.nombre = nombre
        self.formato = formato
        self.fecha = fecha

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nFormato: {self.formato}\nFecha: {self.fecha}\n"


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
                if curso in self.misCursos:
                    print("Ya estás matriculado en este curso.")
                    encontrado = True
                else:
                    contraseña = input("Ingrese la clave de matriculación: ")
                    if contraseña == cursos.contraseñaMatriculacion:
                        self.misCursos.append(cursos)
                        print("Se añadió con éxito!")
                        encontrado = True
        if not encontrado:
            print("Contraseña incorrecta o no existe un curso con ese nombre.")

    def desmatricularCurso(self):
        if not self.misCursos:
            print("No está matriculado en ningún curso.")
            return

        for i, curso in enumerate(self.misCursos, start=1):
            print(f"Índice: {i}, Curso: {curso}")

        eleccion = int(input("Seleccione un curso para desmatricularse: "))
        if 1 <= eleccion <= len(self.misCursos):
            eleccion -= 1
            cursoDesmatricula = self.misCursos[eleccion]
            self.misCursos.remove(cursoDesmatricula)
            print("Se desmatriculó con éxito!")
        else:
            print("Seleccionó una opción inválida.")

    def mostrarCursos(self):
        if not self.misCursos:
            print("No se ha matriculado a ningún curso.")
            return

        resultado = f"{sep}Listado de cursos{sep}\n\n{sep}\n"
        i = 1
        for curso in self.misCursos:
            resultado += f"{i}. {curso}\n{sep}\n"
            i += 1
        print(resultado)
        eleccion = int(input("Seleccione uno de los cursos: "))
        if 1 <= eleccion <= len(self.misCursos):
            cursoEleccion = self.misCursos[eleccion - 1]
            if not cursoEleccion.misArchivos:
                print("El curso no tiene archivos.")
            else:
                print("Archivos del curso:")
                for archivo in cursoEleccion.misArchivos:
                    print(archivo)
        else:
            print("Opción no válida.")


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

    def dictarCurso(self, nombre_curso, archivo=None):
        nuevoCurso = Curso(nombre_curso)
        nuevoCurso.generarContraseña()
        self.misCursos.append(nuevoCurso)
        listaCursos.append(nuevoCurso)
        print("El curso fue añadido con éxito!")

        if archivo:
            nuevoCurso.nuevoArchivo(archivo)

    def mostrarCursos(self):
        if not self.misCursos:
            print("No tienes ningun curso")
            return
        resultado = f"{sep}Listado de cursos{sep}\n\n{sep}\n"
        i = 1
        for curso in self.misCursos:
            resultado += f"{i}. {curso}\n{sep}\n"
            i += 1
        print(resultado)


class Curso:
    codigoCurso = 1

    def __init__(self, nombre):
        self.nombre = nombre
        self.contraseñaMatriculacion = None
        self.misArchivos = []
        self.codigo = Curso.codigoCurso
        self.codigo_str = f"{self.codigo:05}"
        Curso.codigoCurso += 1

    def __str__(self):
        return f"Materia: {self.nombre}\nClave: {self.contraseñaMatriculacion}\nCódigo: {self.codigo_str}"

    def generarContraseña(self):
        contraseña = ''.join(random.choice(
            string.ascii_letters + string.digits) for _ in range(6))
        self.contraseñaMatriculacion = contraseña

    def nuevoArchivo(self, archivo):
        self.misArchivos.append(archivo)


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

# Código para crear profesores y estudiantes y registrarlos en las listas


def registro():
    while True:
        print(f"{sep}Sistema de registros{sep}")
        print("""
1- Registrar un alumno
2- Registrar un profesor
3- Volver al menú principal
        """)
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("Registro de estudiante")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            legajo = int(input("Legajo: "))
            añoIngreso = int(input("Año de ingreso: "))
            estudiante = Estudiante(
                nombre, apellido, email, contraseña, legajo, añoIngreso)
            listaEstudiantes.append(estudiante)

        elif opcion == 2:
            print("Registro de profesor")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            titulo = input("Título: ")
            añoEgreso = int(input("Año de egreso: "))
            profesor = Profesor(nombre, apellido, email,
                                contraseña, titulo, añoEgreso)
            listaProfesores.append(profesor)

        elif opcion == 3:
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción inválida (1-3). Inténtelo de nuevo...")

# Función para mostrar el menú principal


def menu():
    while True:
        print("""
1- Ingresar como alumno
2- Ingresar como profesor
3- Ver cursos
4- Salir del programa
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            estudiante = buscar_estudiante(email)
            if estudiante and estudiante.validarCredenciales(email, contraseña):
                menuAlumnos(email)
            else:
                print("Credenciales inválidas o estudiante no registrado.")
        elif opcion == "2":
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
        elif opcion == "3":
            if not listaCursos:
                print("Aún no hay cursos disponibles :(")
            else:
                listaOrdenada = sorted(
                    listaCursos, key=lambda curso: curso.nombre)
                for cursos in listaOrdenada:
                    print(
                        f"Materia: {cursos.nombre}\t\tCarrera: Tecnicatura Universitaria en Programación")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        elif opcion == "admin":
            registro()
        else:
            print("Seleccionó una opción incorrecta")

# Función para el menú de alumnos


def menuAlumnos(email):
    while True:
        print(f"{sep}Menu alumnos{sep}")
        print("""
1- Matricularse a un curso
2- Desmatricularse de un curso
3- Ver cursos matriculados
4- Volver al menú principal
        """)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            if not listaCursos:
                print("Aún no hay cursos disponibles")
            else:
                i = 1
                for cursos in listaCursos:
                    print(f"{i}. {cursos.nombre}")
                    i += 1
                eleccion = int(
                    input("Seleccione un curso para matricularse: "))
                if 1 <= eleccion <= len(listaCursos):
                    cursoEleccion = listaCursos[eleccion - 1].nombre
                    print(f"El curso elegido es: {cursoEleccion}")
                    for estudiante in listaEstudiantes:
                        if estudiante.email == email:
                            estudiante.matricularCurso(cursoEleccion)
        elif opcion == 2:
            estudiante = buscar_estudiante(email)
            if estudiante:
                estudiante.desmatricularCurso()
        elif opcion == 3:
            estudiante = buscar_estudiante(email)
            if estudiante:
                estudiante.mostrarCursos()
        elif opcion == 4:
            print("Volviendo al menú principal...")
            break
        else:
            print("Ingresó una opción incorrecta (1-4). Inténtelo de nuevo")

# Función para el menú de profesores


def menuProfesores(email):
    profesor = buscar_profesor(email)
    if profesor is None:
        print("No se encontró un profesor registrado con ese correo.")
        return

    while True:
        print(f"{sep}Menú profesor{sep}")
        print("""
1- Dictar curso
2- Ver cursos dictados
3- Volver al menú principal
        """)

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nombre_curso = input("Ingrese el nombre del curso: ")
            if nombre_curso:
                nuevoCurso = Curso(nombre_curso)
                nuevoCurso.generarContraseña()
                profesor.misCursos.append(nuevoCurso)
                listaCursos.append(nuevoCurso)
                print("El curso fue añadido con éxito!")
                print(f"Nombre: {nuevoCurso.nombre}")
                print(f"Código: {nuevoCurso.codigo_str}")
                print(f"Contraseña: {nuevoCurso.contraseñaMatriculacion}")
                print(f"Cantidad de archivos: {len(nuevoCurso.misArchivos)}")
                respuesta = input(
                    "¿Desea agregar un archivo adjunto (Sí-S / No-N)?").upper()
                if respuesta == "S":
                    nombre_archivo = input("Nombre del archivo: ")
                    formato_archivo = input("Formato del archivo: ")
                    fecha_archivo = datetime.today()
                    nuevoArchivo = Archivo(
                        nombre_archivo, formato_archivo, fecha_archivo)
                    nuevoCurso.nuevoArchivo(nuevoArchivo)
                    print("Archivo adjunto añadido con éxito.")
            else:
                print("El nombre del curso no puede estar vacío.")
        elif opcion == 2:
            if not profesor.misCursos:
                print("No tiene cursos dictados actualmente.")
            else:
                i = 1
                for curso in profesor.misCursos:
                    print(f"{i} {curso.nombre}")
                    i += 1
                eleccion = int(input("Seleccione un curso: "))
                if 1 <= eleccion <= len(profesor.misCursos):
                    cursoEleccion = profesor.misCursos[eleccion - 1]
                    print(f"Nombre: {cursoEleccion.nombre}")
                    print(f"Código: {cursoEleccion.codigo_str}")
                    print(
                        f"Contraseña: {cursoEleccion.contraseñaMatriculacion}")
                    print(
                        f"Cantidad de archivos: {len(cursoEleccion.misArchivos)}")
                    respuesta = input(
                        "¿Desea agregar un archivo adjunto (Sí-S / No-N)?").upper()
                    if respuesta == "S":
                        nombre_archivo = input("Nombre del archivo: ")
                        formato_archivo = input("Formato del archivo: ")
                        fecha_archivo = datetime.today()
                        nuevoArchivo = Archivo(
                            nombre_archivo, formato_archivo, fecha_archivo)
                        cursoEleccion.nuevoArchivo(nuevoArchivo)
                        print("Archivo adjunto añadido con éxito.")
        elif opcion == 3:
            print("Volviendo al menú principal...")
            break
        else:
            print("Ingresó una opción incorrecta (1-3). Inténtelo de nuevo")

# Funciones para buscar estudiantes y profesores en las listas


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
