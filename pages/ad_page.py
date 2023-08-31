import time
from pages.base_page import BasePage
from locators.ad_page_locator import AdPageLocators as Locators

class AdPage(BasePage):
    
    def add_favorite(self):
        self.element_is_visible(Locators.ADD_FAVORITE_BTN, 7).click()

    def get_result(self):
        btn = self.element_is_visible(Locators.ADD_FAVORITE_BTN)
        return btn.text
    
    def get_link_to_favorites(self):
        return self.element_is_visible(Locators.FAVORITE_ICON).get_attribute('href')