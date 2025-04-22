import pytest

from .main import BooksCollector


class TestBooksCollector:

    # Проверка добавления одной книги в словарь books_genre
    def test_add_new_book_add_one_book(self):
        collection = BooksCollector()
        collection.add_new_book('Война и мир')
        assert len(collection.get_books_genre()) == 1

    # Негативная проверка добавления книги с именем в 0 символов и более 40 символов
    @pytest.mark.parametrize('book',['','ВойнаиМирВойнаиМирВойнаиМирВойнаиМирВойнаиМир'])
    def test_add_new_book_wrong_name_not_added(self,book):
        collection = BooksCollector()
        collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 0

    # Негативная проверка повторного добавления книги в словарь books_genre
    def test_add_new_book_same_book_not_added(self):
        collection = BooksCollector()
        collection.add_new_book('Война и мир')
        collection.add_new_book('Война и мир')
        assert len(collection.get_books_genre()) == 1

    # Проверка на установление жанра книге из списка genre
    def test_set_book_genre_set_genre(self):
        book = 'Гарри Поттер'
        genre = 'Фантастика'
        collection = BooksCollector()
        collection.add_new_book(book)
        collection.set_book_genre(book,genre)
        assert  collection.books_genre.get(book) == genre

    # Проверка получения жанра книги по её имени
    def test_get_book_genre_genre_appeared(self):
        book = 'Гарри Поттер'
        genre = 'Фантастика'
        collection = BooksCollector()
        collection.add_new_book(book)
        collection.set_book_genre(book,genre)
        assert  collection.get_book_genre(book) == genre

    # Негативная проверка на установление жанра книге не из списка genre
    def test_set_book_genre_not_set_other_genre(self):
        book = 'Война и мир'
        genre = 'Роман'
        collection = BooksCollector()
        collection.add_new_book(book)
        collection.set_book_genre(book,genre)
        assert not collection.get_book_genre(book)

    # Проверка вывода книги с определённым жанром
    def test_get_books_with_specific_genre_receive_books(self):
        collection = BooksCollector()
        books = ['Оно','Гарри Поттер','Убийство в "Восточном экспрессе"']
        genres = ['Ужасы','Фантастика','Детективы']
        for book in books:
            collection.add_new_book(book)

        for i in range(len(books)):
            collection.set_book_genre(books[i], genres[i])
        assert collection.get_books_with_specific_genre('Ужасы') == ['Оно']

    # Проверка вывода книг с жанром, подходящих для детей
    def test_get_books_for_children_receive_books(self):
        collection = BooksCollector()
        books = ['Оно','Гарри Поттер','Убийство в "Восточном экспрессе"']
        genres = ['Ужасы','Фантастика','Детективы']
        for book in books:
            collection.add_new_book(book)

        for i in range(len(books)):
            collection.set_book_genre(books[i], genres[i])

        books_for_children = collection.get_books_for_children()
        assert 'Гарри Поттер' in books_for_children and len(books_for_children) == 1

    # Проверка добавления книги в Избранное
    def test_add_book_in_favorites_book_added(self):
        collection = BooksCollector()
        book ='Война и мир'
        collection.add_new_book(book)
        collection.add_book_in_favorites(book)
        assert len(collection.favorites) == 1

    # Проверка получения списка книг из Избранного
    def test_get_list_of_favorites_books_favorites_appeared(self):
        collection = BooksCollector()
        book ='Война и мир'
        collection.add_new_book(book)
        collection.add_book_in_favorites(book)
        assert collection.get_list_of_favorites_books() == ['Война и мир']

    # Проверка удаления книги из Избранного
    def test_delete_book_from_favorites_book_deleted(self):
        collection = BooksCollector()
        book ='Война и мир'
        collection.add_new_book(book)
        collection.add_book_in_favorites(book)
        collection.delete_book_from_favorites(book)
        assert len(collection.favorites) == 0