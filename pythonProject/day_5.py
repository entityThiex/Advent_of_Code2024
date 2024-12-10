import random


def my_Ass():
    from functools import cmp_to_key

    rules, pages = open('day_5_data.txt').read().split('\n\n')
    cmp = cmp_to_key(lambda x, y: -(x + '|' + y in rules))

    a = [0, 0]
    for p in pages.split():
        p = p.split(',')
        s = sorted(p, key=cmp)
        a[p != s] += int(s[len(s) // 2])

    print(*a)


def get_data():
    with open(r"day_5_data.txt", "r") as fl:

        raw = fl.read()
        rls, upt = raw.split("\n\n")

        rls = [[int(j) for j in i.split("|")] for i in rls.split("\n")]
        upt = [[int(x) for x in u.split(",")] for u in upt.split("\n")]

    return rls, upt


#return the middle element of a given list
def get_middle(ls: list[int]):
    length = len(ls)
    index_middle = length // 2

    return ls[index_middle]


# Creates a dictionary with keys= rule elements and values = needed predeceasing numbers
def create_rule_table():

    result = {}

    for i in rules:
        left = i[0]
        right= i[1]

        if right in result.keys():
            result[right] = result[right] + [left]
        else:
            result[right] = [left]

    return result


def check_updates(update_: list[int]):

    applyable_rules = []

    for rule in rules:
        if rule[0] in update_ and rule[1] in update_:
            applyable_rules.append(rule)

    for rule in applyable_rules:
        slot_1 = update_.index(rule[0])
        slot_2 = update_.index(rule[1])

        if slot_2 < slot_1:
            return False
    return True


def sort_updates(update_: list[int]):

    already_used = []
    while not check_updates(update_):

        #while update_ in already_used:
        random.shuffle(update_)
        #already_used.append(update_.copy())

    return update_


if __name__ == "__main__":
    rules, updates = get_data()
    #rule_table = create_rule_table()
    counter = 0

    for update in updates:
        check = check_updates(update)

        if check:
            #counter += get_middle(update)
            continue

        my_Ass()
        #print(check, update, counter)

    #print(counter)

