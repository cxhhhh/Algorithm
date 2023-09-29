"""
FIT2004 Assignment 2
Student Name: Chen Xin Hui
Student ID: 32695918
"""
import math

"""
Q1: Fast Backups
"""


class Vertex:
    def __init__(self, vertex_id):
        """
        Function description: To initialize the attributes of a vertex

        Input:
            self: the instance of Vertex
            vertex_id: the unique id of vertex
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)
        """
        # For edges
        self.vertex_id = vertex_id
        self.edges = []

        # For traversal
        self.discovered = False
        self.visited = False

        # For backtracking
        self.previous = None

        # For problem
        self.min_residual = math.inf

    def append_edge(self, edge):
        """
        Function description: To append edges to the list of edges for this vertex

        Input:
            self: the instance of Vertex
            edge: a tuple contains four integers (a, b, t),
                  which a is starting vertex, b is ending vertex,
                  c is a positive integer representing the maximum throughput of that channel
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)
        """
        self.edges.append(edge)

    def __str__(self) -> str:
        """
        Function description: To print the vertex and edges

        Input:
            self: the instance of Vertex
        Return:
            output: the list of vertex with edges

        Time complexity:
            Best: O(1)
            Worst: O(E), E is the number of edges
        Space complexity:
            Input: O(1)
            Aux: O(1)
        """
        output = "Vertex " + str(self.vertex_id) + " with edges: "
        for edge in self.edges:
            output += "(" + str(edge) + ") "
        return output


class Edge:
    def __init__(self, a, b, t) -> None:
        """
        Function description: To initialize the attributes of an edge

        Input:
            self: the instance of Edge
            a: the starting vertex of an edge
            b: the ending vertex of an edge
            t: the maximum throughput of that channel
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)
        """
        self.a = a
        self.b = b
        self.t = t
        # The original edge
        self.original = None
        # The reverse edge of the original edge which is reverse direction
        self.reverse = None

    def __str__(self):
        """
        Function description: To print the edges

        Input:
            self: the instance of Edge
        Return:
            output: edges with starting vertex, ending vertex, throughput

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)
        """
        output = str(self.a) + " " + str(self.b) + " " + str(self.t)
        return output


class ResidualNetwork:
    def __init__(self, connections, maxIn, maxOut, origin, targets):
        """
        Function description: To create a residual network graph,
                              add vertices and edges and connect them according to connections

        Approach description: In my approach, the graph of ResidualNetwork class is the residual network graph
                              since this question do not have flow but only have capacity,
                              so I can directly make the residual network graph

        Precondition: Valid input, connections with the format [(a, b, t)], maxIn and maxOut for all vertices,
                      original is an integer, targets is a list of integer
        Postcondition: Create a residual network graph

        Input:
            self: the instance of ResidualNetwork
            connections: a list of tuples(a,b,t) of the direct communication channels between the data centres
            maxIn: a list which the maximum amount of incoming data that each data centre can process per second
            maxOut: a list which the maximum amount of outgoing data that each data centre can process per second
            origin: the start data centre
            targets: the target data centres
        Return:
            None

        Time complexity:
            Best: O(D + C), D is the numbers of data centres; C is the numbers of communication channels
            Worst: O(D + C), D is the numbers of data centres; C is the numbers of communication channels
        Space complexity:
            Input: O(D + C), D is the numbers of data centres; C is the numbers of communication channels
            Aux: O(D + C), D is the numbers of data centres; C is the numbers of communication channels
        """
        # Find the numbers of vertex
        vertex_num = -1
        for a, b, t in connections:
            temp = max(a, b)
            vertex_num = max(vertex_num, temp)

        # Initialize the array to store the vertices, Duplicate the vertices and add one more vertex for targets
        self.vertex_arr = [None] * (2*(vertex_num + 1)+1)

        # Initialise a sink for targets
        self.vertex_arr[len(self.vertex_arr) - 1] = Vertex(len(self.vertex_arr) - 1)

        # Add vertices
        for i in range(len(connections)):
            self.vertex_arr[connections[i][0]] = Vertex(connections[i][0])
            self.vertex_arr[connections[i][1]] = Vertex(connections[i][1])
            # For duplicate node
            self.vertex_arr[connections[i][0] + (vertex_num + 1)] = Vertex(connections[i][0] + (vertex_num + 1))
            self.vertex_arr[connections[i][1] + (vertex_num + 1)] = Vertex(connections[i][1] + (vertex_num + 1))

        # Add edges
        self.add_edges(connections, maxIn, maxOut, origin, targets)

    def __str__(self):
        """
        Function description: To print the vertex

        Input:
            self: the instance of ResidualNetwork
        Return:
            output: edges with starting vertex, ending vertex, throughput

        Time complexity:
            Best: O(L), L is the length of vertex_arr
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)
        """
        return_string = ""
        for vertex in self.vertex_arr:
            return_string = return_string + str(vertex) + "\n"
        return return_string

    def add_edges(self, connections, maxIn, maxOut, origin, targets):
        """
        Function description: To add the edges for the graph with throughput

        Precondition: Valid input, connections with the format [(a, b, t)], maxIn and maxOut for all vertices,
                      original is an integer, targets is a list of integer
        Postcondition: The edges have been added in the graph

        Input:
            self: the instance of ResidualNetwork
            connections: a list of tuples(a,b,t) of the direct communication channels between the data centres
            maxIn: a list which the maximum amount of incoming data that each data centre can process per second
            maxOut: a list which the maximum amount of outgoing data that each data centre can process per second
            origin: the start data centre
            targets: the target data centres
        Return:
            None

        Time complexity:
            Best: O(D + C), D is the numbers of data centres; C is the numbers of communication channels
            Worst: O(D + C), D is the numbers of data centres; C is the numbers of communication channels
        Space complexity:
            Input: O(D + C), D is the numbers of data centres; C is the numbers of communication channels
            Aux: O(1)
        """
        # Find the numbers of vertex
        vertex_num = -1
        for a, b, t in connections:
            temp = max(a, b)
            vertex_num = max(vertex_num, temp)

        # Add a edge from a node to its duplicate node
        for i in range(vertex_num + 1):
            # To make sure the capacity is maxOut for source
            if i == origin:
                current_edge = Edge(origin, origin + vertex_num + 1, maxOut[origin])
            # To make sure the capacity is maxIn for duplicate node of targets
            elif i in targets:
                current_edge = Edge(i, i + vertex_num + 1, maxIn[i])
            else:
                current_edge = Edge(i, i + vertex_num + 1, min(maxIn[i], maxOut[i]))

            # Flip the a and b, this is reverse edge
            reverse_edge = Edge(i + vertex_num + 1, i, 0)

            # Update the original and reverse for current edge
            current_edge.original = current_edge
            current_edge.reverse = reverse_edge
            # Find the current vertex and the current reverse vertex
            current_vertex = self.vertex_arr[i]
            reverse_vertex = self.vertex_arr[i + vertex_num + 1]
            # Add the edge of current vertex and the current reverse vertex
            current_vertex.append_edge(current_edge)
            reverse_vertex.append_edge(reverse_edge)

        # Add edge from a duplicate node to the next node which need to add (vertex_num + 1)
        for i in range(len(connections)):
            current_edge = Edge(connections[i][0] + vertex_num + 1,
                                connections[i][1],
                                connections[i][2])
            reverse_edge = Edge(connections[i][1],
                                connections[i][0] + vertex_num + 1,
                                0)

            # Update the original and reverse for current edge
            current_edge.original = current_edge
            current_edge.reverse = reverse_edge
            # Find the current vertex and the current reverse vertex
            current_vertex = self.vertex_arr[connections[i][0] + vertex_num + 1]
            reverse_vertex = self.vertex_arr[connections[i][1]]
            # Add the edge of current vertex and the current reverse vertex
            current_vertex.append_edge(current_edge)
            reverse_vertex.append_edge(reverse_edge)

        # Add the edges of duplicate nodes of targets to the sink
        for i in targets:
            current_edge = Edge(i + vertex_num + 1, len(self.vertex_arr) - 1, maxIn[i])
            reverse_edge = Edge(len(self.vertex_arr) - 1, i + vertex_num + 1, 0)

            # Update the original and reverse for current edge
            current_edge.original = current_edge
            current_edge.reverse = reverse_edge
            # Find the current vertex and the current reverse vertex
            current_vertex = self.vertex_arr[i + vertex_num + 1]
            reverse_vertex = self.vertex_arr[len(self.vertex_arr) - 1]
            # Add the edge of current vertex and the current reverse vertex
            current_vertex.append_edge(current_edge)
            reverse_vertex.append_edge(reverse_edge)

    def bfs(self, source, sink):
        """
        Function description: BFS Function

        Input:
            self: the instance of ResidualNetwork
            source: source which is the starting vertex
            sink: sink which is the ending vertex
        Return:
            boolean argument

        Time complexity:
            Best: O(1)
            Worst: O(D + C), D is the numbers of data centres; C is the numbers of communication channels
        Space complexity:
            Input: O(1)
            Aux: O(D), D is the numbers of data centres
        """
        # Resetting all vertices
        for v in self.vertex_arr:
            v.discovered = False
            v.previous = None
            v.min_residual = math.inf

        return_bfs = []
        discovered = []
        discovered.append(source)

        # Go through the graph
        while len(discovered) > 0:
            u = discovered.pop(0)
            u.visited = True
            return_bfs.append(u)

            # When reach sink
            if u.vertex_id == sink.vertex_id:
                return True

            # Go through the edges of vertex u
            for edge in u.edges:
                v = self.vertex_arr[edge.b]

                # Connect if next vertex is not discovered and t is not 0
                if v.discovered is False and edge.t != 0:
                    discovered.append(v)
                    v.discovered = True
                    v.previous = edge
                    # Finding the min_residual of the current edge
                    v.min_residual = min(edge.t, u.min_residual)
        return False


def maxThroughput(connections, maxIn, maxOut, origin, targets):
    """
    Function description: Ford Fulkerson Function to find the maximum throughput

    Approach description: Executing Ford Fulkerson Method on the residual network graph,
                          Loop BFS and find the path (start from the sink to backtrack)
                          and then update the throughput (minus or plus min_residual);
                          Until there is no path in graph,
                          then the maximum throughput is the total of throughput of vertex sink

    Precondition: Valid input, connections with the format [(a, b, t)], maxIn and maxOut for all vertices,
                  original is an integer, targets is a list of integer (Same arguments with constructor)
    Postcondition: The maximum possible data throughput from data centre origin to
                   the data centre specified in targets has been found

    Input:
        connections: a list of tuples(a,b,t) of the direct communication channels between the data centres
        maxIn: a list which the maximum amount of incoming data that each data centre can process per second
        maxOut: a list which the maximum amount of outgoing data that each data centre can process per second
        origin: the start data centre
        targets: the target data centres
    Return:
        max_throughput: The maximum possible data throughput from data centre origin to the data centre specified in targets

    Time complexity:
        Best: O(D + C), D is the numbers of data centres; C is the numbers of communication channels
        Worst: O(D * C^2), D is the numbers of data centres; C is the numbers of communication channels
    Space complexity:
        Input: O(D + C), D is the numbers of data centres; C is the numbers of communication channels
        Aux: O(1)
    """
    # Residual network Graph
    residual_network = ResidualNetwork(connections, maxIn, maxOut, origin, targets)

    # source which is the start vertex
    source = residual_network.vertex_arr[origin]
    # sink which is the end vertex
    sink = residual_network.vertex_arr[-1]

    # While loop if graph still has path
    while residual_network.bfs(source, sink):
        # current is sink which is the end vertex
        current = residual_network.vertex_arr[-1]
        min_residual = current.min_residual

        # Augmenting residual
        while current.vertex_id != source.vertex_id:
            # Get the previous edge and the reverse edge
            prev_edge = current.previous
            reverse_edge = prev_edge.reverse

            # Update the throughput
            prev_edge.t -= min_residual
            reverse_edge.t += min_residual

            # Update current which is the previous vertex
            current = residual_network.vertex_arr[current.previous.a]

        # Calculate the maximum throughput
        max_throughput = 0
        for edge in residual_network.vertex_arr[-1].edges:
            max_throughput += edge.t

    return max_throughput
