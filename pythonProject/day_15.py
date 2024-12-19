
def get_data():

    m = []
    ins = []

    with open(r"day_15_data.txt", "r") as fl:
        lines = fl.readlines()
        st = 0
        for i in range(len(lines)):
            line = lines[i]
            if '#' in line:
                if '@' in line:
                    st = (i, line.index('@'))
                    line = line.replace('@','.')
                m.append([x for x in line.strip()])
            elif '<' in line:
                ins.append(line.strip())

    ins = "".join(ins)
    return m, ins, st


def visualize():

    lines = []
    for i in range(max_y):
        lines.append(''.join(graph[i]))

    with open(r"frame.txt", "w") as fl:
        fl.writelines(lines)


def move_robot():
    global graph
    pos_y, pos_x = start

    for instruction in instructions:

        match instruction:

            case '^':
                height = 0

                if graph[pos_y-1][pos_x] == '.':
                    pos_y -= 1
                    continue
                elif graph[pos_y-1][pos_x] == '#':
                    continue
                else:
                    for i in range(pos_y - 1, 0, -1):
                        if graph[i][pos_x] == '#':
                            height = 0
                            break
                        if graph[i][pos_x] == '.':
                            height = i
                            break

                    if height:
                        graph[pos_y-1][pos_x] = '.'
                        graph[height][pos_x] = 'O'
                        pos_y -= 1

            case 'v':
                height = 0

                if graph[pos_y + 1][pos_x] == '.':
                    pos_y += 1
                    continue
                elif graph[pos_y + 1][pos_x] == '#':
                    continue
                else:
                    for i in range(pos_y + 1, max_y):
                        if graph[i][pos_x] == '#':
                            height = 0
                            break
                        if graph[i][pos_x] == '.':
                            height = i
                            break

                    if height:
                        graph[pos_y + 1][pos_x] = '.'
                        graph[height][pos_x] = 'O'
                        pos_y += 1

            case '<':
                width = 0

                if graph[pos_y][pos_x - 1] == '.':
                    pos_x -= 1
                    continue
                elif graph[pos_y][pos_x - 1] == '#':
                    continue
                else:
                    for i in range(pos_x - 1, 0, -1):
                        if graph[pos_y][i] == '#':
                            width = 0
                            break
                        if graph[pos_y][i] == '.':
                            width = i
                            break

                    if width:
                        graph[pos_y][pos_x - 1] = '.'
                        graph[pos_y][width] = 'O'
                        pos_x -= 1

            case '>':
                width = 0

                if graph[pos_y][pos_x + 1] == '.':
                    pos_x += 1
                    continue
                elif graph[pos_y][pos_x + 1] == '#':
                    continue
                else:
                    for i in range(pos_x + 1, max_x):
                        if graph[pos_y][i] == '#':
                            width = 0
                            break
                        if graph[pos_y][i] == '.':
                            width = i
                            break

                    if width:
                        graph[pos_y][pos_x + 1] = '.'
                        graph[pos_y][width] = 'O'
                        pos_x += 1

    counter = 0
    visualize()

    for y in range(max_y):
        for x in range(max_x):

            if graph[y][x] == 'O':
                counter += y * 100 + x

    return counter


if __name__ == "__main__":

    graph, instructions, start = get_data()
    max_x = len(graph[0])
    max_y = len(graph)

    print(move_robot())

    # too high: 1694420
