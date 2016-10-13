#David Justice
#10-6-19
#Queues



class Queue:
    def __init__(self):
        self.items=[]
    def add(self,item):
        self.items.append(item)
    def delete(self):
        itemToDelete = self.items[0]
        del self.items[0]
        return itemToDelete
    def size(self):
        return len(self.items)
    def report(self):
        return self.items



def start():

    givenQueue=Queue()
    givenQueue.add("Bob")
    givenQueue.add("Brodie")
    givenQueue.add("Carrie")
    givenQueue.add("Tanya")
    print(givenQueue.size())
    print(givenQueue.report())
    print(givenQueue.delete())
    print(givenQueue.report())

start()
