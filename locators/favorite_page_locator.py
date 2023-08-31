from selenium.webdriver.common.by import By

class FavoritePageLocators:

    FAVORITE_ADS_LIST = (
        By.XPATH,
        '/html/body/div[1]/div/div[4]/div/div/'\
        'favorite-items-list/div/div/div[1]/div[2]/div/div'
    )

    ADS_CATEGORIES_NUM = (
        By.XPATH,
        '/html/body/div[1]/div/div[4]/div/div/'\
        'favorite-items-list/div/div/div[1]/div[1]/'\
        'div/div/div[1]/div/div/ul/li[1]/button'
    )