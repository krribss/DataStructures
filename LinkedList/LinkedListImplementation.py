class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        cur=self.head
        if cur is None:
            self.head=Node(data,None)
            return
        while cur.next:
            cur=cur.next
        cur.next=Node(data,None)

    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        cur=self.head
        count=0
        while cur:
            count+=1
            cur=cur.next
        return count

    def remove_at_index(self, index):
        count=0
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
        else:
            cur=self.head
            while cur:
                if count==index-1:
                    cur.next=cur.next.next
                    break
                cur=cur.next
                count+=1

    def insert_at_index(self,index,data):
        count=0
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_begin(data)
        else:
            cur=self.head
            while cur:
                if count==index-1:
                    addr=cur.next
                    cur.next=Node(data,addr)
                    break
                cur=cur.next
                count+=1

    def insert_after_value(self, data_after, data_to_insert):
        cur=self.head
        while cur:
            if(cur.data==data_after):
                addr=cur.next
                cur.next=Node(data_to_insert,addr)
                return
            cur=cur.next

        print("No data matching")


    def remove_by_value(self, data):
        cur=self.head
        if self.head is None:
            print("empty list")
            return

        if(cur.data==data):
            self.head=self.head.next
            return

        while cur.next:
            if(cur.next.data==data):
                cur.next=cur.next.next
                return
            cur=cur.next
        print("No matching data to remove")


    def print_list(self):
        cur=self.head
        if cur is None:
            print("List is empty")
            return

        while cur:
            print(str(cur.data),end="->" )
            cur=cur.next


if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_begin(15)
    ll.insert_at_begin(10)
    ll.insert_at_begin(5)
    ll.insert_at_end(20)
    ll.insert_at_end(25)
    ll.insert_values(["banana","Mango","Grapes","Orange"])
    ll.remove_at_index(2)
    ll.insert_at_index(0,"Hello")
    ll.insert_after_value(25,30)
    ll.remove_by_value(20)
    print("Length of the linked list : ",ll.get_length())
    ll.print_list()
