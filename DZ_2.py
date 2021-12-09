with open("text_DZ_2.txt", "r") as f_obj:
    i = 0
    for line in f_obj:
        i += 1
        print(f"Количество слов в строке № {i}: {len(line.split())}")
    print(f"Общее количество строк: {i}")
