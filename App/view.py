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


def print_data(control):
    
    def print_results(control):
        headers1 = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "home_score": "Marcador local",
                    "away_score": "Marcador visitante",
                    "tournament": "Torneo",
                    "city": "Ciudad",
                    "country": "País",
                    "neutral": "Neutral"}
        
        
        first_three = lt.subList(control["model"]["results"], 1, 3)
        
        last_three = lt.subList(control["model"]["results"], lt.size(control["model"]["results"])-2, 3)

        combined_list = lt.newList("ARRAY_LIST")
        
        for i in range(lt.size(first_three)):
            lt.addLast(combined_list, lt.getElement(first_three, i))

        for i in range(lt.size(last_three)):
            lt.addLast(combined_list, lt.getElement(last_three, i))
            
        print(tabulate(lt.iterator(combined_list), headers1, tablefmt="fancy_grid"))
        
    def print_goalscorers(control):
        headers2 = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "team": "Equipo",
                    "scorer": "Anotador",
                    "minute": "Minuto",
                    "own_goal": "Autogol",
                    "penalty": "Penal"}
        
        first_three = lt.subList(control["model"]["goalscorers"], 1, 3)
        
        last_three = lt.subList(control["model"]["goalscorers"], lt.size(control["model"]["goalscorers"])-2, 3)
        
        combined_list = lt.newList("ARRAY_LIST")
        
        for i in range(lt.size(first_three)):
            lt.addLast(combined_list, lt.getElement(first_three, i))
        
        for i in range(lt.size(last_three)):
            lt.addLast(combined_list, lt.getElement(last_three, i))
        
        print(tabulate(lt.iterator(combined_list), headers2, tablefmt="fancy_grid"))

    def print_shootouts(control):
        headers3 = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "winner": "Ganador"}
        
        first_three = lt.subList(control["model"]["shootouts"], 1, 3)
        
        last_three = lt.subList(control["model"]["shootouts"], lt.size(control["model"]["shootouts"])-2, 3)
        
        combined_list = lt.newList("ARRAY_LIST")
        
        for i in range(lt.size(first_three)):
            lt.addLast(combined_list, lt.getElement(first_three, i))
        
        for i in range(lt.size(last_three)):
            lt.addLast(combined_list, lt.getElement(last_three, i))
        
        print(tabulate(lt.iterator(combined_list), headers3, tablefmt="fancy_grid"))

    if lt.isEmpty(control["model"]["results"]) == False:
        print("Los primeros y últimos 3 resultados cargados son: \n")
        print_results(control)
        
    if lt.isEmpty(control["model"]["goalscorers"]) == False:
        print("Los primeros y últimos 3 anotadores cargados son: \n")
        print_goalscorers(control)
    
    if lt.isEmpty(control["model"]["shootouts"]) == False:
        print("Las primeras y últimas 3 tandas de penales son: \n")
        print_shootouts(control)
        
    
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
    
    equipo = input("Ingrese el nombre del equipo: \n")
    n_partidos = int(input("Ingrese el número de partidos: \n"))
    condicion = input("Ingrese la condición: \n")
    
    matches = controller.req_1(control, n_partidos, equipo, condicion)
    
    print("Los partidos son: \n")
    print(tabulate(lt.iterator(matches), tablefmt="fancy_grid"))

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
