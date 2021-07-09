# Classe que representa o nó da árvore.
class Node:

    # Construtor.
    def __init__(self, depth, board):
        self.data = board
        self.children = []
        self.depth = depth

    # Método para adicionar um filho ao nó da árvore.
    def add_child(self, node):
        self.children.append(node)