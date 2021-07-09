from gameboard import GameBoard
from node import Node

def dfs(node):
    f.write('\t'*node.depth+f'{node.data} - {node.depth}\n')
    possibilities.add(node.data)
    if(node.depth > 5):
        return node
    children = node.data.find_children()
    for child in children:
        if child in possibilities:
            continue
        if not child.is_done():
            next_node = dfs(Node(node.depth+1, child))
            node.add_child(next_node)
        else:
            solved = True
            f.write('\t'*(node.depth+1)+f'{child} - {node.depth+1}\n')
            node.add_child(Node(node.depth+1, child))
            continue
    return node

f = open('results.txt', 'a')

init_board = GameBoard()
init_board.randomize()
f.write(f'Estado inicial: {init_board}\n')

if init_board.is_done():
    f.write('O jogo já está resolvido\n\n')
else:
    node = Node(0, init_board)
    possibilities = set()
    solved = False
    dfs(node)
    if solved:
        f.write('O jogo foi resolvido\n\n')
    else:
        f.write('O jogo não foi resolvido\n\n')

f.close()