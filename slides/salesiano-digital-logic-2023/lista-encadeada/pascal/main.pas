program LinkedList;

type
  Node = record
    data: Integer;
    next: ^Node;
  end;

type
  LinkedList = record
    head: ^Node;
  end;

procedure InitializeLinkedList(var list: LinkedList);
begin
  list.head := nil;
end;

procedure Append(var list: LinkedList; data: Integer);
var
  newNode, current: ^Node;
begin
  newNode := New(^Node);
  newNode^.data := data;
  newNode^.next := nil;

  if list.head = nil then
    list.head := newNode
  else
  begin
    current := list.head;
    while current^.next <> nil do
      current := current^.next;
    current^.next := newNode;
  end;
end;

procedure Remove(var list: LinkedList; data: Integer);
var
  current, prev: ^Node;
begin
  current := list.head;
  prev := nil;

  while current <> nil do
  begin
    if current^.data = data then
    begin
      if prev = nil then
        list.head := current^.next
      else
        prev^.next := current^.next;
      Dispose(current);
      Exit;
    end;
    prev := current;
    current := current^.next;
  end;
end;

procedure Print(const list: LinkedList);
var
  current: ^Node;
begin
  current := list.head;
  while current <> nil do
  begin
    Write(current^.data, ' ');
    current := current^.next;
  end;
  Writeln;
end;

var
  linkedList: LinkedList;

begin
  InitializeLinkedList(linkedList);

  Append(linkedList, 1);
  Append(linkedList, 2);
  Append(linkedList, 3);

  Print(linkedList);  // Output: 1 2 3

  Remove(linkedList, 2);
  Print(linkedList);  // Output: 1 3
end.

