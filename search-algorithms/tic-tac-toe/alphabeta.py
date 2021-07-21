from game import TicTacToe
from node import Node

f = open('alphabeta.txt', 'w')  # Arquivo de saída.

# Função que calcula a busca em profundidade para determinar a árvore de possibilidades do jogo da velha.
# A altura da árvore será no máximo 10.
def alpha_beta_with_dfs(node, symbol):
    f.write('\t'*node.depth+f'{node.data} - Nível {node.depth}\n')
    children = node.data.find_children(symbol) # Calculando os filhos do nó atual a partir do estado do jogo.
    for child in children:
        next_node = Node(node.depth+1, child) # Criando um nó que representa o jogo da iteração atual.
        node_weight = child.is_done() # Verificando se alguém ganhou.
        if node_weight == None: # Senão, então temos que ver as possíveis próximas jogadas na iteração seguinte.
            if next_node.depth == 4: # Porém, se o filho está no último nível, que no caso é o 9, então houve empate.
                next_node.weight = 0  # O peso 0 significa que houve empate.
                f.write('\t'*next_node.depth+f'{next_node.data} - Nível {next_node.depth} - empate\n')
            else:
                alpha_beta_with_dfs(next_node, 'x' if symbol == 'o' else 'o') # Chamando a recursão para o nó filho.
        else:
            next_node.weight = node_weight # Atribuindo ao nó o peso 1 se 'X' ganhou e 0 se 'O' ganhou.
            f.write('\t'*next_node.depth+f'{next_node.data} - Nível {next_node.depth} - '+('X' if node_weight == 1 else 'o')+' ganhou\n')
        node.add_child(next_node) # Adicionando ao nó um filho que representa o tabuleiro da iteração atual.
    if symbol == 'X' or symbol == 'x': # Se a jogada atual é de max.
        for child in node.children: # Vamos iterar sobre os filhos do nó atual para verificar qual será o seu peso.
            if node.weight == None or child.weight > node.weight: # Se o peso do nó atual ainda não foi definido ou o peso do filho da iteração atual é maior (max) que o seu.
                node.weight = child.weight # Atribui o peso do filho ao nó atual.
            if node.ancestral("max"): # Se será realizada a poda...
                return # então não precisa verificar os próximos filhos.
    elif symbol == 'O' or symbol == 'o': # Se a jogada atual é de min.
        for child in node.children: # Vamos iterar sobre os filhos do nó atual para verificar qual será o seu peso.
            if node.weight == None or child.weight < node.weight: # Se o peso do nó atual ainda não foi definido ou o peso do filho da iteração atual é menor (min) que o seu.
                node.weight = child.weight # Atribui o peso do filho ao nó atual.
            if node.ancestral("min") : # Se será realizada a poda...
                return # então não precisa verificar os próximos filhos.

game = TicTacToe() # Iniciando um novo jogo.
node = Node(0, game) # Criando nó raiz.
alpha_beta_with_dfs(node, 'x') # Gerando a árvore de possibilidades do jogo.

f.close()