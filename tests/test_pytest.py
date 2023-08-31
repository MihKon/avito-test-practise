from pages.favorite_page import FavoritesPage

class Test:

    def test_favorites(self, driver):
        favorites = FavoritesPage(driver, 'https://www.avito.ru/moskva/vakansii/komplektovschikgruzchik_3287546788')
        favorites.open()
        favorites.add_favorite()
        btn_txt = favorites.get_result()
        assert btn_txt == 'В избранном'