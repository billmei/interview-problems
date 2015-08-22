from __future__ import print_function

class DynamicArray(object):
    """Array that can take an arbitrary number of inputs"""
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.current_index = 0
        self._array = [None] * self.capacity

    def add(self, item):
        if self.current_index > self.capacity - 1:
            self._resize()

        self._array[self.current_index] = item
        self.current_index += 1

    def delete(self, item):
        last_index = 0
        for i, old_item in enumerate(self._array):
            if old_item == item:
                # TODO: Allow the user to put None as an actual value
                self._array[i] = None
            else:
                self._array[last_index] = self._array[i]
                last_index += 1

        self.current_index = last_index
        # TODO: Resize to reduce the size


    def size(self):
        return self.current_index

    def _resize(self):
        """Doubles the size of the array and copies everything over"""
        self.capacity *= 2
        # TODO: Allow the user to put None as an actual value
        new_array = [None] * self.capacity

        for i, item in enumerate(self._array):
            new_array[i] = item

        self._array = new_array

    def __str__(self):
        return ''.join(self._array)

    def _p(self):
        return self._array

my_array = DynamicArray(2)

my_array.add(1)
my_array.add(2)
my_array.add(3)
my_array.add(1)

my_array.delete(1)

# print my_array.size()

class Node(object):
    """Linked List Node"""
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    """Linked List"""
    def __init__(self):
        self.root = None
        self.last_node = self.root
        self.current_size = 0

    def add(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.last_node = self.root
        else:
            self.last_node.next = new_node
            self.last_node = new_node
        self.current_size += 1

    def size(self):
        return self.current_size

    def iter_list(self, func=print):
        current_node = self.root
        while current_node is not None:
            func(current_node)
            current_node = current_node.next

    def delete(self, value):
        """Delete all nodes that match the given value"""
        prev = self.root
        current_node = prev

        while current_node is not None:
            if current_node.value == value:
                if current_node == self.root:
                    prev = current_node.next
                else:
                    prev.next = current_node.next
                    # TODO: Change the self.size
            else:
                prev = current_node

            current_node = current_node.next

        self.last_node = current_node

#     x
# 2 > 3 > 4
#         x

my_linked_list = LinkedList()

my_linked_list.add(1)
my_linked_list.add(2)
my_linked_list.add(3)

# print my_linked_list.root.value
my_linked_list.iter_list()