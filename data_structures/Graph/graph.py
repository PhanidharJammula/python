class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        """ Get all possible paths between given two nodes"""

        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        """ Get the shorted path between given two nodes"""
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if not shortest_path or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


if __name__ == '__main__':
    routes = [
            ("mumbai", "paris"),
            ("mumbai", "dubai"),
            ("paris", "newyork"),
            ("paris", "dubai"),
            ("dubai", "newyork"),
            ("newyork", "toronto")]

    graph = Graph(routes)
    print("graph_dict is %s"%(graph.graph_dict))

    start = "mumbai"
    end = "newyork"
    print("paths between %s and %s are %s"%(start, end, \
            graph.get_paths(start, end)))
    print("shortest path between %s and %s is %s"%(start, end, \
            graph.get_shortest_path(start, end)))

