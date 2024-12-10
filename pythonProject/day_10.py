
def get_data():

    result = []

    with open(r"day_10_data.txt", "r") as fl:
        for line in fl:
            result.append([int(x) for x in line])




