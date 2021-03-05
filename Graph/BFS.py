class BFS():
    def __init__(self):
        self.map={'A':{ 'B', 'C'},
                  'B':{ 'D', 'E','A'},
                  'C':{ 'F', 'G','A'},
                  'D':{ 'B', 'E'},
                  'E':{ 'B', 'D'},
                  'F':{ 'C'},
                  'G':{ 'C'}
                  }
        vertex='A'
        visited_node=set()
        q=[]
        q.append(vertex)
        while q:
            p=q.pop(0)
            print(str(p))
            for neighbors in self.map[p]:
                if neighbors not in visited_node:
                    q.append(neighbors)
            visited_node.add(p)

        print(str(visited_node),end=" ")

if __name__=="__main__":
    b=BFS()
    
                    
        