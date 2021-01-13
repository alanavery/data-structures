class Queue:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=(nodes.pop(0)))
            self.head = node
            for element in nodes:
                node.next = Node(data=(element))
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def enqueue(self, node):
        if not self.head:
            self.head = node
        else:
            for current_node in self:
                pass
            current_node.next = node

    def dequeue(self):
        if not self.head:
            print('The list is empty.')
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


stack1 = Queue(['a', 'b', 'c', 'd', 'e', 'f'])
# stack1 = Queue(['a'])
# stack1 = Queue()
print(stack1)
stack1.enqueue(Node('g'))
print(stack1)
stack1.enqueue(Node('h'))
print(stack1)
stack1.dequeue()
print(stack1)
stack1.dequeue()
print(stack1)
stack1.dequeue()
print(stack1)
