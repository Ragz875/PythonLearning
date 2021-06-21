class Node:
    def __init__(self,data=0,next=None):
        self.node=data
        self.next=next
    def insert(self,data):


# 1 - 2 - 3 - L1
# 2 - 3 - 4 - L2
def merge(l1,l2):
    if not l1 and not l2:
        return None
    if not l1 and l2:
        return l2
    if not l2 and l1:
        return l1

    temp = ListNode(0)
    l3 = temp

    while True:
        # during loop if L1 ends before L2
        if not l1:
            l3.next = l2
            break
        # during loop if L2 ends before L1
        if not l2:
            l3.next = l1
            break
        # while both list has data
        if l1.val <= l2.val:
            l3.next = ListNode(l1.val)
            l1 = l1.next
        else:
            l3.next = ListNode(l2.val)
            l2 = l2.next
        l3 = l3.next

    return temp.next