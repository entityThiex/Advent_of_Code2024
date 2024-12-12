
# get the data as matrix format list[list]]
def get_data():

    result = []

    with open(r"day_12_data.txt", "r") as fl:
        for line in fl:
            result.append([x for x in line.strip()])

    return result


#compute the perimeter of a region
def compute_peri_score(perimeter: dict[int, dict[int, list[int]]]):

    score = []      # end score

    for i in [1, 3]:        # iterate over all vertical boundaries
        for j in perimeter[i].keys():   # iterate over all lists. lists have the same x value

            y_values = perimeter[i][j]      # y values for x
            y_values.sort()         # sort so they are in the right order
            tmp = [y_values.pop(0)]     # get the first element

            while y_values:         #split up the elements in the different boundaries
                dy = y_values.pop(0)
                if dy - tmp[-1] != 1:       #check if between two elements of the list are a gap
                    score.append(tmp)       # if so, conclude the boundary and open a new one
                    tmp = [dy]
                else:
                    tmp.append(dy)     # if there is no gap, keep adding to the list ( boundary is not over yet)
            score.append(tmp)       # add the last list to the score

    for i in [0, 2]:
        for j in perimeter[i].keys():

            x_values = perimeter[i][j]
            x_values.sort()
            tmp = [x_values.pop(0)]

            while x_values:
                dx = x_values.pop(0)
                if dx - tmp[-1] != 1:
                    score.append(tmp)
                    tmp = [dx]
                else:
                    tmp.append(dx)
            score.append(tmp)

    return len(score)       # length of list is now number of individual boundaries


# main function for checking regions as well as their corresponding area and perimeter
def area_peri():

    score = 0

    for y in range(max_y):      # iterate over the matrix
        for x in range(max_x):

            item = data[y][x]       # get current item from matrix

            if item != '#':     # all already visited regions are replaced by #

                queue = [(y,x)]     # queue for the bfs
                visited = [(y, x)]      # visited list for bfs to avoid duplicates
                #perimeter = 0          # ex1 perimeter
                perimeter = {0:{},1:{},2:{},3:{}}       # ex2 perimeter: dict[dict[list[int]]] values are 'sorted' after direction -> x/y value -> y-/x- list
                area = 0

                while queue:        # bfs

                    possible_ways = []      # temporary list to check for duplicates later on
                    dy,dx = queue.pop(0)

                    if dx-1 >= 0 and data[dy][dx-1] == item:    #check all 4 directions and add the values with the corresponding direction to perimeter
                        possible_ways.append((dy, dx-1))
                    else:
                        if dx in perimeter[3].keys():
                            perimeter[3][dx].append(dy)
                        else:
                            perimeter[3][dx] = [dy]
                        #perimeter += 1

                    if dx+1 < max_x and data[dy][dx+1] == item:
                        possible_ways.append((dy, dx+1))
                    else:
                        if dx in perimeter[1].keys():
                            perimeter[1][dx].append(dy)
                        else:
                            perimeter[1][dx] = [dy]
                        #perimeter += 1

                    if dy-1 >= 0 and data[dy-1][dx] == item:
                        possible_ways.append((dy-1, dx))
                    else:
                        if dy in perimeter[0].keys():
                            perimeter[0][dy].append(dx)
                        else:
                            perimeter[0][dy] = [dx]
                        #perimeter += 1

                    if dy+1 < max_y and data[dy+1][dx] == item:
                        possible_ways.append((dy+1, dx))
                    else:
                        if dy in perimeter[2].keys():
                            perimeter[2][dy].append(dx)
                        else:
                            perimeter[2][dy] = [dx]
                        #perimeter += 1

                    for i in possible_ways:     #  check for duplicates and append to queue only the new ones
                        if i not in visited:
                            queue.append(i)
                            visited.append(i)

                perimeter = compute_peri_score(perimeter)  # call perimeter function to calculate perimeter

                area += len(visited)        # area is length of the visited list
                for i in visited:       # replace the current region with # to avoid going over the same region twice
                    data[i[0]][i[1]] = '#'
                score += area * perimeter       # calculate score

    print(score)


if __name__ == "__main__":
    data = get_data()       # driver code
    max_x = len(data[0])
    max_y = len(data)
    area_peri()
