class TreeNode:
	def __init__(self,data):
		self.data=data
		self.children=[]
		self.parent=None

	def add_child(self,child):
		child.parent=self
		self.children.append(child)

	def get_level(self):
		ancestor=0
		p=self.parent
		while p:
			ancestor+=1
			p=p.parent

		return ancestor

	def print_tree(self):
		spaces=' ' * self.get_level() * 3
		prefix= spaces + '|__' if self.parent else ''
		print(prefix + self.data)
		for child in self.children:
			child.print_tree()


def build_tree():
	root=TreeNode('Electronics')
	root.add_child(TreeNode('Laptop'))
	root.add_child(TreeNode('Cell Phone'))
	tv=TreeNode('TV')
	root.add_child(tv)


	return root

# main starts here
if __name__ == '__main__':
	root=build_tree()
	root.get_level()
	root.print_tree()
