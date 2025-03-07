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
 """

import config as cf
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    control = {"model": None}
    control["model"] = model.new_data_structs()
    
    return control

# Funciones para la carga de datos



def load_results(football_data, tamaño):
    
    resultsfile = cf.data_dir + f'/football/results-utf8-{tamaño}.csv'
    input_file = csv.DictReader(open(resultsfile, encoding="utf-8"))
    for result in input_file:
        model.add_result(football_data, result)
        
def load_goalscorers(football_data, tamaño):
    
    goalscorersfile = cf.data_dir + f'/football/goalscorers-utf8-{tamaño}.csv'
    input_file = csv.DictReader(open(goalscorersfile, encoding="utf-8"))
    for goalscorer in input_file:
        model.add_goalscorer(football_data, goalscorer)
    
def load_shootouts(football_data, tamaño):
    
    shootoutsfile = cf.data_dir + f'/football/shootouts-utf8-{tamaño}.csv'
    input_file = csv.DictReader(open(shootoutsfile, encoding="utf-8"))
    for shootout in input_file:
        model.add_shootout(football_data, shootout)
        
          
        
def load_data(control, archivo, tamaño):
    
    archivos = ["1", "2", "3", "4"]
    tamaños = {"1": "small",
               "2": "5pct",
               "3": "10pct",
               "4": "20pct",
               "5": "30pct",
               "6": "50pct",
               "7": "80pct",
               "8": "large"}

    
    if archivo not in archivos or tamaño not in list(tamaños.keys()):
        print("El archivo indicado o el tamaño de la muestra no son válidos")
    else:
        if archivo == "1":
            control["model"]["results"] = model.lt.newList("ARRAY_LIST")
            load_results(control["model"], tamaños[tamaño])
            model.create_access_results(control["model"])
        elif archivo == "2":
            control["model"]["goalscorers"] = model.lt.newList("ARRAY_LIST")
            load_goalscorers(control["model"], tamaños[tamaño])
            model.create_access_goalscorers(control["model"])
        elif archivo == "3":
            control["model"]["shootouts"] = model.lt.newList("ARRAY_LIST")
            load_shootouts(control["model"], tamaños[tamaño])
            model.create_access_shootouts(control["model"])
        elif archivo == "4":
            control["model"]["results"] = model.lt.newList("ARRAY_LIST")
            control["model"]["goalscorers"] = model.lt.newList("ARRAY_LIST")
            control["model"]["shootouts"] = model.lt.newList("ARRAY_LIST")
            load_results(control["model"], tamaños[tamaño])
            load_goalscorers(control["model"], tamaños[tamaño])
            load_shootouts(control["model"], tamaños[tamaño])
            model.create_access_results(control["model"])
            model.create_access_goalscorers(control["model"])
            model.create_access_shootouts(control["model"])
            
            
    
    

# Funciones de ordenamiento

def sort(control, sort_algorithm, datos):
    start_time = get_time()
    model.sort(control["model"], sort_algorithm, datos)
    end_time = get_time()
    delta_time = end_time - start_time
    print(f"Tiempo de ejecución del algoritmo de ordenamiento escogido sobre los datos indicados: {delta_time} ms")
    
# Funciones de consulta sobre el catálogo

def get_datasize(control):
    return model.data_size(control["model"])

def tipo_dato_abstracto(control, tipo):
    
    if tipo == "1":
        control["model"]["results"]["datastructure"] = "ARRAY_LIST"
        control["model"]["goalscorers"]["datastructure"] = "ARRAY_LIST"
        control["model"]["shootouts"]["datastructure"] = "ARRAY_LIST"
        print("Se ha cambiado el tipo de dato abstracto a ARRAY_LIST")
    elif tipo == "2":
        control["model"]["results"]["datastructure"] = "LINKED_LIST"
        control["model"]["goalscorers"]["datastructure"] = "LINKED_LIST"
        control["model"]["shootouts"]["datastructure"] = "LINKED_LIST"
        print("Se ha cambiado el tipo de dato abstracto a LINKED_LIST")
    else:
        print("Opcion no valida")
    

def req_1(control, n_partidos, equipo, condicion):
    
    start_time = get_time()
    partidos_por_equipo, partidos_encontrados = model.req_1(control["model"], n_partidos, equipo, condicion)
    end_time = get_time()
    delta_time = end_time - start_time
    return partidos_por_equipo, partidos_encontrados, delta_time

def req_2(control, n_goles, jugador):
    
    start_time = get_time()
    goles_a_mostrar, goles_encontrados = model.req_2(control["model"], n_goles, jugador)
    end_time = get_time()
    delta_time = end_time - start_time
    
    return goles_a_mostrar, goles_encontrados, delta_time

def req_3(control, equipo, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final):
    
    start_time = get_time()
    partidos_por_equipo = model.req_3(control["model"], equipo, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final)
    end_time = get_time()
    delta_time = end_time - start_time
    
    return partidos_por_equipo, delta_time

def req_4(control, torneo, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final):
    
    start_time = get_time()
    partidos_por_torneo, paises, ciudades = model.req_4(control["model"], torneo, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final)
    end_time = get_time()
    delta_time = end_time - start_time
    
    return partidos_por_torneo, paises, ciudades, delta_time
def req_5(control, anotador, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final):
    
    start_time = get_time()
    goles, n_torneos, n_autogoles, n_penales = model.req_5(control["model"], anotador, año_inicial, mes_inicial, dia_inicial, año_final, mes_final, dia_final)
    end_time = get_time()
    delta_time = end_time - start_time
    
    return goles, n_torneos, n_autogoles, n_penales, delta_time
    
    
def req_6(control, n_equipos, torneo, dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final):
    
    return model.req_6(control["model"], n_equipos, torneo, dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final)

# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el  instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
