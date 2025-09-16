class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def create_linked_list(values):
    head = Node()
    current = head
    for value in values:
        current.next = Node(value)
        current = current.next
    return head


def find_common_elements(A, B):
    C = Node()
    current_c = C
    pa = A.next
    pb = B.next
    while pa is not None and pb is not None:
        if pa.data == pb.data:
            current_c.next = Node(pa.data)
            current_c = current_c.next
            pa = pa.next
            pb = pb.next
        elif pa.data < pb.data:
            pa = pa.next
        else:
            pb = pb.next
    return C