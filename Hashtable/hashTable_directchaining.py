class HashTable():
    def __init__(self):
        self.hash_table=[[]for _ in range(16)]

    def insert_number(self,key,value):
        hash_value=self.compute_hash_value(key)
        self.hash_table[hash_value].append(value)
    
    def insert_string(self,key,value):
        hash_value=self.compute_hash_value_string(key)
        self.hash_table[hash_value].append(value)
    
    def compute_hash_value_string(self,key):
        sum=0
        for char in key:
            sum+=ord(char)
        return sum%len(self.hash_table)
    
    def compute_hash_value(self,key):
        return key%len(self.hash_table)
    
    def get_value(self,key):
        hash_value=self.compute_hash_value_string(key)
        output=self.hash_table[hash_value]
        print("The value for "+str(key)+ " is "+str(output))
    
    def print_hash_table(self):
        print(str(self.hash_table),end=" ")

if __name__=="__main__":
    h=HashTable()
    h.insert_string("John Doe", 'syzhrnvyn') 
    h.insert_string("Jane Doe", 'hysnvh') 
    h.insert_string("xyzts", 'ufncvbjnv') 
    # h.insert_number(9, 'Delhi') 
    # h.insert_number(21, 'Punjab') 
    # h.insert_number(21, 'Noida') 
    h.print_hash_table()
    h.get_value("Jane Doe")