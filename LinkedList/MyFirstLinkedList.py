class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        #print('Node created with data',self.data,' ',self.next)

class LinkedList():
    def __init__(self):
        print('Empty list is created')
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next :
            itr=itr.next
        itr.next=Node(data,None)

    def insert_values(self,list):
        for ele in list:
            self.insert_at_end(ele)

    def display(self,h):
        print('display function is called')
        if h is None:
            print("Linked List is empty")
            return
        itr=h
        while itr:
            print(itr.data,'-->',end='')
            itr=itr.next
        print('None')

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception('Not a valid Index passed')
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            count+=1
            itr = itr.next

    def insert_at(self,index,value):
        print('Insert_at called, requested index is :', index)
        if index < 0 or index >= self.get_length():
            raise Exception('Index out of range')
        if index==0:
            self.insert_at_begining(value)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                temp=Node(value)
                temp.next=itr.next
                itr.next=temp
                break
            count+=1
            itr = itr.next
        self.display(self.head)
    def print_reverse_rec(head):
        if head is not None:
            print_reverse_rec(head.next)
            print('-->',head.data,end='')

    def reverse_linkedlist_iterative(self):
        print('reverse linked list called')
        prev=None
        curr=self.head
        next=None

        while curr :
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev


    def reverse_linkedlist_recur(self,head):
        if head is None or head.next is None :
            return head

        revhead = self.reverse_linkedlist_recur(head.next)
        head.next.next=head
        head.next=None
        return revhead


# main starts here
l1=LinkedList()
l1.insert_at_begining(10)
l1.insert_at_begining(20)
l1.insert_at_begining(30)
l1.display(l1.head)
l1.insert_at_end(100)
l1.display(l1.head)
l1.insert_values(["test","test1"])
l1.display(l1.head)
print('Current linked List length is:',l1.get_length())
l1.remove_at(5)
l1.display(l1.head)
l1.insert_at(3,'0001')
l1.display(l1.head)
#print('print iterative reverse is called :')
#l1.display(l1.reverse_linkedlist_iterative())

print('print recursive reverse is called :')
l1.display(l1.reverse_linkedlist_recur(l1.head))