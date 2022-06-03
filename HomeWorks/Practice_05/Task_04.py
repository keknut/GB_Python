# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Функция чтения файла.
# Если файла с оригинальными данными не будет,
# создаст новый с тестовыми данными.
# Если появится неизвестная ошибка, сообщит об этом в консоль
def read_file(path):
    try:
        print('------\nOpening file with original data...')
        file = open(path, 'r')
        data = file.read()
        print('------\nFile opened successfully\n------')
        file.close()
    except FileNotFoundError:
        print('------\nFile not found!\nCreating a file with a test data set\n------')
        file = open(path, 'w')
        data = 'AAbbaaaaBBBBaaBBccVv'
        file.write(data)
        file.close()
    except Exception:
        print("Something gone wrong!")
    return data

# Функция записи в файл. Записывает в файл данные.
def write_file(path, data_encode):
    data = open(path, 'w')
    data.write(data_encode)
    data.close()

# Функция rle алгоритма. Кодирует оригинальные данные в виде текста,
# возвращает строку с данными в новом, закодированном формате.
def rle_encode(data):
    encoding = ''
    prev_char = data[0]
    count = 0

    if not data: return ''

    for char in data:
        if char == prev_char:
            count += 1
            prev_char = char
        else:
            encoding += str(count) + prev_char
            count = 1
            prev_char = char
    encoding += str(count) + prev_char
    return encoding

# Функция декодирования rle закодировнныех данных.
# Возвращает строку с декодированными данными.
def rle_decode(data):
    if not data: return ''
    result = ''
    for i in range(0, len(data), 2):
        result += data[i + 1] * int(data[i])
    return result


path_original_data = 'GB_Python\HomeWorks\Practice_05\Practice_05_Task_04_original_data.txt'
path_encode_data = 'GB_Python\HomeWorks\Practice_05\Practice_05_Task_04_encode_data.txt'
path_decode_data = 'GB_Python\HomeWorks\Practice_05\Practice_05_Task_04_decode_data.txt'
data = read_file(path_original_data)
print(f'Original data: {data}')

data = rle_encode(data)
write_file(path_encode_data, data)
print(f'Encode data: {data}')

data = rle_decode(data)
write_file(path_decode_data, data)
print(f'Decode data: {data}')
