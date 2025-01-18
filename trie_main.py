from TrieNode import TrieNode


def trie_insert(root, string):
    node = root
    for char in string:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    if 0 not in node.children:
        node.children[0] = TrieNode()
    return node.children[0]


def print_trie(node, prefix=""):
    """Recursively print the trie structure."""
    for char, child_node in node.children.items():
        if char == 0:
            print(f"Word: {prefix}")  # End of a word
        else:
            print_trie(child_node, prefix + char)




trie_root = TrieNode()
trie_insert(trie_root, "hello")
trie_insert(trie_root, "hello there")
trie_insert(trie_root, "hello there world")
trie_insert(trie_root, "hell")
trie_insert(trie_root, "hell on earth")

# Print all words in the Trie
print_trie(trie_root)
