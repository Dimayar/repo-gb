my_dict = {}

with open("text_DZ_6.txt", "r") as f_obj:
    my_list = f_obj.readlines()
    for i in my_list:
        subject, lecture, practice, *lab = i.split()
        my_dict[subject] = int(lecture) + int(practice) + int(*lab)
print(f"Предметы и общее количество занятий: {my_dict}")
