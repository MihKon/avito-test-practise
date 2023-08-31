import time
from pages.ad_page import AdPage
from pages.favorite_page import FavoritePage

AD_LINK = 'https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363'

class Test:

    def test(self, driver):
        ad = AdPage(driver, AD_LINK)
        ad.open()
        btn_favorite = ad.add_favorite()

        assert btn_favorite == 'true'

        link = ad.get_link_to_favorites_icon()
        favorites = FavoritePage(driver, link)
        favorites.open()
        ads_list = favorites.get_ads_list()

        assert ads_list is not None

        categories_num = favorites.get_categories()

        assert int(categories_num[-1]) == 1