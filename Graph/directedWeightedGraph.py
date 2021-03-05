class directedWeightedGraph():
    def __init__(self):
        self.nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        self.distances = {
            'A': {'B': 5, 'D': 1, 'G': 2},
            'B': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
            'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
            'G': {'B': 2, 'D': 1, 'C': 2},
            'C': {'G': 2, 'E': 1, 'F': 16},
            'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
            'F': {'A': 5, 'E': 2, 'C': 16}}
        self.using_dijkstra('A','F')
    
    def using_dijkstra(self,source,destination):
        node_weight={}
        unvisited_nodes=self.distances
        track_path=[]
        track_predecessor={}
        path_options=[]
        
        for node in unvisited_nodes:
            node_weight[node]=float('inf')
        node_weight[source]=0
        
        while unvisited_nodes:
            parent_node=None
            for node in unvisited_nodes:
                if parent_node==None:
                    parent_node=node
                elif node_weight[node]<node_weight[parent_node]:
                    parent_node=node
            path_options=unvisited_nodes[parent_node].items()

            for node,edge_value in path_options:
                if edge_value+node_weight[parent_node]<node_weight[node]:
                    node_weight[node]=edge_value+node_weight[parent_node]
                    track_predecessor[node]=parent_node
            unvisited_nodes.pop(parent_node)
        
        current_node=destination
        while current_node!=source:
            try:
                track_path.insert(0,current_node)
                current_node=track_predecessor[current_node]
            except KeyError:
                print("Path is not reachable")
        
        track_path.insert(0,source)
        
        if node_weight[destination] != float('inf'):
            print("Shorted Distance " +str(node_weight[destination]))
            print("tracking the path from source to destination "+str(track_path),end=" ")

if __name__=="__main__":
    d=directedWeightedGraph()