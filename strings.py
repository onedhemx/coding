import unittest
from collections import Counter

# ================== Основные функции обработки строк ==================

def process_string(text):
    """Преобразует строку, считает буквы 'а', заменяет пробелы на '-'"""
    upper_text = text.upper()
    a_count = text.lower().count('a')
    dashed_text = text.replace(' ', '-')
    return upper_text, a_count, dashed_text

def split_and_print(text):
    """Разбивает строку на слова и выводит их"""
    words = text.split()
    print("\nРазбиение строки на слова:")
    for i, word in enumerate(words, 1):
        print(f"Слово {i}: {word}")
    return words  # Возвращаем список слов для тестирования

def fix_sentence(sentence):
    """Проверяет и исправляет оформление предложения"""
    if not sentence:
        return ""
    
    # Исправление первой буквы
    fixed = sentence[0].upper() + sentence[1:] if sentence else ""
    
    # Проверка последнего символа
    if fixed and fixed[-1] not in {'.', '!', '?'}:
        fixed += '.'
    
    return fixed

# ================== Дополнительные функции из предыдущего задания ==================

def word_count(text):
    """Возвращает количество слов в строке"""
    return len(text.split())

def unique_words(text):
    """Возвращает отсортированный список уникальных слов"""
    words = [word.lower() for word in text.split()]
    return sorted(set(words)) if text else []

def most_frequent_word(text):
    """Возвращает самое частое слово"""
    if not text:
        return ''
    words = [word.lower() for word in text.split()]
    word_counts = Counter(words)
    max_count = max(word_counts.values())
    most_common = [word for word, count in word_counts.items() if count == max_count]
    return most_common[0]

# ================== Тестирование ==================

class TestStringFunctions(unittest.TestCase):
    def test_process_string(self):
        upper, count, dashed = process_string("a b c A B C")
        self.assertEqual(upper, "A B C A B C")
        self.assertEqual(count, 2)
        self.assertEqual(dashed, "a-b-c-A-B-C")
    
    def test_split_and_print(self):
        words = split_and_print("раз два три")
        self.assertEqual(words, ["раз", "два", "три"])
    
    def test_fix_sentence(self):
        self.assertEqual(fix_sentence("тест"), "Тест.")
        self.assertEqual(fix_sentence("Тест"), "Тест.")
        self.assertEqual(fix_sentence("Тест!"), "Тест!")
        self.assertEqual(fix_sentence(""), "")
    
    def test_word_count(self):
        self.assertEqual(word_count("Hello world"), 2)
        self.assertEqual(word_count("   Hello   world   "), 2)
    
    def test_unique_words(self):
        self.assertEqual(unique_words("Hi hi HI"), ['hi'])
        self.assertEqual(unique_words("apple banana Apple"), ['apple', 'banana'])
    
    def test_most_frequent_word(self):
        self.assertIn(most_frequent_word("a b a c b a"), ['a'])
        self.assertIn(most_frequent_word("x y z"), ['x', 'y', 'z'])

# ================== Примеры использования ==================

if __name__ == '__main__':
    print("=== Примеры использования функций ===")
    
    # 1. Обработка строки
    sample_text = "Пример строки для обработки"
    upper, a_count, dashed = process_string(sample_text)
    print(f"\n1. Обработка строки '{sample_text}':")
    print(f"• Верхний регистр: {upper}")
    print(f"• Количество 'а': {a_count}")
    print(f"• С дефисами: {dashed}")
    
    # 2. Разбиение на слова
    print("\n2. Разбиение строки на слова:")
    split_and_print("Раз два три четыре пять")
    
    # 3. Исправление предложения
    sentences = [
        "это предложение без заглавной буквы",
        "Это предложение без точки в конце",
        "Всё правильно оформлено!",
        ""
    ]
    print("\n3. Исправление предложений:")
    for s in sentences:
        print(f"До: '{s}'")
        print(f"После: '{fix_sentence(s)}'")
    
    # 4. Тестирование дополнительных функций
    print("\n4. Дополнительные функции:")
    text = "Cat cat dog DOG dog"
    print(f"Слов в '{text}': {word_count(text)}")
    print(f"Уникальные слова: {unique_words(text)}")
    print(f"Самое частое слово: {most_frequent_word(text)}")
    
    # Запуск тестов
    print("\n=== Запуск тестов ===")
    unittest.main(argv=[''], exit=False)
