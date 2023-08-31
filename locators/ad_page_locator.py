from selenium.webdriver.common.by import By

class AdPageLocators:

    ADD_FAVORITE_BTN = (
        By.XPATH,
        '/html/body/div[1]/div/div[3]/div[1]/div/div[3]/'\
        'div[4]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button'
    )

    FAVORITE_ICON = (
        By.XPATH,
        '/html/body/div[1]/div/div[1]/div/div/div[1]/a[1]'
    )