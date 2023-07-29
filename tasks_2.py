tasks = [
    ("Не лает не кусает, в дом не пускает", "Замок"),
    ("Другая загадка", "Ответ"),
]

good_answers = 0
bad_answers = 0

for item in tasks:

    answer = input(item[0] + ': ')
    if answer == item[1]:
        print("Ответ правильный")
        good_answers += 1
    else:
        print("Ответ неправильный")
        bad_answers += 1
print("Правильных ответов:", good_answers)
print("Неправильных ответов:", bad_answers)
