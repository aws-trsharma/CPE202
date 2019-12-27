"""
CPE 202: Lab 9
Author Tushar Sharma
"""


UNDISCOVERED = 0
DISCOVERED = 1
DONE = 2

RED = 'red'
BLACK = 'black'

class Vertex:
    """
    class for Vertex
    Attributes:
        key(int): a key
        val (int): a value
        edges (list): a list of tuples of (Vertex, weight)
        num_edges (int): number of edges
        status(str): None or discovered or done
        predecessor (Vertex): the predecessor
        color (str): RED or BLACK
    """
    def __init__(self, key):
        self.key = key
        self.edges = []
        self.num_edges = 0
        self.status = UNDISCOVERED
        self.predecessor = None
        self.color = BLACK

    def __repr__(self):
        return "%d" % (self.key)

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.key == other.key \
              and self.edges == other.edges

    def add_edge(self, v):
        """adds an edge to an vertex
        Args:
             v (Vertex) : the destination Vertex
            weight (int) : the weight of the edge
        """

        self.edges.append(v)
        self.num_edges += 1

    def get_edges(self):
        """returns a list of edges
        Returns:
             list : a list of tuples (Vertex, weight)
        """
        return self.edges

class MyGraph:
    """
    Graph class which implements both DFS and BFS search to find connected components and finding if
    it is biparitite
    Attributes:
        filename (file): reads in the specification of the file and creates an adjacency list representation
        of connected components
    """
    def __init__(self, filename):
        self.filename = filename
        file = open(filename, 'r')
        self.num_vertices = int(file.readline())
        self.num_edges = int(file.readline(10))
        if self.num_vertices % 2 == 0:
            self.is_bicolor = False
        else:
            self.is_bicolor = True
        self.vertices = [None] * self.num_vertices
        for line in file:
            vertices_1 = int(line[0])
            vertices_2 = int(line[2])
            self.add_vertex(vertices_1)
            self.add_vertex(vertices_2)
            self.add_edges(vertices_1, vertices_2)
        for vert in range(len(self.vertices)):
            if self.vertices[vert] is None:
                vertex = Vertex(5)
                self.vertices[vert] = vertex
        self.is_cyclic = False
        self.connected_components = []

    def __repr__(self):
        return "%s" % self.vertices

    def add_vertex(self, key):
        vertex = Vertex(key)
        if self.vertices[key - 1] is None:
            self.vertices[key - 1] = vertex

    def add_edges(self, org, to):
        org_v = self.vertices[org - 1]
        to_v = self.vertices[to - 1]
        org_v.add_edge(to_v)
        to_v.add_edge(org_v)

    def get_conn_components(self, mode = 'DFS'):
        """
        Returns a list of lists of connected components
        :param
            mode: DFS or BFS: Search method which keeps going recursively until
            it reaches a end point then backtracks. If BFS entered, Breadth First Search is done
        :return:
            comp_list: (list): list of lists with all connected components
        """
        self.init_vertices()
        comps = []
        new_list = []
        if mode == "DFS":
            for vertices in self.vertices:
                if vertices.status == UNDISCOVERED:
                    comps.append(self.dfs(vertices, []))
            for comp in comps:
                new_list.append(self.sorter(comp))
            return new_list
        else:
            for vertices in self.vertices:
                if vertices.status == UNDISCOVERED:
                    comps.append(self.bfs(vertices, []))
            for comp in comps:
                new_list.append(self.sorter(comp))
            return new_list

    def sorter(self, comp):
        """
        Sorts the method so everything can be put in ascending order
        :param comp:
        :return:
        """
        new_list = []
        for ver in comp:
            new_list.append(ver.key)
        new_list.sort()
        return new_list
    def init_vertices(self):
        """
        Initializes vertices from the vertex class
        :return:
        """
        for vertices in self.vertices:
            vertices.status = UNDISCOVERED
            vertices.predecessor = None
            vertices.color = BLACK
    def dfs (self, start_vertex, component):
        """
        Depth First Search, finds connected components and determines if graph is bicolorable or not
        :param
            vertex: (vertex): vertex which has components
            component:
        :return:
            Connected component as a list of vertex keys
        """
        start_vertex.status = DISCOVERED
        start_vertex.color = RED
        component.append(start_vertex)
        for vertex in start_vertex.get_edges():
            if vertex.status == UNDISCOVERED:
                vertex.predecessor = start_vertex
                self.dfs(vertex, component)
            elif vertex != start_vertex.predecessor:
                self.is_cyclic = True
        start_vertex.status = DONE
        return component

    def bfs(self, start_vertex, component):
        """
        Breadth First Search, find connected components and determines if graph is bicolorable or not
        :param
            vertex: (vertex) connected to components
            component:
        :return:
            connected components as a list of vertex keys
        """
        queue1 = queue()
        component.append(start_vertex)
        start_vertex.status = DISCOVERED
        start_vertex.color = RED
        queue1.enqueue(start_vertex)
        while not queue1.isEmpty():
            current = queue1.dequeue()
            for edge in current.get_edges():
                if edge.status == UNDISCOVERED:
                    edge.status = DISCOVERED
                    edge.color = RED
                    queue1.enqueue(edge)
                    component.append(edge)
            current.status = DONE
        return component

    def get_vertex(self, name):
        if name not in self.vertices:
            raise KeyError

        return self.vertices[name]

    def bicolor(self):
        """
        returns True if graph is bicolorable. Returns False otherwise.
        :return:
            value of bicolor
        """
        self.get_conn_components()
        return self.is_bicolor
"""
Queue used by DFS in order to to search
"""
class queue:
    """
    the number of items in the queue
    """
    def __init__(self):
        self.items = []

    def __repr__(self):

        return "%s" % self.items
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):

        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

graph = MyGraph("graph_testinput2.txt")
print(graph.vertices)
print(graph.get_conn_components())
print(graph.bicolor())
