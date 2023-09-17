"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""
# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    football_data = {"results": None,
                     "goalscorers": None,
                     "shootouts": None,}
    
    football_data["results"] = lt.newList("ARRAY_LIST")
    football_data["goalscorers"] = lt.newList("ARRAY_LIST")
    football_data["shootouts"] = lt.newList("ARRAY_LIST")
    
    return football_data


# Funciones para agregar informacion al modelo

def add_result(data_structs, data):
    
    lt.addLast(data_structs["results"], data)
    
def add_goalscorer(data_structs, data):
    
    lt.addLast(data_structs["goalscorers"], data)
    
def add_shootout(data_structs, data):
    
    lt.addLast(data_structs["shootouts"], data)

def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    results_size = lt.size(data_structs["results"])
    shootouts_size = lt.size(data_structs["shootouts"])
    goalscorers_size = lt.size(data_structs["goalscorers"])
    
    return results_size, shootouts_size, goalscorers_size
    


def req_1(data_structs, equipo, condicion, n_partidos):
    """
    Función que soluciona el requerimiento 1
    """
    def es_equipo_local(partido):
        return partido["home_team"] == equipo
    
    
    partidos_por_equipo = st.newStack()
    
    for i in lt.iterator(data_structs["results"]):
        if i["home_team"] == equipo or i["away_team"] == equipo:
            if condicion == 3:
                st.push(partidos_por_equipo, i)
            elif condicion == 1:
                if es_equipo_local(i):
                    st.push(partidos_por_equipo, i)
            elif condicion == 2:
                if not es_equipo_local(i):
                    st.push(partidos_por_equipo, i)
            else:
                print("Condicion no valida")
            
    partidos_encontrados = st.size(partidos_por_equipo)
    partidos_a_mostrar = lt.newList("ARRAY_LIST")
    
    if n_partidos <= partidos_encontrados:
        for i in range(1, n_partidos + 1):
            lt.addLast(partidos_a_mostrar, st.pop(partidos_por_equipo))
            
    else:
        for i in range(1, partidos_encontrados + 1):
            lt.addLast(partidos_a_mostrar, st.pop(partidos_por_equipo))
            
    return partidos_a_mostrar, partidos_encontrados
        
        
    
    
                
                
            
def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria_results(data_1, data_2):
    if data_1["date"] < data_2["date"]:
        return True
    elif data_1["date"] == data_2["date"]:
        if data_1["country"] < data_2["country"]:
            return True
    else:
        return False
    
def sort_criteria_goalscorers(data_1, data_2):
    if data_1["date"] < data_2["date"]:
        return True
    elif data_1["date"] == data_2["date"]:
        if data_1["scorer"] < data_2["scorer"]:
            return True
    else:
        return False
    
def sort_criteria_shootouts(data_1, data_2):
    if data_1["date"] < data_2["date"]:
        return True
    elif data_1["date"] == data_2["date"]:
        if data_1["winner"] < data_2["winner"]:
            return True
    else:
        return False
 

def sorting_algorithm(data_structs, sort_criteria, sort_algorithm):
    
    if sort_algorithm == "1":
        ins.sort(data_structs, sort_criteria)
    elif sort_algorithm == "2":
        se.sort(data_structs, sort_criteria)
    elif sort_algorithm == "3":
        sa.sort(data_structs, sort_criteria)
    else:
        print("Algoritmo no válido")
        
        
def sort(data_structs, sort_algorithm, datos):
    """
    Función encargada de ordenar la lista con los datos
    """
    if datos == "1":
        sorting_algorithm(data_structs["results"], sort_criteria_results, sort_algorithm)
    elif datos == "2":
        sorting_algorithm(data_structs["goalscorers"], sort_criteria_goalscorers, sort_algorithm)
    elif datos == "3":
        sorting_algorithm(data_structs["shootouts"], sort_criteria_shootouts, sort_algorithm)
    elif datos == "4":
        sorting_algorithm(data_structs["results"], sort_criteria_results, sort_algorithm)
        sorting_algorithm(data_structs["goalscorers"], sort_criteria_goalscorers, sort_algorithm)
        sorting_algorithm(data_structs["shootouts"], sort_criteria_shootouts, sort_algorithm)
    else:
        print("Opcion no valida")
        
        

