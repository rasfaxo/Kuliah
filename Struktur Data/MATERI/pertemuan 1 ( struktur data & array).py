class Node :
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def push(self, new_data):
        new_node=Node((new_data))
        new_node.next=self.head
        self.head=new_node

    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous nide must be in LinkedList.")
            return
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

#example usage

Linked_list = LinkedList()

Linked_list.push(3)
Linked_list.push(5)
Linked_list.push(7)
Linked_list.insert_after(Linked_list.head.next,7)

Linked_list.print_list()