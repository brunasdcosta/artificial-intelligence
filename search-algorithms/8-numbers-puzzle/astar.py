from gameboard import GameBoard
from node import Node

def astar(node):
    global f, possibilities, solved # Definindo as variáveis globais que serão manipuladas por esta função.
    children = node.data.find_children() # Recuperando os filhos do nó raiz.
    while node.qty_wrong_placed != 0 and set(children) - possibilities: # Enquanto ainda há elementos no lugar errado e possibilidades a serem exploradas.
        f.write(f'{node.data} - Nível: {node.depth} - Peso: {node.astar_weight} - Quantidade de elementos errados: {node.qty_wrong_placed}\n')
        for child in children: # Iterando sobre os filhos do nó da iteração atual.
            if child in possibilities: # Se o filho já foi explorado, então não devemos considerá-lo para a próxima iteração.
                continue
            next_node = Node(node.depth+1, child) # Criando um nó que representa o tabuleiro filho da iteração atual.
            next_node.set_astar_weight(child.qty_incorrect_places()) # Atribuindo ao nó criado o peso para a busca A*.
            node.add_child(next_node) # Adicionando o nó criado na árvore.
            possibilities.add(child) # Adicionando o tabuleiro da iteração atual na lista de possibilidades.
        if node.children: # Se o nó da iteração atual tem filhos.
            node.children.sort(key = lambda x:x.astar_weight, reverse = False) # Ordenando os filhos do nó por ordem de menor peso.
            node = node.children[0] # Atualizando a variável "node" com o seu filho de menor peso.
            children = node.data.find_children() # Recuperando os filhos do nó para a próxima iteração.
    if node.qty_wrong_placed == 0: # Se não há elementos no lugar errado.
        solved = True
        f.write(f'{node.data} - Nível: {node.depth} - Peso: {node.astar_weight} - Quantidade de elementos errados: {node.qty_wrong_placed}\n')

possibilities = set() # Conjunto utilizado para impedir repetição de nós na árvore.
solved = False # Variável para controlar se o jogo foi resolvido ou não.

f = open('astar.txt', 'a') # Arquivo de saída.

init_board = GameBoard() # Iniciando um novo jogo.
init_board.randomize() # Randomizando o tabuleiro.
# init_board.set_board([[1, 2, 3], [8, 6, 4], [7, None, 5]]) # Atribuindo um tabuleiro com um único movimento para ser concluído.
possibilities.add(init_board) # Adicionando o estado inicial no conjunto de possibilidades.
f.write(f'Novo jogo usando busca A*.\nEstado inicial: {init_board}\n')

if init_board.is_done():
    f.write('O jogo já está resolvido\n\n')
else:
    node = Node(0, init_board)
    node.set_astar_weight(init_board.qty_incorrect_places())
    astar(node)
    if solved == True:
        f.write('O jogo foi resolvido\n\n')
    else:
        f.write('O jogo não foi resolvido\n\n')

f.close()