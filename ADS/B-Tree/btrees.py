class Btreenode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.child = []
        self.keys = []
        self.par = None


class btree:
    def __init__(self, t):
        self.root = Btreenode(True)
        self.t = t

    def insert_key(self, val, root):

        if len(root.keys) == (2 * self.t) - 1:
            if self.root.leaf and root.par is None:
                self.root = self.split(root)

            else:
                temp = self.split(root)
                temp.par.keys.append(temp.keys[0])
                idx = len(self.root.keys)-1
                parent = temp.par
                parent.child[idx].par = None
                parent.child[idx].keys=temp.child[0].keys
                parent.child.append(Btreenode(True))
                parent.child[idx+1].keys = temp.child[idx].keys
                return parent.child[2]
        else:
            self.insert_non_full(val, root)
            return root

    def insert_non_full(self, val, root):

        if root.leaf:
            root.keys.append(val)
            root.keys.sort()
        else:
            if val > root.keys[-1]:
                root.child[-1] = self.insert_key(val, root.child[-1])
            elif val < root.keys[0]:
                self.insert_key(val, root.child[0])
            else:
                for i, j in enumerate(root.keys):
                    if val < j:
                        self.insert_key(val, root.child[j - 1])

    def split(self, root):
        if root.leaf:
            n = len(root.keys) // 2
            temp = Btreenode()
            temp.keys.append(root.keys[n])
            temp.child = [None] * 2
            temp.child[0] = Btreenode(True)
            temp.child[1] = Btreenode(True)
            temp.child[0].par = temp
            temp.child[1].par = temp
            temp.par = root.par
            for j, i in enumerate(root.keys):
                if j == n:
                    break
                temp.child[0].keys.append(i)

            for i in range(n + 1, len(root.keys)):
                temp.child[1].keys.append(root.keys[i])

            return temp
    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

B = btree(3)
B.insert_key(6, B.root)
B.insert_key(11, B.root)
B.insert_key(7, B.root)
B.insert_key(8, B.root)
B.insert_key(1, B.root)
B.insert_key(5, B.root)
B.insert_key(13, B.root)
B.insert_key(9, B.root)
B.insert_key(10, B.root)
B.insert_key(14, B.root)
B.insert_key(12, B.root)
B.insert_key(4, B.root)
B.insert_key(3, B.root)
B.insert_key(2, B.root)
B.print_tree(B.root)