class DFS():
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
        stack=[]
        stack.append(vertex)
        visited_node=set()
        while stack:
            p=stack.pop()
            print(str(p))
            for neihbors in self.map[p]:
                if neihbors not in visited_node:
                    stack.append(neihbors)
            visited_node.add(p)
        for item in visited_node:
            print(str(item),end=" ")

if __name__=="__main__":
    d=DFS()
    
                    