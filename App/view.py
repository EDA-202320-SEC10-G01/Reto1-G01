"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import list as lt
assert cf
from tabulate import tabulate
import traceback
import threading


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    
    return controller.new_controller()
    
def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Consultar ultimos N partidos jugados por un equipo")
    print("3- Consultar los primeros N goles de un jugador")
    print("4- Consultar partidos de un equipo en un periodo especifico")
    print("5- Consultar partidos relacionados con un torneo en un periodo especifico")
    print("6- Consultar anotaciones de un jugador en un periodo especifico")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10 -Escoger representacion de la lista en el modelo")
    print("11- Ordenar datos")
    print("0- Salir")

#Funciones para cargar los datos y ordenarlos

def load_data(control):
    
    archivo = input("""Ingrese el numero asociado al archivo a cargar: \n
    1. Resultados de los partidos \n
    2. Anotadores en los partidos \n
    3. Tandas de penales \n
    4. Todos \n""")
    
    tamaño = input("""Ingrese el numero asociado al tamaño de la muestra: \n
    1. small \n
    2. 5pct \n
    3. 10pct \n
    4. 20pct \n
    5. 30pct \n
    6. 50pct \n
    7. 80pct \n
    8. large \n""")
    
    orden = input("""Desea ordenar los datos antes de que se muestren en pantalla? \n
    1. Si \n
    2. No \n""")
    
    
    controller.load_data(control, archivo, tamaño)   
    if orden == "1":
        sort(control)
    else:
        pass

def sort(control):
    sort_algo = input ("""Ingrese el numero asociado al algoritmo de ordenamiento: \n
    1. Selection Sort \n
    2. Insertion Sort \n
    3. Shell Sort \n
    4. Merge Sort \n
    5. Quick Sort \n""")
    
    datos = input("""Ingrese que datos desea ordenar: \n
    1. Resultados \n
    2. Anotadores \n
    3. Tandas de penal \n
    4. Todos \n""")
    
    
    controller.sort(control, sort_algo, datos)  

#Funciones para imprimir las tablas y los datos

def print_table(data, headers):

    if lt.size(data) == 0:
        print("No se encontraron datos para mostrar")

    elif lt.size(data) > 6:
        first_three = lt.subList(data, 1, 3) 
        last_three = lt.subList(data, lt.size(data)-2, 3)
        combined_list = lt.newList("ARRAY_LIST")
        
        for i in lt.iterator(first_three):
            lt.addLast(combined_list, i)
        
        for i in lt.iterator(last_three):
            lt.addLast(combined_list, i)
        
        print(f"De {lt.size(data)} elementos, se muestran los primeros y ultimos 3\n")
        print(tabulate(lt.iterator(combined_list), headers, tablefmt="fancy_grid"))
        
    else:
        print(f"Se encontraron {lt.size(data)} elementos mostrados a continuacion\n")
        print(tabulate(lt.iterator(data), headers, tablefmt="fancy_grid"))

        
    
def print_data(control):
    
    headers_results = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "home_score": "Marcador local",
                    "away_score": "Marcador visitante",
                    "tournament": "Torneo",
                    "city": "Ciudad",
                    "country": "País",
                    "neutral": "Neutral"}
    headers_goalscorer = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "team": "Equipo",
                    "scorer": "Anotador",
                    "minute": "Minuto",
                    "own_goal": "Autogol",
                    "penalty": "Penal"}
    headers_shootouts = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "winner": "Ganador"}
    

    if lt.isEmpty(control["model"]["results"]) == False:
        print_table(control["model"]["results"], headers_results)
        
    if lt.isEmpty(control["model"]["goalscorers"]) == False:
        print_table(control["model"]["goalscorers"], headers_goalscorer)
    
    if lt.isEmpty(control["model"]["shootouts"]) == False:
        print_table(control["model"]["shootouts"], headers_shootouts)

#Funciones para imprimir los requerimientos

def print_req_1(control):
    
    headers = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "home_score": "Marcador local",
                    "away_score": "Marcador visitante",
                    "tournament": "Torneo",
                    "city": "Ciudad",
                    "country": "País"}
    
    equipo = input("Ingrese el nombre del equipo: \n")
    n_partidos = int(input("Ingrese el número de partidos: \n"))
    condicion = int(input("""Ingrese el numero asociado a la condición: \n
    1. Local \n
    2. Visitante \n
    3. Indiferente \n"""))
    
    
    partidos_por_equipo, partidos_encontrados, delta_time = controller.req_1(control, equipo, condicion, n_partidos)

    print("\n=============== Datos del usuario ==================")
    print("Nombre del equipo: ", equipo)
    print("Numero de partidos: ", n_partidos)
    print("Condicion: ", condicion)
    
    print("\n=============== Respuesta del programa ==================")
    print("Numero de partidos encontrados: ", partidos_encontrados)
    print(f"Seleccionando {lt.size(partidos_por_equipo)} partidos")
    print(f"Tiempo de ejecución del algoritmo sobre los datos indicados: {delta_time} ms")
    
    print_table(partidos_por_equipo, headers)

def print_req_2(control):
    
    headers = {"date": "Fecha",
               "home_team": "Equipo local",
               "away_team": "Equipo visitante",
               "team": "Equipo",
               "scorer": "Anotador",
               "minute": "Minuto",
               "own_goal": "Autogol",
               "penalty": "Penal"}
    
    n_goles = int(input("Ingrese el número de goles: \n"))
    jugador = input("Ingrese el nombre del jugador: \n")
    
    goles_a_mostrar, goles_encontrados, delta_time = controller.req_2(control, n_goles, jugador)
    
    print("\n=============== Datos del usuario ==================")
    print("Numero de goles: ", n_goles)
    print("Nombre del jugador: ", jugador)
    
    print("\n=============== Respuesta del programa ==================")
    print("Numero de goles encontrados: ", goles_encontrados)
    print(f"Seleccionando {lt.size(goles_a_mostrar)} goles")
    print(f"Tiempo de ejecución del algoritmo de sobre los datos indicados: {delta_time} ms")

    print_table(goles_a_mostrar, headers)
    
def print_req_3(control):
    
    headers = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "home_score": "Marcador local",
                    "away_score": "Marcador visitante",
                    "tournament": "Torneo",
                    "city": "Ciudad",
                    "country": "País"}
    
    año_inicial = input("Ingrese el año inicial: \n")
    mes_inicial = input("Ingrese el mes inicial: \n")
    dia_inicial = input("Ingrese el dia inicial: \n")
    
    año_final = input("Ingrese el año final: \n")
    mes_final = input("Ingrese el mes final: \n")
    dia_final = input("Ingrese el dia final: \n")
    
    
    equipo = input("Ingrese el nombre del equipo: \n")
    
    
    partidos_por_equipo, delta_time = controller.req_3(control, equipo, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final)
    
    print("\n=============== Datos del usuario ==================")
    print(f"Fecha inicial: {año_inicial}-{mes_inicial}-{dia_inicial}")
    print(f"Fecha final: {año_final}-{mes_final}-{dia_final}")
    print("Nombre del equipo: ", equipo)
    
    print("\n=============== Respuesta del programa ==================")
    print(f"Seleccionando {lt.size(partidos_por_equipo)} partidos")
    print(f"Tiempo de ejecución del algoritmo sobre los datos indicados: {delta_time} ms")
    
    print_table(partidos_por_equipo, headers)
    
def print_req_4(control):
    
    headers = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "shootout": "Tanda de penales",
                    "shootout_winner": "Ganador penales"}
    
    año_inicial = input("Ingrese el año inicial: \n")
    mes_inicial = input("Ingrese el mes inicial: \n")
    dia_inicial = input("Ingrese el dia inicial: \n")
    
    año_final = input("Ingrese el año final: \n")
    mes_final = input("Ingrese el mes final: \n")
    dia_final = input("Ingrese el dia final: \n")
    
    torneo = input("Ingrese el nombre del torneo: \n")
    
    partidos_por_torneo, paises, ciudades, delta_time = controller.req_4(control, torneo, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final)
    
    print("\n=============== Datos del usuario ==================")
    print(f"Fecha inicial: {año_inicial}-{mes_inicial}-{dia_inicial}")
    print(f"Fecha final: {año_final}-{mes_final}-{dia_final}")
    print("Nombre del torneo: ", torneo)
    
    print("\n=============== Respuesta del programa ==================")
    print("Numero de partidos encontrados: ", lt.size(partidos_por_torneo))
    print("Numero de paises encontrados: ", len(paises))
    print("Numero de ciudades encontradas: ", len(paises))
    print("Tiempo de ejecución del algoritmo sobre los datos indicados: ", delta_time)
    
    print_table(partidos_por_torneo, headers)
      
      
def print_req_5(control):
    
    headers = {"date": "Fecha",
               "minute": "Minuto",
               "home_team": "Equipo local",
               "away_team": "Equipo visitante",
               "team": "Equipo",
               "home_score": "Marcador local",
               "away_score": "Marcador visitante",
               "tournament": "Torneo",
               "penalty": "Penal",
               "own_goal": "Autogol"}
    
    año_inicial = input("Ingrese el año inicial: \n")
    mes_inicial = input("Ingrese el mes inicial: \n")
    dia_inicial = input("Ingrese el dia inicial: \n")
    
    año_final = input("Ingrese el año final: \n")
    mes_final = input("Ingrese el mes final: \n")
    dia_final = input("Ingrese el dia final: \n")
    
    anotador = input("Ingrese el nombre del anotador: \n")
    
    goles, n_torneos, n_autogoles, n_penales, delta_time = controller.req_5(control, anotador, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final)
    
    
    print("\n=============== Datos del usuario ==================")
    print(f"Fecha inicial: {año_inicial}-{mes_inicial}-{dia_inicial}")
    print(f"Fecha final: {año_final}-{mes_final}-{dia_final}")
    print("Nombre del anotador: ", anotador)
    
    print("\n=============== Respuesta del programa ==================")
    print("Numero de goles encontrados: ", lt.size(goles))
    print("Numero de torneos encontrados: ", n_torneos)
    print("Numero de autogoles encontrados: ", n_autogoles)
    print("Numero de penales encontrados: ", n_penales)
    print("Tiempo de ejecucion del algoritmo  sobre los datos indicados: ", delta_time)
    
    print_table(goles, headers)
          
      
      
    
def print_req_6(control):
    
    headers = {"team": "Equipo",
               "puntos": "Puntos",
               "diferencia_goles": "Diferencia de goles",
                "partidos_jugados": "Partidos jugados",
                "puntos_linea_penal": "Puntos linea penal",
                "puntos_autogol": "Puntos autogol",
                "victorias": "Victorias",
                "empates": "Empates", 
                "derrotas": "Derrotas",
                "goles_jugadores_propios": "Goles jugadores propios",
                "goles_jugadores_rivales": "Goles jugadores rivales"}
    
    año_inicial = input("Ingrese el año inicial: \n")
    mes_inicial = input("Ingrese el mes inicial: \n")
    dia_inicial = input("Ingrese el dia inicial: \n")
    
    año_final = input("Ingrese el año final: \n")
    mes_final = input("Ingrese el mes final: \n")
    dia_final = input("Ingrese el dia final: \n")
    
    n_equipos = int(input("Ingrese el numero de equipos: \n"))
    torneo = input("Ingrese el nombre del torneo: \n")
    
    equipos_a_mostrar, equipos_encontrados = controller.req_6(control, n_equipos, torneo, dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final)
    
    print("\n=============== Datos del usuario ==================")
    print(f"Fecha inicial: {año_inicial}-{mes_inicial}-{dia_inicial}")
    print(f"Fecha final: {año_final}-{mes_final}-{dia_final}")
    print("Numero de equipos: ", n_equipos)
    
    print("\n=============== Respuesta del programa ==================")
    print("Numero de equipos encontrados: ")
    print(f"Seleccionando {lt.size(equipos_a_mostrar)} equipos")
    
    print_table(equipos_a_mostrar, headers)

    
    
    
                
               

    
def print_tipo_dato_abstracto(control):
    
    tipo = input("""Ingrese el tipo de dato que desea para representar la listas de datos:  \n
    1. Array List \n
    2. Linked List \n""")
    
    controller.tipo_dato_abstracto(control, tipo)

# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    
    default_limit = 1000
    threading.stack_size(67108864*2)
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread()
    thread.start()
    
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()

        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            load_data(control)
            size = controller.get_datasize(control)
            print_data(control)
            print(f"Se cargaron {size[0]} resultados, {size[1]} tandas de penal y {size[2]} anotadores\n")

        elif int(inputs) == 2:
            print_req_1(control)
        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print(control["model"]["goalscorers_access"])

        elif int(inputs) == 9:
            print(control["model"]["shootouts_access"])
            
        elif int(inputs) == 10:
            print_tipo_dato_abstracto(control)
        
        elif int(inputs) == 11:
            sort(control)
            print_data(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
