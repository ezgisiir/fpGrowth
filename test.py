class TreeNode:
    def __init__(self, value, freq, parent):
        self.value = value
        self.freq = freq
        self.parent = parent
        self.next = None


class Tree:

    def __init__(self):
        self.root = TreeNode(None, None, None)

    def count(self):
        count = 1
        node = self.root
        while node.next is not None:
            count = count + 1
            node = node.next
        return count

    def add(self, tree_node):
        node = self.root
        next_node = node.next
        while next_node is not None:
            node = next_node
            next_node = node.next
        node.next = tree_node


tree = Tree()

print(tree.count())
