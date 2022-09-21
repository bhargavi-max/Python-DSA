from Node import Node
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def enqueue(self, value):
                new_item_add=Node(value)
                print("Adding " + str(new_item_add.get_value())+" to the queue")

                if self.is_empty():
                    self.head=new_item_add
                    self.tail=new_item_add
                else:
                    self.tail.set_next_node(new_item_add)
                    self.tail=new_item_add
                self.size+=1
       
    def dequeue(self):
        if self.size > 0:
            item_remove=self.head
            print(str(item_remove.get_value()) +"is removed")
            if self.get_size()==1:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.get_next_node()
            self.size-=1
            return item_remove.get_value()
        else:
            print("queue is empty you can't remove an element")
    def peek(self):
        if self.size>0:
            return self.head.get_value()
        else:
            print("Nothing to Show")
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    
    def printqueue(self):
        print("Queue: ")
        a=self.head
        while a is not None:
                print(a.get_value() , end=" ")
                a=a.next_node

q= Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.peek())
q.printqueue()