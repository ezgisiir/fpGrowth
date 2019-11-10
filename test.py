class TreeNode:
    def __init__(self, value, freq, parent):
        self.value = value
        self.freq = freq
        self.parent = parent
        self.next = []


def add_child_to_parent(parent, value):
    word_node = TreeNode(value, 1, parent)
    parent.next.append(word_node)
    return word_node


class Tree:

    def __init__(self):
        self.root = TreeNode(None, None, None)

    def add_words(self, words_to_add):
        node = self.root
        children = node.next

        for word in words_to_add:
            matching_node = None
            if children is None or len(children) == 0:
                matching_node = add_child_to_parent(node, word)
            else:
                child_found = False
                for child in children:
                    if child.value == word:
                        matching_node = child
                        child.freq = child.freq + 1
                        child_found = True

                if not child_found:
                    matching_node = add_child_to_parent(node, word)

            node = matching_node
            children = node.next


tree = Tree()

words = ['K', 'E', 'M', 'O', 'Y']
tree.add_words(words)

words = ['K', 'E', 'O', 'Y']
tree.add_words(words)

words = ['K', 'E', 'M']
tree.add_words(words)

words = ['K', 'M', 'Y']
tree.add_words(words)

words = ['K', 'E', 'O']
tree.add_words(words)


print('Gokhan')
