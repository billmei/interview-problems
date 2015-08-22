#!/usr/bin/env python

import random

class Node():
    def __init__(self):
        self.val = 'Node'
        self.left = None
        self.right = None


    def has_available_children(self):
        return self.left is None or self.right is None

    def random_child(self):
        """
        Pick a random child node
        If there's only one child slot available, default to that one.
        Otherwise, randomly pick one of the two
        """
        if self.left is not None and self.right is None:
            return 'right'
        elif self.left is None and self.right is not None:
            return 'left'
        else:
            choice = random.randint(0, 1)
            if choice == 0:
                return 'left'
            else:
                return 'right'

class BinaryTree(object):
    """docstring for BinaryTree"""
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.root = None

    def generate(self):
        """
        Generates a random binary tree
        """
        
        nodes_inserted = 0

        self.root = Node()
        nodes_inserted += 1

        # TODO: num_nodes == 1?
        # TODO: num_nodes < 1?

        current_node = self.root

        while nodes_inserted < self.num_nodes:
            if not current_node.has_available_children():
                # go into a random choice of either left or right
                current_node = current_node.random_child()
            else:
                # TODO: Refactor the Node class so that you don't need to pass
                #       a string reference to getattr
                child = getattr(current_node, current_node.random_child())
                child = Node()
                nodes_inserted += 1
                current_node = self.root

        return self.root

    # def __str__(self):
    #     current_node = self.root
    #     result = []



    #     while current_node is not None:
    #         result.append(current_node.val)

b_tree = BinaryTree(10)





