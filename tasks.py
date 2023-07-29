tasks = [
    {
        "task": "Не лает не кусает, в дом не пускает",
        "answer": "Замок"
    },
    {
        "task": "Другая загадка",
        "answer": "Ответ"
    },
    {
        "task": "Не лает не кусает, в дом не пускает",
        "answer": "Замок"
    },
    {
        "task": "Не лает не кусает, в дом не пускает",
        "answer": "Замок"
    },
]


good_answers = 0
bad_answers = 0

for item in tasks:
    print(item)
    answer = input(item['task'] + ': ')
    print('Ваш ответ:', answer)
    if answer == item["answer"]:
        print("Ответ правильный")
        good_answers += 1
    else:
        print("Ответ неправильный")
        bad_answers += 1

print("Правильных ответов:", good_answers)
print("Неправильных ответов:", bad_answers)

print("Неправильных ответов:", bad_answers)