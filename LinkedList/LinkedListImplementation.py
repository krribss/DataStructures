class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtBegin(self,data):
        node=Node(data,self.head)
        self.head=node

    def insertAtEnd(self,data):
        cur=self.head
        if cur is None:
            self.head=Node(data,None)
            return
        while cur.next:
            cur=cur.next
        cur.next=Node(data,None)

    def insertValues(self,data_list):
        for data in data_list:
            self.insertAtEnd(data)

    def printList(self):
        cur=self.head
        if cur is None:
            print("List is empty")
            return

        while cur:
            print(str(cur.data),end="->" )
            cur=cur.next


if __name__=='__main__':
    ll=LinkedList()
    ll.insertAtBegin(15)
    ll.insertAtBegin(10)
    ll.insertAtBegin(5)
    ll.insertAtEnd(20)
    ll.insertAtEnd(25)
    ll.insertValues(["banana","Mango","Grapes","Orange"])
    ll.printList()
