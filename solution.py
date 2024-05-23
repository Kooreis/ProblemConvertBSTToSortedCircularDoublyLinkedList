class BSTtoCDLL:
    def __init__(self):
        self.head = None
        self.prev = None

    def convert(self, root):
        if root is None:
            return

        self.convert(root.left)

        node = Node(root.data)

        if self.prev is None:
            self.head = node
        else:
            self.prev.right = node
            node.left = self.prev

        self.prev = node

        self.convert(root.right)