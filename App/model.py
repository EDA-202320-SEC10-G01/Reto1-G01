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
    
    partidos_por_equipo = lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(data_structs["results"]):
        if i["home_team"] == equipo or i["away_team"] == equipo:
            if condicion == 3:
                lt.addLast(partidos_por_equipo, i)
            elif condicion == 1:
                if i["home_team"] == equipo and i["neutral"] == "False":
                    lt.addLast(partidos_por_equipo, i)
            elif condicion == 2:
                if i["away_team"] == equipo:
                    lt.addLast(partidos_por_equipo, i)
            else:
                print("Condicion no valida")
            
    partidos_encontrados = lt.size(partidos_por_equipo)
    partidos_a_mostrar = lt.newList("ARRAY_LIST")
    
    if n_partidos <= partidos_encontrados:
        partidos_a_mostrar = lt.subList(partidos_por_equipo, 1, n_partidos)
        
    else:
        partidos_a_mostrar = lt.subList(partidos_por_equipo, 1, partidos_encontrados)
        
    return partidos_a_mostrar, partidos_encontrados
                   
def req_2(data_structs, n_goles, jugador):
    
    goles_marcados = st.newStack()

    for i in lt.iterator(data_structs["goalscorers"]):
        if i["scorer"] == jugador:
            st.push(goles_marcados, i)
                   
    goles_encontrados = st.size(goles_marcados)
    goles_a_mostrar = lt.newList("ARRAY_LIST")
    
    if n_goles <= goles_encontrados:
        for i in range(1, n_goles + 1):
            lt.addLast(goles_a_mostrar, st.pop(goles_marcados))
        
    else:
        for i in range(1, goles_encontrados + 1):
            lt.addLast(goles_a_mostrar, st.pop(goles_marcados))
            
        
    return goles_a_mostrar, goles_encontrados
        
def req_3(data_structs, equipo, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final):

    partidos_por_equipo = lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(data_structs["results"]):
        fecha = i["date"].split("-")
        if revisar_intervalo(fecha[2], fecha[1], fecha[0], dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final):
            if i["home_team"] == equipo or i["away_team"] == equipo:
                lt.addLast(partidos_por_equipo, i)
                
    return partidos_por_equipo


def req_4(data_structs, torneo, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final):
        
    
        shootouts = {}
        
        for shootout in lt.iterator(data_structs["shootouts"]):
            llave = f"{shootout['date']}-{shootout['home_team']}-{shootout['away_team']}"
            shootouts[llave] = shootout
            
        partidos = lt.newList("ARRAY_LIST")
        
        for result in lt.iterator(data_structs["results"]):
            fecha = result["date"].split("-")
            llave = f"{result['date']}-{result['home_team']}-{result['away_team']}"
            if revisar_intervalo(fecha[2], fecha[1], fecha[0], dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final) and result["tournament"] == torneo:
                if llave in shootouts:
                    result["shootout"] = True
                    result["shootout_winner"] = shootouts[llave]["winner"]
                    lt.addLast(partidos, result)
                elif result["home_score"] > result["away_score"] or result["home_score"] < result["away_score"]:
                    result["shootout"] = False
                    result["shootout_winner"] = "None"
                    lt.addLast(partidos, result)
                else:
                    result["shootout"] = "DESCONOCIDO "
                    result["shootout_winner"] = "DESCONOCIDO"
                    lt.addLast(partidos, result)
                    
        return partidos, {}, {}
                    

    
def req_5 (data_structs, anotador, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final):
    
    
    results = {}
    
    for result in lt.iterator(data_structs["results"]):
        llave = f"{result['date']}-{result['home_team']}-{result['away_team']}"
        results[llave] = result
         
    goles = lt.newList("ARRAY_LIST")
    torneos = {}
    autogoles = 0
    penales = 0
    
    for goalscorer in lt.iterator(data_structs["goalscorers"]):
        date = goalscorer["date"].split("-")
        if goalscorer["scorer"] == anotador and revisar_intervalo(date[2], date[1], date[0], dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final):
            llave = f"{goalscorer['date']}-{goalscorer['home_team']}-{goalscorer['away_team']}"
            if llave in results:
                goalscorer["tournament"] = results[llave]["tournament"]
                goalscorer["home_score"] = results[llave]["home_score"]
                goalscorer["away_score"] = results[llave]["away_score"]
                lt.addLast(goles, goalscorer)
            else:
                goalscorer["tournament"] = "DESCONOCIDO"
                goalscorer["home_score"] = "DESCONOCIDO"
                goalscorer["away_score"] = "DESCONOCIDO"
                lt.addLast(goles, goalscorer)
                
                
            if goalscorer["tournament"] not in torneos:
                torneos[goalscorer["tournament"]] = 1
            else:
                torneos[goalscorer["tournament"]] += 1
            
            if goalscorer["own_goal"] == "True":
                autogoles += 1
            
            if goalscorer["penalty"] == "True":
                penales += 1
                
                
    return goles, len(torneos), autogoles, penales
    
        
        
        
    
    


def req_6(data_structs, n_equipos, torneo, dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final):
    
    def puntos_linea_penal(result, equipo, diccionario_shootouts):
        
        if result["home_score"] != result["away_score"]:
            return 0
        else:
            llave = f"{result['date']}-{result['home_team']}-{result['away_team']}"
            if llave in diccionario_shootouts:
                shootout = diccionario_shootouts[llave]
                if equipo == shootout["winner"]:
                    return 3
                else:
                    return 0
            else:
                return 0
            
    def autogoles(result, equipo, diccionario_goalscorers):
        
        autogoles = 0
        llave = f"{result['date']}-{result['home_team']}-{result['away_team']}"
        
        if llave in diccionario_goalscorers:
            goles = diccionario_goalscorers[llave]
            for gol in lt.iterator(goles):
                if gol["team"] != equipo and gol["own_goal"] == "True":
                    autogoles += 1
        
        return autogoles
    
    
    def puntos_obtenidos(result, equipo):
        
        if equipo == result["home_team"]:
            if result["home_score"] > result["away_score"]:
                return 3, [1,0,0]
            elif result["home_score"] == result["away_score"]:
                return 1, [0,1,0]
            else:
                return 0, [0,0,1]
            
        elif equipo == result["away_team"]:
            if result["home_score"] < result["away_score"]:
                return 3, [1,0,0]
            elif result["home_score"] == result["away_score"]:
                return 1, [0,1,0]   
            else:
                return 0, [0,0,1]
        
    
    def crear_estadisticas(result, diccionario_shootouts, diccionario_goalscorers):
        
        estadistica_uno = {}
        estadistica_dos = {}
        
        estadistica_uno["team"] = result["home_team"]
        estadistica_uno["puntos"] = puntos_obtenidos(result, result["home_team"])[0]
        estadistica_uno["diferencia_goles"] = int(result["home_score"]) - int(result["away_score"])
        estadistica_uno["partidos_jugados"] = 1
        estadistica_uno["puntos_linea_penal"] = 0
        estadistica_uno["puntos_autogol"] = 0
        estadistica_uno["victorias"] = puntos_obtenidos(result, result["home_team"])[1][0]
        estadistica_uno["empates"] = puntos_obtenidos(result, result["home_team"])[1][1]
        estadistica_uno["derrotas"] = puntos_obtenidos(result, result["home_team"])[1][2]
        estadistica_uno["goles_jugadores_propios"] = int(result["home_score"]) - autogoles(result, result["home_team"], diccionario_goalscorers)
        estadistica_uno["goles_jugadores_rivales"] = int(result["away_score"])
        
        estadistica_dos["team"] = result["away_team"]
        estadistica_dos["puntos"] = puntos_obtenidos(result, result["away_team"])[0]
        estadistica_dos["diferencia_goles"] = int(result["away_score"]) - int(result["home_score"])
        estadistica_dos["partidos_jugados"] = 1
        estadistica_dos["puntos_linea_penal"] = 0
        estadistica_dos["puntos_autogol"] = 0
        estadistica_dos["victorias"] = puntos_obtenidos(result, result["away_team"])[1][0]
        estadistica_dos["empates"] = puntos_obtenidos(result, result["away_team"])[1][1]
        estadistica_dos["derrotas"] = puntos_obtenidos(result, result["away_team"])[1][2]
        estadistica_dos["goles_jugadores_propios"] = int(result["away_score"]) - autogoles(result, result["away_team"], diccionario_goalscorers)
        estadistica_dos["goles_jugadores_rivales"] = int(result["home_score"])
        
        return estadistica_uno, estadistica_dos
    
    
    
    
    
    diccionario_shootouts = {}    
    for shootout in lt.iterator(data_structs["shootouts"]):    
        llave = f"{shootout['date']}-{shootout['home_team']}-{shootout['away_team']}"
        diccionario_shootouts[llave] = shootout
        
    diccionario_goalscorers = {}
    for goalscorer in lt.iterator(data_structs["goalscorers"]):
        llave = f"{goalscorer['date']}-{goalscorer['home_team']}-{goalscorer['away_team']}"
        if llave not in diccionario_goalscorers:
            diccionario_goalscorers[llave] = lt.newList("ARRAY_LIST")
            lt.addLast(diccionario_goalscorers[llave], goalscorer)
        else:
            lt.addLast(diccionario_goalscorers[llave], goalscorer)
    
    
    
            
        
    estadisticas_torneo = lt.newList("ARRAY_LIST")
    
    indices_estadisticas = {}
    
    for result in lt.iterator(data_structs["results"]):
        fecha = result["date"].split("-")
        if result["tournament"] == torneo and revisar_intervalo(fecha[2], fecha[1], fecha[0], dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final):
            estadistica_uno, estadistica_dos = calcular_estadisticas(result, diccionario_shootouts)
            if estadistica_uno["team"] not in indices_estadisticas:
                indices_estadisticas[estadistica_uno["team"]] = lt.size(estadisticas_torneo) + 1
                lt.addLast(estadisticas_torneo, estadistica_uno)
            else:
                estadistica = lt.getElement(estadisticas_torneo, indices_estadisticas[estadistica_uno["team"]])
                estadistica["puntos"] += estadistica_uno["puntos"]
                estadistica["diferencia_goles"] += estadistica_uno["diferencia_goles"]
                estadistica["partidos_jugados"] += estadistica_uno["partidos_jugados"]
                estadistica["puntos_linea_penal"] += estadistica_uno["puntos_linea_penal"]
                estadistica["puntos_autogol"] += estadistica_uno["puntos_autogol"]
                estadistica["victorias"] += estadistica_uno["victorias"]
                estadistica["empates"] += estadistica_uno["empates"]
                estadistica["derrotas"] += estadistica_uno["derrotas"]
                estadistica["goles_jugadores_propios"] += estadistica_uno["goles_jugadores_propios"]
                estadistica["goles_jugadores_rivales"] += estadistica_uno["goles_jugadores_rivales"]
                lt.changeInfo(estadisticas_torneo, indices_estadisticas[estadistica_uno["team"]], estadistica)
                
            if estadistica_dos["team"] not in indices_estadisticas:
                indices_estadisticas[estadistica_dos["team"]] = lt.size(estadisticas_torneo) + 1
                lt.addLast(estadisticas_torneo, estadistica_dos)
            else:
                estadistica = lt.getElement(estadisticas_torneo, indices_estadisticas[estadistica_dos["team"]])
                estadistica["puntos"] += estadistica_dos["puntos"]
                estadistica["diferencia_goles"] += estadistica_dos["diferencia_goles"]
                estadistica["partidos_jugados"] += estadistica_dos["partidos_jugados"]
                estadistica["puntos_linea_penal"] += estadistica_dos["puntos_linea_penal"]
                estadistica["puntos_autogol"] += estadistica_dos["puntos_autogol"]
                estadistica["victorias"] += estadistica_dos["victorias"]
                estadistica["empates"] += estadistica_dos["empates"]
                estadistica["derrotas"] += estadistica_dos["derrotas"]
                estadistica["goles_jugadores_propios"] += estadistica_dos["goles_jugadores_propios"]
                estadistica["goles_jugadores_rivales"] += estadistica_dos["goles_jugadores_rivales"]
                lt.changeInfo(estadisticas_torneo, indices_estadisticas[estadistica_dos["team"]], estadistica)
                
                
    quk.sort(estadisticas_torneo, sort_criteria_estadisticas)
    
    equipos_encontrados = lt.size(estadisticas_torneo)
    
    if n_equipos <= equipos_encontrados:
        equipos_a_mostrar = lt.subList(estadisticas_torneo, 1, n_equipos)
        
    else:
        equipos_a_mostrar = lt.subList(estadisticas_torneo, 1, equipos_encontrados)
        
    return equipos_a_mostrar, equipos_encontrados
    
    
    
               
    
                    


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
    
    if comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "mayor":
        return True
    elif comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "igual":
        if data_1["home_team"] < data_2["home_team"]:
            return True
    else:
        return False
    
def sort_criteria_goalscorers(data_1, data_2):
    
    fecha_1 = data_1["date"].split("-")
    fecha_2 = data_2["date"].split("-")
    
    if comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "mayor":
        return True
    elif comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "igual":
        if data_1["home_team"] < data_2["home_team"]:
            return True        
    else:  
        return False
    
    
def sort_criteria_shootouts(data_1, data_2):
    
    fecha_1 = data_1["date"].split("-")
    fecha_2 = data_2["date"].split("-")
    
    if comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "mayor":
        return True
    elif comparar_fechas(fecha_1[2], fecha_1[1], fecha_1[0], fecha_2[2], fecha_2[1], fecha_2[0]) == "igual":
        if data_1["home_team"] < data_2["home_team"]:
            return True    
    else:
        return False
    
def sort_criteria_estadisticas(data_1, data_2):
    
    if data_1["puntos"] > data_2["puntos"]:
        return True
    elif data_1["puntos"] == data_2["puntos"]:
        if data_1["diferencia_goles"] > data_2["diferencia_goles"]:
            return True
        elif data_1["diferencia_goles"] == data_2["diferencia_goles"]:
            return True
        else:
            return False
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
        
        

