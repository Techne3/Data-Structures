from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('./queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        # compare root node, if greater or equal go right
        if value >= self.value:
            # if no child
            if self.right == None:
                # insert
                self.right = BinarySearchTree(value)
            # else try again, continue right
            else:
                return self.right.insert(value)
        # if lesser go left
        elif value < self.value:
            # if no child
            if self.left == None:
                # insert
                self.left = BinarySearchTree(value)
            # else try again, continue left
            else:
                return self.left.insert(value)

    # else try again and repeat to left

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
    # def contains(self, target):
    #     if self.value == target:
    #         return True
    #         elif target < self.value:
    #             if self.left is None:
    #                 return False
    #             else:
    #                 return self.left.contains(target)
    #         else:
    #             if self.right is None:
    #                 return False
    #         else:
    #             return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right is not None:
            self = self.right
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # print(self.value);
        cb(self.value)
        if self.left is not None and self.right is not None:
            return self.left.for_each(cb), self.right.for_each(cb)
        elif self.right is not None:
            return self.right.for_each(cb)
        elif self.left is not None:
            return self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
