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
    football_data = {"results": lt.newList("ARRAY_LIST"),
                     "goalscorers": lt.newList("ARRAY_LIST"),
                     "shootouts": lt.newList("ARRAY_LIST"),
                     "shootouts_access": {},
                     "results_access": {},
                     "goalscorers_access": {}}

    
    return football_data


# Funciones para agregar informacion al modelo

def add_result(data_structs, data):
    
    lt.addLast(data_structs["results"], data)
    
def add_goalscorer(data_structs, data):
    
    lt.addLast(data_structs["goalscorers"], data)
    
def add_shootout(data_structs, data):
    
    lt.addLast(data_structs["shootouts"], data)
    
def create_access_results(data_structs):
    
    results_access = {}
    
    for result in lt.iterator(data_structs["results"]):
        llave = f"{result['date']}-{result['home_team']}-{result['away_team']}"
        results_access[llave] = result
        
    data_structs["results_access"] = results_access
    
def create_access_shootouts(data_structs):
    
    shootouts_access = {}
    
    for shootout in lt.iterator(data_structs["shootouts"]):
        llave = f"{shootout['date']}-{shootout['home_team']}-{shootout['away_team']}"
        shootouts_access[llave] = shootout
        
    data_structs["shootouts_access"] = shootouts_access
    
def create_access_goalscorers(data_structs):
        
    goalscorers_access = {}
        
    for goalscorer in lt.iterator(data_structs["goalscorers"]):
        llave = f"{goalscorer['date']}-{goalscorer['home_team']}-{goalscorer['away_team']}-{goalscorer['scorer']}"
        if llave in goalscorers_access:
            lt.addLast(goalscorers_access[llave], goalscorer)
        else:
            goalscorers_access[llave] = lt.newList("ARRAY_LIST")
            lt.addLast(goalscorers_access[llave], goalscorer)
            
    data_structs["goalscorers_access"] = goalscorers_access
    

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
 
    partidos_por_equipo = qu.newQueue("ARRAY_LIST")
    
    for i in lt.iterator(data_structs["results"]):
        if i["home_team"] == equipo or i["away_team"] == equipo:
            if condicion == 3:
                qu.enqueue(partidos_por_equipo, i)
            elif condicion == 1:
                if i["home_team"] == equipo and i["neutral"] == "False":
                    qu.enqueue(partidos_por_equipo, i)
            elif condicion == 2:
                if i["away_team"] == equipo:
                    qu.enqueue(partidos_por_equipo, i)
            else:
                print("Condicion no valida")
            
    partidos_encontrados = qu.size(partidos_por_equipo)
    partidos_a_mostrar = lt.newList("ARRAY_LIST")
    
    while partidos_encontrados > 0 and lt.size(partidos_a_mostrar) < n_partidos:
        lt.addLast(partidos_a_mostrar, qu.dequeue(partidos_por_equipo))


        
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
        
            
        partidos = lt.newList("ARRAY_LIST")
        
        for result in lt.iterator(data_structs["results"]):
            fecha = result["date"].split("-")
            llave = f"{result['date']}-{result['home_team']}-{result['away_team']}"
            if revisar_intervalo(fecha[2], fecha[1], fecha[0], dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final) and result["tournament"] == torneo:
                if llave in data_structs["shootouts_access"]:
                    result["shootout"] = True
                    result["shootout_winner"] = data_structs["shootouts_access"][llave]["winner"]
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
         
    goles = lt.newList("ARRAY_LIST")
    torneos = {}
    autogoles = 0
    penales = 0
    
    for goalscorer in lt.iterator(data_structs["goalscorers"]):
        date = goalscorer["date"].split("-")
        if goalscorer["scorer"] == anotador and revisar_intervalo(date[2], date[1], date[0], dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final):
            llave = f"{goalscorer['date']}-{goalscorer['home_team']}-{goalscorer['away_team']}"
            if llave in data_structs["results_access"]:
                goalscorer["tournament"] = data_structs["results_access"][llave]["tournament"]
                goalscorer["home_score"] = data_structs["results_access"][llave]["home_score"]
                goalscorer["away_score"] = data_structs["results_access"][llave]["away_score"]
                lt.addLast(goles, goalscorer)
            else:
                goalscorer["tournament"] = "DESCONOCIDO"
                goalscorer["home_score"] = "DESCONOCIDO"
                goalscorer["away_score"] = "DESCONOCIDO"
                lt.addLast(goles, goalscorer)
                
                
            if goalscorer["tournament"] not in torneos:
                torneos[goalscorer["tournament"]] = 1
            
            if goalscorer["own_goal"] == "True":
                autogoles += 1
            
            if goalscorer["penalty"] == "True":
                penales += 1
                
                
    return goles, len(torneos), autogoles, penales
    
        
        
        
    
    


def req_6(data_structs, n_equipos, torneo, dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final):
    
    def obtener_puntos(resultado, equipo):
        if resultado["home_team"] == equipo:
            if resultado["home_score"] > resultado["away_score"]:
                return 3, [1, 0, 0]
            elif resultado["home_score"] == resultado["away_score"]:
                return 1, [0, 1, 0]
            else:
                return 0, [0, 0, 1]
        elif resultado["away_team"] == equipo:
            if resultado["home_score"] < resultado["away_score"]:
                return 3, [1, 0, 0]
            elif resultado["home_score"] == resultado["away_score"]:
                return 1, [0, 1, 0]
            else:
                return 0, [0, 0, 1]
    
    def goles_por_resultado(resultado, equipo, data_structs):
        
        llave = f"{resultado['date']}-{resultado['home_team']}-{resultado['away_team']}"
        goles = lt.newList("ARRAY_LIST")
        
        if llave in data_structs["goalscorers_access"]:
            for i in lt.iterator(data_structs["goalscorers_access"][llave]):
                if i["team"] == equipo:
                    lt.addLast(goles, i)
               
        return goles
    
    def calcular_goles_penal(resultado, equipo, data_structs):
        
        llave = f"{resultado['date']}-{resultado['home_team']}-{resultado['away_team']}"
        goles = 1
        
        if llave in data_structs["goalscorers_access"]:
            for i in lt.iterator(data_structs["goalscorers_access"][llave]):
                if i["team"] == equipo and i["penalty"] == "True":
                    goles += 1
               
        return goles
    
    def calcular_autogoles(resultado, equipo, data_structs):
        
        llave = f"{resultado['date']}-{resultado['home_team']}-{resultado['away_team']}"
        autogoles = 0
        
        if llave in data_structs["goalscorers_access"]:
            for i in lt.iterator(data_structs["goalscorers_access"][llave]):

                if i["team"] == equipo and i["own_goal"] == "True":
                    autogoles += 1
               
        return autogoles
    
    def crear_estadistica(resultado, data_structs):
        
        puntos_equipo1 = obtener_puntos(resultado, resultado["home_team"])[0]
        goles_penal_equipo1 = calcular_goles_penal(resultado, resultado["home_team"], data_structs)
        autogoles_equipo1 = calcular_autogoles(resultado, resultado["home_team"], data_structs)

        
        puntos_equipo2 = obtener_puntos(resultado, resultado["away_team"])[0]
        goles_penal_equipo2 = calcular_goles_penal(resultado, resultado["away_team"], data_structs)
        autogoles_equipo2 = calcular_autogoles(resultado, resultado["away_team"], data_structs)

        
        
        estadistica_uno = {"team": resultado["home_team"],
                           "puntos": puntos_equipo1,
                           "diferencia_goles": int(resultado["home_score"]) - int(resultado["away_score"]),
                           "partidos_jugados": 1,
                            "goles_penal": goles_penal_equipo1,
                            "autogoles": autogoles_equipo1,
                            "victorias": obtener_puntos(resultado, resultado["home_team"])[1][0],
                            "empates": obtener_puntos(resultado, resultado["home_team"])[1][1],
                            "derrotas": obtener_puntos(resultado, resultado["home_team"])[1][2],
                            "goles_favor": int(resultado["home_score"]) - goles_penal_equipo2,
                            "goles_en_contra": int(resultado["away_score"])}
                            
        estadistica_dos = {"team": resultado["away_team"],
                            "puntos": puntos_equipo2,
                            "diferencia_goles": int(resultado["away_score"]) - int(resultado["home_score"]),
                            "partidos_jugados": 1,
                             "goles_penal": goles_penal_equipo2,
                             "autogoles": autogoles_equipo2,
                             "victorias": obtener_puntos(resultado, resultado["away_team"])[1][0],
                             "empates": obtener_puntos(resultado, resultado["away_team"])[1][1],
                             "derrotas": obtener_puntos(resultado, resultado["away_team"])[1][2],
                             "goles_favor": int(resultado["away_score"]) - goles_penal_equipo1,
                             "goles_en_contra": int(resultado["home_score"])}
        
        return estadistica_uno, estadistica_dos
             
    equipos = lt.newList("ARRAY_LIST")
    posicion_equipos = {}
    
    for resultado in lt.iterator(data_structs["results"]):
        
        fecha = resultado["date"].split("-")

        if resultado["tournament"] == torneo and revisar_intervalo(fecha[2], fecha[1], fecha[0], dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final):
           
            estadistica_uno, estadistica_dos = crear_estadistica(resultado, data_structs)
            
            if resultado["home_team"] not in posicion_equipos:
                posicion_equipos[resultado["home_team"]] = lt.size(equipos) + 1
                lt.addLast(equipos, estadistica_uno)
                
            else:
                posicion = posicion_equipos[resultado["home_team"]]
                equipo = lt.getElement(equipos, posicion)
                
                equipo["puntos"] += estadistica_uno["puntos"]
                equipo["diferencia_goles"] += estadistica_uno["diferencia_goles"]
                equipo["partidos_jugados"] += estadistica_uno["partidos_jugados"]
                equipo["goles_penal"] += estadistica_uno["goles_penal"]
                equipo["autogoles"] += estadistica_uno["autogoles"]
                equipo["victorias"] += estadistica_uno["victorias"]
                equipo["empates"] += estadistica_uno["empates"]
                equipo["derrotas"] += estadistica_uno["derrotas"]
                equipo["goles_favor"] += estadistica_uno["goles_favor"]
                equipo["goles_en_contra"] += estadistica_uno["goles_en_contra"]

                    
                lt.changeInfo(equipos, posicion, equipo)
            
            if resultado["away_team"] not in posicion_equipos:
                posicion_equipos[resultado["away_team"]] = lt.size(equipos) + 1
                lt.addLast(equipos, estadistica_dos)
            
            else:
                posicion = posicion_equipos[resultado["away_team"]]
                equipo = lt.getElement(equipos, posicion)
                
                equipo["puntos"] += estadistica_dos["puntos"]
                equipo["diferencia_goles"] += estadistica_dos["diferencia_goles"]
                equipo["partidos_jugados"] += estadistica_dos["partidos_jugados"]
                equipo["goles_penal"] += estadistica_dos["goles_penal"]
                equipo["autogoles"] += estadistica_dos["autogoles"]
                equipo["victorias"] += estadistica_dos["victorias"]
                equipo["empates"] += estadistica_dos["empates"]
                equipo["derrotas"] += estadistica_dos["derrotas"]
                equipo["goles_favor"] += estadistica_dos["goles_favor"]
                equipo["goles_en_contra"] += estadistica_dos["goles_en_contra"]
                

                    
                lt.changeInfo(equipos, posicion, equipo)
                    
    sa.sort(equipos, sort_criteria_estadisticas)               

    
    return equipos, posicion_equipos
    
                
                    


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
        
        

