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


class ConditionalPatternBase:

    def __init__(self, freq, list_of_word):
        self.freq = freq
        self.words = list_of_word
        self.word_set = frozenset(list_of_word)

    def get_size(self):
        return len(self.words)

    def contains(self, word):
        return word in self.word_set


class Tree:

    def __init__(self):
        self.root = TreeNode(None, None, None)
        self.word_nodes = dict()

    def add_words(self, words_to_add):
        node = self.root
        children = node.next

        for word in words_to_add:
            matching_node = None
            if word not in self.word_nodes:
                self.word_nodes[word] = []
            if children is None or len(children) == 0:
                matching_node = add_child_to_parent(node, word)
                self.word_nodes[word].append(matching_node)
            else:
                child_found = False
                for child in children:
                    if child.value == word:
                        matching_node = child
                        child.freq = child.freq + 1
                        child_found = True

                if not child_found:
                    matching_node = add_child_to_parent(node, word)
                    self.word_nodes[word].append(matching_node)

            node = matching_node
            children = node.next

    def get_conditional_pattern_base(self, word_sample):
        conditional_pattern_base_list = []
        word_nodes = self.word_nodes[word_sample]

        for node in word_nodes:
            freq = node.freq
            parent_words = []

            parent = node.parent
            while parent is not None:
                if parent.value is not None:
                    parent_words.append(parent.value)
                parent = parent.parent

            conditional_pattern_base_list.append(ConditionalPatternBase(freq, parent_words))

        return conditional_pattern_base_list


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

conditional_pattern_list = tree.get_conditional_pattern_base('O')
print('Gokhan')
