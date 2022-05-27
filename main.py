#*************************************************************************************************************************************
#This file contains function for running MST algorithms and return the ouput in the form of json object
#It uses python eel package for creating the HTML based UI and exposes the function run_MST_algo() so that it can be called 
#from JavaScript.
#Author: Sarvesh Rembhotkar
#UTA ID: 1001966297
#Date: 11th April 2022
#*************************************************************************************************************************************

import eel
import algorithm
import json
from datetime import datetime


#MST is the name of the project and all the files are created in this project
eel.init("MST")

#Expose the Kruskal alogorithm function to Javascript
@eel.expose

#Function for getting the input JSON shared by JS calling function, reading the parameters from JSON, calling the 
#algorthms and sending the output to the calling JS function in the form of JSON
def run_MST_algo(input_json, lst_edge):
    
    data = json.loads(input_json)
 
    num_nodes = int(data["numnodes"])
    k_algo = data["k_algo"]
    p_algo = data["p_algo"]
    
    #print(lst_edge)
    kruskal_output = []
    kruskal_start = 0
    kruskal_end = 0
    prims_output = []
    prims_start = 0
    prims_end = 0
    k_run_time = 0
    p_run_time = 0
    rt_diff = 0

    if k_algo == "Y":
        kruskal_start = datetime.now()
        graph = algorithm.Graph(num_nodes,"K")
        for edge in lst_edge:
            print(edge)
            #print(type(edge))
            if edge != "":
                arr_edge = edge.split(",")
                graph.add_edge(int(arr_edge[0]), int(arr_edge[1]), int(arr_edge[2]))
        graph.print_graph()
        kruskal_output = graph.kruskal_algo()
        kruskal_end = datetime.now()
        k_run_time = (kruskal_end-kruskal_start).total_seconds()
    if p_algo == "Y":
        prims_start = datetime.now()
        graph = algorithm.Graph(num_nodes,"P")
        for edge in lst_edge:
            print(edge)
            #print(type(edge))
            if edge != "":
                arr_edge = edge.split(",")
                graph.add_edge(int(arr_edge[0]), int(arr_edge[1]), int(arr_edge[2]))
        prims_output = graph.prims_algo()
        prims_end = datetime.now()
        p_run_time = (prims_end - prims_start).total_seconds()
    #create json for Kruskal's MST, Prim's MST, Kruskal algo run time, Prim's algo run time and the run time difference
    if (k_run_time!=0 and p_run_time!=0):
        rt_diff = f"{k_run_time - p_run_time: .4f}"
    #create dictionary object for values to be returned to the calling JavaScript function
    dict = {
        "K_MST" : kruskal_output,
        "K_runtime" : k_run_time,
        "P_MST" : prims_output,
        "P_runtime" : p_run_time,
        "rt_diff" : rt_diff
    }
    #Convery dictionary into JSON object
    json_obj = json.dumps(dict, indent = 4)
    
    print(f"The time taken for Kruskals MST (in seconds) is {k_run_time}")
    print(f"The time taken for Prims MST (in seconds) is {p_run_time}")
    #return (later-now).total_seconds()
    return json_obj

#start the html file
eel.start("index.html")