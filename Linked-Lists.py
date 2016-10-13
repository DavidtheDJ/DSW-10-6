#David Justice
#10-12-16
#Linked Lists

class Node:
    def __init__(self, contents=None, next=None):
        self.contents = contents
        self.next  = next

    def getContents(self):
        return self.contents

    def __str__(self):
        return str(self.contents)

    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.contents)
        self.contents = new_node
    
    def delete(self,data):
        current = self.contents
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = currnet
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.content = current.get_next()
        else:
            previous.set_next(surrent.get_next())

def print_list(node):
    while node:
        print(node.getContents())
        node = node.next
    print()

def testList():
    node1 = Node("car")
    node2 = Node("bus")
    node3 = Node("lorry")
    node4 = Node("train")
    #added = Node.insert("train")
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print_list(node1)

testList()
