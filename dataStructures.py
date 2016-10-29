class Tree:
    class Node:
        """ Node class should not be used outside the context of a tree, so it is nested within the Tree class. """
        def __init__(self,data):
            """ Note that Node is aware of it's parent and it's children which will make traversing the tree easier. """
            self.data = data
            self.parent = None
            self.children = []

        def addChild(self,data):
            """ Appends child node with itself as the parent. """
            node = Tree.Node(data)
            node.parent = self
            self.children.append(node)

        def getChild(self,data):
            """ Returns child node requested, if present. """
            for child in self.children:
                if child.data == data:
                    return child
            return None

        def __repr__(self):
            """ Returns a string containing printable representation of our Node. """
            return self.data

    def __init__(self,data):
        """ Creates a tree. A node is set as the root."""
        self.root = self.Node(data)