from sorting_algorithms import bubble_sort, quick_sort, insertion_sort
from random import sample

empty_list = []
single_list = [13]
double_list = [19, 2]
long_list = sample(range(-1000, 1001), 500)
word_list = open("word_list.txt", "r").read().splitlines()

class TestBubble:
    def test_empty(self):
        assert bubble_sort(empty_list.copy()) == sorted(empty_list.copy())

    def test_single(self):
        assert bubble_sort(single_list.copy()) == sorted(single_list.copy())

    def test_double(self):
        assert bubble_sort(double_list.copy()) == sorted(double_list.copy())

    def test_long(self):
        assert bubble_sort(long_list.copy()) == sorted(long_list.copy())

    def test_words(self):
        assert bubble_sort(word_list.copy()) == sorted(word_list.copy())

class TestQuick:
    def test_empty(self):
        assert quick_sort(empty_list.copy()) == sorted(empty_list.copy())

    def test_single(self):
        assert quick_sort(single_list.copy()) == sorted(single_list.copy())

    def test_double(self):
        assert quick_sort(double_list.copy()) == sorted(double_list.copy())

    def test_long(self):
        assert quick_sort(long_list.copy()) == sorted(long_list.copy())

    def test_words(self):
        assert quick_sort(word_list.copy()) == sorted(word_list.copy())

class TestInsertion:
    def test_empty(self):
        assert insertion_sort(empty_list.copy()) == sorted(empty_list.copy())

    def test_single(self):
        assert insertion_sort(single_list.copy()) == sorted(single_list.copy())

    def test_double(self):
        assert insertion_sort(double_list.copy()) == sorted(double_list.copy())

    def test_long(self):
        assert insertion_sort(long_list.copy()) == sorted(long_list.copy())

    def test_words(self):
        assert insertion_sort(word_list.copy()) == sorted(word_list.copy())
        
