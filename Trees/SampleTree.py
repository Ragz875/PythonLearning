class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self, child):
        child.parent=self
        self.children.append(child)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        for child in self.children :
            child.print_tree()

    def get_level(self):
        ancestor=0
        p= self.parent
        while p:
            p=p.parent
            ancestor+=1
        return ancestor

def build_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Dell'))
    laptop.add_child(TreeNode('Lenovo'))

    Cellphone = TreeNode('Cell Phone')
    Cellphone.add_child(TreeNode('Apple'))
    Cellphone.add_child(TreeNode('Samsung'))

    tv=TreeNode('TV')
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Sony'))


    root.add_child(laptop)
    root.add_child(Cellphone)
    root.add_child(tv)
    return root

if __name__ == '__main__' :
    root = build_tree()
    root.print_tree()
    print("Root level is :", root.get_level())
