class BFS_SSSP():
    def __init__(self,start,end):
        self.edges={'A':{ 'B', 'C'},
                  'B':{ 'D', 'E','A'},
                  'C':{ 'F', 'G','A'},
                  'D':{ 'B', 'E'},
                  'E':{ 'B', 'D'},
                  'F':{ 'C','M','N'},
                  'G':{ 'C'},
                  'N':{'O','F','M'},
                  'M':{'F','N'},
                  'O':{'N'}
                  }
        q=[]
        q.append(start)
        track_path=set()
        visited_nodes=set()
        neighbors=[]
        if start==end:
            print("Goal reached-start is equal to end")
            return
        while q:
            p=q.pop(0)
            node=p
            if len(p)>1:
                node=p[-1]
            if node not in visited_nodes:
                for neighbors in self.edges[node]:
                   new_path=list(p)
                   new_path.append(neighbors)
                   q.append(new_path)
                   if neighbors==end:
                       print(str(new_path))
                       return
            visited_nodes.add(node)

if __name__=="__main__":
    u=BFS_SSSP('A','G')