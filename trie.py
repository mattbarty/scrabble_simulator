DICTIONARY = "valid_words.txt"


class Node:
    id = 0

    def __init__(self, char) -> None:
        self.id = Node.id
        Node.id += 1

        self.terminal_node = False
        self.parent = '*'
        self.char = char
        self.children = {}
        self.pos = 0

    def __repr__(self) -> str:
        return f'({self.id} {self.char})'


def add_node(trie, word):

    curr_node = trie
    previous_node = None

    for i, char in enumerate(word):
        if char in curr_node.children:
            previous_node = curr_node
            curr_node = curr_node.children[char]
        else:
            curr_node.children[char] = Node(char)
            curr_node.parent = previous_node
            previous_node = curr_node
            curr_node.pos = i
            curr_node = curr_node.children[char]

    curr_node.children['$'] = Node('$')
    curr_node.parent = previous_node
    terminal_node = curr_node.children['$']
    terminal_node.parent = previous_node
    terminal_node.terminal_node = True


def create_trie(dictionary):
    trie = Node('*')

    with open(dictionary, 'r') as file:
        lexicon = file.read().split('\n')

    for word in sorted(lexicon):
        add_node(trie, word)

    return trie