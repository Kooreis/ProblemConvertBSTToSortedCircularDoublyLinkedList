Here is a Python solution for converting a Binary Search Tree (BST) to a sorted circular doubly linked list:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

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

    def BSTtoCDLL(self, root):
        self.convert(root)

        self.head.left = self.prev
        self.prev.right = self.head

        return self.head

    def display(self, head):
        itr = head
        while True:
            print(itr.data, end = " ")
            itr = itr.right
            if itr == head:
                break

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    converter = BSTtoCDLL()
    head = converter.BSTtoCDLL(root)
    converter.display(head)
```

This Python program first creates a BST with the given input data, then converts the BST into a circular doubly linked list and finally displays the data in the linked list. The conversion is done in a way that the linked list remains sorted.