import main





class MazeNode:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Maze(main.MyTree):

    def __init__(self, size_x: int, size_y: int, name: str, start_node: MazeNode, end_node: MazeNode):
        man_dist = abs(end_node.x - start_node.x) + abs(end_node.y - start_node.y)
        super().__init__(name, man_dist)
        self.node = start_node
        self.size_x = size_x
        self.size_y = size_y

    def add_maze_node(self, node_to: MazeNode, cost: int):
        man_dist = abs(self.end_node.x - node_to.x) + abs(self.end_node.y - node_to.y)
        self.add_edge(Maze(self.name, node_to, maze_end), cost)

    def __str__(self):
        return self.name


'''maze_start = Maze("Start", maze_start, maze_end)
'''
mazes = [[0, 8, 16, 24, 32, 40, 48, 56],
         [1, 9, 17, 25, 33, 41, 49, 57],
         [2, 10, 18, 26, 34, 42, 50, 58],
         [3, 11, 19, 27, 35, 43, 51, 59],
         [4, 12, 20, 28, 36, 44, 52, 60],
         [5, 13, 21, 29, 37, 45, 53, 61],
         [6, 14, 22, 30, 38, 46, 54, 62],
         [7, 15, 23, 31, 39, 47, 55, 63]]

for i in range(8):
    for j in range(8):
        print("%d," % mazes[j][i], end="")
print()
