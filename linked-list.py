class Linked_List:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

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


llist1 = Linked_List()
# print(llist1)

first_node = Node('a')
llist1.head = first_node
# print(llist1)

second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
# print(llist1)

llist2 = Linked_List(['a', 'b', 'c', 'd', 'e'])
print(llist2)

for node in llist2:
    print(node)
