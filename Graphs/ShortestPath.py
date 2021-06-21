    class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dic={}

        for key,val in self.edges:
            if key not in self.graph_dic :
                self.graph_dic[key]=[val]
            else:
                self.graph_dic[key].append(val)

# print all possible paths from start to end
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        #print('Main path iterations :',path)
        if start == end :
            print('start = end met ',start , '=', end)
            #print(path)
            return [path]

        if start not in self.graph_dic :
            print('This start not found in graph dic',start)
            return []

# driving logic
        res_paths = []
        for dest in self.graph_dic[start]:
            if dest not in path:
                new_paths=self.get_paths(dest,end,path)
                #print('new paths :', new_paths)
                for sub_path in new_paths:
                    res_paths.append(sub_path)
        return res_paths

# Shortest path
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:    return path
        if start not in self.graph_dict:    return None

        shortest_path = None
        for dest in self.graph_dict[start]:
            if dest not in path:
                sp = self.get_shortest_path(dest, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


if __name__ == '__main__' :
    routes =[('mumbai','paris'),('mumbai','dubai'),
             ('paris','dubai'),('paris','new york'),
             ('dubai','new york'), ('new york','torento')]
    route_graph = Graph(routes)
    print('Edges passed :',routes)
    print('Route dictionary :',route_graph.graph_dic)
    start='mumbai'
    end='new york'
    print(route_graph.get_paths(start,end))


