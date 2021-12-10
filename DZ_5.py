from random import randint

with open("text_DZ_5.txt", "w") as f_obj:
    
    numbers = ''
    for el in range(1, 5):
        numbers += str(randint(1, 100)) + ' '
    f_obj.writelines(numbers)
    
with open("text_DZ_5.txt", "r") as f_obj:
    my_numb = f_obj.readlines()
    for line in my_numb:
        result = line.split()
print(f"Общая сумма: {sum(map(int, result))}")
