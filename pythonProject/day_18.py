
def get_data():

    result = []

    with open(r"day_18_data.txt", "r") as fl:
        for line in fl:

            line = line.strip()
            result.append(tuple(map(int,line.split(","))))
    return result


def find_path(by:int):

    queue = [(0,0,0)]
    visited = [(0,0)]
    finished = []
    kb = data[:by]

    while queue:

        possible = []
        x,y,score = queue.pop(0)

        if (x,y) == (70,70):
            finished.append(score)
            continue

        if x > 0 and (x-1,y) not in kb:
            possible.append((x-1,y, score+1))
        if x < max_size and (x+1,y) not in kb:
            possible.append((x+1,y, score+1))
        if y > 0 and (x,y-1) not in kb:
            possible.append((x, y-1, score+1))
        if y < max_size and (x,y+1) not in kb:
            possible.append((x, y+1, score+1))

        for i in possible:
            if i[:-1] not in visited:
                queue.append(i)
                visited.append(i[:-1])

    if len(finished) == 0:
        return 0

    return min(finished)


def is_way():

    upper = len(data)
    lower = 0
    remodeled = data.copy()

    while remodeled:

        middle = lower + (upper - lower) // 2
        if not lower < middle < upper:
            return lower + 1

        result = find_path(middle)

        if result:
            lower = middle
        else:
            upper = middle

    return 0


if __name__ == "__main__":

    data = get_data()
    max_size = 70
    no_way = 1

    #print(is_way())


    print(find_path(1))
    print(data[1])
