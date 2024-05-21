Here is a C# console application that converts a Binary Search Tree (BST) to a sorted circular doubly linked list:

```csharp
using System;

public class Node
{
    public int data;
    public Node left, right;

    public Node(int item)
    {
        data = item;
        left = right = null;
    }
}

public class BinaryTree
{
    Node root, head, prev;

    void BinaryTree2DoubleLinkedList(Node root)
    {
        if (root == null)
            return;

        BinaryTree2DoubleLinkedList(root.left);

        if (prev == null)
            head = root;
        else
        {
            root.left = prev;
            prev.right = root;
        }
        prev = root;

        BinaryTree2DoubleLinkedList(root.right);
    }

    void BinaryTree2CircularDoubleLinkedList(Node root)
    {
        BinaryTree2DoubleLinkedList(root);

        head.left = prev;
        prev.right = head;
    }

    void printList(Node node)
    {
        Node temp = node;
        do
        {
            Console.Write(temp.data + " ");
            temp = temp.right;
        }
        while (temp != node);
    }

    public static void Main(String[] args)
    {
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(4);
        tree.root.left = new Node(2);
        tree.root.right = new Node(5);
        tree.root.left.left = new Node(1);
        tree.root.left.right = new Node(3);

        tree.BinaryTree2CircularDoubleLinkedList(tree.root);

        Console.WriteLine("Output Circular Doubly Linked list is :");
        tree.printList(tree.head);
    }
}
```

This program creates a binary tree and then converts it to a circular doubly linked list. The `BinaryTree2DoubleLinkedList` method is used to convert the binary tree to a doubly linked list. The `BinaryTree2CircularDoubleLinkedList` method is used to convert the doubly linked list to a circular doubly linked list. The `printList` method is used to print the circular doubly linked list.