from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list.py')


class LRUCache:

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = {}
        self.order = DoublyLinkedList()

    def get(self, key):
        # If key is in storage
        if key in self.storage:
            # Move it to the end
            node = self.storage[key]
            self.order.move_to_end(node)
            # return the value
            return node.value[1]
        # If key is NOT in storage
        else:
            return None

    def set(self, key):
        # check and see if the key is in the dict
        if key in self.storage:
            # If it is
            node = self.storage[key]
            # overwrite the value
            node.value = (key, value)
            # move it to the end
            self.order.move_to_end(node)
            # nothing else to do so exit function
            return
        # If  it isn't
        # check if the cache is full
        if self.size == self.limit:
            # if cache is full
            # remove the oldest entry from dictionary
            del self.storage[self.order.head.value[0]]
            # and LL
            self.order.remove_from_head()
        # Reduce the size
            self.size -= 1
        # Add to the linked list (key and value)
        self.order.add_to_tail((key, value))
        # Add the key and value to the dictionary
        self.storage[key] = self.order.tail
        # Increment size
        self.size += 1
