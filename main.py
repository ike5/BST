from Node import Node


class BST:
    def __init__(self):
        self.root = None



    def remove(self, key):
        parent = None
        current_node = self.root
        while current_node is not None:
            if current_node.key == key:
                if current_node.left is None and current_node.right is None:
                    # remove leaf
                    if parent is None:  # Node is root
                        self.root = None
                    elif parent.left == current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    return True  # node found and removed
                elif current_node.right is None:
                    # remove node with only left child
                    if parent is None:  # Node is root
                        self.root = current_node.left
                    elif parent.left == current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return True  # node found and removed
                elif current_node.left is None:
                    # remove node with only right child
                    if parent is None:  # node is root
                        self.root = current_node.right
                    elif parent.left == current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return True  # Node found and removed
                else:
                    # remove node with two children
                    # find successor (leftmost child of right subtree)
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left

                    # copy successor's key to current node
                    current_node.key = successor.key
                    parent = current_node

                    # reassign current node and key so that loop continues with new key
                    current_node = successor.right
                    key = successor.key

            elif current_node.key > key:
                # search right
                parent = current_node
                current_node = current_node.right
            else:
                # search left
                parent = current_node
                current_node = current_node.left
        return False  # node not found

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
