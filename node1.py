class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
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


root = Node(27)
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
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.PrintTree())
