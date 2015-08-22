def autocomplete(in_str, trie):
    node = trie
    for char in in_str:
        node = node.get_child(char)

    output = []
    candidates = [(i, in_str) for i in node.children]

    while len(candidates):
        branch, current_word = candidates.pop()

        if not branch.value:
            output.append(current_word)

        else:
            current_word += branch.value
            for child in branch.children:
                candidates.append((child, current_word))

        # Cut off at three results
        if len(output) >= 4:
            return output

    return output

class TrieNode():
    """TrieNode Tree"""
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_to(self, node):
        node.children.append(self)

    def get_child(self, value):
        for node in self.children:
            if node.value == value:
                return node

    def __str__(self):
        return str(self.value) + \
         ''.join([i for i in self.children])

root = TrieNode('')

d = TrieNode('d')
d.add_to(root)

o = TrieNode('o')
o.add_to(d)

g = TrieNode('g')
g.add_to(o)

s = TrieNode('s')
s.add_to(g)

b = TrieNode('a')
b.add_to(d)

r = TrieNode('r')
r.add_to(b)

e = TrieNode('e')
e.add_to(r)

a = TrieNode(None)
a.add_to(g)
a.add_to(o)
a.add_to(s)
a.add_to(e)

print autocomplete('d', root)
