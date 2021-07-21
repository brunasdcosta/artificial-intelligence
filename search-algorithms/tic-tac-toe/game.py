from copy import deepcopy

# Classe que representa o jogo da velha.
class TicTacToe:

    # Construtor.
    def __init__(self):
        self.matrix = self.matrix = [[None for j in range(3)] for i in range(3)] # Criando uma matrix de ordem 3.

    # Set da matriz que representa o jogo.
    def set_game(self, matrix):
        self.matrix = matrix

    # Método para marcar uma jogada.
    # Retorna verdadeiro se, e somente se, a jogada foi realizada com sucesso.
    def mark(self, i, j, symbol):
        # Aqui precisamos analisar se o valor da célula que queremos marcar é 'None' - um espaço vazio. Senão, a jogada não é válida.
        # Também fazemos a verificação do símbolo que será usado ao marcar a célula, que só pode ser 'X' ou 'O'.
        if self.matrix[i][j] == None and (symbol == 'X' or symbol == 'x' or symbol == 'O' or symbol == 'o'):
            self.matrix[i][j] = symbol
            return True
        return False

    # Método que retorna um array constituído de arrays de índices das posições vazias, demarcadas com 'None', na matriz que representa o jogo.
    # Caso não tenha mais posições vazias, o retorno será um array vazio.
    def find_none_index(self):
        index = []
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == None:
                    index.append([i, j])
        return index

    # Método que retorna um array com as possibilidades de jogadas a partir do estado atual do jogo.
    # Retorna um 'None' caso não haja mais possibilidades.
    def find_children(self, symbol):
        if symbol == 'X' or symbol == 'x' or symbol == 'O' or symbol == 'o': # Verificando se o símbolo passado é 'X' ou 'O'.
            children = [] # Array de possibilidades de próxima jogada.
            indexes = self.find_none_index() # Encontrando as posições vazias. A partir delas que saberemos quais células podemos marcar.
            for index in indexes:
                child = deepcopy(self) # Criando uma cópia independente do jogo atual.
                child.mark(index[0], index[1], symbol) # Marcando na cópia uma jogada possível.
                children.append(child)
            return children
        return None
    
    # Função que captura o peso a partir de um símbolo.
    # O símbolo 'X' sempre será o max. Consequentemente, o símbolo 'O' sempre será o min.
    def weight(self, symbol):
        if symbol == 'X' or symbol == 'x':
            return 1
        elif symbol == 'O' or symbol == 'o':
            return -1

    # Método que verifica se alguém ganhou o jogo.
    # Retorna 1 se o 'X' ganhou, -1 se o 'O' ganhou e 'None' se ainda não há vitórias.
    def is_done(self):
        # Verificando se há uma tripla nas diagonais.
        if (self.matrix[0][0] == self.matrix[1][1] and self.matrix[1][1] == self.matrix[2][2]) or (self.matrix[0][2] == self.matrix[1][1] and self.matrix[1][1] == self.matrix[2][0]):
            return self.weight(self.matrix[1][1])
        for k in range(3):
            if self.matrix[k][0] == self.matrix[k][1] and self.matrix[k][1] == self.matrix[k][2]: # Tripla na horizontal.
                return self.weight(self.matrix[k][0])
            elif self.matrix[0][k] == self.matrix[1][k] and self.matrix[1][k] == self.matrix[2][k]: # Tripla na vertical.
                return self.weight(self.matrix[0][k])
        return None

    # Método que transforma um objeto do tipo TicTacToe em uma string.
    def __str__(self):
        output = "["
        for i in range(3):
            output += "["
            for j in range(3):
                output += f"{self.matrix[i][j]}, " if j<=1 else f"{self.matrix[i][j]}"
            output += "], " if i<=1 else "]"
        output += "]"
        return output