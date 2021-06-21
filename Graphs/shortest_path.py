def get_routes_dic(routes):
    route_dic={}
    for source,dest in routes:
        if source not in route_dic:
            route_dic[source]=[dest]
        else:
            route_dic[source].append(dest)
    print('Route dictionary is :',route_dic)
    return route_dic

def get_paths(source,end,path=[]):
    path = path + [source]
 #   print('path :', path)
    # base condition
    if source == end:
#        print('path :',path)
        return [path]
    
    final_paths=[]
    
    # driving logic
    for dest1 in route_dic[source]:
        if dest1 not in path:
            new_path=get_paths(dest1,end,path)
            print('new_path :', new_path)
            for path in new_path:
                final_paths.append(path)

    return final_paths


def get_shortest_path(source, end, path= [] ):
    path = path + [source]
    if source == end:
        return [path]

    short_path= None
    # driving logic
    for dest1 in route_dic[source]:
        if dest1 not in path:
            new_path = get_paths(dest1, end, path)
            if short_path is None or len(new_path) < len(short_path):
                short_path=new_path

    return short_path


if __name__ == '__main__' :
    print('Main starts here')

    routes =[('mumbai','paris'),('mumbai','dubai'),
             ('paris','dubai'),('paris','new york'),
             ('dubai','new york'), ('new york','torento')]

    route_dic=get_routes_dic(routes)
    print(route_dic)
    source='mumbai'
    end='new york'
    print(f'Available paths between {source} and {end} are:', get_paths(source,end))
    print(f'Shortest path between {source} and {end} is :',get_shortest_path(source,end))
