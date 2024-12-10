import re


def get_data():

    matrix = []
    raw_ = []

    with open(r"day_4_data_var1", "r") as fl:
        for line in fl:
            matrix.append([i for i in line])
            raw_.append(line.strip())
    return matrix, raw_


def find_xmas():

    result = 0          #Area for variables
    max_y = len(data)
    max_x = len(data[-1])

    for line in raw:        # Check for all occurrences in line
        match1 = re.findall(r"(XMAS)", line)
        match2 = re.findall(r"(SAMX)", line)
        result += len(match1) + len(match2)

    for y in range(max_y):      # Iterate through the matrix
        for x in range(max_x):

            if data[y][x] == 'X':        # Now check all remaining 6 direktions

                if y >= 3:       # Check upwards
                    if data[y-1][x] == 'M' and data[y-2][x] == 'A' and data[y-3][x] == 'S':
                        result += 1

                if y < max_y - 3:       # Check downwards
                    if data[y+1][x] == 'M' and data[y+2][x] == 'A' and data[y+3][x] == 'S':
                        result += 1

                if y >= 3 and x >= 3:        #check upper left
                    if data[y-1][x-1] == 'M' and data[y-2][x-2] == 'A' and data[y-3][x-3] == 'S':
                        result += 1

                if y < max_y - 3 and x >= 3:        #check lower left
                    if data[y+1][x-1] == 'M' and data[y+2][x-2] == 'A' and data[y+3][x-3] == 'S':
                        result += 1

                if y >= 3 and x < max_x - 3:        # Check upper right
                    if data[y-1][x+1] == 'M' and data[y-2][x+2] == 'A' and data[y-3][x+3] == 'S':
                        result += 1

                if y < max_y - 3 and x < max_x - 3:     # Check lower right
                    if data[y+1][x+1] == 'M' and data[y+2][x+2] == 'A' and data[y+3][x+3] == 'S':
                        result += 1

    return result


def find_cross_mas():

    result = 0
    max_x = len(data[-1])
    max_y = len(data)

    for y in range(max_y):
        for x in range(max_x):

            if data[y][x] != "A" or x == 0 or x == max_x-1 or y == 0 or y == max_y-1:
                continue


            low_right = data[y+1][x+1] + data[y][x] + data[y-1][x-1]
            low_left = data[y+1][x-1] + data[y][x] + data[y-1][x+1]

            if (low_right == "MAS" or low_right[::-1] == "MAS") and (low_left == "MAS" or low_left[::-1] == "MAS"):
                result += 1

    return result


if __name__ == "__main__":
    data, raw = get_data()

    print(find_xmas())
    #print(find_cross_mas())

    #print(raw)
