from Node import Node


class BST:
    def __init__(self):
        self.root = None



    def print_in_order(self, node):
        if node is None:
            return
        self.print_in_order(node.left)
        print(node)
        self.print_in_order(node.right)

    def get_height(self, node):
        if node is None:
            return -1
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return 1 + max(left_height, right_height)

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
