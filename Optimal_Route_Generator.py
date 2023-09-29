"""
FIT2004 Assignment 1
Student Name: Chen Xin Hui
Student ID: 32695918
"""

from queue import Queue
import math

"""
Q1: Should I give a ride?
"""


class MinHeap:
    MIN_CAPACITY = 1

    def __init__(self, max_size) -> None:
        """
        Function description: To initialize an instance of MinHeap
                              Set length is 0, create heap array and index array of MinHeap

        Input:
            self: the instance of MinHeap
            max_size: a greatest number of nodes of MinHeap
        Return:
            None

        Time complexity:
            Best: O(N), N is the value of max_size
            Worst: O(N), N is the value of max_size
        Space complexity:
            Input: O(1)
            Aux: O(N), N is the value of max_size

        Reference: Referred to the FIT2004 Tutorial 6 video and FIT1008 Week12
        """
        self.length = 0
        size = max(self.MIN_CAPACITY, max_size) + 1
        self.minHeap = [None] * size
        self.index_arr = [None] * (size - 1)

    def __len__(self) -> int:
        """
        Function description: To return the total length of the MinHeap

        Input:
            self: the instance of MinHeap
        Return:
            self.length: the total length of MinHeap

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 6 video and FIT1008 Week12
        """
        return self.length

    def is_full(self) -> bool:
        """
        Function description: To check if this minHeap is full or not

        Input:
            self: the instance of MinHeap
        Return:
            True if the MinHeap array is full, else False

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 6 video and FIT1008 Week12
        """
        return self.length + 1 == len(self.minHeap)

    def rise(self, node) -> None:
        """
        Function description: To rise the node to the correct position;
                              if the value is smaller, then this element will rise

        Input:
            self: the instance of MinHeap
            node: an element in array
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(log N), N is the number of elements of MinHeap
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 6 video and FIT1008 Week12
        """
        # Get the index of node
        node_index = self.index_arr[node.vertex_id]
        # Time compare
        while node_index > 1 and self.get_time(node) < self.get_time(self.minHeap[node_index // 2]):
            # Swap the element
            self.swap(node_index, node_index // 2)
            # Update the index
            node_index = node_index // 2

    def swap(self, node1_index, node2_index) -> None:
        """
        Function description: To swap two nodes in the minHeap

        Input:
            self: the instance of MinHeap
            node1_index: the index of node 1
            node2_index: the index of node 2
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 6 video and FIT1008 Week12
        """
        node1 = self.minHeap[node1_index].vertex_id
        node2 = self.minHeap[node2_index].vertex_id
        self.index_arr[node1], self.index_arr[node2] = node2_index, node1_index
        self.minHeap[node1_index], self.minHeap[node2_index] = self.minHeap[node2_index], self.minHeap[node1_index]

    def serve(self) -> int:
        """
        Function description: To serve the minimum element in the minHeap and return it

        Input:
            self: the instance of MinHeap
        Return:
            min_element: the minimum element in the minHeap

        Time complexity:
            Best: O(1)
            Worst: O(log N), N is the number of elements of MinHeap
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 6 video and FIT1008 Week12
        """
        # Get the minimum element
        min_element = self.minHeap[1]
        # Swap the root and the last
        self.swap(1, self.length)
        # Update the length
        self.length -= 1
        # Sink, make sure the position is correct
        if self.length > 0:
            self.sink(self.minHeap[1])
        return min_element

    def sink(self, node) -> None:
        """
        Function description: To sink the node to the correct position;
                              if the value is bigger, then this element will sink

        Input:
            self: the instance of MinHeap
            node: an element in array
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(log N), N is the number of elements of MinHeap
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 6 video and FIT1008 Week12
        """
        # Get the index of node
        node_index = self.index_arr[node.vertex_id]
        while node_index * 2 <= self.length:
            # Get the left or right node which is smaller
            child_index = self.smaller_child_index(node)
            # Time compare
            if self.get_time(node) <= self.get_time(self.minHeap[child_index]):
                break
            # Swap the element
            self.swap(child_index, node_index)
            # Update the index
            node_index = child_index

    def smaller_child_index(self, node) -> int:
        """
        Function description: To find the smaller node, the smaller node will be left child or the right child

        Input:
            self: the instance of MinHeap
            node: an element in array
        Return:
            the index of smaller child

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 6 video and FIT1008 Week12
        """
        # Get the index of node
        node_index = self.index_arr[node.vertex_id]
        # Time compare
        if node_index * 2 == self.length or self.get_time(self.minHeap[node_index * 2]) < self.get_time(
                self.minHeap[node_index * 2 + 1]):
            # If left child is smaller, return the index of left child
            return node_index * 2
        else:
            # If right child is smaller, return the index of right child
            return node_index * 2 + 1

    def add(self, node) -> None:
        """
        Function description: To add a new element into the minHeap, and make sure the element at the correct position

        Input:
            self: the instance of MinHeap
            node: a node which want to add into the minHeap
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(log N), N is the number of elements of MinHeap
        Space complexity:
            Input: O(1)
            Aux: O(log N), N is the number of elements of MinHeap

        Reference: Referred to the FIT2004 Tutorial 6 video and FIT1008 Week12
        """
        if self.is_full():
            raise IndexError
        # Update the length
        self.length += 1
        # Update the node in the minHeap
        self.minHeap[self.length] = node
        # Update the index of node
        self.index_arr[node.vertex_id] = self.length
        # Rise, make sure the position is correct
        self.rise(node)

    def get_time(self, node) -> int:
        """
        Function description: To return the time of s node

        Input:
            self: the instance of MinHeap
            node: an element in array
        Return:
            node.time: the time of s node

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 6 video and FIT1008 Week12
        """
        return node.time


class Vertex:
    def __init__(self, vertex_id):
        """
        Function description: To initialize the attributes of a vertex

        Input:
            self: the instance of MinHeap
            vertex_id: the unique id of vertex
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 5 video
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
        self.time = math.inf
        self.isPassenger = False

    def add_edges(self, edge):
        """
        Function description: To add edges to the list of edges for this vertex

        Input:
            self: the instance of MinHeap
            edge: a tuple contains four integers (a, b, c and d),
                  which a is starting vertex, b is ending vertex,
                  c is spending time when alone in that edge, d is spending time when pickup in that edge
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 5 video
        """
        self.edges.append(edge)

    def __str__(self) -> str:
        """
        Function description: To print the vertex and edges

        Input:
            self: the instance of MinHeap
        Return:
            output: the list of vertex with edges

        Time complexity:
            Best: O(1)
            Worst: O(E), E is the number of edges
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 5 video
        """
        output = "Vertex " + str(self.vertex_id) + " with edges: "
        for edge in self.edges:
            output += "(" + str(edge) + ") "
        return output


class Edge:
    def __init__(self, a, b, c, d):
        """
        Function description: To initialize the attributes of an edge

        Input:
            self: the instance of MinHeap
            a: the starting vertex of an edge
            b: the ending vertex of an edge
            c: spending time when alone of an edge
            d: spending time when pickup of an edge
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 5 video
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        """
        Function description: To print the edges

        Input:
            self: the instance of MinHeap
        Return:
            output: edges with starting vertex, ending vertex, time alone and time pickup

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)

        Reference: Referred to the FIT2004 Tutorial 5 video
        """
        output = str(self.a) + " " + str(self.b) + " " + str(self.c) + " " + str(self.d)
        return output


class ReverseGraph:
    def __init__(self, roads: list[tuple[int, int, int, int]], passengers: list):
        """
        Function description: To create a reverse graph which means the edges are from end to start

        Precondition: Valid input, roads with the format [(a, b, c, d)]
        Postcondition: Create the reverse graph which it is from end to start

        Input:
            self: an instance of ReverseGraph
            roads: list of roads which is the edges of graph (a, b, c, d), start, end, time_alone, time_pickup
            passengers: list of passengers of location
        Return:
            None

        Time complexity:
            Best: O(L), L is the length of reverse_roads
            Worst: O(L), L is the length of reverse_roads
        Space complexity:
            Input: O(L), L is the length of reverse_roads
            Aux: O(L), L is the length of reverse_roads

        Reference: Referred to the FIT2004 Workshop and assignment brief
        """
        # Reversing all edges
        reverse_roads = [(b, a, c, d) for a, b, c, d in roads]

        # Find the numbers of vertex
        vertex_num = -1
        for a, b, c, d in reverse_roads:
            temp = max(a, b)
            vertex_num = max(vertex_num, temp)

        # Initialize the array to store the vertices
        self.vertex_arr = [None] * (vertex_num + 1)
        self.vertexArr_len = vertex_num + 1

        # Add vertices
        for a, b, c, d in reverse_roads:
            vertex_a = Vertex(a)
            vertex_b = Vertex(b)
            self.vertex_arr[a] = vertex_a
            self.vertex_arr[b] = vertex_b

        for i in range(len(reverse_roads)):
            # Add the edge from end to start which is reverse
            reverse_edge = Edge(reverse_roads[i][0], reverse_roads[i][1], reverse_roads[i][2], reverse_roads[i][3])
            reverse_vertex = self.vertex_arr[reverse_roads[i][0]]
            reverse_vertex.add_edges(reverse_edge)

        # Check if the vertex is a passenger
        for passenger in passengers:
            self.vertex_arr[passenger].isPassenger = True

    def dijkstra(self, start: int) -> None:
        """
        Function description: To find the shortest time from start node to the other vertices in the ReverseGraph

        Precondition: Valid input, start is a non-negative integer
        Postcondition: Shortest time is found from start to the other vertices

        Input:
            self: an instance of ReverseGraph
            start: the starting location of the road
        Return:
            vertex_time: a list that store all the shortest time to this vertex
            vertex_previous: a list that store all the previous index to this vertex

        Time complexity:
                Best: O(E), E is the length of roads
                Worst: O(E log V), E is the length of roads, V is the length of vertex_arr
        Space complexity:
                Input: O(1)
                Aux: O(E + V), E is the length of roads, V is the length of vertex_arr

        Reference: Referred to the FIT2004 Workshop and assignment brief
        """

        def update(a, b):
            """
            Function description: To update the time, previous and the minHeap

            Input:
                a: start vertex of this edge
                b: end vertex of this edge
            Return:
                 None

            Time complexity:
                Best: O(1)
                Worst: O(1)
            Space complexity:
                Input: O(1)
                Aux: O(1)
            """
            b.time = new_time
            b.previous = a
            minheap_dijkstra.rise(b)

        # Set the initial value to start vertex
        start_node = self.vertex_arr[start]
        start_node.discovered = True
        start_node.previous = None
        start_node.time = 0

        # Create MinHeap with the number of edges
        minheap_dijkstra = MinHeap(len(self.vertex_arr))

        # Reset the vertex
        for vertex in self.vertex_arr:
            minheap_dijkstra.add(vertex)
            if vertex.vertex_id != start:
                vertex.discovered = False
                vertex.visited = False
                vertex.previous = None
                vertex.time = math.inf

        # Go through the graph
        while len(minheap_dijkstra) > 0:
            a = minheap_dijkstra.serve()

            # To check there is no routes from source to a
            if not a.discovered:
                continue

            a.visited = True

            # Go through all the edges of a
            for edge in a.edges:
                b = self.vertex_arr[edge.b]
                # This is reverse graph, so the time is time pickup
                new_time = a.time + edge.d
                # Set b to discovered if b is not discovered
                if not b.discovered:
                    b.discovered = True
                    update(a, b)
                # not visited means that it is not finalised, still can use
                elif not b.visited and b.time > new_time:
                    update(a, b)

        # Store all the shortest time for vertex
        vertex_time = []
        for i in range(self.vertexArr_len):
            vertex_time.append(self.vertex_arr[i].time)

        # Store all the previous vertex
        vertex_previous = []
        for i in range(self.vertexArr_len):
            vertex_previous.append(self.vertex_arr[i].previous)

        return vertex_time, vertex_previous

    def __str__(self):
        return_string = ""
        for vertex in self.vertex_arr:
            return_string = return_string + str(vertex) + "\n"
        return return_string


class Graph:

    def __init__(self, roads: list[tuple[int, int, int, int]], passengers: list):
        """
        Function description: To create a graph which means the edges are from start to end

        Precondition: Valid input, roads with the format [(a, b, c, d)]
        Postcondition: Create the graph which it is from start to end

        Input:
            self: an instance of Graph
            roads: list of roads which is the edges of graph (a, b, c, d), start, end, time_alone, time_pickup
            passengers: list of passengers of location
        Return:
            None

        Time complexity:
            Best: O(L), L is the length of roads
            Worst: O(L), L is the length of roads
        Space complexity:
            Input: O(L), L is the length of roads
            Aux: O(L), L is the length of roads

        Reference: Referred to the FIT2004 Workshop and assignment brief
        """
        # Find the numbers of vertex
        vertex_num = -1
        for a, b, c, d in roads:
            temp = max(a, b)
            vertex_num = max(vertex_num, temp)

        # Initialize the array to store the vertices
        self.vertex_arr = [None] * (vertex_num + 1)
        self.vertexArr_len = vertex_num + 1

        # Add vertices
        for a, b, c, d in roads:
            vertex_a = Vertex(a)
            vertex_b = Vertex(b)
            self.vertex_arr[a] = vertex_a
            self.vertex_arr[b] = vertex_b

        for i in range(len(roads)):
            # Add the edge from start to end
            current_edge = Edge(roads[i][0], roads[i][1], roads[i][2], roads[i][3])
            current_vertex = self.vertex_arr[roads[i][0]]
            current_vertex.add_edges(current_edge)

        # Check if the vertex is a passenger
        for passenger in passengers:
            self.vertex_arr[passenger].isPassenger = True

    def dijkstra(self, start: int) -> None:
        """
        Function description: To find the shortest time from start node to the other vertices in the Graph

        Precondition: Valid input, start is a non-negative integer
        Postcondition: Shortest time is found from start to the other vertices

        Input:
            self: an instance of Graph
            start: the starting location of the road
        Return:
            vertex_time: a list that store all the shortest time to this vertex
            vertex_previous: a list that store all the previous index to this vertex

        Time complexity:
                Best: O(E), E is the length of roads
                Worst: O(E log V), E is the length of roads, V is the length of vertex_arr
        Space complexity:
                Input: O(1)
                Aux: O(E + V), E is the length of roads, V is the length of vertex_arr

        Reference: Referred to the FIT2004 Workshop and assignment brief
        """

        def update(a, b):
            """
            Function description: To update the time, previous and the minHeap

            Input:
                a: start vertex of this edge
                b: end vertex of this edge
            Return:
                 None

            Time complexity:
                Best: O(1)
                Worst: O(1)
            Space complexity:
                Input: O(1)
                Aux: O(1)
            """
            b.time = new_time
            b.previous = a
            minheap_dijkstra.rise(b)

        # Set the initial value to start vertex
        start_node = self.vertex_arr[start]
        start_node.discovered = True
        start_node.previous = None
        start_node.time = 0

        # Create MinHeap with the number of edges
        minheap_dijkstra = MinHeap(len(self.vertex_arr))

        # Reset the vertex
        for vertex in self.vertex_arr:
            minheap_dijkstra.add(vertex)
            if vertex.vertex_id != start:
                vertex.discovered = False
                vertex.visited = False
                vertex.previous = None
                vertex.time = math.inf

        # Go through the graph
        while len(minheap_dijkstra) > 0:
            a = minheap_dijkstra.serve()

            # To check there is no routes from source to a
            if not a.discovered:
                continue

            a.visited = True
            # Go through all the edges of a
            for edge in a.edges:
                b = self.vertex_arr[edge.b]
                # This is graph, so the time is time alone
                new_time = a.time + edge.c
                # Set b to discovered if b is not discovered
                if not b.discovered:
                    b.discovered = True
                    update(a, b)
                # not visited means that it is not finalised, still can use
                elif not b.visited and b.time > new_time:
                    update(a, b)

        # Store all the shortest time for vertex
        vertex_time = []
        for i in range(self.vertexArr_len):
            vertex_time.append(self.vertex_arr[i].time)

        # Store all the previous vertex
        vertex_previous = []
        for i in range(self.vertexArr_len):
            vertex_previous.append(self.vertex_arr[i].previous)

        return vertex_time, vertex_previous


def optimalRoute(start, end, passengers, roads):
    """
    Function description: To get the optimal route to go from start location to end location with the minimum possible
                          total travel time

    Precondition: Valid input, start and end are in roads, roads with the format [(a, b, c, d)]
    Postcondition: the optimal route to go from start location to end location with the minimum possible
                   total travel time is returned

    Input:
        self: an instance of Graph
        start: the starting location of the road
        end: the ending location of the road
        passengers: a list of locations where there are potential passengers
        roads: a list of roads with the corresponding travel times
    Return:
        optimal_route: the optimal route as a list of integers

    Time complexity:
            Best: O(E log V), E is the length of roads, V is the length of vertex_arr
            Worst: O(E log V), E is the length of roads, V is the length of vertex_arr
    Space complexity:
            Input: O(1)
            Aux: O(E + V), E is the length of roads, V is the length of vertex_arr

    Reference: Referred to the FIT2004 Workshop and assignment brief
    """
    # Create a graph
    graph = Graph(roads, passengers)
    # Create a reverse graph
    reverse_graph = ReverseGraph(roads, passengers)

    # Find the shortest time alone from start to end by using dijkstra
    time_from_start, start_route = graph.dijkstra(start)
    # Find the shortest time pickup from end to start by using dijkstra
    time_from_end, end_route = reverse_graph.dijkstra(end)

    shortest_time_carpool = math.inf
    shortest_time_index = -1
    # Combine the time of graph and reverse graph
    for i in range(reverse_graph.vertexArr_len):
        # Add the time(alone) from start to passenger and the time(pickup) from end to passenger
        if time_from_start[i] + time_from_end[i] < shortest_time_carpool and reverse_graph.vertex_arr[i].isPassenger:
            shortest_time_carpool = time_from_start[i] + time_from_end[i]
            shortest_time_index = i
    # Get the shortest time when driving alone
    shortest_time_alone = time_from_start[-1]

    # Get the route by using previous
    def route(vert):
        if not vert:
            return []
        res = route(vert.previous)
        res.append(vert.vertex_id)
        return res
    # Backtracking to get the route from start to passenger
    optimal_route_alone = route(graph.vertex_arr[shortest_time_index])
    # Backtracking to get the route from end to passenger
    optimal_route_carpool = route(reverse_graph.vertex_arr[shortest_time_index])

    # Set default route is driving alone
    optimal_route = route(graph.vertex_arr[end])

    # If time_carpool is shorter than time_alone, change route to pick up the passenger
    if shortest_time_carpool < shortest_time_alone:
        # optimal_route_alone also has the passenger location, so need to delete one
        optimal_route_carpool.pop()
        # The order of optimal_route_carpool is from end to passenger, so need to reverse
        optimal_route_carpool.reverse()
        # Combine the route
        optimal_route = optimal_route_alone + optimal_route_carpool

    return optimal_route


# ---------------------------------------------------------------------------
# --------------------------------- Testing ---------------------------------
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    roads = [(0, 3, 5, 3), (3, 4, 35, 15), (3, 2, 2, 2), (4, 0, 15, 10), (2, 4, 30, 25), (2, 0, 2, 2), (0, 1, 10, 10), (1, 4, 30, 20)]
    passengers = [2,1]
print("Question 1:")
print(optimalRoute(0, 4, passengers, roads))


# The following testing are from ed
def test_different_shortest_paths():
    start = 2
    end = 5
    passengers = [3]
    roads = [
        (6, 2, 22, 6),
        (3, 6, 4, 3),
        (0, 7, 8, 3),
        (5, 0, 9, 6),
        (5, 4, 6, 5),
        (4, 3, 24, 2),
        (1, 2, 26, 23),
        (7, 4, 26, 8),
        (7, 3, 12, 5),
        (4, 5, 10, 3),
        (2, 0, 14, 1),
        (5, 7, 6, 6)
    ]
    res_1 = [2, 0, 7, 3, 6, 2, 0, 7, 4, 5]  # Both results should yield 58 mins
    res_2 = [2, 0, 7, 4, 5]
    my_res = optimalRoute(start, end, passengers, roads)
    return my_res == res_1 or my_res == res_2


def test_start_at_some_location():
    start = 6
    end = 7
    passengers = [4, 2, 9]
    roads = [
        (9, 0, 7, 4),
        (7, 4, 3, 1),
        (8, 7, 6, 1),
        (3, 5, 1, 1),
        (2, 9, 6, 4),
        (6, 4, 5, 4),
        (2, 4, 6, 2),
        (7, 3, 8, 7),
        (0, 9, 1, 1),
        (2, 3, 5, 5),
        (5, 3, 6, 6),
        (1, 9, 6, 5),
        (0, 7, 5, 5),
        (1, 8, 2, 1),
        (6, 9, 6, 5),
        (2, 1, 2, 2)
    ]
    result = [6, 9, 0, 7]  # optimal route should take 15 mins
    return optimalRoute(start, end, passengers, roads) == result


def test_reroute_from_start():
    start = 0
    end = 4
    passengers = [2, 1]
    roads = [
        (0, 4, 30, 5),
        (0, 1, 5, 4),
        (1, 3, 3, 2),
        (3, 2, 2, 1),
        (2, 0, 1, 1)]
    result = [0, 1, 3, 2, 0, 4]
    # print(optimalRoute(start, end, passengers, roads))
    return optimalRoute(start, end, passengers, roads) == result


print(test_different_shortest_paths())
print(test_start_at_some_location())
print(test_reroute_from_start())

