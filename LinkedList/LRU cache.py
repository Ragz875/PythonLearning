# LRU cache implementation using linkedlist
class DLNode():
    def __init__(self):
        self.prev=None
        self.key=0
        self.value=0
        self.next=None
        print('New Node created')

class LRUcache():
    def __init__(self,capacity):
    #initial status when LRCache object is instantiated
        # Cache properties
        self.cache={}
        self.size=0
        self.capacity=capacity

        # Queue DS properties
        self.head,self.tail=DLNode(),DLNode()
        self.head.next=self.tail
        self.tail.prev=self.head

        print(f'LRU LL is created, current cache capacity is {capacity}')

    def get(self,key):
        #search first in Cache

        if key not in self.cache:
            return -1

        node=self.cache[key]
        self.remove_node(node)
        self.add_node(node)

        return node.value

    def remove_node(self,node):
        prev=node.prev
        next=node.next

        prev.next=next
        next.prev=prev

    def add_node(self,node):
        # always insert new node right after the head
        node.prev=self.head
        node.next=self.head.next

        self.head.next.prev=node
        self.head.next=node

    def put(self, key, val):
        # check if key is present in cache and get the node

        if key not in self.cache:
             # new key with new node address to be added to the cache
             new_node=DLNode()
             new_node.key=key
             new_node.value=val

              #cache update and queue update should be in sync
             self.cache[key]=new_node
             self.add_node(new_node)
             self.size+=1

             if self.size > self.capacity:
                 # queue node remove and cache remove in sync
                 tail=self.pop_tail()
                 del self.cache[tail.key]
                 self.size-=1

        else:
            # if key present means update the new value in the node and perform remove and add
            node=self.cache[key]
            node.value=val
            self.remove_node(node)
            self.add_node(node)

    def pop_tail(self):

        res=self.tail.prev
        self.remove_node(res)

        return res

if __name__=='__main__':
    lruobj=LRUcache(2)
    lruobj.put(1, 1)
    lruobj.put(2, 2)
    print('lruobj.get(1) :', lruobj.get(1))
    lruobj.put(3, 3)
    print('lruobj.get(1) :', lruobj.get(2))
    lruobj.put(4, 4)
    print('lruobj.get(1) :', lruobj.get(1))
    print('lruobj.get(1) :', lruobj.get(3))
    print('lruobj.get(1) :', lruobj.get(4))



















