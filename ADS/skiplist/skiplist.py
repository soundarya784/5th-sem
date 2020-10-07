import random


class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)


class skipList:
    def __init__(self, max_lvl):
        self.max_lvl = max_lvl
        self.level = 0
        self.head = self.create_node(self.max_lvl, -1)

    def create_node(self, key, lvl):
        new_node = Node(lvl, key)
        return new_node

    def insert_node(self, key):
        update = [None] * (self.max_lvl + 1)
        cur = self.head

        for i in range(self.level, -1, -1):
            while cur.forward[i] and cur.forward[i].key < key:
                cur = cur.forward[i]
            update[i] = cur

        ran_level = random.randint(0, self.max_lvl - 1)
        if ran_level > self.level:
            self.level = ran_level

        new_node = self.create_node(ran_level, key)

        for i in range(ran_level + 1):
            if update[i] == None:
                new_node.forward[i] = None
            else:
                new_node.forward[i] = update[i].forward[i]
            if update[i] == None:
                update[i] = None
            else:
                update[i].forward[i] = new_node

            print(f"inserted a node with {key}")

    def displayList(self):
        temp = self.head
        for i in range(self.level + 1):
            cur = self.head.forward[i]
            print(f"level {i}")
            while cur != None:
                print(cur.key)
                cur = cur.forward[i]

    def deleteElement(self, search_key):

        update = [None] * (self.max_lvl + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while (current.forward[i] and current.forward[i].key < search_key):
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current != None and current.key == search_key:

            for i in range(self.level + 1):

                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while (self.level > 0 and \
                   self.head.forward[self.level] == None):
                self.level -= 1
            print("Successfully deleted {}".format(search_key))

    def searchElement(self, key):
        current = self.head
        for i in range(self.level, -1, -1):
            while (current.forward[i] and
                   current.forward[i].key < key):
                current = current.forward[i]

        current = current.forward[0]
        if current and current.key == key:
            print("Found key ", key)


li = skipList(2)
li.insert_node(3)
li.insert_node(4)
li.insert_node(10)
li.insert_node(2)
li.displayList()
li.deleteElement(3)
li.displayList()
li.searchElement(2)
