from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_amazon():
    # driver=webdriver.Chrome(executable_path=r"C:\Users\User\Desktop\chromedriver")
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.amazon.com/")
    driver.maximize_window()
    time.sleep(3)
    search=driver.find_element_by_name("field-keywords").send_keys("IPHONE")
    time.sleep(3)
    find=driver.find_element_by_id("nav-search-submit-button").click
    time.sleep(3)
    check=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/span").text
    time.sleep(3)
    driver.close()
print("Your session is successfully done!")

test_amazon()
#Nel, no need to assign to variable if you dont use them
#Nel, click is function, so need to use click()
# other part is correct, goof job