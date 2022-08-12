# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest




class GoogleSearchUnitTest(unittest.TestCase): #Creo una clase que hereda de UnitTest para realizar el test
    @classmethod
    def setUpClass(cls): #Defino un setUp, esto es lo que pasará una vez siempre antes de ejecutar el test
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)

    @classmethod
    def test_googleSearch(self): #Defino el test
        self.driver.get("https://www.google.com/")
        self.inputBuscar = self.driver.find_element_by_name("q")
        self.inputBuscar.send_keys("Python")
        self.inputBuscar.send_keys(Keys.ENTER)

    @classmethod
    def tearDownClass(cls): #Defino el tearDownClass, que es lo que se sucederá siempre al finalizar el test
        cls.driver.close()
        print("Test finished")












