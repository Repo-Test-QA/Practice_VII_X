from selenium.webdriver.common.by import By

class PageItem:
    def __init__(self, my_driver):
        self.quantity = (By.ID, 'quantity_wanted')
        self.plus = (By.CLASS_NAME, 'icon-plus')
        self.driver = my_driver

    def enter_quantity(self, quantity):
        # Antes de ingresar la cantidad, vamos a limpiar la caja de texto.
        self.driver.find_element(*self.quantity).clear()
        self.driver.find_element(*self.quantity).send_keys(quantity)

    # Vamos a crear un método donde vamos a clickear n veces y yo le diga cuantas veces se va a clickear
    def add_elements(self, clicks):
        # Pasamos la cantidad de veces a hacer click, es un integer porque se va a realizar una operación con esta
        for i in range(clicks):
            self.driver.find_element(*self.plus).click()

    # Este método devuelve el valor que tengo en el campo de texto para verificar
    # que el valor es 28 (cantidad ingresada 25 + nro de clicks sobre el botón 3)
    def get_number_of_elements(self):
        # Vamos a corroborar que es un valor y no un texto. Nos vamos a traer el valor.
        # get_attribute => no solo sirve para traer el atributo value, sino también para otros atributos del elemento
        return self.driver.find_element(*self.quantity).get_attribute('value')