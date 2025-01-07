from Node import Node


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
            return

        cur = self.root
        while cur is not None:
            if node.key < cur.key:
                if cur.left is None:
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right


if __name__ == "__main__":
    pass
