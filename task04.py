# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def RleZip(text): # Функция сжатия
    if len(text) < 1: return ''
    s = ''
    prev_char= text[0] # тут храним пердыдущий символ в тексте
    count = 0 # счетчик числа вхождения символа в исходном тексте
    for char in text:
        if prev_char != char: # символ поменялся - поэтому записываем его
            s += prev_char+str(count) # пишем символ, и сколько раз он встретился
            prev_char = char
            count = 1 # новый символ и уже встретился 1 раз
        else:
            if count == 9:  # т.к. после одного символа стоит только одна цифра - поэтому
                            #  больше 9 символов подряяд не делаем.
                s += prev_char+str(count) # грузим сжатый символ в строку
                count = 1
            else:
                count += 1
    s += char+str(count) # обрабатываем последный символ
    return s

def RleUnZip(text): #  функция распаковки файла
    ret = [text[i:i+2] for i in range(0, len(text), 2)] # делим текст на список по 2 символа
    return "".join(ret[i][0]*int(ret[i][1]) for i in range(len(ret))) # пишем строку по i символов
                                                                      # подряд для каждой пары

with open('kolobok_orig.txt','r', encoding='UTF-8') as f: # читаем оригинальный файл
    text = f.read()

with open('kolobok.rle','w', encoding='UTF-8') as f: # Сжимаем текст и пишем его в файл
    f.write(RleZip(text))

with open('kolobok.rle','r', encoding='UTF-8') as f: #  Читаем сжатый файл и расжимаем его
    text = RleUnZip(f.read())

with open('kolobok_unzip.txt','w', encoding='UTF-8') as f: # Пишем расжатый текст в новый файл
    f.write(text)

# плохо жмет - в тексте мало одинаковых символов подряд идет... вот картинки всякие - другое дело
