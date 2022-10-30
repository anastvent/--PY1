def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha() == True:
            letters = ""
            letters += letter
            dict_[letter] = str_.count(letter)
    return dict_

def percentage(dict_):
    sum_ = sum(dict_.values())
    for key, percent in dict_.items():
        dict_[key] = round(percent / sum_ * 100, 2)
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
