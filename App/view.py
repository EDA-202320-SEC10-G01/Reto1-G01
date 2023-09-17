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
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback

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
    print("2- Consultar ultimos partidos jugados por un equipo")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10 -Escoger representacion de la lista en el modelo")
    print("11- Ordenar datos")
    print("0- Salir")


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
        
    
def sort(control):
    sort_algo = input ("""Ingrese el numero asociado al algoritmo de ordenamiento: \n
    1. Selection Sort \n
    2. Insertion Sort \n
    3. Shell Sort \n""")
    
    datos = input("""Ingrese que datos desea ordenar: \n
    1. Resultados \n
    2. Anotadores \n
    3. Tandas de penal \n
    4. todos \n""")
    
    
    controller.sort(control, sort_algo, datos)  

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
    
    
    partidos_por_equipo, partidos_encontrados = controller.req_1(control, equipo, condicion, n_partidos)

    print(f"Se encontraron {partidos_encontrados} partidos que cumplen con la condiciónes dadas, de los cuales se tomaron los {lt.size(partidos_por_equipo)} mas recientes \n)")
    print_table(partidos_por_equipo, headers)

def print_tipo_dato_abstracto(control):
    
    tipo = input("""Ingrese el tipo de dato que desea para representar la listas de datos: \n
    1. Array List \n
    2. Linked List \n""")
    
    controller.tipo_dato_abstracto(control, tipo)

# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
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
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)
            
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
