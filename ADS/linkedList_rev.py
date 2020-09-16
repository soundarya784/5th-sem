'''
Reverses k nodes of a linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next1 = None


class LinkedList:
    def __init__(self):
        self.head = None
        
#inserting
    def insert_val(self):
        return int(input("enter value to be inserted"))

    def insert_front(self):
        val = self.insert_val()
        if self.head is None:
            self.head = Node(val)
            return

        new_node = Node(val)
        new_node.next1 = self.head
        self.head = new_node



    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end="")
            temp = temp.next1
        print()
    def k_rev(self,head, k):
        prev = None
        cur = head
        next = None
        count = 0
        while(cur is not None and count < k):
            next = cur.next1
            cur.next1 = prev
            prev = cur
            cur = next
            count += 1

        if next is not None:
            head.next1 = self.k_rev(next, k)

        return prev



if __name__ == "__main__":

    llist = LinkedList()
    i = 1
    while i <= 5:
        llist.insert_front()
        i+=1
        
    llist.print_list()
    llist.head = llist.k_rev(llist.head,3)
    llist.print_list()



