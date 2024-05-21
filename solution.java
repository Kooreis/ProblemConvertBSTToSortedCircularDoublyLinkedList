Here is a Java console application that converts a Binary Search Tree (BST) to a sorted circular doubly linked list:

```java
class Node {
    int val;
    Node left, right;

    public Node(int val) {
        this.val = val;
        left = right = null;
    }
}

public class Main {
    Node head, prev;

    void bstToSortedDoublyLinkedList(Node root) {
        if (root == null) return;

        bstToSortedDoublyLinkedList(root.left);

        if (prev == null) {
            head = root;
        } else {
            root.left = prev;
            prev.right = root;
        }
        prev = root;

        bstToSortedDoublyLinkedList(root.right);
    }

    Node bTreeToCList(Node root) {
        bstToSortedDoublyLinkedList(root);
        head.left = prev;
        prev.right = head;

        return head;
    }

    void display(Node head) {
        Node itr = head;
        do {
            System.out.print(itr.val + " ");
            itr = itr.right;
        } while (itr != head);
        System.out.println();
    }

    public static void main(String args[]) {
        Main tree = new Main();
        Node root = new Node(4);
        root.left = new Node(2);
        root.right = new Node(5);
        root.left.left = new Node(1);
        root.left.right = new Node(3);

        Node head = tree.bTreeToCList(root);
        tree.display(head);
    }
}
```

This program first creates a BST with nodes 4, 2, 5, 1, 3. Then it converts the BST to a sorted circular doubly linked list and displays the list. The output will be "1 2 3 4 5".