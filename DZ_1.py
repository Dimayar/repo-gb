with open("text_DZ_1.txt", "w") as f_obj:
    
    while True:
        word = input('Ведите слова: ')
        f_obj.writelines(word + '\n')
        if not word:
            break
