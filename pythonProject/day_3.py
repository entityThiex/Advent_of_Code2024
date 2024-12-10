import re


def get_data():
    with open(r"day_3_data.txt", "r") as file:
        data = file.read()
    return data


def find_mul():
    match = re.findall(r'mul\(([0-9]+,[0-9]+)\)', data)
    out = [[int(x) for x in pair.split(",")] for pair in match]
    return out


def mul_list(ls:list[list[int]]):
    counter = 0
    for i in ls:
        x = i[0]
        y = i[1]

        counter += x * y
    return counter


def get_instructions():
    match = re.findall(r"mul\(([0-9]+,[0-9]+)\)|(do\(\))|(don't\(\))", data)
    do = True
    muls = []
    for i in match:
        if 'do()' in i:
            do = True
            continue
        if "don't()" in i:
            do = False
            continue

        if do:
            muls.append(i[0])

    out = [[int(x) for x in pair.split(",")] for pair in muls]

    return out


if __name__ == '__main__':
    data = get_data()
    multiplications = get_instructions()
    result = mul_list(multiplications)

    print(result)


#get_data()
