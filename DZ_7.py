import json

profit = {}
average_profit = {}
sum_prof = 0
i = 0
with open("text_DZ_7.txt", "r") as f_obj:
    my_list = f_obj.readlines()
    for el in my_list:
        el = el.split()
        prof = int(el[2]) - int(el[3])
        profit.update({el[0]: prof})
        if profit.setdefault(el[0]) >= 0:
            sum_prof = sum_prof + profit.setdefault(el[0])
            i +=1
    if i <= 0:
        print('Средней прибыли нет.')
    else:
        average_profit.update({'average_profit': round(sum_prof/i)})
    print(f"Прибыль каждой компании: {profit}; Средняя прибыльрибыль: {average_profit}")

with open("my_file_DZ_7.json", "w") as write_f:
    json.dump(profit, write_f)
    json.dump(average_profit, write_f)
    