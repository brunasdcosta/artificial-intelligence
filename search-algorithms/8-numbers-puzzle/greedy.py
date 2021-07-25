from gameboard import GameBoard
from node import Node

def greedy(node):
    global f, possibilities, solved # Definindo as variáveis globais que serão manipuladas por esta função.
    greedy_choice = node.data.choose_greedy(possibilities) # Escolhendo, para o nó raiz, o nó filho de maior peso.
    while greedy_choice != None: # Enquanto não encontrar uma folha ou solucionar o jogo...
        f.write('\t'*node.depth + f'{node.data} - Nível {node.depth} - Quantidade de elementos corretos: {node.data.qty_correct_places()}\n')
        if not greedy_choice.is_done(): # Se o filho atual não é o estado final...
            possibilities.add(greedy_choice) # Adiciona o filho no conjunto de possibilidades.
            next_node = Node(node.depth+1, greedy_choice) # Criando o nó que representa o filho.
            node.add_child(next_node) # Adicionando o nó na árvore.
            greedy_choice = next_node.data.choose_greedy(possibilities) # Buscando o próximo nó filho a ser explorado.
            node = next_node
        else:
            solved = True
            f.write('\t'*(node.depth+1) + f'{greedy_choice} - Nível {node.depth+1} - Quantidade de elementos corretos: {greedy_choice.qty_correct_places()} \n ')
            return

possibilities = set() # Conjunto utilizado para impedir repetição de nós na árvore.
solved = False # Variável para controlar se o jogo foi resolvido ou não.

f = open('greedy.txt', 'a') # Arquivo de saída.

init_board = GameBoard() # Iniciando um novo jogo.
init_board.randomize() # Randomizando o tabuleiro.
# init_board.set_board([[1, 2, 3], [8, 6, 4], [7, None, 5]]) # Atribuindo um tabuleiro com um único movimento para ser concluído.
possibilities.add(init_board) # Adicionando o estado inicial no conjunto de possibilidades.
f.write(f'Novo jogo usando busca gulosa.\nEstado inicial: {init_board}\n')

if init_board.is_done():
    f.write('O jogo já está resolvido\n\n')
else:
    node = Node(0, init_board) # Criando um nó para armazenar o primeiro estado do tabuleiro.
    greedy(node) # Aplicando a busca gulosa no nó do estado inicial.
    if solved:
        f.write('O jogo foi resolvido\n\n')
    else:
        f.write('O jogo não foi resolvido\n\n')

f.close()