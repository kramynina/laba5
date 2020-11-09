class Node:

    def __init__(self, data):
        self.one = None
        self.two = None
        self.three = None
        self.four = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < 8:
                if self.one is None:
                    self.one = Node(data)
                else:
                    self.one.insert(data)
            elif data >= 8 and data < 16:
                if self.two is None:
                    self.two = Node(data)
                else:
                    self.two.insert(data)
            elif data >= 16 and data < 24:
                if self.three is None:
                    self.three = Node(data)
                else:
                    self.three.insert(data)
            elif data >= 24:
                if self.four is None:
                    self.four = Node(data)
                else:
                    self.four.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.one:
            print(f"Вершина {self.data}")
            print(f"Первая {self.one.data}")
            self.one.PrintTree()
        if self.two:
            print(f"Вершина {self.data}")
            print(f"Вторая {self.two.data}")
            self.two.PrintTree()
        if self.three:
            print(f"Вершина {self.data}")
            print(f"Третья {self.three.data}")
            self.three.PrintTree()
        if self.four:
            print(f"Вершина {self.data}")
            print(f"Четвёртая {self.four.data}")
            self.four.PrintTree()


root = Node(71)
root.insert(7)
root.insert(10)
root.insert(19)
root.insert(35)
root.PrintTree()