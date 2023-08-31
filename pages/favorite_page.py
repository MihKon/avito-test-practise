import time
from pages.base_page import BasePage
from locators.favorite_page_locator import FavoritePageLocators as Locators

class FavoritePage(BasePage):

    def get_ads_list(self):
        return self.element_is_visible(Locators.FAVORITE_ADS_LIST, 7)
    
    def get_categories(self):
        return self.element_is_visible(Locators.ADS_CATEGORIES_NUM).text