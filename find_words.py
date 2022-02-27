import trie

DICTIONARY = "valid_words.txt"

trie = trie.create_trie(DICTIONARY)


def find_anchor_nodes(trie: trie.Node, anchor: str) -> list:
    anchor_nodes = []  # -- Collects Nodes

    def traverse(trie=trie, anchor: str = anchor):
        curr_node = trie
        for child in curr_node.children:
            if child == anchor:
                anchor_nodes.append(curr_node.children[child])
            if curr_node.children[child].terminal_node == False:
                traverse(curr_node.children[child], anchor)

    traverse(trie, anchor)  # -- Traverse trie and populate anchor_nodes

    return anchor_nodes


def search_prefix(node: trie.Node, rack: list) -> str:
    if node.id == 0:
        return '*'  # -- Mark return as being a complete prefix
    else:
        for letter in rack:
            if letter == node.parent.char or node.parent.id == 0:
                new_rack = rack.copy()
                new_rack.remove(letter)
                char = node.char
                return search_prefix(node.parent, new_rack) + char
        return '_'  # -- Mark return as being an incomplete prefix


if __name__ == '__main__':
    pass