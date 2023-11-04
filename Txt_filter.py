"""
Задание:
Написать программу, которая предлагает пользователю выбрать текстовый фильтр и применить его к набранному тексту.

Описание: Твоя задача — создать меню для выбора текстовых фильтров. Каждый фильтр изменяет введённый текст согласно
своей функциональности. Тебе нужно сделать меню, которое предлагает пользователю выбрать текстовый фильтр из не менее
трёх предложенных вариантов и применять его к тексту. Какие это могут быть фильтры, выбирай сам(а)!

Задачи: Придумай идеи для фильтров и описания к ним. Это может быть КРИЧАЩИЙ ФИЛЬТР или шепчущий фильтр.
Или🙂же🙂фильтр,🙂который🙂разделяет🙂слова🙂смайлами. УдИвИ_нАс! Собери все фильтры, их названия и описания в один
словарь. Выведи меню с фильтрами из словаря. Напиши цикл, который позволяет пользователю выбирать фильтры для
применения, пока он не решит выйти из программы. Если пользователь выбирает фильтр, программа должна предоставить ему
описание выбранного фильтра и спросить, хочет ли он применить фильтр к тексту. Если пользователь соглашается,
программа должна запросить текст, к которому будет применён выбранный фильтр, и вывести результат применения фильтра.
А если пользователь не соглашается, нужно снова показать ему меню. Если пользователь выбирает «Выход»,
программа должна завершиться."""


def validate(list_values):
    choice = input(language[lang]['input']).lower()
    while choice.lower() not in list_values:
        choice = input(f'{language[lang]['input error']}{list_values}\n{language[lang]['input']}').lower()
    return choice


def validateint(list_values):
    while True:
        try:
            choice = int(input(language[lang]['input']))
        except ValueError:
            print(language[lang]['input error'])
        else:
            if choice in list_values:
                break
            else:
                print(language[lang]['input error'])
    return choice


def caps(txt):
    return txt.upper()


def gost(txt):
    sentences = txt.split('.')
    gosted_sentences = []
    for sentence in sentences:
        gostedd_sentences = sentence.strip().capitalize()
        gosted_sentences.append(gostedd_sentences + '. ')
    done_txt = ''.join(gosted_sentences)
    return done_txt


def fence(txt):
    spl_txt = list(txt.lower())
    k = 0
    new_txt = []
    for letter in spl_txt:
        if k % 2 == 0:
            new_txt.append(letter.upper())
        else:
            new_txt.append(letter)
        k += 1
    done_txt = ''.join(new_txt)
    return done_txt


def ice(txt):
    return txt.replace(' ', '🍦', txt.count(' '))


language = {
    'ru': {
        'hi': 'Привет тут ты можешь применить фильтры к тексту и тем самым его стилизовать.',
        'choosing': 'Выбери из списка что тебе приглянулось.',
        'qw': 'Ты хочешь этот фильтр?',
        'yn': ['да', 'нет'],
        'input': 'Ввод: ',
        'input error': 'Пожалуйста, выберите из предложенных вариантов ',
    },
    'en': {
        'hi': 'Hi here you can apply filters to the text and thereby stylize it',
        'choosing': 'Choose from the list what you liked.',
        'qw': 'Do you want this filter?',
        'yn': ['yes', 'no'],
        'input': 'Input: ',
        'input error': 'Please choose from the suggested options ',
    }
}

masks = {
    'masks_en': {
        1: {
            'name': 'CAPS',
            'description': 'Makes all letters BIG',
            'filter': caps
        },
        2: {
            'name': 'GOST',
            'description': 'Everything after the dot gets big. Does everything according to GOST.',
            'filter': gost
        },
        3: {
            'name': 'FeNcE',
            'description': 'WeLl, WhAt cAn i sAy fEnCe',
            'filter': fence
        },
        4: {
            'name': 'I🍦Want🍦Ice🍦Cream',
            'description': 'Instead🍦of🍦space🍦ice🍦cream',
            'filter': ice
        },
        5: {
            'name': 'Exit',
            'description': 'Exit from program',
            'filter': exit
        }
    },

    'masks_ru': {
        1: {
            'name': 'КАПС',
            'description': 'Делает все буквы БОЛЬШИМИ',
            'filter': caps
        },
        2: {
            'name': 'ГОСТ',
            'description': 'Все после точки становится большим. Делает все по ГОСТу.',
            'filter': gost
        },
        3: {
            'name': 'ЗаБоР',
            'description': 'Ну чТо тУт сКаЗаТь зАбОр',
            'filter': fence
        },
        4: {
            'name': 'Я🍦Хочу🍦Мороженку',
            'description': 'Вместо🍦пробела🍦мороженка',
            'filter': ice
        },
        5: {
            'name': 'Выход',
            'description': 'Выход из программы',
            'filter': exit
        }
    }
}

lang = 'en'
print('Hi User! chose language. / Привет Пользователь! выбери язык.\n'
      'Ru/En')
lang = validate(['ru', 'en'])
mask_lg = 'masks_' + lang
print(language[lang]['hi'])
while True:
    print(language[lang]['choosing'])
    for option in masks[mask_lg]:
        print(f'{option}) {masks[mask_lg][option]['name']}')
    option = validateint(masks[mask_lg].keys())
    print(f'{masks[mask_lg][option]['name']}\n{masks[mask_lg][option]['description']}', language[lang]['qw'], sep='\n')
    qw = validate(language[lang]['yn'])
    if qw == language[lang]['yn'][0]:
        print(masks[mask_lg][option]['filter'](input(language[lang]['input'])))
