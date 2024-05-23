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
}