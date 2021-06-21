# recursive level order display
# Needs to be implemented later
class NewNode():
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

class BinTree():
    def __init__(self,data=None):
        self.root=NewNode(data)
        self.path=[]

    def add_child(self,data):
        print('add child called ')
        q=[]
        q.append(self.root)

        while len(q):
            temp=q[0]
            q.pop(0)
            if temp.left is None:
                temp.left=NewNode(data)
                print(f'left Node {data} added')
                break
            else:
                q.append(temp.left)
                print('left:', q)

            if temp.right is None:
                temp.right=NewNode(data)
                print(f'right Node {data} added')
                break
            else:
                q.append(temp.right)
                print('right:', q)
    def print_tree(self,traversal_type):
        if traversal_type == 'inorder':
            print('inorder is called ')
            self.inorder(self.root)
        elif traversal_type == 'preorder':
            print('preorder is called ')
            self.preorder(self.root)
        elif traversal_type == 'postorder':
            print('postorder is called ')
            self.postorder(self.root)

    def inorder(self,temp):
        if temp:
            self.inorder(temp.left)
            print(temp.data, end='-->')
            self.inorder(temp.right)
    def preorder(self,temp):
        if temp:
            print(temp.data, end='-->')
            self.preorder(temp.left)
            self.preorder(temp.right)

    def postorder(self,temp):
        if temp:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data, end='-->')

    def findpath1(self):
        path=[]
        q=[]
        q.append(self.root)

        while len(q):
            temp=q[0]
            q.pop(0)
            if temp.left is not None:
                path.append(temp.data)
                q.append(temp.left)
            elif temp.right is not None:
                path.append(temp.data)
                q.append(temp.right)

        print(path)


if __name__ == '__main__':
    BT=BinTree(111)
    for i in range(2,6,1):
        BT.add_child(i)
    BT.print_tree('inorder')
    BT.findpath1()




