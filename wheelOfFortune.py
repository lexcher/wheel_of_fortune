import random

def finds_the_same_letters(user_answer, word):
    '''Находит и возврощает список с индексами повторяющихся символов'''
    return [idx for idx, ch in enumerate(word) if user_answer == ch]

def user_attempts_choice(user_attempts):
    '''Количество попыток'''
    return {1: 7, 2: 5, 3: 3}.get(user_attempts)

list_of_words = ['книга', 'месяц', 'ручка', 'шарик', 'носок', 'месяц', 'олень']

while len(list_of_words) != 0:
    word = random.choice(list_of_words)
    crypto_word = ['\u25A0'] * len(word)
    user_attempts = int(input('Выберите уровень сложности: 1-легкий; 2-средний; 3-сложный: '))
    attempts_count = user_attempts_choice(user_attempts)
    print(f'У вас {attempts_count} попыток.')
    print(f'В слове {len(word)} букв.')
    while '\u25A0' in crypto_word:
        if attempts_count == 0:
            print('К сожалению у вас закончились попытки.')
            break
        user_answer = input('Введите букву или слово целиком: ').lower()
        if user_answer == word:
            break
        letter_list = finds_the_same_letters(user_answer, word)
        if len(letter_list):
            for i in letter_list:
                crypto_word[i] = user_answer
            print(' '.join(crypto_word))
        else:
            print(f'К сожалению буквы "{user_answer}" нет в этом слове.')
            attempts_count -= 1
            print(f'У вас осталось "{attempts_count}" попыток.')
    print(f'Поздравляем, это и правда слово "{word}".')
    list_of_words.remove(word)
    if input('Продолжить: д/н? ').lower() != 'д':
        break
print('Поздравляем, игра окончена.')