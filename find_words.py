import trie

DICTIONARY = "valid_words.txt"

trie = trie.create_trie(DICTIONARY)


def find_anchor_nodes(trie, anchor: str) -> list:
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


if __name__ == '__main__':
    pass