import json

def get_curr_course(path="exchange/data/correct_course.json"):
    with open(path, 'r') as file:
        return json.load(file)


def get_bank(path="exchange/data/bank.json"):
    with open(path, 'r') as file:
        return json.load(file)


# TODO має бути можливисть робити знижку чи змінною чи манімуляцією з mul
def cal_cell_course(cource, mul):
    for curr_name in cource.keys():
        for sec_curr, rate in cource[curr_name]["buy"].items():
            cource[curr_name]["sell"].update({sec_curr: round(rate * (1 + mul), 2)})
    return cource


def exchange(amount, cource, operation, old_curr, new_curr):
    return amount * cource[old_curr][operation][new_curr]

def input_data(data, num=0, result=[], count=0):
    while num < len(data):
            if data[num]["question"]:
                input_value = input(data[num]["question"])
                if input_value == "reset":
                    return input_data(data)
                elif input_value == "back":
                    if count == 0:
                        num -= 1
                        result = result[:len(result) - 1]
                        continue
                    else:
                        num = num - count - 1
                        result = result[:len(result) - count - 1]
                        count = 0
                        continue
                if data[num]["func"]:
                    input_value = float(input_value)
                result.append(input_value)
                num += 1
            else:
                result.append(data[num]["fixture"])
                num += 1
                count += 1
    return result