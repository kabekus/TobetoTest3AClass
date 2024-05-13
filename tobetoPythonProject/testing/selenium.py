from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import chromedriver_autoinstaller

# chromeDriver installer ile kodların chrome'da çalışmasını sağlayan driverın otomatik indirmesini sağlıyor

class Test_Sauce:
    def __init__(self): 
       chromedriver_autoinstaller.install() 
       self.driver = webdriver.Chrome()
       self.driver.maximize_window() #Ekranı büyütür 
       self.driver.get("https://www.saucedemo.com/")  #test edilecek sayfanın linki

    def test_invalid_login(self):
        # sleep(30)   #verilen süre kadar açılan ekranı durdurmak için kullandık
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        userName = self.driver.find_element(By.ID,"user-name")
        userName.send_keys("1")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("1")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU:  {testResult}")

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        

        #action chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(username,"standard_user")
        actions.send_keys_to_element(password,"secret_sauce") #iki işlemi birleştirdik
        actions.move_to_element(loginButton) #Elementin olduğu yere sayfayı taşı anlamına geliyor
        actions.perform() # Demediğimiz sürece yukarıda sıraladığımız aksiyonlarımız çalışmaz. 
        #Aynı işlemleri birden fazla yerde yapıyorsak ihtiyaç duyarız
        loginButton.click()
        appLogo = self.driver.find_element(By.CLASS_NAME,"app_logo")
        testResult = appLogo.text == "Swag Labs"
        print(f"TEST SONUCU:  {testResult}")

testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login() 
