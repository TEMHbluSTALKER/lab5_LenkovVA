import re
import random
import time
#Функции
###################################################
def TaskSelection():
    print("Выберите номер задачи:\n"
          "1 - Страны и столицы.\n"
          "2 - Игра Эрудит.\n"
          "3 - Студенты и иностранные языки.")
    number = input()
    match number:
        case "1":
            CountriesAndCapitals()
        case "2":
            ScrabbleGame()
        case "3":
            StudentsAndForeignLanguages()
        case _:
            print("Введен неправильный номер.")
            TaskSelection()

###################################################
def CountriesAndCapitals():
    Countries = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин",
                "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава",
                "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                "Северная Македония": "Скопье", "Сербия": "Белград"}
    for key in Countries:
        print(key, " - ", Countries[key])
    print('---------------------------------')
    while 1 == 1:
        try:
            SelectedCountry = input('Введите название страны: ')
            print(Countries[SelectedCountry])
        except KeyError:
            print('Введена неправильная страна.')
        else:
            break
    print('---------------------------------')
    print('Отсортированный словарь:')
    for key in sorted(Countries):
        print(key, " - ", Countries[key])
###################################################

def ScrabbleGame():
    Alphabet = {"авеинорст": 1,
                "дклмпу": 2,
                "бгёья": 3,
                "йы": 4,
                "жзхцч": 5,
                "шэю": 8,
                "фщъ": 10}
    Sum = 0
    while 1==1:
        Word = input('Введите слово: ')
        Word = Word.lower()
        pattern = re.fullmatch(r"[а-яё]{1,}", Word)
        if pattern:
            break
    for i in Word:
        for key, value in Alphabet.items():
            if i in key:
                Sum += value
                break
    print('Стоимость слова', Sum, 'баллов.')
###################################################

def StudentsAndForeignLanguages():
    languages = ["Русский", "Английский", "Французский", "Немецкий", "Китайский", "Японский", "Корейский", "Испанский", "Польский", "Чешский"]
    languagesNum = ["0-Русский", "1-Английский", "2-Французский", "3-Немецкий", "4-Китайский", "5-Японский", "6-Корейский", "7-Испанский", "8-Польский", "9-Чешский"]
    students = []
    print('Введите фамилии студентов (вводятся через ENTER, для прекращения ввода введите STOP).')
    BreakOutFlag = False
    while 1 == 1:
        while 1==1:
            Word = input('Введите фамилию студента: ')
            if Word == 'stop':
                BreakOutFlag = True
                break
            pattern = re.fullmatch(r"[а-яёА-ЯЁ]{1,}", Word)
            if pattern:
                students.append(Word)
                break
        if BreakOutFlag:
            break
    print('Список студентов:')
    print(students)
    print('Внесите информацию по владению языками каждым из студентов (Введите номера языков из списка, начиная с 0).')
    print('Список доступных языков:')
    print(languagesNum)
    StudentsLanguages = []
    for i in students:
        print('Введите сколькими языками владеет', i)
        counter = input()
        counter = int(counter)
        for j in range(1, counter+1):
            print('Введите номер', j, 'языка.')
            while 1==1:
                try:
                    Number = input()
                    Number = int(Number)
                    StudentsLanguages.append(languages[Number])
                except ValueError:
                    print('Введен неправильный номер.')
                else:
                    break
    NumberOfStudentsWhoKnowChinese = StudentsLanguages.count('Китайский')
    StudentsLanguages = sorted(set(StudentsLanguages))
    print('Студенты знают', len(StudentsLanguages), 'языков:')
    print(StudentsLanguages)
    print('Количество студентов, знающих китайский:', NumberOfStudentsWhoKnowChinese)
###################################################

#Основная программа
TaskSelection()
