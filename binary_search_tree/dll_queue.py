from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list.py')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Each element has a reference to both the next and the previous element.
        self.storage = DoublyLinkedList()

    # enqueue -> Adds an item to the queue. If the queue is full, then it is said to
    # be an Overflow condition
    # adding so set the size to += 1

    def enqueue(self, value):
        self.size += 1

        return self.storage.add_to_tail(value)

    # dequeue  ->  removes the item from the queue.
    # use the remove_from_head from doubly_linked_list

    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
