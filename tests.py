from main import BooksCollector
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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()



    @pytest.mark.parametrize("book_name", [
        "Interesting Book",
        "A" * 40,
    ])
    def test_add_new_book(collector,book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize("book_name", [
        "A" * 41,
        "",
    ])
    def test_add_invalid_book_names(collector,book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize("book_name, genre", [
        ("Harry Potter", "Фантастика"),
        ("Peter Rabbit", "Комедии"),
    ])
    def test_set_book_genre(collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre(book_name) == genre

    @pytest.mark.parametrize("book_name, genre", [
        ("Gone with the wind", "Ужасы"),
    ])
    def test_set_invalid_book_genre(collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre(book_name) == ""


    @pytest.mark.parametrize("books_and_genres, target_genre", [
        ([("Big Little Lies", "Детективы"), ("Sherlock Holmes", "Детективы")], "Детективы"),
        ([("Piter Pan", "Мультфильмы"), ("Treasure Island", "Детективы")], "Ужасы"),
    ])
    def test_get_books_with_specific_genre(collector, books_and_genres, target_genre):
        for book, genre in books_and_genres:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        result = collector.get_books_with_specific_genre(target_genre)
        assert all(collector.get_book_genre(book) == target_genre for book in result)


    @pytest.mark.parametrize("books_and_genres", [
        [("Peter Pan", "Мультфильмы"), ("It", "Ужасы")],
        [("It", "Ужасы"), ("Sherlock", "Детективы")],
    ])
    def test_get_books_for_children(collector, books_and_genres):
        for book, genre in books_and_genres:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        children_books = collector.get_books_for_children()
        assert all(collector.get_book_genre(book) not in collector.genre_age_rating for book in children_books)

    @pytest.mark.parametrize("book_name", [
        "Piter Pan",
        "Horizont",
    ])
    def test_add_book_in_favorites(collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_already_in_favorites(collector):
        collector.add_new_book("Piter Pan")
        collector.add_book_in_favorites("Piter Pan")
        collector.add_book_in_favorites("Piter Pan")
        assert collector.get_list_of_favorites_books().count("Piter Pan") == 1

    def test_delete_book_from_favorites(collector):
        collector.delete_book_from_favorites("Horizont")
        assert "Horizont" not in collector.get_list_of_favorites_books()


