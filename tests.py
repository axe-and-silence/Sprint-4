from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
          
        # Примечание: В заготовке из GitHub комментарий изначально был написан так "словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2"
        #, но это ошибочный комментарий, т.к. в main.py отсутствует метод get_books_rating. get_books_rating был заменен на get_books_genre как метод, позволяющий 
        # пройти проверку метода add_new_book
        
        #словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
   
    def test_add_new_book_check_empty_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книгу
        collector.add_new_book('Синий Трактор')
        
        # вызываем метод get_books_genre, чтобы проверить, что метод add_new_book добавляет книгу с пустым жанром
        assert collector.get_books_genre() ==  {'Синий Трактор': ''}   
    
    # создаем параметризацию из значений списка genre     
    def test_get_books_with_specific_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        
        # добавляем произвольную книгу
        collector.add_new_book('Осколки Чести')
 
        # добавленной в предыдущем шаге книге назначаем произвольный жанр входящий в список genre
        collector.set_book_genre('Осколки Чести','Фантастика')
        
        # проверяем, что при передачи в метод get_book_genre аргумента в виде жанра из предыдущего шага возвращается нужная книга
        assert collector.get_books_with_specific_genre('Фантастика') == ['Осколки Чести']
    
    def test_get_books_with_specific_genre_multigenre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        
        # добавляем произвольные книги
        collector.add_new_book('Осколки Чести')
        collector.add_new_book('Стальная Крыса')
        collector.add_new_book('Синий Трактор')
        
        # добавленным в предыдущем шаге книгам назначаем жанр входящий в список genre
        collector.set_book_genre('Осколки Чести','Фантастика')
        collector.set_book_genre('Стальная Крыса','Фантастика')
        collector.set_book_genre('Синий Трактор','Мультфильмы')
        
        #проверяем, что при передаче в аргументе жанра "Фантастика" нам возвращаются добавленнык книги Осколки Чести, Стальная Крыса
        assert collector.get_books_with_specific_genre('Фантастика') == ['Осколки Чести', 'Стальная Крыса']
         
    def test_get_books_for_children(self):
        
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        
        # добавляем произвольные книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Двенадцать стульев')
        collector.add_new_book('Синий Трактор')
        collector.add_new_book('Осколки Чести')
        
        # добавленным в предыдущем шаге книгам назначаем жанр входящий в список genre
        collector.set_book_genre('Двенадцать стульев','Комедии')
        collector.set_book_genre('Синий Трактор','Мультфильмы')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Детективы')
        collector.set_book_genre('Осколки Чести','Фантастика')
        
        # проверяем что метод выдаёт список книг, жанр которых входит в genre_age_rating
        assert collector.get_books_for_children() == ['Двенадцать стульев', 'Синий Трактор','Осколки Чести']
    
    def test_add_book_in_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        
        # добавляем произвольные книги
        collector.add_new_book('Синий Трактор')
        
        # добавленной в предыдущем шаге книге назначаем произвольный жанр входящий в список genre
        collector.set_book_genre('Синий Трактор','Мультфильмы')
        
        # пользуясь методом add_book_in_favorites добавляем произвольные книги в список favorites используя книги из списка books_genre, отсуствующие в books_genre, дубли
        collector.add_book_in_favorites('Синий Трактор')
        
        # проверяем, что метод get_list_of_favorites_books возващает только те 2 книги, которые были в books_genre и нет дублей
        assert collector.get_list_of_favorites_books() == ['Синий Трактор']
    
    def test_delete_book_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        
        # добавляем книгу
        collector.add_new_book('Двенадцать стульев')
        
        # добавленной в предыдущем шаге книге назначаем произвольный жанр входящий в список genre
        collector.set_book_genre('Двенадцать стульев','Комедии')
        
        # добавляем эти 2 книги в список favorites
        collector.add_book_in_favorites('Двенадцать стульев')
        
        # пользуясь методом delete_book_from_favorites удаляем одну из книг
        collector.delete_book_from_favorites('Двенадцать стульев')
        
        # проверяем, что метод get_list_of_favorites_books возвращает пустой список
        assert collector.get_list_of_favorites_books() == []
    
    def test_get_books_genre_without_genre(self):
            # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Война и Мир')
        
        # добавленной в предыдущем шаге книге назначаем произвольный жанр НЕ ВХОДЯЩИЙ в список genre
        collector.set_book_genre('Война и Мир','Роман')
        
        # проверяем, что метод get_books_genre возвращает словарь,в котором есть книга, но нет жанра, поскольку метод set_book_genre не добавляет жанры вне списка genre
        assert collector.get_books_genre() ==  {'Война и Мир': ''}
                 
    def test_get_book_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        
        # добавляем произвольные книги
        collector.add_new_book('Двенадцать стульев')
 
        # добавленным в предыдущем шаге книгам назначаем все жанры входящий в список genre
        collector.set_book_genre('Двенадцать стульев','Комедии')
        
        # проверяем, что при передачи в метод get_book_genre аргумента в виде книги из предыыдущего шага нам возвращается конкретный жанр
        assert collector.get_book_genre('Двенадцать стульев') == 'Комедии'
    
    #Создаем параметризацию с произвольными длинными названиями книг    
    @pytest.mark.parametrize('longname',['12345678901234567890123456789012345678901', 'Книга с Очень Длинным Названием Созданная', 'Ещё Одна Книга с Оченб Длинным Названием '])
    def test_add_book_longname(self,longname):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()    
        
        # добавляем произвольные книги
        collector.add_new_book(longname)
        
        # проверяем что ни одна книга не добавилась и словарь пуст
        assert collector.get_books_genre() == {}
        
    @pytest.mark.parametrize('validname',['Бам', 'Бум', 'Пседво длинное название но не до конца а'])
    def test_add_book_validname(self,validname):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()    
        
        # добавляем произвольные книги
        collector.add_new_book(validname)
        
        # проверяем, что все название из параметризации прошли проверку и добавились в словарь
        assert len(collector.get_books_genre()) == 1
