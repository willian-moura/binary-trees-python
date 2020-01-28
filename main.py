
class Tree:
    def __init__(self, key):
        self.E = None
        self.D = None
        self.key = key
        self.count = 1

    def insert(self, k):
        if self.key:
            if self.key < k:
                if self.D is None:
                    self.D = Tree(k)
                else:
                    self.D.insert(k)
            elif k < self.key:
                if self.E is None:
                    self.E = Tree(k)
                else:
                    self.E.insert(k)
            elif self.key == k:
                self.count += 1
        else:
            self.key = k


def show_erd(tree):
    if tree:
        show_erd(tree.E)
        print("%d " % tree.key)
        show_erd(tree.D)
    else:
        return


def show_edr(tree):
    if tree:
        show_erd(tree.E)
        show_erd(tree.D)
        print("%d " % tree.key)
    else:
        return


def show_red(tree):
    if tree:
        print("%d " % tree.key)
        show_erd(tree.E)
        show_erd(tree.D)
    else:
        return


t = Tree(5)
t.insert(3)
t.insert(1)
t.insert(2)
t.insert(4)

print("EDR")
show_edr(t)
print("ERD")
show_erd(t)
print("RED")
show_red(t)

