# Задача "Найдёт везде"

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):                # Метод по созданию словаря со всеми словами
        all_words = {}
        for i in range(len(self.file_names)):
            with open(self.file_names[i], 'r', encoding='utf-8') as file:
                string = file.read().replace('\n', ' ').replace('\r', ' ')
                symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for symbol in symbols_to_remove:
                    string = string.replace(symbol, '')
                all_words[self.file_names[i]] = string.split()
        return all_words

    def find(self, word):                   # Метод, который возвращает позицию первого вхождения слова в текст
        word_position = {}
        for i in self.get_all_words():
            word_position[i] = [item.lower() for item in self.get_all_words()[i]].index(word.lower()) + 1
        return word_position

    def count(self, word):                  # Метод, который возвращает количество вхождений слова в текст
        word_count = {}
        for i in self.get_all_words():
            word_count[i] = [item.lower() for item in self.get_all_words()[i]].count(word.lower())
        return word_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
