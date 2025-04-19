# Финальный проект 4-ого спринта

**Проверка добавления одной книги в словарь "books_genre":**

* test_add_new_book_add_one_book

**Негативная проверка добавления книги с именем в 0 символов и более 40 символов:**

* test_add_new_book_wrong_name_not_added

**Негативная проверка повторного добавления книги в словарь "books_genre":**

* test_add_new_book_same_book_not_added

**Проверка на установление жанра книге из списка "genre":**

* test_set_book_genre_set_genre

**Негативная проверка на установление жанра книге не из списка "genre":**

* test_set_book_genre_not_set_other_genre

**Проверка вывода книги с определённым жанром:**

* test_get_books_with_specific_genre_receive_books

**Проверка вывода книг с жанром, подходящих для детей:**

* test_get_books_for_children_receive_books

**Проверка добавления книги в Избранное:**

* test_add_book_in_favorites_book_added

**Проверка удаления книги из Избранного:**

* test_delete_book_from_favorites_book_deleted
