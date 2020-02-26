class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

    def find_middle(self):
        middle = self
        end = self
        while end != None:
            end = end.next
            if end:
                end = end.next
                middle = middle.next
        print("Middle is: " + str(middle.value))


root = Node(3)
cur = root
cur.add(4)
cur = cur.next
cur.add(5)
cur = cur.next
cur.add(6)
cur = cur.next

cur.find_middle()
