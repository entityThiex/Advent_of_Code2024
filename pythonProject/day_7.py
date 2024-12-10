
def get_data():
    result = []
    with open(r"day_7_data.txt", "r") as fl:
        for line in fl:
            line = line.split(":")

            left = int(line[0])
            right = line[1]

            operands = right.strip()
            operands = [int(x) for x in operands.split()]

            result.append((left, operands))

    return result


def brute_force(check: int, op: list[int], result=0):

    if check == result and len(op) == 0:
        return check
    elif len(op) == 0:
        return 0

    if result == 0:
        result = op.pop(0)

    next_ = op[0]

    return brute_force(check, op[1:], result + next_) or brute_force(check, op[1:], result * next_)


def brute_force2(check: int, op: list[int], result=0):

    if check == result and len(op) == 0:
        return check
    elif len(op) == 0:
        return 0

    if result == 0:
        result = op.pop(0)

    next_ = op[0]



    return brute_force2(check, op[1:], result + next_) or brute_force2(check, op[1:], result * next_) or brute_force2(check, op[1:], int(str(result) + str(next_)))


if __name__ == "__main__":

    data = get_data()
    counter = 0

    for i in data:
        sol = brute_force2(i[0], i[1])
        print(sol)
        counter += sol

    print(counter)
