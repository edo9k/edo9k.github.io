#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node* next;
};

struct LinkedList {
  struct Node* head;
};

void append(struct LinkedList* list, int data) {
  struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
  new_node->data = data;
  new_node->next = NULL;

  if (list->head == NULL) {
    list->head = new_node;
  } else {
    struct Node* current = list->head;
    while (current->next != NULL) {
      current = current->next;
    }
    current->next = new_node;
  }
}

void removeNode(struct LinkedList* list, int data) {
  struct Node* current = list->head;
  struct Node* prev = NULL;

  while (current != NULL) {
    if (current->data == data) {
      if (prev == NULL) {
        list->head = current->next;
      } else {
        prev->next = current->next;
      }
      free(current);
      return;
    }
    prev = current;
    current = current->next;
  }
}

void print(struct LinkedList* list) {
  struct Node* current = list->head;
  while (current != NULL) {
    printf("%d ", current->data);
    current = current->next;
  }
  printf("\n");
}

int main() {
  struct LinkedList linked_list;
  linked_list.head = NULL;

  append(&linked_list, 1);
  append(&linked_list, 2);
  append(&linked_list, 3);

  print(&linked_list);  // Output: 1 2 3

  removeNode(&linked_list, 2);
  print(&linked_list);  // Output: 1 3
                      
  return 0;
}

