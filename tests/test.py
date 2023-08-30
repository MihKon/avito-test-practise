from pages.favorite_page import FavoritesPage

class Test:

    def test_favorites(self, driver):
        favorites = FavoritesPage(driver, '')
        favorites.open()