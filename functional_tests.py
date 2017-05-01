import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys




GECKODRIVER_PATH = r'geckodriver/geckodriver.exe'
HOST_NAME = 'http://127.0.0.1:8000'


class AppointmentsTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=GECKODRIVER_PATH)

    def tearDown(self):
        self.browser.quit()

    def test_appointments_app(self):
        self.browser.get(HOST_NAME)
        
        self.assertIn('Записаться', self.browser.title)
        
        get_h2_data = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn('Форма для записи на прием к врачу', get_h2_data)

        get_all_h3_data = ' '.join(
            [i.text for i in self.browser.find_elements_by_tag_name('h3')]
            )
        self.assertIn('Выбор врача', get_all_h3_data)
        self.assertIn('Данные о пациенте', get_all_h3_data)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
