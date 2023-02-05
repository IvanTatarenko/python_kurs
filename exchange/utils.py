import json
from typing import  Union

def get_curr_course(path="exchange/data/correct_course.json") -> dict:
    """
    Отримуємо курс валют з файлу
    :param path: шлях до фалу
    :return: дані з файлу
    """
    with open(path, 'r') as file:
        return json.load(file)


def get_bank(path="exchange/data/bank.json") -> dict:
    """
    Отримуємо наявні купюри з файлу
    :param path: шлях до файлу
    :return: дані з файлу
    """
    with open(path, 'r') as file:
        return json.load(file)


# TODO має бути можливисть робити знижку чи змінною чи манімуляцією з mul
def cal_cell_course(cource: dict, mul: Union[int, float]) -> dict:
    """
    Рахує кус продажу
    :param cource: курс купівлі валют
    :param mul: коефіцієнт збільшення ціни продажу
    :return: курс купівлі та продажу
    """
    for curr_name in cource.keys():
        for sec_curr, rate in cource[curr_name]["buy"].items():
            cource[curr_name]["sell"].update({sec_curr: round(rate * (1 + mul), 2)})
    return cource


def exchange(amount: Union[int, float], cource: dict, operation: str, old_curr: str, new_curr: str) -> Union[int, float]:
    """
    Рахує обмін
    :param amount: сума обміну
    :param cource: поточний курс
    :param operation: вид операції обміну
    :param old_curr: валюта яку хочуть обміняти
    :param new_curr: валюта яка буде отримана
    :return: отримані гроші
    """
    return amount * cource[old_curr][operation][new_curr]

def input_data(data: dict, num=0, result=[], count=0) -> list:
    """
    Запитання для взаємодії з клієнтом
    :param data: запитання
    :param num: змінна для підрахунку пройдених запитань
    :param result: відповіді користувача
    :param count: пробущені пункти
    :return: відповіді користувача
    """
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