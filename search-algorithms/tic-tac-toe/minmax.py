from os import X_OK
from game import TicTacToe
from node import Node

# Função que calcula a busca em profundidade para determinar a árvore de possibilidades do jogo da velha.
# A altura da árvore será no máximo 10.
def min_max_with_dfs(node, symbol):
    global f
    f.write('\t'*node.depth+f'{node.data} - Nível {node.depth}\n')
    children = node.data.find_children(symbol) # Calculando os filhos do nó atual a partir do estado do jogo.
    for child in children:
        next_node = Node(node.depth+1, child) # Criando um nó que representa o jogo da iteração atual.
        node_weight = child.is_done() # Verificando se alguém ganhou.
        if node_weight == None: # Senão, então temos que ver as possíveis próximas jogadas na iteração seguinte.
            if next_node.depth == 9: # Porém, se o filho está no último nível, que no caso é o 9, então houve empate.
                next_node.weight = 0  # O peso 0 significa que houve empate.
                next_node.data.weight = 'noone'
                f.write('\t'*next_node.depth + f'{next_node.data} - Nível {next_node.depth} - empate\n')
            else:
                min_max_with_dfs(next_node, 'x' if symbol == 'o' else 'o') # Chamando a recursão para o nó filho.
        else:
            next_node.weight = node_weight # Atribuindo ao nó o peso 1 se 'X' ganhou e 0 se 'O' ganhou.
            f.write('\t'*next_node.depth+f'{next_node.data} - Nível {next_node.depth} - '+('x' if node_weight == 1 else 'o')+' ganhou\n')
        node.add_child(next_node) # Adicionando ao nó um filho que representa o tabuleiro da iteração atual.
    if symbol == 'X' or symbol == 'x': # Se a jogada atual é de max.
        node.weight = max(node.children) # Atribui ao nó atual o maior peso dos seus filhos.
    elif symbol == 'O' or symbol == 'o': # Se a jogada atual é de min.
        node.weight = min(node.children) # Atribui ao nó atual o menor peso dos seus filhos.

# Função que recupera um índice para a jogada do usuário.
def get_index_from_user():
    indexes = input('Qual posição você quer jogar? Utilize o formato \'linha,coluna\': ')
    try:
        i_str, j_str = indexes.split(',')
        try:
            i = int(i_str) # Convertendo o valor da linha de str para int.
            j = int (j_str) # Convertendo o valor da coluna de str para int.
            if i>=1 and i<=3 and j>=1 and j<=3:
                return [i, j]
            else:
                print('Por favor, informe linhas e colunas no intervalo de 1 à 3.')
                return get_index_from_user()
        except ValueError:
            print('Os índices passados não são válidos. Tente novamente.')
            return get_index_from_user()
    except ValueError:
        print('Por favor, utilize o formato especificado.')
        return get_index_from_user()

# Função que exibe o jogo atual no formato de jogo da velha.
# Retirada de: https://stackoverflow.com/a/58806047
def print_current_game(game, tile_width=3):
    output = ""
    for i, row in enumerate(game):
        element = row[0]
        element_str = '{:^{width}}'.format('' if element==None else element, width=tile_width)
        output = output + element_str
        for element in row[1:]:
            element_str = '|{:^{width}}'.format('' if element==None else element, width=tile_width)
            output = output + element_str
        output = output + '\n'
        if i is not len(game) - 1:
            element_str = '{:-^{width}}'.format("", width=((tile_width + 1) * len(row) - 1))
            output = output + element_str
            output = output + '\n'
    print(output)

# Função que contém o fluxo do jogo. No caso do algoritmo ser o jogador max, então, antes de chamar esta função, ele deve primeiro fazer a sua jogada.
# algorithm_player = 'min', 'max'
def common_game_flow(algorithm_player):
    global gameover, number_of_moves, current_game, node
    while not gameover and number_of_moves < 9:
        indexes = get_index_from_user() # Recuperando a jogada do usuário.
        if not current_game.mark(indexes[0]-1, indexes[1]-1, option): # Realizando a jogada do usuário.
            print('Jogada inválida! Por favor, escolha uma posição vazia.')
            continue
        print('Jogada feita!\nEstado atual do jogo:')
        print_current_game(current_game.matrix)
        number_of_moves+=1
        if not current_game.is_done() == None: # Se alguém ganhou...
            if current_game.winner == 'x': # com certeza foi o usuário, mas fazemos a verificação mesmo assim.
                print('Você ganhou o jogo, parabéns!')
            else:
                print('O computador ganhou!')
            gameover = True
        else:
            if number_of_moves == 9: # Se já foram realizadas as 9 jogadas.
                print('O jogo empatou!')
                gameover = True
            else:
                print('Agora, o computador irá fazer a jogada dele...')
                node = node.choose_next_move(algorithm_player, current_game) # O algoritmo escolhendo a sua jogada.
                current_game = node.data
                print('Jogada escolhida!\nEstado atual do jogo:')
                print_current_game(current_game.matrix)
                number_of_moves+=1
                if node.data.winner == 'none': # Se a jogada leva a um empate.
                    print('O jogo empatou!')
                    gameover = True
                elif node.data.winner == 'O' or node.data.winner == 'o': # Se o algoritmo ganhou.
                    print('O computador ganhou!')
                    gameover = True

f = open('minmax.txt', 'w')  # Arquivo de saída.
game = TicTacToe() # Iniciando um jogo vazio.
node = Node(0, game) # Criando nó raiz.
min_max_with_dfs(node, 'x') # Gerando a árvore de possibilidades do jogo.
f.close()

########## Início do jogo com o usuário ##########

print('Bem-vindo ao jogo da velha!')
print('Pelas nossas regras, o jogador X sempre começa.')

# Vendo quem irá começar primeiro.
option = input('Você deseja jogar com X ou O? ')
while option!='X' and option!='x' and option!='O' and option!='o':
    print('Opção inválida.')
    indexes = input('Você deseja jogar com X ou O? ')

current_game = TicTacToe() # Tabuleiro do jogo.
gameover = False # Variável de controle de parada. Se for verdadeira, então alguém ganhou ou empatou o jogo.
number_of_moves = 0 # Variável para controlar a quantidade de jogadas.

if option=='X' or option=='x':
    print('Você será o jogador X!')
    common_game_flow('min')
elif option=='O' or option=='o':
    print('Você será o jogador O!\nO computador irá escolher sua primeira jogada...')
    node = max(node.children) # Escolhendo a primeira jogada. Ela será a do filho de maior peso, uma vez que o algoritmo é o jogador max.
    current_game = node.data
    print('Jogada escolhida!\nEstado atual do jogo:')
    print_current_game(current_game.matrix)
    number_of_moves+=1
    common_game_flow('max')
    if gameover == False:
        print('O jogo empatou!')

########## Fim do jogo com o usuário ##########