with open("text_DZ_3.txt", "r") as f_obj:
    
    mini = ''
    income = []
    for salary in f_obj:
        salary = salary.split()
        income.append(int(salary[2]))
        medium = sum(income)/len(income)
        if int(salary[2]) < 20000:
            mini += str(salary[0]) + ', '
print(f"Оклад менее 20 тыс. руб. : {mini[:-2]}")
print(f"Средняя величина дохода сотрудников: {medium} руб.")
