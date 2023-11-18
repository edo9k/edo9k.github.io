class Node {
  int data;
  Node next;

  public Node(int data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  private Node head;

  public LinkedList() {
    this.head = null;
  }

  public void append(int data) {
    Node newNode = new Node(data);
    if (head == null) {
      head = newNode;
    } else {
      Node current = head;
      while (current.next != null) {
        current = current.next;
      }
      current.next = newNode;
    }
  }

  public void remove(int data) {
    if (head != null && head.data == data) {
      head = head.next;
      return;
    }
    Node current = head;
    while (current != null && current.next != null) {
      if (current.next.data == data) {
        current.next = current.next.next;
        return;
      }
      current = current.next;
    }
  }

  public void print() {
    Node current = head;
    while (current != null) {
      System.out.print(current.data + " ");
      current = current.next;
    }
    System.out.println();
  }
}

public class Main {
  public static void main(String[] args) {
    LinkedList linkedList = new LinkedList();
    linkedList.append(1);
    linkedList.append(2);
    linkedList.append(3);

    linkedList.print(); // Output: 1 2 3

    linkedList.remove(2);

    linkedList.print(); // Output: 1 3

  }
}
