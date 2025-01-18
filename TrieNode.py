class TrieNode:
    def __init__(self):
        # dictionary to store children nodes
        self.children = {}
        # boolean to indicate end of a word
        self.is_end_of_word = False
