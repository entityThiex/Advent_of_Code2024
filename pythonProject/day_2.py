
def get_data():     # getter for the data from day_2_data.txt
    with open(r"day_2_data_var1.txt", "r") as fl:
        out = fl.readlines()

    out = [[int(x) for x in line.split(" ")] for line in out]
    return out


def check_safety(data:list[int]):

    increase = False        # variable to check if the list is increasing or decreasing

    for i in range(len(data)):

        if i == len(data) - 1:     # Return 1 if the data is safe
            return 1

        num1 = data[i]      # Set needed variables
        num2 = data[i+1]
        _sum = num1 - num2

        if i == 0:      # Check cases in which the data would be unsafe and return 0 for such
            if num1 < num2:
                increase = True
        else:
            if increase:
                if num1 > num2:
                    return 0
            else:
                if num1 < num2:
                    return 0

        if _sum == 0 or _sum < -3 or _sum > 3:
            return 0

# Ignore this, was a try, smart_dampener_check works and is better
def dampener_check(data: list[int]):

    increase = data[0] < data[-1]

    for i in range(1, len(data)-1):

        if i == len(data) - 1:     # Return 1 if the data is safe
            return 1

        num1 = data[i-1]
        num2 = data[i]
        num3 = data[i+1]

        sum1 = num1 - num2
        sum2 = num2 - num3
        sum3 = num1 - num3

        if sum1 > sum2 and increase:        #check increasing or decreasing order
            if sum3 < 0:
                data.pop(i)
                return check_safety(data)
        elif sum1 < sum2 and not increase:
            if sum3 > 0:
                data.pop(i)
                return check_safety(data)

        if sum1 == 0:       #check if the first two numbers are equivalent, if so, delete the second
            if sum3 != 0:
                data.pop(i)
                return check_safety(data)

        if sum1 < -3 or sum1 > 3:
            if not sum3 < -3 and not sum3 > 3:
                data.pop(i)
                return check_safety(data)


def smart_dampener_check(data: list[int]):
    variants = [data[:i] + data[i+1:] for i in range(len(data))]
    return any([check_safety(x) for x in variants])


if __name__ == '__main__':     #driver code
    data = get_data()
    counter = 0

    for field in data:
        counter += check_safety(field)
    print(counter)


#print(get_data())
