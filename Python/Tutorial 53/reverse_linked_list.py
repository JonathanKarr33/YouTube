class node:
    def __init__ (self,data=None ):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def display(self):
        temp = self.head
        while(temp):
            print (temp.data, end = " ")
            temp = temp.next
        print(" ")

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next      
        self.head = prev 


my_data = linked_list()
my_data.append(20)
my_data.append(30)
my_data.append(15)
my_data.append(4)
my_data.display()
my_data.reverse()
my_data.display()