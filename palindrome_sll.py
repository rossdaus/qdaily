class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def setup_list(data):
    """Setup a linked list using itterable, data. Return head node"""
    prev = None
    for x in data:
        if not prev:
            prev = Node(x)
            head = prev
        else:
            node = Node(x)
            prev.next = node
            prev = node
    return head

def reverse_list(node):
    """Reverse linked list given a head node."""
    n = Node(node.data) # Create the tail node
    while node:
        if node.next:
            newhead = Node(node.next.data)
            newhead.next = n
            n = newhead
        node = node.next
    return newhead

def is_palindrome(ll):
    """Return whether linked list is a palindrome."""
    rl = reverse_list(ll)
    while rl:
        if rl.data != ll.data:
            return False
        rl, ll = rl.next, ll.next
    return True

goods = ("redder", "refer", "boob", "mam")
bads = ("banana", "defied", "minimum", "apple")

for word in goods + bads:
    ll = setup_list(word)
    answer = is_palindrome(ll)
    print(word, answer)
