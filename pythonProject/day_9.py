
def get_data():

    result = []

    with open(r"day_9_data.txt", "r") as fl:

        line = fl.read()

    mi = 0
    even = 0

    for i in line:

        i = int(i)

        if even % 2 == 0:

            while i:
                result.append(mi)
                i -= 1

            even += 1
            mi += 1

        else:
            while i:
                result.append(".")
                i -= 1

            even += 1

    return result


def compact_list():

    result = []
    length = len(data)
    rev = [x for x in data[::-1] if x != "."]

    for i in range(length):

        if data[i] != ".":      # not specific enough, last two elements are duplicates
            if data[i] not in rev:
                return result

            result.append(data[i])

        else:

            result.append(rev.pop(0))

    return result


if __name__ == "__main__":

    data = get_data()

    sorted_list = compact_list()
    print(sorted_list)
    end_result = sum([sorted_list[i] * i for i in range(len(sorted_list))])

    print(end_result)
