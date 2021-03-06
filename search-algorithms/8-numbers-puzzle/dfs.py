from gameboard import GameBoard
from node import Node

# Função que calcula a busca em profundidade iterativa.
def dfs(node):
    global limit, possibilities, solved, results_depth, f # Definindo as variáveis globais que serão manipuladas por esta função.
    f.write('\t'*node.depth+f'{node.data} - Nível {node.depth}\n') # Escrevendo o valor do node atual.
    if node.depth >= limit: # Definindo um limite máximo para a profundidade da busca.
        return
    children = node.data.find_children() # Calculando os filhos do nó atual a partir do estado do seu tabuleiro.
    for child in children:
        if child in possibilities: # Se o filho já foi aberto mais acima na árvore, então não devemos considerá-lo para a próxima iteração.
            continue
        if not child.is_done(): # Se o filho não é um estado final, então vamos considerá-lo na próxima iteração.
            possibilities.add(child)
        else:
            solved = True
            results_depth.add(node.depth+1)
            f.write('\t'*(node.depth+1)+f'{child} - Nível {node.depth+1} - Resolvido\n')
        node.add_child(Node(node.depth+1, child)) # Adicionando ao nó um filho que representa o tabuleiro da iteração atual.
    for child in node.children: # Iterando sobre os filhos do nó atual, calculados a partir do laço anterior.
        if not child.data.is_done(): # Se o filho não é um estado final, então...
            dfs(child) # Devemos manter na recursão.

limit = 10 # Variável utilizada para controle de profundidade.
possibilities = set() # Conjunto utilizado para impedir repetição de nós na árvore.
solved = False # Variável para controlar se o jogo foi resolvido ou não.
results_depth = set() # Conjunto que contém os níveis que há jogos resolvidos.

f = open('dfs.txt', 'a') # Arquivo de saída.
init_board = GameBoard() # Iniciando um novo jogo.
init_board.randomize() # Randomizando o tabuleiro.
# init_board.set_board([[1, 2, 3], [8, 6, 4], [7, None, 5]]) # Atribuindo um tabuleiro com um único movimento para ser concluído.
possibilities.add(init_board) # Adicionando o estado inicial no conjunto de possibilidades.
f.write(f'Novo jogo usando busca em profundidade com limite {limit}.\nEstado inicial: {init_board}\n')

if init_board.is_done():
    f.write('O jogo já está resolvido\n\n')
else:
    node = Node(0, init_board) # Criando um nó para armazenar o primeiro estado do tabuleiro.
    dfs(node) # Aplicando a busca em profundidade no nó do estado inicial.
    if solved:
        f.write(f'O jogo foi resolvido.\nA melhor solução é a de nível {min(results_depth)}\n\n')
    else:
        f.write('O jogo não foi resolvido\n\n')

f.close()