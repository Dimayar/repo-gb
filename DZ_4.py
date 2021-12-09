my_dict = {'One' : 'Один',
       'Two' : 'Два',
       'Three' : 'Три',
       'Four' : 'Четыре'}
new_file = []

with open("text_DZ_4.txt", "r") as f_obj:
    my_list = f_obj.readlines()
    for i in my_list:
        i = i.split(' ')
        new_file.append(my_dict.get(i[0]) + ' ' + i[1] + ' ' + i[2])
with open("text_DZ_4_new.txt", "w") as f_obj:
    f_obj.writelines(new_file)
