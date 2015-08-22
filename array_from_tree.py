def build_array_from_tree(root):
    "Convert a tree into an array (flatten a tree)"
    current_stack = []
    output = []
    next_queue = Queue()

    current_stack.append(root)

    while len(current_stack) > 0 and \
          len(next_queue) > 0:

        output.append([])

        while len(current_stack) > 0:
            item = current_stack.pop()
            output[-1].append(item)

            for child in item.children():
                next_queue.enqueue(child)

        while len(next_queue) > 0:
            current_stack.append(next_queue.dequeue())
