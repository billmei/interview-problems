def find_bst_vals(bst_root, a, b):

    def find_vals(node, a, b, output):
        if node is None:
            pass
        elif node.value > a and \
             node.value < b:
            output.append(node.value)
            find_vals(node.left, a, b, output)
            find_vals(node.right, a, b, output)
        elif node.value >= b:
            find_vals(node.left, a, b, output)
        elif node.value <= a:
            find_vals(node.right, a, b, output)

    output = []
    find_vals(bst_root, a, b, output)
    return output


class Node(object):
    """docstring for Node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        output = ''

        if self is None:
            return 'Value: None\n'
        else:
            output += 'Value: ' + str(self.value) + '\n'

        if self.left is None:
            output += 'Left: None\n'
        else:
            output += 'Left: ' + str(self.left) + '\n'

        if self.right is None:
            output += 'Right: None\n'
        else:
            output += 'Right: ' + str(self.right) + '\n'


        return output

bst_root = Node(7)
b = Node(3)
c = Node(10)
d = Node(1)
e = Node(5)
f = Node(9)

bst_root.left = b
bst_root.right = c
b.left = d
b.right = e
c.left = f

# print bst_root
print find_bst_vals(bst_root, 2, 10)
