from pages.ad_page import AdPage
from pages.favorite_page import FavoritePage

AD_LINK = 'https://www.avito.ru/moskva/vakansii/komplektovschikgruzchik_3287546788'

class Test:

    def test_1(self, driver):
        ad = AdPage(driver, AD_LINK)
        ad.open()
        ad.add_favorite()
        btn_txt = ad.get_result()

        assert btn_txt == 'В избранном'

        link = ad.get_link_to_favorites()
        favorites = FavoritePage(driver, link)
        favorites.open()
        ads_list = favorites.get_ads_list()

        assert ads_list is not None

        categories_num = favorites.get_categories()

        assert int(categories_num[-1]) == 1

    def test_2(self, driver):
        pass

    def test_3(self, driver):
        pass

    def test_4(self, driver):
        pass

    def test_5(self, driver):
        pass
