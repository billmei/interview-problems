// Sorted Linked List Insert Problem

// 0 -> 1 -> 4 -> 6

//Node.insert(head, 4);

// Pass in head as the initial pointer
// Assuming you only have ints
Node.prototype.insert = function(ptr, item) {
  if (!ptr.next) {
  // Insert as next item if you're at the end
    ptr.next = new Node(item);
  } else if (ptr.value <= item && ptr.next.value > item) {
  // Insert if value is between current node and next node
    var temp = ptr.next;
    ptr.next = new Node(item);
    ptr.next.next = temp;
    temp = null;
  } else {
  // Otherwise go to the next node
    Node.insert(ptr.next);
  }
};