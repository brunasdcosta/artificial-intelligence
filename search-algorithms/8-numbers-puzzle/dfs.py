from gameboard import GameBoard
from node import Node

possibilities = set()

# TODO terminar busca
def dfs(node):
    print(f'node atual: {node.data}')
    children = node.data.find_children()
    i = 1
    for child in children:
        if child in possibilities:
            children.remove(child)
            continue
        possibilities.add(child)
        print(f'filho {i}: {child}')
        if not child.is_done():
            dfs(Node(node.depth+1, child))

init_board = GameBoard()
# init_board.randomize()
init_board.set_board([[1, 2, 3], [None, 8, 4], [7, 6, 5]])
if init_board.is_done():
    print("o jogo ja terminou")
else:
    node = Node(0, init_board)
    possibilities.add(node.data)
    dfs(node)