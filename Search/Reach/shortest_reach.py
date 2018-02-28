class Graph:
    def __init__(self, n):
        self.n = n
        self.nodes = {}

    def connect(self, x, y):
        """Connects x and y nodes"""
        if x not in self.nodes:
            self.nodes[x] = set()

        self.nodes[x].add(y)

        if y not in self.nodes:
            self.nodes[y] = set()

        self.nodes[y].add(x)

    def find_shortest_path(self, start, end):
        visited = []
        frontier = [[start]]

        while frontier:
            current_path = frontier.pop(0)
            head = current_path[-1]

            if head in visited:
                continue

            if head == end:
                return current_path

            for neighbor in self.nodes.get(head, []):
                path_to_neighbor = list(current_path) + [neighbor]
                frontier.append(path_to_neighbor)

            visited.append(head)

        return None

    def get_layers(self, start):
        visited = set()
        frontier = [[start]]
        layers = [] # [{2, 3, 4}, {5, 6, 7}, {7, 8 , 9}]

        while frontier:
            current_layer = frontier.pop(0)
            layers.append(current_layer)

            new_layer = set()
            for node in current_layer:
                if node in visited:
                    continue

                visited.add(node)
                if node in self.nodes:
                    neighbors = self.nodes[node]
                    new_layer = new_layer.union(neighbors)

            if new_layer:
                frontier.append(list(new_layer))

        return layers



    def find_all_distances(self, start):
        """returns the total path length to each other node"""
        result = [-1] * (n+1)

        layers = self.get_layers(start)
        for i, layer in enumerate(layers[1:]):
            for element in layer:
                if result[element] == -1:
                    result[element] = i * 6 + 6

        return result[1:start] + result[start+1:]



t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)

    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x, y)

    s = int(input())
    print(' '.join(map(str, graph.find_all_distances(s))))

