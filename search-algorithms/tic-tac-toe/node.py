# Classe que representa o nó da árvore.
class Node:

    # Construtor.
    def __init__(self, depth=None, board=None, parent=None):
        self.depth = depth      # Profundidade do nó.
        self.data = board       # Valor do nó.
        self.parent = parent    # Pai do nó.
        self.weight = None      # Peso do nó.
        self.children = []      # Nós filhos do nó.

    # Método para adicionar um filho ao nó da árvore.
    def add_child(self, node):
        self.children.append(node)

    # Método que verifica os valores dos ancestrais dos nós. Utilizado para o corte alpha-beta.
    # Retorna verdadeiro se foi realizada a poda. Caso contrário, retorna falso.
    def ancestral(self, level):
        if level == 'max': # Se o nível do nó é max.
            current_parent = self.parent # Recuperando o pai do nó.
            while current_parent != None: # Percorre a árvore até que o current_parent atual seja a raiz.
                if current_parent.weight <= self.weight: # Realiza a poda se existir um ancestral min com peso menor ou igual que o do nó atual.
                    return True
                else: # Se o peso do ancestral for maior, continua subindo na árvore.
                    current_parent = current_parent.parent.parent
        elif level == 'min': # Se o nível do nó é min.
            current_parent = self.parent # Recuperando o pai do nó.
            while current_parent != None: # Percorre a árvore até que o current_parent atual seja a raiz.
                if current_parent.weight >= self.weight: # Realiza a poda se existir um ancestral max com peso maior ou igual que o do nó atual.
                    return True
                else: # Se o peso do ancestral for menor, continua subindo na árvore.
                    current_parent = current_parent.parent.parent
        return False

    # Método utilizado para printar a árvore.
    def print_tree(self):
        print('\t'*self.depth+f'{self.data} - Nível {self.depth}'+(f' - Peso {self.weight}' if self.weight!=None else '')+(f' - Pai {self.parent}' if self.parent!=None else ''))
        for child in self.children:
            child.print_tree()

    # Método que transforma um objeto do tipo Node em uma string.
    def __str__(self):
        return self.data

    # Método para realizar a operação de igualdade entre objetos do tipo Node.
    def __eq__(self, other):
        return self.weight == other

    # Método para realizar a operação de menor que entre objetos do tipo Node.
    def __lt__(self, other):
        return self.weight < other

    # Método para realizar a operação de maior que entre objetos do tipo Node.
    def __gt__(self, other):
        return self.weight > other