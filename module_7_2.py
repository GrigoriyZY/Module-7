# Задача "Записать и запомнить"

def custom_write(file_name: str, strings: list):            # Функция записи в файл строк
    file = open(file_name, 'w', encoding="utf-8")
    strings_positions = {}
    line = 1
    for i in range(len(strings)):
        cursor_position = (line, file.tell())               # Определяем позицию курсора
        file.write(f'{strings[i]}\n')
        strings_positions[cursor_position] = strings[i]     # Формируем словарь
        line += 1
    file.close()
    return strings_positions


info = [                                                    # Выполняемый код
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
