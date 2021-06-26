class node:
    def __init__ (self,data=None ):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
    
    def length(self):
        current = self.head
        index = 0
        while current.next != None:
            current = current.next
            index += 1
        return index

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get (self,index):
        if index >= self.length() or index < 0:
            print("Error out of range")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def remove(self,index):
        if index >= self.length() or index < 0:
            print("Error out of range")
            return
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

    def __getitem__ (self,index):
        return self.get(index)

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.display()
my_list.remove(1)
my_list.display()
my_list.append(1)
my_list.display()