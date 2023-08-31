from time import sleep
from pages.base_page import BasePage
from locators.ad_page_locator import AdPageLocators as Locators

class AdPage(BasePage):
    
    def add_favorite(self):
        btn = self.element_is_visible(Locators.ADD_FAVORITE_BTN, 7)
        btn.click()
        sleep(2)
        return btn.get_attribute('data-is-favorite')

    # def get_result(self):
    #     return self.element_is_visible(Locators.ADD_FAVORITE_BTN).get_attribute('data-is-favorite')
    
    def get_link_to_favorites_icon(self):
        return self.element_is_visible(Locators.FAVORITE_ICON).get_attribute('href')
    
    # def get_link_to_favorites_hwin(self):
    #     return self.element_is_visible(Locators.HIDE_WINDOW).get_attribute('href')