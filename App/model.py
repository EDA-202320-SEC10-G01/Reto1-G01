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
    

#Funciones de los requerimientos

def req_1(data_structs, equipo, condicion, n_partidos):
    """
    Función que soluciona el requerimiento 1
    """
    def es_equipo_local(partido):
        return (partido["home_team"] == equipo and partido["neutral"] == "False")
    
    
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
                   
def req_2(data_structs, n_goles, jugador):
    
    goles_marcados = lt.newList("ARRAY_LIST")

    for i in lt.iterator(data_structs["goalscorers"]):
        if i["scorer"] == jugador:
            lt.addLast(goles_marcados, i)
            
    goles_encontrados = lt.size(goles_marcados)
    
    if n_goles <= goles_encontrados:
        goles_a_mostrar = lt.subList(goles_marcados, 1, n_goles)
        
    else:
        goles_a_mostrar = lt.subList(goles_marcados, 1, goles_encontrados)
        
    return goles_a_mostrar, goles_encontrados
        
def req_3(data_structs, equipo, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final):

    partidos_por_equipo = lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(data_structs["results"]):
        fecha = i["date"].split("-")
        if revisar_intervalo(fecha[2], fecha[1], fecha[0], dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final):
            if i["home_team"] == equipo or i["away_team"] == equipo:
                lt.addLast(partidos_por_equipo, i)
                
    return partidos_por_equipo


    
                    
            
    
                    


def comparar_fechas(primer_dia, primer_mes, primer_año, segundo_dia, segundo_mes, segundo_año):
    if int(primer_año) < int(segundo_año):
        return "menor"
    elif int(primer_año) == int(segundo_año):
        if int(primer_mes) < int(segundo_mes):
            return "menor"
        elif int(primer_mes) == int(segundo_mes):
            if int(primer_dia) < int(segundo_dia):
                return "menor"
            elif int(primer_dia) == int(segundo_dia):
                return "igual"
            else:
                return "mayor"
        else:
            return "mayor"
    else:
        return "mayor"
    
    
def revisar_intervalo(dia, mes, año, dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final):
    
    if comparar_fechas(dia, mes, año, dia_inicial, mes_inicial, año_inicial) == "mayor" and comparar_fechas(dia, mes, año, dia_final, mes_final, año_final) == "menor":
        return True
    elif comparar_fechas(dia, mes, año, dia_inicial, mes_inicial, año_inicial) == "igual" or comparar_fechas(dia, mes, año, dia_final, mes_final, año_final) == "igual":
        return True
    else:
        return False
    


def sort_criteria_results(data_1, data_2):
    
    fecha_1 = data_1["date"].split("-")
    fecha_2 = data_2["date"].split("-")
    
    if comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "menor":
        return True
    elif comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "igual":
        if data_1["home_team"] < data_2["home_team"]:
            return True
    else:
        return False
    
def sort_criteria_goalscorers(data_1, data_2):
    
    fecha_1 = data_1["date"].split("-")
    fecha_2 = data_2["date"].split("-")
    
    if comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "menor":
        return True
    elif comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "igual":
        if data_1["home_team"] < data_2["home_team"]:
            return True        
    else:  
        return False
    
    
def sort_criteria_shootouts(data_1, data_2):
    
    fecha_1 = data_1["date"].split("-")
    fecha_2 = data_2["date"].split("-")
    
    if comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "menor":
        return True
    elif comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "igual":
        if data_1["home_team"] < data_2["home_team"]:
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
    elif sort_algorithm == "4":
        merg.sort(data_structs, sort_criteria)
    elif sort_algorithm == "5":
        quk.sort(data_structs, sort_criteria)
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
        
        

