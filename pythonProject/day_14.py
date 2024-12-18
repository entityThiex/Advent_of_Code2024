import re


def get_data():

    result = []

    with open(r"day_14_data.txt", "r") as fl:
        for line in fl:

            line = line.strip()
            bot_pos = tuple(map(int ,re.findall(r"(-*\d+)", line)))
            result.append(bot_pos)

    return result


def move_single_robot(bot:tuple[int,int,int,int]):

    pos_x, pos_y, vec_x, vec_y = bot

    for _ in range(100):

        pos_x += vec_x
        pos_y += vec_y

        if pos_y > max_y:
            pos_y -= max_y +1
        if pos_y < 0:
            pos_y += max_y +1

        if pos_x > max_x:
            pos_x -= max_x +1
        if pos_x < 0:
            pos_x += max_x +1

    if pos_x < 50:
        if pos_y < 51:
            quarter[1] += 1
        elif pos_y > 51:
            quarter[3] += 1

    elif pos_x > 50:
        if pos_y < 51:
            quarter[2] += 1
        elif pos_y > 51:
            quarter[4] += 1


def move_all_bots():

    global data

    for bot_index in range(len(data)):

        bot = data[bot_index]
        pos_x, pos_y, vec_x, vec_y = bot

        pos_x += vec_x
        pos_y += vec_y

        if pos_y > max_y:
            pos_y -= max_y + 1
        if pos_y < 0:
            pos_y += max_y + 1

        if pos_x > max_x:
            pos_x -= max_x + 1
        if pos_x < 0:
            pos_x += max_x + 1

        data[bot_index] = (pos_x, pos_y,vec_x,vec_y)


def visualize():
    mapped = []

    bot_positions = [(x,y) for x,y,dx,dy in data]

    for y in range(103):
        line = ""
        for x in range(101):

            if (x,y) in bot_positions:
                line += '#'
            else:
                line += '.'
        line += '\n'
        mapped.append(line)

    with open(r"frame.txt", "w") as fl:
        fl.writelines(mapped)


def build_a_fucking_christmas_tree():

    global data
    #data.sort(key=lambda tup: tup[1])
    counter = 0

    for _ in range(90):
        move_all_bots()

    while True:

        move_all_bots()

        visualize()

        inp = input("Continue?")

        if inp == 'c':
            print(counter)
        elif inp == 'q':
            break

        counter += 1


def locate_tree(n:int):

    all_ = []

    for time in range(n):

        move_all_bots()
        quarts = {x: 0 for x in [1, 2, 3, 4]}

        for i in data:

            pos_x, pos_y, vec_x, vec_y = i

            if pos_x < 50:
                if pos_y < 51:
                    quarts[1] += 1
                elif pos_y > 51:
                    quarts[3] += 1

            elif pos_x > 50:
                if pos_y < 51:
                    quarts[2] += 1
                elif pos_y > 51:
                    quarts[4] += 1

        summed = quarts[1] * quarts[2] * quarts[3] * quarts[4]

        all_.append((summed, time))
        print(summed, time)

    print(min(all_))


if __name__ == "__main__":

    quarter = {x:0 for x in [1, 2, 3, 4]}
    data = get_data()
    max_x = 100
    max_y = 102

    #locate_tree(1000000)

    for _ in range(7):
        move_all_bots()
    visualize()

    #build_a_fucking_christmas_tree()

    #for i in range(len(data)):
     #   bot_ = data[i]
      #  move_single_robot(bot_)

    #summed = quarter[1] * quarter[2] * quarter[3] * quarter[4]
    #print(summed)

    #  false
