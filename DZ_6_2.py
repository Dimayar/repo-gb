my_dict = {}
res = []

with open("text_DZ_6.txt", "r") as f_obj:
    my_list = f_obj.readlines()
    for i in my_list:
        i = i.split()
        for el in range(1, len(i)):
            res.append(int(i[el]))
        my_dict.update({i[0]: sum(res)})
        res.clear()
print(f"Предметы и общее количество занятий: {my_dict}")