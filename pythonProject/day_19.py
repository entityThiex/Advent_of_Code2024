from functools import cache


def get_data():

    pat = []
    col =''

    with open(r"day_19_data.txt", "r") as fl:

        dump = fl.readlines()

        for line in dump:
            if ',' in line:
                col = line.strip().replace(" ", "").split(',')
            elif line == '\n':
                continue
            else:
                line = line.strip()
                pat.append(line)

    return col, pat

@cache
def rec_comparison(to_comp:str):

    available = [x for x in colors if x in to_comp]

    middle_counter = 0

    if len(to_comp) == 0:
        return 1

    for towel in available:

        if to_comp[:len(towel)] == towel and rec_comparison(to_comp[len(towel):]):
            return 1

    return middle_counter


if __name__ == "__main__":

    colors, patterns = get_data()
    counter = 0

    for pattern in patterns:
        counter += rec_comparison(pattern)

    print(counter)
