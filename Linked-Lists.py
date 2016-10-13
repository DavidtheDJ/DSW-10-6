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

    def insert(self,node):
        node.next = self.next  
        self.next = node

    def delete_node(node, contents):
        PreviousNode = node

        if node.contents == contents:
            node.contents = "blank"
            node = node.next
        else:
            while node:            
                if node.contents == contents:
                    PreviousNode.next = node.next               

                PreviousNode = node
                node = node.next
            
    
        

def print_list(node):
    while node:
        print(node.getContents())
        node = node.next
    print()

def testList():
    node1 = Node("car")
    node2 = Node("bus")
    node3 = Node("lorry")
    node1.next = node2
    node2.next = node3
    node2.insert(Node("bike"))
    node1.insert(Node("skateboard"))
    Node.delete_node(node1, "car")
    print_list(node1)

testList()
