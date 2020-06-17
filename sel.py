import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

imie = "janusz"
nazwisko = "json"
adres = " testowa 11"
kod = "11-111"
miasto = "Wroclaw"
emajl = "111@scb.p"
fon = "725000000"
loging = "jan666"
haszlo = "123jan99"

class TestEkobieca(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.ekobieca.pl')

    def test_invalid_email(self):
        driver = self.driver
        znajdz_zaloguj = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="account_link link hidden-phone"]'))).click()
        znajdz_buton = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn signin-form_register2"]'))).click()
        wybierz_osoba_prywatna = driver.find_element_by_xpath("//input[@id='client_type2']").click()
        wpisz_imie = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_firstname'))).send_keys(imie)
        wpisz_nazwisko = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'client_lastname'))).send_keys(nazwisko)
        wpisz_adres = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'client_street'))).send_keys(adres)
        wpisz_kod = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'client_zipcode'))).send_keys(kod)
        wpisz_miasto = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'client_city'))).send_keys(miasto)
        wpisz_mejla = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'client_email'))).send_keys(emajl)
        wpisz_telefon = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'client_phone'))).send_keys(fon)
        wpisz_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'client_login'))).send_keys(loging)
        wpisz_haslo = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'client_password'))).send_keys(haszlo)
        wpisz_ponownie_haslo = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'repeat_password'))).send_keys(haszlo)
        regulamin = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="terms_agree"]')))
        driver.execute_script("arguments[0].click();", akceptacja)
        zarejestruj = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="submit_clientnew_form"]')))
        driver.execute_script("arguments[0].click();", zarejestruj)


    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
