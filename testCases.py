from selenium import webdriver
import unittest
from pageIndex import PageIndex
from pageResult import PageResult
from pageItem import PageItem
import time


class TestCase(unittest.TestCase):

    # Precondiciones
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)

        # Creamos un objeto de la clase PageIndex
        self.indexPage = PageIndex(self.driver)
        # Creamos un objeto de la clase PageResult
        self.resultPage = PageResult(self.driver)
        # Creamos un objeto de la clase PageItem
        self.itemPage = PageItem(self.driver)

    @unittest.skip('Not need now')
    def test_search_no_elements(self):
        self.indexPage.search('Hola')
        self.assertEqual(self.resultPage.return_no_element_text(), 'No results were found for your search "Hola"')

    @unittest.skip('Not need now')
    def test_search_find_dresses(self):
        self.indexPage.search('Dress')
        self.assertTrue('DRESS' in self.resultPage.return_section_title())

    @unittest.skip('Not need now')
    def test_search_find_tshirts(self):
        self.indexPage.search('T-Shirts')
        self.assertTrue('T-SHIRTS' in self.resultPage.return_section_title(), self.resultPage.return_section_title())

    @unittest.skip('Not need now')
    def test_tarea(self):
        self.indexPage.search('T-Shirts')
        self.resultPage.click_orange_button()
        self.itemPage.enter_quantity('25')
        self.itemPage.add_elements(3)
        # Asigno a una variable lo que devuelve el método (28), en este caso el valor del elemento
        number = self.itemPage.get_number_of_elements()
        # Verificamos me diante el assert si el valor es igual a 28 (lo que nosotros sabemos)
        self.assertTrue(number == '28')

        # Vamos a agregar unos segundos para verificar que se muestre la cantidad ingresada
        # time.sleep(3)

    def test_selection(self):
        self.indexPage.search('T-Shirts')
        # Seleccionamos el elemento por el texto, es decir el parámetro text
        self.resultPage.select_by_text('Product Name: A to Z')
        time.sleep(3)

        # Seleccionamos el elemento por el valor, es decir el parámetro value
        self.resultPage.select_by_value('reference:asc')
        time.sleep(3)

        # Seleccionamos el elemento por el indice (4 => Product Name: Z to A), es decir el parámetro number
        self.resultPage.select_by_index(4)
        time.sleep(3)



    # Postcondiciones, que quiero que pase, cuando termina una prueba.
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()








