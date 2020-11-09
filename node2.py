import math


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def createBalancedTree(self, data):
        return self.BalancedTree(data, 0, len(data)-1)

    def BalancedTree(self, data, start, end):
        if end < start:
            return None
        mid = math.floor((start+end)/2)
        tree = Node(data[mid])
        tree.left = self.BalancedTree(data, start, mid - 1)
        tree.right = self.BalancedTree(data, mid + 1, end)
        return tree

    def createlist(self, root):
        res = []
        if root:
            res = self.createlist(root.left)
            res.append(root.data)
            res = res + self.createlist(root.right)
        return res

# Print the Tree
    def PrintTree(self):
        if self.left:
            print(f"Вершина {self.data}")
            print(f"Лево {self.left.data}")
            self.left.PrintTree()
        if self.right:
            print(f"Вершина {self.data}")
            print(f"Право {self.right.data}")
            self.right.PrintTree()

root = Node(12)
root.insert(1)
root.insert(4)
root.insert(9)
root.insert(10)
root.insert(5)
root.insert(8)
root.insert(11)
root.insert(2)
root.insert(14)
root.insert(3)
root.insert(7)
root.insert(20)
root.insert(16)
listTree = root.createlist(root)
Balance = root.createBalancedTree(listTree)
print(Balance.PrintTree())

