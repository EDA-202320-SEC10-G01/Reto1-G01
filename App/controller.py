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
        elif archivo == "2":
            control["model"]["goalscorers"] = model.lt.newList("ARRAY_LIST")
            load_goalscorers(control["model"], tamaños[tamaño])
        elif archivo == "3":
            control["model"]["shootouts"] = model.lt.newList("ARRAY_LIST")
            load_shootouts(control["model"], tamaños[tamaño])
        elif archivo == "4":
            control["model"]["results"] = model.lt.newList("ARRAY_LIST")
            control["model"]["goalscorers"] = model.lt.newList("ARRAY_LIST")
            control["model"]["shootouts"] = model.lt.newList("ARRAY_LIST")
            load_results(control["model"], tamaños[tamaño])
            load_goalscorers(control["model"], tamaños[tamaño])
            load_shootouts(control["model"], tamaños[tamaño])
    
    

# Funciones de ordenamiento

def sort(control, sort_algorithm, datos):
    model.sort(control["model"], sort_algorithm, datos)
    
# Funciones de consulta sobre el catálogo

def get_datasize(control):
    return model.data_size(control["model"])


def req_1(control, n_partidos, equipo, condicion):
    
    return model.req_1(control["model"], n_partidos, equipo, condicion)


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
