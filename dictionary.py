class LimitedDictionary:
    def __init__(self):
        self.dictionary = {}
        self.max_size = 10

    def add_word(self, word, meaning):
        if len(self.dictionary) >= self.max_size:
            print("Словарь полон! Невозможно добавить новое слово.")
            return
        if word in self.dictionary:
            print(f"Слово '{word}' уже есть в словаре. Его значение будет обновлено.")
        self.dictionary[word] = meaning
        print(f"Слово '{word}' успешно добавлено в словарь.")

    def get_meaning(self, word):
        return self.dictionary.get(word, "Такого слова нет в словаре.")

    def remove_word(self, word):
        if word in self.dictionary:
            del self.dictionary[word]
            print(f"Слово '{word}' успешно удалено из словаря.")
        else:
            print(f"Слово '{word}' отсутствует в словаре.")

    def display_dictionary(self):
        print("Текущий словарь:")
        for word, meaning in self.dictionary.items():
            print(f"{word}: {meaning}")
if __name__ == "__main__":
    ld = LimitedDictionary()
    ld.add_word("apple", "яблоко")
    ld.add_word("banana", "банан")
    ld.add_word("cat", "кошка")
    ld.add_word("dog", "собака")
    ld.add_word("elephant", "слон")
    ld.add_word("fish", "рыба")
    ld.add_word("giraffe", "жираф")
    ld.add_word("house", "дом")
    ld.add_word("ice", "лёд")
    ld.add_word("jacket", "куртка")
    ld.add_word("kite", "воздушный змей")
    print(ld.get_meaning("cat"))
    print(ld.get_meaning("kite"))
    ld.remove_word("banana")
    ld.remove_word("kite")
    ld.add_word("kite", "воздушный змей")

    ld.display_dictionary()
