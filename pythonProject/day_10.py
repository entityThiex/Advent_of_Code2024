
def get_data():

    result = []
    zero = []

    with open(r"day_10_data.txt", "r") as fl:
        for line in fl:
            result.append([int(x) for x in line.strip()])

    for y in range(len(result)):
        for x in range(len(result[-1])):

            point = result[y][x]

            if point == 0:
                zero.append((y, x))

    return result, zero


def search_init(start: tuple[int,int]):

    x = start[1]
    y = start[0]
    nxt = [(x, y, 0)]       # queue for the bfs, initialized with the starting point
    score = 0       # score for the starting point
    visited = []        # list for duplicates

    while len(nxt):     # bfs, while loop for the elements in nxt

        position = nxt.pop(0)       # get next element from nxt

        x = position[0]     # extract data from position
        y = position[1]
        value = position[2]

        if value == 9 and (x,y) not in visited:      # if end reached and not in visited, increment score
            score += 1
            visited.append((x, y))

        if x + 1 < max_x and graph[y][x+1] - value == 1:        # check out of bounds and value +1
            nxt.append((x+1, y, graph[y][x+1]))         # append the next element in the row to nxt
                                                        # continue with the others like this
        if x - 1 >= 0 and graph[y][x-1] - value == 1:
            nxt.append((x-1, y, graph[y][x-1]))

        if y + 1 < max_y and graph[y+1][x] - value == 1:
            nxt.append((x, y+1, graph[y+1][x]))

        if y - 1 >= 0 and graph[y-1][x] - value == 1:
            nxt.append((x, y-1, graph[y-1][x]))

    return score        # return the score of the starting point


if __name__ == "__main__":

    graph, starting_points = get_data()
    print(starting_points)
    max_y = len(graph)
    max_x = len(graph[0])
    counter = 0

    for i in starting_points:
        counter += search_init(i)

    print(counter)

    #for part two, remove the visited check
