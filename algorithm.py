#*************************************************************************************************************************************
#This file contains Class graph for defining the spanning tree data structure and functions for determining minimum spanning tree(MST)
#using Kruskal's and Prim's algorithm.
#Author: Sarvesh Rembhotkar
#UTA ID: 1001966297
#Date: 11th April 2022
#The time complexity Of Kruskal's Algorithm is: O(E log V) where V = number of vertices in a graph
#The time complexity of Prim's algorithm is O(V^2) where V = number of vertices in a graph
#*************************************************************************************************************************************

import time
from datetime import datetime
import json

#*************************************************************************************************************************************
#This class is for defining a weighted Graph. It accepts no. of vertices and has function for adding an edge with a weight, a function
# for printing the Graph on console and for returning it to the calling function, a function for identifying MST using Kruskal's 
# algorithm and a function for identifying MST using Prim's algorithm.
#Autohor: Sarvesh Rembhotkar
#Date: 11th April 2022
#*************************************************************************************************************************************

class Graph:
    #Constructor for initiating the Graph instance with required no. of vertices. It also  accpets a parameter called type to
    #indicate the algorithm K for Kruskal and P for Prim
    def __init__(self, vertices, type):
        self.V = vertices
        self.type = type
        if type == "K":
            self.graph = []
        else:
            self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)]
    #add the start point, end point and a weight for the edge
    def add_edge(self, u, v, w):
        if self.type == "K":
            self.graph.append([u, v, w])
        else:
            self.graph[u][v]=w
            self.graph[v][u]=w

    # Search function
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    #print the graph on the screen
    def print_graph(self):
        print("The input graph is :")
        for u, v, w in self.graph:
            print("%d - %d: %d" % (u, v, w))

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Function for Applying Kruskal's algorithm. It returns the MST as a  list
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        print("The output of Kruskal's algorithm is :")
        output = []
        for u, v, weight in result:
            output.append(str(u) + " : " + str(v) + " - " + str(weight))
            print("%d - %d: %d" % (u, v, weight))
        return output

    # Function for Applying Prim's algorithm. It returns the MST as a  list
    def prims_algo(self):
        # Defining a really big number, that'll always be the highest weight in comparisons
        postitive_inf = float('inf')

        # This is a list showing which nodes are already selected 
        # so we don't pick the same node twice and we can actually know when stop looking
        selected_nodes = [False for node in range(self.V)]

        # Matrix of the resulting MST
        result = [[0 for column in range(self.V)] 
                for row in range(self.V)]
    
        indx = 0
    
        # While there are nodes that are not included in the MST, keep looking:
        while(False in selected_nodes):
            # We use the big number we created before as the possible minimum weight
            minimum = postitive_inf

            # The starting node
            start = 0

            # The ending node
            end = 0

            for i in range(self.V):
            # If the node is part of the MST, look its relationships
                if selected_nodes[i]:
                    for j in range(self.V):
                        # If the analyzed node have a path to the ending node AND its not included in the MST (to avoid cycles)
                        if (not selected_nodes[j] and self.graph[i][j]>0):  
                            # If the weight path analyzed is less than the minimum of the MST
                            if self.graph[i][j] < minimum:
                            # Defines the new minimum weight, the starting vertex and the ending vertex
                                minimum = self.graph[i][j]
                                start, end = i, j
        
            # Since we added the ending vertex to the MST, it's already selected:
            selected_nodes[end] = True

            # Filling the MST Adjacency Matrix fields:
            result[start][end] = minimum
        
            if minimum == postitive_inf:
                result[start][end] = 0

            indx += 1
        
            result[end][start] = result[start][end]

        # Print the resulting MST
        # for node1, node2, weight in result:
        output = []
        print("The MST of Prims algorithm is :")
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    output.append(str(i) + " : " + str(j) + " - " + str(result[i][j]))
                    print("%d - %d: %d" % (i, j, result[i][j]))
        return output

#Function main for testing the algorithms
def main():
    start_time = time.time()
    now = datetime.now()
    graph = Graph(9,"K")
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 7)
    graph.add_edge(1, 2, 11)
    graph.add_edge(1, 3, 9)
    graph.add_edge(1, 5, 20)
    graph.add_edge(2, 5, 1)
    graph.add_edge(3, 6, 6)
    graph.add_edge(3, 4, 2)
    graph.add_edge(4, 6, 10)
    graph.add_edge(4, 8, 15)
    graph.add_edge(4, 7, 5)
    graph.add_edge(4, 5, 1)
    graph.add_edge(5, 7, 3)
    graph.add_edge(6, 8, 5)
    graph.add_edge(7, 8, 12)
    graph.print_graph()
    graph.kruskal_algo()
    end_time = time.time()
    later = datetime.now()
    print(f"The time taken for Kruskals MST is {end_time-start_time}")
    print(f"The time taken for Kruskals MST (in seconds) is {(later-now).total_seconds()}")

    start_time = time.time()
    now = datetime.now()
    graph1 = Graph(9,"P")
    graph1.add_edge(0, 1, 4)
    graph1.add_edge(0, 2, 7)
    graph1.add_edge(1, 2, 11)
    graph1.add_edge(1, 3, 9)
    graph1.add_edge(1, 5, 20)
    graph1.add_edge(2, 5, 1)
    graph1.add_edge(3, 6, 6)
    graph1.add_edge(3, 4, 2)
    graph1.add_edge(4, 6, 10)
    graph1.add_edge(4, 8, 15)
    graph1.add_edge(4, 7, 5)
    graph1.add_edge(4, 5, 1)
    graph1.add_edge(5, 7, 3)
    graph1.add_edge(6, 8, 5)
    graph1.add_edge(7, 8, 12)
    graph1.prims_algo()
    end_time = time.time()
    later=datetime.now()
    print(f"The time taken for Prims MST is {end_time-start_time}")
    print(f"The time taken for Prims MST (in seconds) is {(later-now).total_seconds()}")

if __name__ == "__main__":
    main()