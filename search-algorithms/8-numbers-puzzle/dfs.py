from gameboard import GameBoard
from node import Node

possibilities = set() # Conjunto utilizado para impedir repetição de nós na árvore.
solved = False # Variável para controlar se o jogo foi resolvido ou não.

f = open('results.txt', 'a') # Arquivo de saída.

# Função que calcula a busca em profundidade iterativa.
def dfs(node):
    global solved, possibilities # Definindo as variáveis globais que serão manipuladas por esta função.
    f.write('\t'*node.depth+f'{node.data} - Nível {node.depth}\n') # Escrevendo o valor do node atual.
    if(node.depth > 10): # Definindo um limite máximo para a profundidade da busca.
        return
    children = node.data.find_children() # Calculando os filhos do nó atual a partir do estado do seu tabuleiro.
    for child in children:
        if child in possibilities: # Se o filho já foi aberto mais acima na árvore, então não devemos considerá-lo para a próxima iteração.
            continue
        if not child.is_done(): # Se o filho não é um estado final, então vamos considerá-lo na próxima iteração.
            possibilities.add(child)
        else:
            solved = True
            f.write('\t'*(node.depth+1)+f'{child} - Nível {node.depth+1}\n - Resolvido')
        node.add_child(Node(node.depth+1, child)) # Adicionando ao nó um filho que representa o tabuleiro da iteração atual.
    for child in node.children: # Iterando sobre os filhos do nó atual, calculados a partir do laço anterior.
        if not child.data.is_done(): # Se o filho não é um estado final, então...
            dfs(Node(node.depth+1, child.data)) # Devemos manter na recursão.

init_board = GameBoard() # Iniciando um novo jogo.
init_board.randomize() # Randomizando o tabuleiro.
# init_board.set_board([[1, 2, 3], [8, 6, 4], [7, None, 5]]) # Atribuindo um tabuleiro com um único movimento para ser concluído.
possibilities.add(init_board) # Adicionando o estado inicial no conjunto de possibilidades.
f.write(f'Novo jogo! Estado inicial: {init_board}\n')

if init_board.is_done():
    f.write('O jogo já está resolvido\n\n')
else:
    node = Node(0, init_board) # Criando um nó para armazenar o primeiro estado do tabuleiro.
    dfs(node) # Aplicando a busca em profundidade no nó do estado inicial.
    if solved:
        f.write('O jogo foi resolvido\n\n')
    else:
        f.write('O jogo não foi resolvido\n\n')

f.close()