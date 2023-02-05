# TODO add bank calculation


from settings import INPUT_QUESTIONS
from utils import get_curr_course, cal_cell_course, exchange, input_data

# говоритиь що тут в нас скрипт який тре виконати
if __name__ == "__main__":
    
    #отримуємо курс купівлі та рахуємо курс продажу
    cource = get_curr_course()
    cource = cal_cell_course(cource, 0.05)
    
    # Вивід курсів валют
    print(f"{'':*^17}")
    print(f"*{'BUY':^5}{'':5}{'SELL':^5}*")
    for i in cource['UAH']['buy']:
        print(f"*{cource['UAH']['buy'][i]:<6.2f}{i:^3}{cource['UAH']['sell'][i]:>6.2f}*")
    print(f"{'':*^17}")
    


    amount, op, old_curr, new_curr = input_data(INPUT_QUESTIONS)
    new_ammount = exchange(amount, cource, op, old_curr, new_curr)
    print(f"We will {op} {amount} {new_curr} for {new_ammount} {old_curr}")