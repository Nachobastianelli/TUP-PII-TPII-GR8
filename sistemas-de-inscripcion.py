from abc import ABC, abstractmethod
import random

estudiantes = []
profesores = []
totalCursos = []


class Persona(ABC):

    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contraseña = contraseña

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def validar_credenciales(self, emailIngresado=None, contraseñaIngresada=None):
        pass


class Estudiante(Persona):
    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str, legajo: int, año_inscripcion: int):
        super().__init__(nombre, apellido, email, contraseña)
        self.legajo = legajo
        self.año_inscripcion = año_inscripcion
        self.cursos = []

    def registro(self):
        print("Programa de registro de estudiante:\n")
        nombreEstudiante = str(input("Ingrese su nombre:"))
        apellidoEstudiante = str(input("Ingrese su apellido"))
        emailEstudiante = str(input("Ingrese su email"))

        for estudiante in estudiantes:
            if emailEstudiante == estudiante.email:
                print("El email ya fue ingresado. Intentalo de nuevo")
                return

        contraseñaEstudiante = str(input("Ingrese su contraseña"))
        def generar_legajo(): return ''.join(random.choice('0123456789')
                                             for _ in range(5))
        legajo = generar_legajo()
        print(f"Su legajo es: {legajo}")
        año_inscripcionEstudiante = str(
            input("Ingrese su año de ingreso: (dd/mm/aaaa)"))

        estudiante = Estudiante(nombreEstudiante, apellidoEstudiante, emailEstudiante,
                                contraseñaEstudiante, legajo, año_inscripcionEstudiante)

        estudiantes.append(estudiante)

    def validar_credenciales(self, emailIngresado=None, contraseñaIngresada=None):
        if emailIngresado is not None and contraseñaIngresada is not None:
            for estudiante in estudiantes:
                if emailIngresado == estudiante.email and contraseñaIngresada == estudiante.contraseña:
                    return True

        return False

    def matricularse(self, opcionCurso):
        listaCursos = ["Programación I", "Programación II",
                       "Laboratorio", "InglesI", "InglesII"]
        encontrado = False
        for estudiante in estudiantes:
            if estudiante.cursos == listaCursos[opcionCurso]:
                print("Ya estas inscripcto en este curso.")
                encontrado = True
                return
            if encontrado == False:
                estudiante.cursos = + listaCursos[opcionCurso]
                return
            """
                def matricularse(self, curso): Probar esta alternativa si no fucniona arriba
                    if curso not in self.cursos:
                    self.cursos.append(curso)
            """

    def mostrarCursos(self, emailCursos):
        encontrado = False
        for estudiante in estudiantes:
            if emailCursos == estudiante.email:
                encontrado = True
                return f"Los cursos que esta cursando son: {estudiante.cursos}"
        if not encontrado:
            return "No hay ningun email asociado."
        return "no tiene cursos"

    def __str__(self) -> str:
        return f"Estudiante: {self.nombre} {self.apellido}, Legajo: {self.legajo}"

    """def validar_credenciales(self, mail_a_validar, Clave_a_validar):
        for estudiante in self.estudiantes:
            pass"""


class Profesor(Persona):
    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str, titulo: str, año_graduacion: int):
        super().__init__(nombre, apellido, email, contraseña)
        self.titulo = titulo
        self.año_graduacion = año_graduacion
        self.maestros = []

    def validar_credenciales(self, emailIngresado=None, contraseñaIngresada=None):
        pass

# Pre-cargamos alumnos y profesores


estudiantes = Estudiante()


def menu():
    opcion = 0
    while (opcion != 4):
        opcion = int(input(
            "Seleccione una de las opciones:\n1- Ingresar como alumno\n2- Ingresar como profesor\n3-Ver cursos\n4-Salir\n"))

        if opcion == 1:
            pass

        elif opcion == 2:
            pass

        elif opcion == 3:
            pass

        elif opcion == 4:
            pass

        else:
            print("Eligio una opcion incorrecta (1-4). Intentelo de nuevo\n")


def menuIngresoAlumno():
    opcion = 0
    while opcion != 3:
        opcion = int(input(
            "Seleccione una opcion:\n1- Registrarse\n2- Loguearse\n3- Volver al menu principal"))
        if opcion == 1:
            estudiantes.registro()

        elif opcion == 2:
            emailIngresado = str(input("Ingrese su mail"))
            contraseñaIngresada = str(input("Ingrese su contraseña"))
            verificar = estudiantes.validar_credenciales(
                emailIngresado, contraseñaIngresada)
            if verificar == True:
                opc = int(input(
                    "Seleccione una opcion:\n1- Matricularse a un curso\n2- Ver cursos\n 3- Volver al menu principal\n"))

                if opc == 1:

                    opcionCurso = int(input(
                        "Ingrese una de las opciones:\n1- Programación I\n2- Programación II\n3- Laboratorio\n4- Ingles I\n5- Ingles II\n"))
                    if opcionCurso == 1:
                        i = 0
                    elif opcionCurso == 2:
                        i = 1
                    elif opcionCurso == 3:
                        i = 2
                    elif opcionCurso == 4:
                        i = 3
                    elif opcionCurso == 5:
                        i = 4
                    else:
                        print(
                            "Selecciono una opcion incorrecta (1-5). Intentelo de nuevo...")
                    estudiantes.matricularse(i)
                elif opc == 2:
                    emailCursos = str(
                        input("Ingrese el email para ver sus cursos:"))
                    resultado = estudiantes.mostrarCursos(emailCursos)
                    print(resultado)

                elif opc == 3:
                    menu()

                else:
                    print("Opcion incorrecta (1-3)\nIntentelo de nuevo...\n")

            else:
                print("Email o contraseña incorrecta")
        elif opcion == 3:
            return menu()

        else:
            print("Opcion incorrecta (1-3). Intentelo de nuevo...\n")
