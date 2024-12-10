
def get_data():
    result = []
    word_book = []
    with open(r"day_8_data.txt", "r") as fl:
        for line in fl:
            line = line.strip()
            result.append(line)

            word_book += [x for x in line if x != "."]

    word_book = [i for i in word_book if word_book.count(i) > 1]
    word_book = list(set(word_book))

    return result, word_book


def antinodes(literal: str):

    positions = []      # variable area
    max_y = len(matrix)
    max_x = len(matrix[-1])
    result = []

    for y in range(max_y):      #find all locations of the current literal
        for x in range(max_x):

            check = matrix[y][x]

            if check == literal:
                positions.append((y,x))

    for i in positions:         # calculate all antinodes and append them to the output
        for j in positions:

            if i == j:
                continue

            y1 = i[0]
            y2 = j[0]
            x1 = i[1]
            x2 = j[1]

            dx = x1 - x2
            dy = y1 - y2

            if max_x > x1 + dx >= 0 and max_y > y1 + dy >= 0:
                result.append((y1 + dy, x1 + dx))


    return result


def antinodes_trace(literal: str):

    positions = []      # variable area
    max_y = len(matrix)
    max_x = len(matrix[-1])
    result = []

    for y in range(max_y):      #find all locations of the current literal
        for x in range(max_x):

            check = matrix[y][x]

            if check == literal:
                positions.append((y,x))

    result += positions     # all antennas themselve are now antinodes, so we can add them directly after we found them

    for i in positions:         # calculate all antinodes and append them to the output
        for j in positions:

            if i == j:
                continue

            y1 = i[0]
            y2 = j[0]
            x1 = i[1]
            x2 = j[1]

            dx = x1 - x2
            dy = y1 - y2

            tx = x1 + dx
            ty = y1 + dy

            while  max_x > tx >= 0 and max_y > ty >= 0:     # append antinodes in line until we are out of bounds
                result.append((ty, tx))
                tx += dx
                ty += dy


    return result


if __name__ == "__main__":
    matrix, word_list = get_data()
    counter = []

    for word in word_list:
        num = antinodes_trace(word)
        print(num)
        counter += num

    counter = len(set(counter))

    print(counter)
