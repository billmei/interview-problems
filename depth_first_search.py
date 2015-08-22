def depth_first_search(query, graph, visited=None):
    """Depth first search of a graph with an ajacency list representation"""
    if visited is None:
        visited = [False] * len(graph)
    # Start at index 0
    # For each neighbor, recurse through its neighbors by adding it to a stack
    # of things to visit. Mark these in a separate array.
    to_visit = 0
    for i, node in enumerate(graph):
        if visited[to_visit]:
            # We already visited it
            to_visit = i
        else:
            if node['value'] == query:
                return node['value']

            depth_first_search(query, node['neighbors'], visited)

    return None # query not found


class Graph(object):
    """An ajacency list representation of a graph"""
    def __init__(self):
        self.array = []
        self.i = 0

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        return self

    def next(self):
        if self.i < len(self.array):
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

    def put(self, value):
        self.array.append({
            'value' : value,
            'neighbors' : []
        })

    def connect(self, idx_1, idx_2):
        first = self.array[idx_1]
        second = self.array[idx_2]
        first['neighbors'].append(second)
        second['neighbors'].append(first)

    def get(self, idx):
        return self.array[idx].value

my_graph = Graph()
my_graph.put(0)
my_graph.put(1)
my_graph.put(2)
my_graph.put(3)
my_graph.put(4)
my_graph.put(5)
my_graph.put(6)
my_graph.put(7)

my_graph.connect(0, 1)
my_graph.connect(0, 3)
my_graph.connect(0, 4)
my_graph.connect(1, 4)
my_graph.connect(1, 2)
my_graph.connect(2, 5)
my_graph.connect(4, 6)
my_graph.connect(6, 7)

print depth_first_search(3, my_graph)