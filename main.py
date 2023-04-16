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
    students = {"Иванов", "Петров", "Смирнов", "Сидоров", "Васильев", "Кузнецов", "Попов", "Федоров", "Лебедев", "Семенов"}
    languages = {"Русский", "Английский", "Французский", "Немецкий", "Китайский"}

    lang_stud = {}

    for st in students:
        kolvo = random.randint(1, 3)
        lang_stud[st] = random.sample(list(languages), kolvo)

    unique_lang = set()
    for i in lang_stud:
        unique_lang = unique_lang.union(set(lang_stud[i]))

    # print(lang_stud)
    print("Множество различных языков, которые знают студенты: ", sorted(unique_lang), f" ({len(unique_lang)})")

    china = [i for i in lang_stud if "Китайский" in lang_stud[i]]
    print("Студенты, знающие китайский: ", china)






    languages = ["Русский", "Английский", "Французский", "Немецкий", "Китайский", "Японский", "Корейский", "Испанский", "Польский", "Чешский"]
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
    print(languages)
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
    print(sorted(set(StudentsLanguages)))
    print('Количество студентов, знающих китайский:', NumberOfStudentsWhoKnowChinese)





    stud = {"Mikel", "Tomas", "Jo"}
    studBase = {'name' : {'cLang' : 1, 'langs' : []}}
    StudentsLanguages = set()
    setOfChineseAgents = set()
    for i in stud:
        cLang = int(input(f"How many languages does {i} know? "))
        studBase[i] = {}
        studBase[i]['cLang'] = cLang
        studBase[i]['langs'] = []
        for x in range(cLang):
            lang = input(f"{i} knows ").lower()
            studBase[i]['langs'].append(lang)
            if lang not in languages:
                languages.add(lang)
            if lang == "chinese":
                setOfChineseAgents.add(i)
        print(f"{i} knows {studBase[i]['cLang']} langs and it {sorted(studBase[i]['langs'])}")
    print(f'{len(setOfChineseAgents)} student know chinese and it {setOfChineseAgents}')
    print(f"all languages that students know {sorted(languages)}")





###################################################

#Основная программа
TaskSelection()
