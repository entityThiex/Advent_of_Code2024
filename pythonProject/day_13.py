import re

def get_data():

    result = []

    with open(r"day_13_data.txt", "r") as fl:
        inp = fl.read()

    separate_games = inp.split("\n\n")      # split the input into the different games

    for i in separate_games:
        lines = i.split("\n")

        a = re.findall(r"X\+([0-9]+)|Y\+([0-9]+)", lines[0])    # get the x/y values from a game
        b = re.findall(r"X\+([0-9]+)|Y\+([0-9]+)", lines[1])
        p = re.findall(r"X=([0-9]+)|Y=([0-9]+)", lines[2])

        a = (int(a[0][0]), int(a[1][1]))        # turn the regex find into usable data
        b = (int(b[0][0]), int(b[1][1]))
        p = (int(p[0][0]), int(p[1][1]))

        result.append([a,b,p])      # append to the result

    return result


def find_least_tokens(gm:list[tuple[int,int]]):

    a = gm[0]
    b = gm[1]
    p = gm[2]

    numerator_x = p[0] // b[0] + 1
    numerator_y = p[1] // b[1] + 1

    numerator_b = min(numerator_x, numerator_y)

    while True:
        remainder_x = p[0] - b[0] * numerator_b
        remainder_y = p[1] - b[1] * numerator_b

        if (remainder_x % a[0]) == 0 and (remainder_y % a[1]) == 0:
            numerator_a = remainder_y // a[1]
            break

        if numerator_b < 0:
            return 0

        numerator_b -= 1

    if numerator_b > 100 or numerator_a > 100:
        return 0


    return numerator_a * 3 + numerator_b


if __name__ == "__main__":

    data = get_data()
    counter = 0

    for game in data:
        counter += find_least_tokens(game)

    print(counter)

    # too high 97005
    # correct 36838
    # too low 17322
