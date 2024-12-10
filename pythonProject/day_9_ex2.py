
def get_data():

    result = []

    with open(r"day_9_data.txt", "r") as fl:
        line = fl.read()

    contingency = 0
    indexer = 1

    for i in line:

        if contingency % 2 == 0:
            result.append((indexer, int(i)))
            indexer += 1

        else:
            result.append((0, int(i)))

        contingency += 1

    return result


def whole_x_change():

    result = []
    visited = []

    for i in range(len(data))[::-1]:        # Go through the elements from behind

        if not data[i][0] or data[i][0] in visited:
            continue

        visited.append(data[i][0])

        last = data[i]

        for j in range(i):          # check previous elements if they are free

            first = data[j]

            if first[0]:       # check if the id is not 0 -> is a file
                continue

            elif first[1] >= last[1]:       # if free space, check if there is enough space available
                data[j] = (0, first[1] - last[1])   # replace the old data with the new one
                data.pop(i)
                data.insert(j, last)
                break

    for i in data:
        size = i[1]
        id_ = i[0]


        if id_ != 0:
            while size:
                result.append(id_-1)
                size -= 1
        else:
            while size:
                result.append(0)
                size -= 1

    return result




if __name__ == "__main__":
    data = get_data()
    sorted_list = whole_x_change()
    print(sorted_list)
    end_result = sum([sorted_list[i] * i for i in range(len(sorted_list))])

    print(end_result)

