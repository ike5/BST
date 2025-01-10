import copy
import random
from Node import Node

root = None


def search(root, key):
    current_node = root
    while current_node is not None:
        if key == current_node.key:
            return current_node  # found
        elif key < current_node.key:
            current_node = current_node.left
        else:
            current_node = current_node.right
    return None  # Not found


def insert(root, node):
    if root is None:
        root = node
    else:
        current_node = root
        while current_node is not None:
            if node.key < current_node.key:
                if current_node.left is None:
                    current_node.left = node
                    current_node = None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = node
                    current_node = None
                else:
                    current_node = current_node.right


def remove(root, key):
    parent = None
    current_node = root
    while current_node is not None:
        if current_node.key == key:
            if current_node.left is None and current_node.right is None:
                # remove leaf
                if parent is None:  # Node is root
                    root = None
                elif parent.left == current_node:
                    parent.left = None
                else:
                    parent.right = None
                return True  # node found and removed
            elif current_node.right is None:
                # remove node with only left child
                if parent is None:  # Node is root
                    root = current_node.left
                elif parent.left == current_node:
                    parent.left = current_node.left
                else:
                    parent.right = current_node.left
                return True  # node found and removed
            elif current_node.left is None:
                # remove node with only right child
                if parent is None:  # node is root
                    root = current_node.right
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


def print_in_order(node):
    if node is None:
        return
    print_in_order(node.left)
    print(node.key)
    print_in_order(node.right)


def get_height(node):
    if node is None:
        return -1
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    return 1 + max(left_height, right_height)


"""
BST Insert algorithm for BST with nodes containing parent pointers
"""


def bst_insert(root, node):
    if root is None:
        root = node
        node.parent = None
        return

    cur = root
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


def bst_replace_child(parent, current_child, new_child):
    if parent.left != current_child and parent.right != current_child:
        return False

    if parent.left == current_child:
        parent.left = new_child
    else:
        parent.right = new_child

    if new_child is not None:
        new_child.parent = parent

    return True


def bst_remove_key(tree, key):
    node = bst_search(tree, key)
    bst_remove_node(tree, node)


def bst_remove_node(tree, node: Node):
    if node is None:
        return

    # case 1: Internal node with 2 children
    if node.left is not None and node.right is not None:
        # find successor
        successor_node = node.right
        while successor_node.left is not None:
            successor_node = successor_node.left
        # copy value/data from successor_node to node
        node = copy.copy(successor_node)

        # recursively remove successor_node
        bst_remove_node(tree, successor_node)

    # case 2: root node with 1 or 0 children
    elif node == tree.root:
        if node.left is not None:
            tree.root = node.left
        else:
            tree.root = node.right
        # make sure the new root if non-null has a null parent
        if tree.root is not None:
            tree.root.parent = None
    # case 3: Internal with left child only
    elif node.left is not None:
        bst_replace_child(node.parent, node, node.left)
    # case 4: Internal with right child only or leaf
    else:
        bst_replace_child(node.parent, node, node.right)


def bst_search(tree, key):
    return bst_search_recursive(tree.root, key)


def bst_search_recursive(node: Node, key):
    if node is not None:
        if key == node.key:
            return node
        elif key < node.key:
            return bst_search_recursive(node.left, key)
        else:
            return bst_search_recursive(node.right, key)
    return None
