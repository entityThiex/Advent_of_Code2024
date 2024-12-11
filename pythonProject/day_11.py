from functools import cache


def get_data():

    with open(r"day_11_data.txt", "r") as fl:
        inp = fl.read()

    inp = inp.strip().split()
    result = [int(x) for x in inp]

    return result


def stone_dance(n: int):

    global stones

    for _ in range(n):

        rolling_stones = []

        for stone in stones:

            literal = str(stone)

            if stone == 0:
                rolling_stones.append(1)

            elif len(literal) % 2 == 0:

                middle = len(literal) // 2

                rolling_stones.append(int(literal[:middle]))
                rolling_stones.append(int(literal[middle:]))

            else:
                new_stone = stone * 2024

                rolling_stones.append(new_stone)

        stones = rolling_stones

@cache
def stone_parade(stone: int, n=75):
    literal = str(stone)

    if n == 0:
        return 1

    if stone == 0:
        return stone_parade(1, n-1)
    elif len(literal) % 2 == 0:
        middle = len(literal) // 2
        return stone_parade(int(literal[:middle]), n-1) + stone_parade(int(literal[middle:]), n-1)
    else:
        return stone_parade(stone * 2024, n-1)


if __name__ == "__main__":

    stones = get_data()
    #stone_dance(75)

    counter = 0
    for i in stones:
        counter += stone_parade(i)

    print(counter)
    print(len(stones))
