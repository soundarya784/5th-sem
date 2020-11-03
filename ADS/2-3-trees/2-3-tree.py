class Node:
    def __init__(self, data, par=None):
        # print ("Node __init__: " + str(data))
        self.data = list([data])
        self.parent = par
        self.child = list()

    def __str__(self):
        if self.parent:
            return str(self.parent.data) + ' : ' + str(self.data)
        return 'Root : ' + str(self.data)

    def __lt__(self, node):
        return self.data[0] < node.data[0]

    def _isLeaf(self):
        return len(self.child) == 0

    # merge new_node sub-tree into self node
    def _add(self, new_node):
        # print ("Node _add: " + str(new_node.data) + ' to ' + str(self.data))
        for child in new_node.child:
            child.parent = self
        self.data.extend(new_node.data)
        self.data.sort()
        self.child.extend(new_node.child)
        if len(self.child) > 1:
            self.child.sort()
        if len(self.data) > 2:
            self._split()

    # find correct node to insert new node into tree
    def _insert(self, new_node):
        # print ('Node _insert: ' + str(new_node.data) + ' into ' + str(self.data))

        # leaf node - add data to leaf and rebalance tree
        if self._isLeaf():
            self._add(new_node)

        # not leaf - find correct child to descend, and do recursive insert
        elif new_node.data[0] > self.data[-1]:
            self.child[-1]._insert(new_node)
        else:
            for i in range(0, len(self.data)):
                if new_node.data[0] < self.data[i]:
                    self.child[i]._insert(new_node)
                    break

    # 3 items in node, split into new sub-tree and add to parent
    def _split(self):
        # print("Node _split: " + str(self.data))
        left_child = Node(self.data[0], self)
        right_child = Node(self.data[2], self)
        if self.child:
            self.child[0].parent = left_child
            self.child[1].parent = left_child
            self.child[2].parent = right_child
            self.child[3].parent = right_child
            left_child.child = [self.child[0], self.child[1]]
            right_child.child = [self.child[2], self.child[3]]

        self.child = [left_child]
        self.child.append(right_child)
        self.data = [self.data[1]]

        # now have new sub-tree, self. need to add self to its parent node
        if self.parent:
            if self in self.parent.child:
                self.parent.child.remove(self)
            self.parent._add(self)
        else:
            left_child.parent = self
            right_child.parent = self

    # find an item in the tree; return item, or False if not found
    def _find(self, item):
        # print ("Find " + str(item))
        if item in self.data:
            return self
        elif self._isLeaf():
            return False
        elif item > self.data[-1]:
            return self.child[-1]._find(item)
        else:
            for i in range(len(self.data)):
                if item < self.data[i]:
                    return self.child[i]._find(item)

    # def _finditem(self, item):
    #     # print ("Find " + str(item))
    #     if item in self.data:
    #         return item
    #     elif self._isLeaf():
    #         return False
    #     elif item > self.data[-1]:
    #         return self.child[-1]._find(item)
    #     else:
    #         for i in range(len(self.data)):
    #             if item < self.data[i]:
    #                 return self.child[i]._find(item)

    # print preorder traversal
    def _preorder(self):
        print(self)
        for child in self.child:
            if child != None:
                child._preorder()

    def _delete(self, element):

        pos = self._find(element)
        if pos == False:
            return
        if pos._isLeaf():
            pos.data.remove(element)

        elif len(pos.data) == 1:
            if len(pos.child) == 2 and pos.child[1] == None:
                val = pos.child[0].data
                pos.child[0] = None
                pos.data.extend(val)
                pos.data.remove(element)
                return


            elif len(pos.child) == 2 and pos.child[1] != None:
                val = pos.child[1].data
                pos.data.remove(element)
                pos.data.extend(val)
                pos.child[1] = None
                print()



class Tree:
    def __init__(self):
        print("Tree __init__")
        self.root = None

    def insert(self, item):
        print("Tree insert: " + str(item))
        if self.root is None:
            self.root = Node(item)
        else:
            self.root._insert(Node(item))
            while self.root.parent:
                self.root = self.root.parent
        return True

    def find(self, item):
        return self.root._find(item)

    def remove(self, item):
        self.root.remove(item)

    def delete(self, element):
        self.root._delete(element)

    def preorder(self):
        self.root._preorder()


tree = Tree()

lst = [13, 24, 15,16,100,5]
for item in lst:
    tree.insert(item)

tree.preorder()
# print("after deletion:")
# tree.preorder()
# tree.delete(15)
# print("after deletion:")
# tree.preorder()
# tree.delete(24)
# print("after deletion:")
# tree.preorder()
