class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list:

    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next

        cur.next = new_node
        new_node.prev = cur


    def length(self):
        cur = self.head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count

    def get(self, index):
        if index >= self.length():
            print('Error')
            return "hello"

        cur_index = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur_index == index:
                return cur.data
            cur_index += 1

    def erase(self, key):
        cur = self.head

        while cur:
            if cur == self.head and cur.data == key:
                #case 1: when next is none and is the head
                if cur.next == None:
                    cur = None
                    self.head = None
                    return
                #case#2 when it is the head and next is a new node
                else:
                    next = cur.next
                    next.prev = None
                    cur.next = None
                    cur = None
                    self.head = next

            elif cur.data == key:
                next = cur.next
                prev = cur.prev
                prev.next = next
                next.prev = prev
                cur = None
                cur.next = None
                cur.prev = None
                return
            else:
                prev = cur.prev
                prev.next = None
                cur = None
                cur.prev = None
                return

            cur = cur.next


    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


# ----------------------- MAIN --------------------#

dlist = doubly_linked_list()

dlist.append(1)
dlist.append(2)
dlist.append(3)

dlist.print()

dlist.erase(3)

print('-------------')
dlist.print()
