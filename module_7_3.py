class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name_ in self.file_names:
            with open(file_name_, encoding='utf-8') as file_:
                words_list = []
                for line_ in file_:
                    line_ = line_.lower().strip()

                    for punctuation_mark in [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']:
                        line_ = line_.replace(punctuation_mark, '')

                    if line_.__len__() > 0:
                        words_list += line_.split(' ')


            all_words.__setitem__(file_name_, words_list)

        return all_words


    def find(self, word_):
        all_pos ={}
        for name_, words_ in self.get_all_words().items():
            pos_ = words_.index(word_.lower()) + 1

            if pos_ > 0:
                all_pos.__setitem__(name_, pos_)

        return all_pos


    def count(self, word_):
        all_counters = {}
        for name_, words_ in self.get_all_words().items():
            quantity_ = words_.count(word_.lower())
            if quantity_ > 0:
                all_counters.__setitem__(name_, quantity_)

        return all_counters

# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
