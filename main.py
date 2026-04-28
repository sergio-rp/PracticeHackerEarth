from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class PracticeHackerEarth:

    redirect_link = (By.CSS_SELECTOR, 'a[href="/redirector"]')
    h3_header = (By.XPATH, '//h3[contains(text(),"Redirect")]')
    redirect = (By.ID, 'redirect')
    h3_header_SC = (By.XPATH, '//h3[text()="Status Codes"]')

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.hackerearth.com/')
        self.wait = WebDriverWait(self.driver, 10)

    def get_title_redirect_link(self):
        self.wait.until(EC.element_to_be_clickable(self.redirect_link)).click()
        self.wait.until(EC.visibility_of_element_located(self.h3_header))
        return {'title': self.driver.title}

    def get_codes(self):
        self.wait.until(EC.element_to_be_clickable(self.redirect)).click()
        self.wait.until(EC.visibility_of_element_located(self.h3_header_SC))
        items = self.driver.find_elements(By.CSS_SELECTOR, "ul li a")
        codes = [item.text for item in items]
        return {'Codes':codes}

    def get_500_status_code_text(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, "ul li a")
        link = None
        for item in items:
            if item.text == "500":
                link = item.get_attribute("href")
                break
        self.driver.get(link)
        text = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.example p"))).text
        return {'text': text}

    def tearDown(self):
        self.driver.quit()

test = PracticeHackerEarth()

print(test.get_title_redirect_link())
print(test.get_codes())
print(test.get_500_status_code_text())

test.tearDown()