from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageIndex:

    def __init__(self, my_driver):
        self.query_top = (By.ID, 'search_query_top')
        self.query_button = (By.NAME, 'submit_search')
        self.driver = my_driver

    def search(self, item):
        try:
            search_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top))
            search_box.send_keys(item)
            search_button = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(self.query_button))
            search_button.click()
        except:
            print('No se encuentra el elemento')





