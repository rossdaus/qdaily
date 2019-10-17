class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.prev = None
            self.head = newNode
        else:
            newNode = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
            newNode.prev = cur
            newNode.next = None


def setup_list(data):
    """Setup a double linked list using itterable, data."""
    dll = DoubleLinkedList()
    for x in data:
        dll.append(x)
    return dll

def is_palindrome(dll):
    # find the tail
    node = dll.head
    while node.next:
        node = node.next
    tailnode = node

    # compare each end, up to the centre
    a, b = dll.head, tailnode
    while a.data == b.data:
        print("matches: ", a.data, b.data)
        a_prev = a # in case of even length list
        a, b = a.next, b.prev
        if a is b or a_prev is b:
            # We have reached the middle
            return True if a.data == b.data else False
    print("mismatch: ", a.data, b.data)
    return False


goods = ("redder", "refer", "boob", "mam")
bads = ("banana", "defied", "minimum", "apple")

for x in goods + bads:
    dll = setup_list(x)
    answer = is_palindrome(dll)
    print("---------->", x, answer)
