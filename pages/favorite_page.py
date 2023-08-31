import time
from pages.base_page import BasePage
from locators.favorite_page_locator import FavoritePageLocators as Locators

class FavoritesPage(BasePage):
    
    def add_favorite(self):
        self.element_is_visible(Locators.FAVORITE_BTN).click()
        time.sleep(2)

    def get_result(self):
        btn = self.element_is_visible(Locators.FAVORITE_BTN)
        return btn.text