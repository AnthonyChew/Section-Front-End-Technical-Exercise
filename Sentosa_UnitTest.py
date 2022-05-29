# import all required frameworks
from re import X
import unittest
unittest.TestLoader.sortTestMethodsUsing = None

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# TestCase Class and create a new test class
class SentosaTestUnit(unittest.TestCase):
 
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:/Users/antho/AppData/Local/Google/Chrome/User Data") 

        #Fetch current profile with all cookies
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        #Init 10 sec wait 
        self.wait = WebDriverWait(self.driver, 10)       
        
    def test_A_Login(self):
        #Get desire URL
        self.driver.get('https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20')

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/uatsentosab2c.onmicrosoft.com"))

        #username and password
        username = ""
        password = ""

        userName_tb = self.driver.find_element(By.ID, "signInName")
        password_tb = self.driver.find_element(By.ID, "password")

        userName_tb.send_keys(username)
        password_tb.send_keys(password + Keys.RETURN)

        #wait for button to appear
        self.wait.until(expected_conditions.presence_of_element_located((By.ID,"ReadOnlyEmail_ver_but_send")))

        getOTPbtn = self.driver.find_element(By.ID,"ReadOnlyEmail_ver_but_send")
        getOTPbtn.click()

        #swith to new tab
        #login to email
        #get otp
        #copy and paste otp and login

    def test_B_LoggedIn(self):
        
        #Get desire URL
        self.driver.get('https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20')

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/earn-points"))

        #check is test success
        assert self.driver.title == "Earn Points"

    def test_C_EarningPointHappay(self):    

        #Get desire URL
        self.driver.get('https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20')

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/earn-points"))

        amount = 5090 #input amount
        pin = 981277  #staff pin

        #get amount and verify elements
        amount_tb = self.driver.find_element(By.ID,"amount-0")
        verifyBtn = self.driver.find_element(By.ID,"login")
        
        #populate amount tb
        amount_tb.send_keys(amount)
        verifyBtn.click()

        #wait for section class to change
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='sc-cJSrbW cTnOZq earn-points-verify-wrapper']")))

        #find pin element and input
        staffPin = self.driver.find_element(By.ID,"pin-0")
        staffPin.send_keys(pin)

        #find and slide the slider
        slider = self.driver.find_element(By.CLASS_NAME,"rsbcSlider")
        webdriver.ActionChains(self.driver).drag_and_drop_by_offset(slider,500,0).perform()

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/review-successful"))

        #check is test success
        assert self.driver.title == "Review Successful"

    def test_D_EarningPointUnsuccessful(self):    
          
        #Get desire URL
        self.driver.get('https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20')

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/earn-points"))

        amount = 1900 #input amount

        #get amount and verify elements
        amount_tb = self.driver.find_element(By.ID,"amount-0")

        #populate amount tb
        amount_tb.send_keys(amount)

        random = self.driver.find_element(By.CLASS_NAME,'description__copy')
        random.click()

        #wait for section class to change
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='message-content']")))

        #get error container
        error_tb = self.driver.find_element(By.CLASS_NAME,"message-content")

        #verify btn
        verifyBtn = self.driver.find_element(By.ID,"login")

        #check is test success
        assert error_tb == "Spend at least S$20 to earn points" and verifyBtn.is_enabled()

    def test_E_EarningPointHappay(self):    

        #Get desire URL
        self.driver.get('https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20')

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/earn-points"))

        amount = 5090 #input amount
        pin = 123456  #staff pin

        #get amount and verify elements
        amount_tb = self.driver.find_element(By.ID,"amount-0")
        verifyBtn = self.driver.find_element(By.ID,"login")
        
        #populate amount tb
        amount_tb.send_keys(amount)
        verifyBtn.click()

        #wait for section class to change
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='sc-cJSrbW cTnOZq earn-points-verify-wrapper']")))

        #find pin element and input
        staffPin = self.driver.find_element(By.ID,"pin-0")

        #loop 5 times
        for i in range(5):
            
            #input staff pin
            staffPin.send_keys(pin)

            #find and slide the slider
            slider = self.driver.find_element(By.CLASS_NAME,"rsbcSlider")
            webdriver.ActionChains(self.driver).drag_and_drop_by_offset(slider,500,0).perform()

            #Wait for URL to change 
            self.wait.until(expected_conditions.url_contains("/review-successful"))

        #wait until warning element appears
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='warning container']")))

        #find warning btn and click on it
        warningBtn = self.driver.find_element(By.CLASS_NAME , "sc-bZQynM iSLvLI warning__button warning__button--submit")
        warningBtn.click()
        
        #wait till URL change
        self.wait.until(expected_conditions.url_contains("/review-successful"))

        #find and check string 
        stringToCheck = self.driver.find_element(By.CLASS_NAME , 'wave__meta')
        assert stringToCheck == "Soak up the sun, while we review your points in 3 working days." 
    
    def test_F_AccountLocked(self):
        
        #Get desire URL
        self.driver.get('https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20')

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/earn-points"))

        #find and check string 
        stringToCheck = self.driver.find_element(By.CLASS_NAME , "copy__desc")
        assert stringToCheck == "Enjoy the sun, sand, and water while we review your points within 3 working days."

    def test_G_EarningPointHappayAfterAccountUnlock(self):    

        #Get desire URL
        self.driver.get('https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20')

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/earn-points"))

        amount = 5090 #input amount
        pin = 981277  #staff pin

        #get amount and verify elements
        amount_tb = self.driver.find_element(By.ID,"amount-0")
        verifyBtn = self.driver.find_element(By.ID,"login")
        
        #populate amount tb
        amount_tb.send_keys(amount)
        verifyBtn.click()

        #wait for section class to change
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='sc-cJSrbW cTnOZq earn-points-verify-wrapper']")))

        #find pin element and input
        staffPin = self.driver.find_element(By.ID,"pin-0")
        staffPin.send_keys(pin)

        slider = self.driver.find_element(By.CLASS_NAME,"rsbcSlider")
        webdriver.ActionChains(self.driver).drag_and_drop_by_offset(slider,500,0).perform()

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/review-successful"))

        #check is test success
        assert self.driver.title == "Review Successful"

    def test_H_EarningPointLvUpNotCap(self):    

        #Get desire URL
        self.driver.get('https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20')

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/earn-points"))

        amount = 56090 #input amount
        pin = 981277  #staff pin

        #get amount and verify elements
        amount_tb = self.driver.find_element(By.ID,"amount-0")
        verifyBtn = self.driver.find_element(By.ID,"login")
        
        #populate amount tb
        amount_tb.send_keys(amount)
        verifyBtn.click()

        #wait for section class to change
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='sc-cJSrbW cTnOZq earn-points-verify-wrapper']")))

        #find pin element and input
        staffPin = self.driver.find_element(By.ID,"pin-0")
        staffPin.send_keys(pin)

        slider = self.driver.find_element(By.CLASS_NAME,"rsbcSlider")
        webdriver.ActionChains(self.driver).drag_and_drop_by_offset(slider,500,0).perform()

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/review-successful"))

        #wait for celebration to be done

        #check is test success
        assert self.driver.title == "Review Successful"

    def test_I_EarningPointAfterCap(self):    

        #Get desire URL
        self.driver.get('https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20')

        #Wait for URL to change 
        self.wait.until(expected_conditions.url_contains("/earn-points"))

        amount = 5090 #input amount
        pin = 981277  #staff pin

        #get amount and verify elements
        amount_tb = self.driver.find_element(By.ID,"amount-0")

        #check is test success
        assert amount_tb.is_enabled() == False


    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()