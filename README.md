Список проверок:
test_add_new_book_add_two_books - проверяет add_new_book, в частности, что добавляется именно две книги (проверка методов add_new_book и get_books_genre)
test_add_new_book_check_empty_genre - проверяет, что при использовании метода add_new_book в словарь books_genre добавляется книга без жанра (проверка методов add_new_book и get_books_genre)
test_get_books_with_specific_genre - проверяет, что при передачи в метод get_book_genre аргумента в виде жанра из предыдущего шага возвращается нужная книга (проверка методов add_new_book, set_books_genre,get_books_with_specific_genre)  
test_get_books_with_specific_genre_multigenre - проверяет, что при наличии нескольких книг одного и разных жанра, метод get_books_with_specific_genre возвращает названия книг только конкретные жанры (проверка методов add_new_book, set_books_genre,get_books_with_specific_genre)
test_get_books_for_children - проверяет метод get_books_for_children выдаёт список книг, жанр которых входит в genre_age_rating (проверка методов add_new_book, set_books_genre,get_books_with_specific_genre)
test_add_book_in_favorites - проверяет метод add_book_in_favorites, через добавление книг из списка genre, вне списка genre и дублей (проверка методов add_new_book, set_books_genre,add_book_in_favorites,get_list_of_favorites_books)
test_delete_book_favorites - проверяет метод delete_book_favorites. добавляем 2 книги в список избранного и одну удалем, ожидаем, что в списке будет 1 одна книга (проверка методов add_new_book, set_books_genre,add_book_in_favorites,delete_book_from_favorites,get_list_of_favorites_books)
test_set_book_genre_without_genre - проверяем, что при попытке добавить к книге жанр вне списка genre значение остаётся пустым (проверка методов add_new_book, set_books_genre, get_books_genre)
test_get_book_genre - проверяет, что при передачи в метод get_book_genre аргумента в виде книги из предыыдущего шага нам возвращается конкретный жанр  (проверка методов add_new_book, get_book_genre)
test_add_book_longname - проверяет, что книги с длинными названиями не добавятся в словарь
test_add_book_validname - проверяет, что книги с валидными названиями добавляются в словарь
