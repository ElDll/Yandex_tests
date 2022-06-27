from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//div[@class='desk-notif-card__login-new-items']/a")
    DISK_BUTTON = (By.XPATH, '//a[@class="home-link home-link_black_yes"]')


class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//*[(@id = "passp-field-login")]')
    LOGIN_PHONE_FIELD = (By.XPATH, '//input[@placeholder]')
    SWITCH_EMAIL_BUTTON= (By.XPATH, '//button[@data-type="login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@class="Textinput-Control"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@class="Button2 Button2_size_l Button2_view_action Button2_width_max Button2_'
                              'type_submit"]')


class DiskPageLocators:
    CLOSE_ADVERTISING = (By.XPATH, '//button[@class="Button2 Button2_size_m Subscription-Onboarding-Close"]')

    CREATE_BUTTON = (By.XPATH, '//button')

    CREATE_FOLDER_BUTTON = (By.XPATH, '//div[@class="create-resource-popup-with-anchor__create-items"]/button[1]')
    CREATE_FOLDER_INPUT_NAME = (By.XPATH, '//input[@value="Новая папка"]')
    CREATE_FOLDER_SAVE_BUTTON = (By.XPATH, '//div[@class="confirmation-dialog__footer"]/button')

    CREATE_DOCUMENT_BUTTON = (By.XPATH, '//div[@class="create-resource-popup-with-anchor__create-items"]/button[2]')




