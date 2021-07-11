from gameboard import GameBoard
from node import Node
from queue import Queue

queue = Queue() # Fila para controle da sequência de nós que serão abertos.
possibilities = set() # Conjunto utilizado para impedir repetição de nós na árvore.
solved = False # Variável para controlar se o jogo foi resolvido ou não.

f = open('results.txt', 'a') # Arquivo de saída.

# Função que calcula a busca em largura.
def bfs():
    global queue, possibilities, solved # Definindo as variáveis globais que serão manipuladas por esta função.
    current_node = None # Definindo variável que irá armazenar o valor do nó na frente da fila.
    if not queue.empty(): # Se a fila não estiver vazia, então...
        current_node = queue.get() # pegando o nó que está na frente da fila.
        if current_node.parent == None:
            f.write('\t'*current_node.depth+f'{current_node.data} - Nível {current_node.depth}\n')
        else:
            f.write('\t'*current_node.depth+f'{current_node.data} - Nível {current_node.depth} - Pai {current_node.parent.data}\n')
        if(current_node.depth > 10): # Definindo um limite máximo para a profundidade da busca.
            return
        children = current_node.data.find_children() # Calculando os filhos do nó atual a partir do estado do seu tabuleiro.
        for child in children:
            if child in possibilities: # Se o filho já foi aberto mais acima na árvore, então não devemos considerá-lo para a próxima iteração.
                continue
            next_node = Node(current_node.depth+1, child, current_node) # Criando um nó que representa o tabuleiro da iteração atual.
            current_node.add_child(next_node) # Adicionando ao nó o filho que representa o tabuleiro da iteração atual.
            if not child.is_done(): # Se o filho não é um estado final, então vamos considerá-lo na próxima iteração.
                possibilities.add(child)
                queue.put(next_node) # Adicionando esse filho na fila.
            else:
                solved = True
                f.write('\t'*next_node.depth+f'{next_node.data} - Nível {next_node.depth} - Pai {next_node.parent.data} - Resolvido\n') # Escrevendo o valor do node atual.
        bfs() # Chamando o método novamente.

init_board = GameBoard() # Iniciando um novo jogo.
init_board.randomize() # Randomizando o tabuleiro.
# init_board.set_board([[1, 2, 3], [8, 6, 4], [7, None, 5]]) # Atribuindo um tabuleiro com um único movimento para ser concluído.
possibilities.add(init_board) # Adicionando o estado inicial no conjunto de possibilidades.
f.write(f'Novo jogo! Estado inicial: {init_board}\n')

if init_board.is_done():
    f.write('O jogo já está resolvido\n\n')
else:
    node = Node(0, init_board) # Criando um nó para armazenar o primeiro estado do tabuleiro.
    queue.put(node) # Adicionando o nó raiz na fila.
    bfs() # Aplicando a busca em largura no nó do estado inicial.
    if solved:
        f.write('O jogo foi resolvido\n\n')
    else:
        f.write('O jogo não foi resolvido\n\n')

f.close()