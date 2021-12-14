class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
    
    def printTree(self):
        print(self.data)

    def insert(self, node):
        if node.data < self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def dfs_search(node):
    if node is None:
        return
    if node:
        dfs_search(node.left)
        print(node.data)
        dfs_search(node.right)

def DoraTE (curr = [0, 0], visited = [], node = None):
    if node:
        visited.append(node.data)
        if node.left:
            if node.left.data not in visited:
                print(node.data)
                DoraTE(visited, node.left)

root = Node(10)
root.insert(Node(5))
root.insert(Node(15))
root.insert(Node(2))
root.insert(Node(7))
root.insert(Node(12))

dfs_search(root)