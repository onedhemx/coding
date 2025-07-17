import unittest
from collections import Counter

def word_count(text):
    """Возвращает количество слов в строке text."""
    return len(text.split())

def unique_words(text):
    """Возвращает отсортированный список уникальных слов в нижнем регистре."""
    words = [word.lower() for word in text.split()]
    return sorted(set(words)) if text else []

def most_frequent_word(text):
    """Возвращает самое частое слово (любое из них при равенстве частот)."""
    if not text:
        return ''
    words = [word.lower() for word in text.split()]
    word_counts = Counter(words)
    max_count = max(word_counts.values())
    most_common = [word for word, count in word_counts.items() if count == max_count]
    return most_common[0]  # Возвращаем первое из самых частых

class TestTextFunctions(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("Hello world"), 2)
        self.assertEqual(word_count("   Hello   world   "), 2)
        self.assertEqual(word_count(""), 0)
        self.assertEqual(word_count("One"), 1)
        self.assertEqual(word_count("Multiple     spaces here"), 3)

    def test_unique_words(self):
        self.assertEqual(unique_words("Hi hi HI"), ['hi'])
        self.assertEqual(unique_words("apple banana Apple"), ['apple', 'banana'])
        self.assertEqual(unique_words(""), [])
        self.assertEqual(unique_words("zebra apple banana"), ['apple', 'banana', 'zebra'])

    def test_most_frequent_word(self):
        # Проверяем, что результат входит в допустимые варианты
        self.assertIn(most_frequent_word("a b a c b a"), ['a'])
        self.assertIn(most_frequent_word("x y z"), ['x', 'y', 'z'])
        self.assertEqual(most_frequent_word(""), '')
        self.assertIn(most_frequent_word("Cat cat dog DOG dog"), ['cat', 'dog'])

if __name__ == '__main__':
    unittest.main()
