import re


def get_data():

    with open(r"day_17_data.txt", "r") as fl:
        file = fl.read()
        lines = file.split("\n\n")

        register = re.findall(r"([0-9]+)", lines[0])
        op_list = lines[1].split()[1].strip().split(",")

    a = int(register[0])
    b = int(register[1])
    c = int(register[2])

    return a,b,c, op_list


def eval_combo(com:str):
    combo_operand = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 'A',
        '5': 'B',
        '6': 'C'
    }

    result = combo_operand[com]

    if not isinstance(result, int):
        if result == 'A':
            result = A
        elif result == 'B':
            result = B
        else:
            result = 'C'

    return result


def adv(combo:str):

    global A
    numerator = A

    combo = eval_combo(combo)

    A = numerator // (2 ** combo)


def bxl(literal:str):

    global B
    literal = int(literal)

    B = B ^ literal


def bst(combo:str):

    global B
    combo = eval_combo(combo)

    B = (combo % 8)


def jnz(literal:str):

    literal = int(literal)

    if A != 0:
        global pointer
        pointer = literal
        return True
    else:
        return False


def bxc(literal:str):
    global B

    B = B ^ C


def out(combo:str):

    combo = eval_combo(combo)
    output.append(combo % 8)


def bdv(combo:str):

    global B
    combo = eval_combo(combo)

    B = A // (2 ** combo)


def cdv(combo:str):

    global C
    combo = eval_combo(combo)

    C = A // (2 ** combo)


def eval_debugger():

    global pointer

    while pointer < instruction_set:

        operator = instructions[pointer]
        operand = instructions[pointer+1]

        if operator == '3':

            result = eval_operator[operator](operand)

            if result:
                continue

        else:
            eval_operator[operator](operand)
        pointer += 2

    out_value = ",".join(map(str, output))
    return out_value
    #print(out_value)


def reset():
    global A,B,C,pointer,output

    A = 0
    B = 0
    C = 0
    pointer = 0
    output = []


def duplicate_program():

    global A
    queue = [(1,0)]
    result = []

    while queue:
        index, item_a = queue.pop(0)
        for a in range(item_a, item_a+8):       # go through all possible base 8 values
            reset()
            A = a
            test = eval_debugger()
            test2 = ",".join(instructions[-index:])
            if test == test2:
                queue.append((index+1, a * 8))      # go to the next level of base 8 values
                if index == instruction_set:
                    result.append(a)
                    break

    print(min(result))



if __name__ == "__main__":

    A, B, C, instructions = get_data()
    counter = 0
    pointer = 0
    output = []
    instruction_set = len(instructions)
    eval_operator = {
        '0': adv,
        '1': bxl,
        '2': bst,
        '3': jnz,
        '4': bxc,
        '5': out,
        '6': bdv,
        '7': cdv
    }

    #eval_debugger()
    duplicate_program()
