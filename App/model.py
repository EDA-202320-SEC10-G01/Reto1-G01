﻿"""
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


    
# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    results_size = lt.size(data_structs["results"])
    shootouts_size = lt.size(data_structs["shootouts"])
    goalscorers_size = lt.size(data_structs["goalscorers"])
    
    return results_size, shootouts_size, goalscorers_size
    


def req_1(data_structs, n_partidos, equipo, condicion):
    
    """
    Función que soluciona el requerimiento 1
    """
    
    def is_team_local(result, equipo):
        if result["neutral"] == "False" and result["home_team"] == equipo:
            return True
        else:
            return False
        
    queue = qu.newQueue()
    counter = 1
    while queue["size"] < n_partidos:
            result = lt.getElement(data_structs["results"], counter)
            counter += 1
            if equipo == result["home_team"] or equipo == result["away_team"]:
                if condicion == "indiferente":
                    qu.enqueue(queue, result)
                elif condicion == "local":
                    if is_team_local(result, equipo):
                        qu.enqueue(queue, result)
                elif condicion == "visitante":
                    if not is_team_local(result, equipo):
                        qu.enqueue(queue, result)
            else:
                pass
            
    return queue
                
                
                


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


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


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs, sort_criteria):
    """
    Función encargada de ordenar la lista con los datos
    """
    quk.sort(data_structs, sort_criteria)
