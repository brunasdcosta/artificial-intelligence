# Classe que representa o nó da árvore.
class Node:

    # Construtor.
    def __init__(self, depth=None, data=None, parent=None):
        self.depth = depth
        self.data = data
        self.parent = parent
        self.children = []

    # Método para adicionar um filho ao nó da árvore.
    def add_child(self, node):
        self.children.append(node)