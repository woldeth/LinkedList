class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next

        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elms = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elms.append(cur_node.data)
        print(elms)

    def get(self,index):
        if index >= self.length():
            print("Error")
            return None
        cur_index = 0
        cur_node = self.head

        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1

    def erase(self, index):
        if index >= self.length():
            print('Error')
            return None
        cur_index = 0
        cur_node = self.head

        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1


def reverse_print(x: Node) -> None:
    cur_node = x
    elems = []
    while cur_node != None:
        elems.append(cur_node.data)
        cur_node = cur_node.next

    for item in elems[::-1]:
        print(item)

def reverse(x: Node) -> Node:
    cur_node = x
    elems = []
    while cur_node != None:
        elems.append(cur_node.data)
        cur_node = cur_node.next

    elems = elems[::-1]

    head = x
    cur_node = x
    for item in elems:
        cur_node.data = item
        print(cur_node, cur_node.data)
        cur_node = cur_node.next

    return head






    # def append(self, data):
    #     new_node = Node(data)
    #     cur = self.head
    #     while cur.next != None:
    #         cur = cur.next
    #
    #     cur.next = new_node








my_list = linked_list()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)


reverse_print(my_list.head)
print(reverse(my_list.head))















































