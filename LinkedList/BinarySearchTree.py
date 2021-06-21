# implement BST and its methods including traversals
class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,val):
        if val == self.data :
            return

        if val < self.data :
            if self.left :
                self.left.add_child(val)
            else:
                self.left=BST(val)
        if val > self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right=BST(val)

    def in_order_traversal(self):
        elements=[]
        #Visit left tree
        if self.left :
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        #visit right node
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements=[]
        # visit base node
        elements.append(self.data)

        #Visit left sub tree
        if self.left :
            elements += self.left.pre_order_traversal()
        #visit right sub tree
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements=[]

        #Visit left sub tree
        if self.left :
            elements += self.left.post_order_traversal()
        #visit right sub tree
        if self.right:
            elements+=self.right.post_order_traversal()

        # visit base node
        elements.append(self.data)

        return elements

    def search(self,val):
        print(' In search method', self.data)
        if val == self.data :
            print('in ==', self.data)
            return True

        if val < self.data :
            if self.left:
                self.left.search(val)
            else:
                print('In < else')
                return False
        if val > self.data :
            if self.right:
                self.right.search(val)
            else:
                print('In > else')
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data :
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)

        return self

# helper method
def build_BST(ele):
    root=BST(ele[0])
    for i in range(1,len(ele)):
        root.add_child(ele[i])
    return root

if __name__ == "__main__" :
    elements=[17,4,1,20,9,23,18,34,4]
    bstree=build_BST(elements)

    #print(bstree.in_order_traversal())
    print(bstree.pre_order_traversal())
    #print(bstree.post_order_traversal())
    bstree.search(200)
    print('minimum in BStree : ' , bstree.find_min())
    print('maximum in BStree : ' , bstree.find_max())
    bstree1=bstree.delete(20)
    print('new list')
    print(bstree1.in_order_traversal())