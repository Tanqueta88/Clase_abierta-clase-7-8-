import unittest #libreria que ejecuta las pruebas propiamente dichas
from selenium import webdriver #libreria que aporta a muchos lenguajes
from clase_abierta.pageindex import PageIndex
from pageItems import PageItems
# Aca agrego un comentario para probar subir cambios en el archivo a Git

class SearchCases(unittest.TestCase): #las clases se definen con la palabra reservada CLASS

    def setUp(self): #METODO SUTUP:se ejecuta antes de cada prueba (Precondicion)
        self.driver = webdriver.Chrome('/home/daniel/workspaces/fogar-testing/Automation - Clases/chromedriver')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.indexPage = PageIndex(self.driver)  # crea el objeto del tipo PageItems= indexPage
        self.itemsPage = PageItems(self.driver)
        #self.driver.maximize_window() #maximi ventana
        #self.driver.set_window_size(800, 600) #tamaño de ventana

    def test_search_no_elements(self): #los metodos se definen con la palabra reservada DEF
        self.indexPage.search('hola')
        self.assertEqual(self.itemsPage.return_no_element_text(), "No results were found for your search \"hola\"")

    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())

    def test_selections(self):
        self.indexPage.search('t-shirt')
        self.itemsPage.select_by_text('Product Name: A to Z')
        time.sleep(3)

    def tearDown(self): #METODO TEARDOWN: Se ejecuta al terminar cada prueba (post condicio)
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
