from random import choice
from copy import deepcopy # Função que realiza uma cópia de um objeto para um objeto diferente/independente.

# Classe que representa o tabuleiro do jogo dos 8 números.
class GameBoard:

    # Construtor.
    def __init__(self): 
        self.matrix = [[None for j in range(3)] for i in range(3)] # Criando uma matrix de ordem 3.

    # Gera um jogo aleatório.
    def randomize(self):
        values = [None, 1, 2, 3, 4, 5, 6, 7, 8] # Array de possíveis valores para o tabuleiro do jogo.
        for i in range(3):
            for j in range(3):
                value = choice(values) # Escolhe aleatoriamente um valor do array 'values'.
                self.matrix[i][j] = value
                values.remove(value) # Remove o valor escolhida para que ele não possa ser aleatorizado mais de uma vez.

    # Set da matriz que representa o tabuleiro do jogo.
    def set_board(self, matrix):
        self.matrix = matrix

    # Método para mover uma célula da matriz para cima.
    # Retorna verdadeiro se, e somente se, o deslocamento foi realizado com sucesso.
    def move_up(self, i, j):
        # Aqui precisamos verificar se há espaço para cima, ou seja, o valor de i>=1. Caso contrário, iríamos acessar um índice fora do limite.
        # Também temos que analisar se o valor da célula que queremos mover para é 'None' - um espaço vazio. Senão, a jogada não é válida.
        if i-1 > -1 and self.matrix[i-1][j] == None:
            self.matrix[i-1][j] = self.matrix[i][j]
            self.matrix[i][j] = None
            return True
        return False

    # Método para mover uma célula da matriz para baixo.
    # Retorna verdadeiro se, e somente se, o deslocamento foi realizado com sucesso.
    def move_down(self, i, j):
        # Aqui precisamos verificar se há espaço para baixo, ou seja, o valor de i<=1. Caso contrário, iríamos acessar um índice fora do limite.
        # Também temos que analisar se o valor da célula que queremos mover para é 'None' - um espaço vazio. Senão, a jogada não é válida.
        if i+1 < 3 and self.matrix[i+1][j] == None:
            self.matrix[i+1][j] = self.matrix[i][j]
            self.matrix[i][j] = None
            return True
        return False

    # Método para mover uma célula da matriz para a esquerda.
    # Retorna verdadeiro se, e somente se, o deslocamento foi realizado com sucesso.
    def move_left(self, i, j):
        # Aqui precisamos verificar se há espaço para a esquerda, ou seja, o valor de j>=1. Caso contrário, iríamos acessar um índice fora do limite.
        # Também temos que analisar se o valor da célula que queremos mover para é 'None' - um espaço vazio. Senão, a jogada não é válida.
        if j-1 > -1 and self.matrix[i][j-1] == None:
            self.matrix[i][j-1] = self.matrix[i][j]
            self.matrix[i][j] = None
            return True
        return False

    # Método para mover uma célula da matriz para a direita.
    # Retorna verdadeiro se, e somente se, o deslocamento foi realizado com sucesso.
    def move_right(self, i, j):
        # Aqui precisamos verificar se há espaço para baixo, ou seja, o valor de j<=1. Caso contrário, iríamos acessar um índice fora do limite.
        # Também temos que analisar se o valor da célula que queremos mover para é 'None' - um espaço vazio. Senão, a jogada não é válida.
        if j+1 < 3 and self.matrix[i][j+1] == None:
            self.matrix[i][j+1] = self.matrix[i][j]
            self.matrix[i][j] = None
            return True
        return False

    # Método que retorna um array com os índices da posição vazia, demarcada como 'None', na matriz que representa o tabuleiro do jogo.
    # Caso ela não seja encontrada, o retorno será nulo - 'None'.
    def find_none_index(self):
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == None:
                    return [i, j] # [linha, coluna]
        return None

    # Método que retorna um array com as n possibilidades de jogadas a partir do estado atual do jogo, onde n = 2, 3, 4.
    def find_children(self):
        index = self.find_none_index() # Encontrando a posição vazia atual. A partir dela que saberemos quais células podemos mover.
        i = index[0] # Índice da linha da posição vazia.
        j = index[1] # Índice da coluna da posição vazia.
        if i == 0: # Se estamos na primeira linha e...
            if j == 0: # na primeira coluna, então vamos ter duas opções para a próxima jogada:
                child1 = deepcopy(self) # Criando uma cópia independente do tabuleiro atual.
                child1.move_up(1, 0) # - Mover a célula de linha 1 e coluna 0 para cima.
                child2 = deepcopy(self) # Criando outra cópia independente do tabuleiro atual.
                child2.move_left(0, 1) # - Mover a célula de linha 0 e coluna 1 para a esquerda.
                return [child1, child2]
            elif j == 1: # na segunda coluna, então vamos ter três opções para a próxima jogada:
                child1 = deepcopy(self)
                child1.move_right(0, 0) # - Mover a célula de linha 0 e coluna 0 para a direita.
                child2 = deepcopy(self)
                child2.move_up(1, 1) # - Mover a célula de linha 1 e coluna 1 para cima.
                child3 = deepcopy(self)
                child3.move_left(0, 2) # - Mover a célula de linha 0 e coluna 2 para a esquerda.
                return [child1, child2, child3]
            elif j == 2: # na terceira coluna, então vamos ter duas opções para a próxima jogada:
                child1 = deepcopy(self)
                child1.move_right(0, 1) # - Mover a célula de linha 0 e coluna 1 para a direita.
                child2 = deepcopy(self)
                child2.move_up(1, 2) # - Mover a célula de linha 1 e coluna 2 para cima.
                return [child1, child2]
        elif i == 1: # Se estamos na segunda linha e...
            if j == 0: # na primeira coluna, então vamos ter três opções para a próxima jogada:
                child1 = deepcopy(self)
                child1.move_down(0, 0) # - Mover a célula de linha 0 e coluna 0 para baixo.
                child2 = deepcopy(self)
                child2.move_up(2, 0) # - Mover a célula de linha 2 e coluna 0 para cima.
                child3 = deepcopy(self)
                child3.move_left(1, 1) # - Mover a célula de linha 1 e coluna 1 para a esquerda.
                return [child1, child2, child3]
            elif j == 1: # na segunda coluna, então vamos ter quatro opções para a próxima jogada:
                child1 = deepcopy(self)
                child1.move_right(1, 0) # - Mover a célula de linha 1 e coluna 0 para a direita.
                child2 = deepcopy(self)
                child2.move_down(0, 1) # - Mover a célula de linha 0 e coluna 1 para baixo.
                child3 = deepcopy(self)
                child3.move_up(2, 1) # - Mover a célula de linha 2 e coluna 1 para cima.
                child4 = deepcopy(self)
                child4.move_left(1, 2) # - Mover a célula de linha 1 e coluna 2 para a esquerda.
                return [child1, child2, child3, child4]
            elif j == 2: # na terceira coluna, então vamos ter três opções para a próxima jogada:
                child1 = deepcopy(self)
                child1.move_down(0, 2) # - Mover a célula de linha 0 e coluna 2 para baixo.
                child2 = deepcopy(self)
                child2.move_right(1, 1) # - Mover a célula de linha 1 e coluna 1 para a direita.
                child3 = deepcopy(self)
                child3.move_up(2, 2) # - Mover a célula de linha 2 e coluna 2 para cima.
                return [child1, child2, child3]
        elif i == 2: # Se estamos na terceira linha e...
            if j == 0: # na primeira coluna, então vamos ter duas opções para a próxima jogada:
                child1 = deepcopy(self)
                child1.move_down(1, 0) # - Mover a célula de linha 1 e coluna 0 para baixo.
                child2 = deepcopy(self)
                child2.move_left(2, 1) # - Mover a célula de linha 2 e coluna 1 para a esquerda.
                return [child1, child2]
            elif j == 1: # na segunda coluna, então vamos ter três opções para a próxima jogada:
                child1 = deepcopy(self)
                child1.move_right(2, 0) # - Mover a célula de linha 2 e coluna 0 para a direita.
                child2 = deepcopy(self)
                child2.move_down(1, 1) # - Mover a célula de linha 1 e coluna 1 para baixo.
                child3 = deepcopy(self)
                child3.move_left(2, 2) # - Mover a célula de linha 2 e coluna 2 para a esquerda.
                return [child1, child2, child3]
            elif j == 2: # na terceira coluna, então vamos ter duas opções para a próxima jogada:
                child1 = deepcopy(self)
                child1.move_right(2, 1) # - Mover a célula de linha 2 e coluna 1 para a direita.
                child2 = deepcopy(self)
                child2.move_down(1, 2) # - Mover a célula de linha 1 e coluna 2 para baixo.
                return [child1, child2]

    # Método que escolhe o nó filho de maior peso.
    def choose_greedy(self, possibilities):
        children = self.find_children()
        greedy_choice = None
        for child in children:
            if child in possibilities:
                continue
            if greedy_choice == None:
                greedy_choice = child
            elif greedy_choice.qty_correct_places() < child.qty_correct_places():
                greedy_choice = child
        return greedy_choice

    # Método que calcula a quantidade de elementos na posição correta.
    def qty_correct_places(self):
        val = 0
        if self.matrix[0][0] == 1: 
            val += 1
        if self.matrix[0][1] == 2:
            val += 1
        if self.matrix[0][2] == 3:
            val += 1
        if self.matrix[1][0] == 8:
            val += 1
        if self.matrix[1][2] == 4:
            val += 1
        if self.matrix[2][0] == 7:
            val += 1
        if self.matrix[2][1] == 6:
            val += 1
        if self.matrix[2][2] == 5:
            val += 1
        return val

    # Método que calcula a quantidade de elementos na posição errada.
    def qty_incorrect_places(self):
        val = 0
        if self.matrix[0][0] != 1: 
            val += 1
        if self.matrix[0][1] != 2:
            val += 1
        if self.matrix[0][2] != 3:
            val += 1
        if self.matrix[1][0] != 8:
            val += 1
        if self.matrix[1][2] != 4:
            val += 1
        if self.matrix[2][0] != 7:
            val += 1
        if self.matrix[2][1] != 6:
            val += 1
        if self.matrix[2][2] != 5:
            val += 1
        return val

    # Método que verifica se o objetivo foi alcançado, ou seja, se todos os números estão no lugar.
    def is_done(self):
        if self.matrix[0][0] == 1 and self.matrix[0][1] == 2 and self.matrix[0][2] == 3 and self.matrix[1][0] == 8 and self.matrix[1][1] == None and self.matrix[1][2] == 4 and self.matrix[2][0] == 7 and self.matrix[2][1] == 6 and self.matrix[2][2] == 5:
            return True
        return False

    # Método que transforma um objeto do tipo GameBoard em uma string.
    def __str__(self):
        output = "["
        for i in range(3):
            output += "["
            for j in range(3):
                output += f"{self.matrix[i][j]}, " if j<=1 else f"{self.matrix[i][j]}"
            output += "], " if i<=1 else "]"
        output += "]"
        return output
    
    # Método que retorna o valor hash da classe.
    # Foi implementado para que pudesse fazer a comparação das classes.
    def __hash__(self):
        return 0

    # Método para comparar com outro objeto do tipo 'GameBoard'.
    # Retorna verdadeiro se as duas matrizes 'matrix' são iguais. Falso, caso contrário.
    def __eq__(self, other):
        if not isinstance(other, type(self)): return False
        for i in range(3):
            for j in range(3):
                if not self.matrix[i][j] == other.matrix[i][j]: return False
        return True