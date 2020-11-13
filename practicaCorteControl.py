import csv
import os

def pedirNombre():
    while True:
        nombre = input("Se creará un archivo \n\tingrese nombre del archivo que desea crear:  ")
        try:
            return str(f"{nombre}.csv")
        except ValueError:
            print("error al nombrar archivo")


def cargardatos(archivo,campos):
    guardar = "si"
    filasCarga = []
    while guardar == "si":
        empleado = {}

        for campo in campos:
            empleado[campo] = input(f"Ingrese {campo} del Empleado: ")
        filasCarga.append(empleado)
        guardar = input("Desea seguir agregando empleados? Si/No")

    try:
        # nombreArchivo = pedirNombre()
        hayAlgunArchivo = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as file:
            archivoAGrabar = csv.DictWriter(file, fieldnames=campos)

            if not hayAlgunArchivo:
                archivoAGrabar.writeheader()

            archivoAGrabar.writerows(filasCarga)
            print("Empleado Cargado Exitosamente!")
            return
    except IOError:
        print("no se reconoce el archivo.")

def recuperarVacacionesPendientes(archivo, legajos):

        archivo2 = legajos

        archivo2 = open(archivo2)#se abre el archivo notas
        archivo = open(archivo)#se abre el achivo alumnos
        archivo2CSV = csv.reader(archivo2, delimiter=";")#se lee el archivo notas
        archivo1CSV = csv.reader(archivo, delimiter=",")#se lee el archivo

        # Saltea los encabezados
        next(archivo2CSV)
        next(archivo1CSV)
        contadorDias = 0
        totalVacaciones = 0
        diasTomados = 0
        diasRestantes = 0
        contador = 0
        # Empieza a leer
        empleado = next(archivo1CSV, None)
        legajo = next(archivo2CSV, None)
        expresion = input("legajo a buscar:  ")
        for linea in archivo2CSV:
            if expresion in legajo:
                if expresion in linea[0]:
                    contadorDias += 1


        while (empleado and legajo):
            # print(f"{legajo[0]}")
            if (not legajo or legajo[0] != empleado[0]):
                print("\tNo se registran legajos")
            while (empleado and legajo and legajo[0] == empleado[0]):
                for vez in archivo1CSV:
                    if  expresion in vez:

                        print(empleado)
                        diasRestantes = int(vez[0]) - contador
                        print(f"dias tomados: {vez[3]}, debe {diasRestantes}")
                    # diasPendientes += int(vez[0])
                    contadorDias += int(legajo[0])
                # print(f"\tse tomo Vacaciones los dias {legajo[1]} ")
                legajo = next(archivo2CSV, None)
            empleado = next(archivo1CSV, None)



            diasRestantes = diasPendientes - contadorDias
            # print(f"dias tomados: {contadorDias}, debe {diasRestantes}")
        archivo2.close()
        archivo.close()



# def recupero(archivoEmpleados, archivoLegajos):
#
#     try:
#         with open(archivoEmpleados, 'r', newline="") as file:
#             with open(archivoLegajos, 'r', newline="") as file2:
#                 empleados_csv = csv.reader(file)
#                 legajos_csv = csv.reader(file2)
#
#                 empleado = next(empleados_csv)
#                 legajo = next(legajos_csv)
#                 busqueda = input("legajo a buscar:  ")
#
#                 columnas = empleados_csv.
#
#
#                 while empleado and legajo:
#                     for vuelta in empleados_csv:
#                         print(legajo)
#                         empleado = next(empleados_csv, None)
#                         legajo = next(legajos_csv, None)
#
#
#
#
#             pass
#     except Exception as e:
#         raise
#
#
#


def main():

    LEGAJOS= "legajo.csv"
    CAMPOS = ['Legajo','Apellido','Nombre','Total Vacaciones']
    CAMPOSLEGAJOS = ['Legajo','Fecha']
    while True:
        print("\tElija una opcion:\n\t 1.Cargar datos de Empleados \n\t 2.Consulta dias de VacacionesPendientes\n\t 3.Salir")
        opcion = input("")


        if opcion == "1":

            archivo = pedirNombre()
            cargardatos(archivo, CAMPOS)


        if opcion == "2":
            archivo = input("ingrese nombre del archivo a recuperar")
            try:
                recuperarVacacionesPendientes(f"{archivo}.csv",LEGAJOS)
            except IOError:
                print("error de lectura I/O")
            # except:
            #     print("otro tipo de error")

        if opcion == "3":
            exit()
        else:
            print("elija una opcion valida")
main()
