import binarytree

def convert_to_bintree(root):
    new_root = binarytree.Node(root.key)
    if root.left != None:
        new_root.left = convert_to_bintree(root.left)
    if root.right != None:
        new_root.right = convert_to_bintree(root.right)
    return new_root

class Node:
    def __init__(self, key=0, parent = None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

def search(root, val):
    if root == None or root.key == val:
        return root
    print(root.key)
    if val < root.key:
        return search(root.left, val)
    return search(root.right, val)

def insert(root, node):
    if root.key > node.key:
        if root.left == None:
            root.left = node
            node.parent = root
        else:
            insert(root.left, node)
    else:
        if root.right == None:
            root.right = node
            node.parent = root
        else:
            insert(root.right, node)

def tree_size(root):
    if root is None:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)


T = Node(7)
insert(T, Node(1))
insert(T, Node(0))
insert(T, Node(4))
insert(T, Node(3))
insert(T, Node(5))
insert(T, Node(10))
insert(T, Node(14))
insert(T, Node(13))
print_tree(T)
a = build_tree([51, 2, 321, 4, 5])
print(tree_max(a))
