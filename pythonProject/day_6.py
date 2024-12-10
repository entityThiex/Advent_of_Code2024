
def get_data():

    with open(r"day_6_data.txt", "r") as fl:
        result = [[x for x in line] for line in fl]

    cords = 0

    for row in range(len(result)):
        for element in range(len(result[row])):
            if result[row][element] == "^":
                cords = row, element

    return result, cords


def map_the_cop():

    still_on_map = True     #Variable area
    direction = 0
    x = start_cords[1]
    y = start_cords[0]
    max_x = len(graph[-1])
    max_y = len(graph)

    while still_on_map:     #running loop

        match direction:        #match the direction (0-3) for the rotation the guard is in

            case 0:     # facing upwards
                graph[y][x] = 'x'       # Mark position with a small x

                y -= 1      # go to the next location
                if y < 0:       # if out of map break the loop
                    still_on_map = False

                elif graph[y][x] == '#':        # if you run into an obstruction, go back and turn right
                    y += 1                      # the other cases work alike
                    direction += 1

            case 1:     # facing right
                graph[y][x] = 'x'

                x += 1
                if x >= max_x:
                    still_on_map = False

                elif graph[y][x] == '#':
                    x -= 1
                    direction += 1

            case 2:     # facing downwards
                graph[y][x] = 'x'

                y += 1
                if y >= max_y:
                    still_on_map = False

                elif graph[y][x] == '#':
                    y -= 1
                    direction += 1

            case 3:    # facing left
                graph[y][x] = 'x'

                x -= 1
                if x < 0:
                    still_on_map = False

                if graph[y][x] == '#':
                    x += 1
                    direction = 0

            case _:
                print("An error seems to have occurred. x: ", x, ", y: ", y, ", direction: ", direction)
                break


def show_path():

    still_on_map = True     #Variable area
    direction = 0
    x = start_cords[1]
    y = start_cords[0]
    max_x = len(graph[-1])
    max_y = len(graph)
    possibilities = 0
    dupe_prev = []

    while still_on_map:     #running loop

        position = graph[y][x]

        match direction:        #match the direction (0-3) for the rotation the guard is in

            case 0:     # facing upwards
                if position == '-':
                    graph[y][x] = '+'

                elif position == '+':
                    if graph[y][x+1] == '-' and (y-1, x) not in dupe_prev:
                        possibilities += 1
                        dupe_prev.append((y-1,x))

                else:
                    graph[y][x] = '|'       # Mark position with a small x

                y -= 1      # go to the next location
                if y < 0:       # if out of map break the loop
                    still_on_map = False

                elif graph[y][x] == '#':        # if you run into an obstruction, go back and turn right
                    y += 1                      # the other cases work alike
                    direction += 1
                    graph[y][x] = '+'

            case 1:     # facing right

                if position == '|':
                    graph[y][x] = '+'
                elif position == '+':
                    if graph[y+1][x] == '|' and (y, x+1) not in dupe_prev:
                        possibilities += 1
                        dupe_prev.append((y,x+1))
                else:
                    graph[y][x] = '-'

                x += 1
                if x >= max_x:
                    still_on_map = False

                elif graph[y][x] == '#':
                    x -= 1
                    direction += 1
                    graph[y][x] = '+'

            case 2:     # facing downwards

                if position == '-':
                    graph[y][x] = '+'
                elif position == '+':
                    if (y+1, x) not in dupe_prev and graph[y][x-1] == '-':
                        possibilities += 1
                        dupe_prev.append((y+1,x))
                else:
                    graph[y][x] = '|'

                y += 1
                if y >= max_y:
                    still_on_map = False

                elif graph[y][x] == '#':
                    y -= 1
                    direction += 1
                    graph[y][x] = '+'

            case 3:    # facing left

                if position == '|' or position == '+':
                    graph[y][x] = '+'
                if (y, x-1) not in dupe_prev and graph[y-1][x] == '-':
                    possibilities += 1
                    dupe_prev.append((y, x-1))
                else:
                    graph[y][x] = '-'

                x -= 1
                if x < 0:
                    still_on_map = False

                if graph[y][x] == '#':
                    x += 1
                    direction = 0
                    graph[y][x] = '+'

            case _:
                print("An error seems to have occurred. x: ", x, ", y: ", y, ", direction: ", direction)
                break

    print(possibilities)
    print(len(dupe_prev), dupe_prev)


def wrap_up():
    counter = 0
    for i in graph:
        counter +=  i.count('x')

    return counter


def visualize():

    for i in graph:
        print("".join(i))


if __name__ == "__main__":
    graph, start_cords = get_data()

    # map_the_cop()
    show_path()

    # print(wrap_up())
    #visualize()

    # print(graph)
