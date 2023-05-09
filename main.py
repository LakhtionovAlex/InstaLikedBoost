import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

# Pass your username and password to variables
try:
    driver.get('https://instagram.com')
    time.sleep(2)

    text_box = driver.find_element(by=By.NAME, value='username')
    time.sleep(3)
    text_box.clear()
    text_box.send_keys(username)
    time.sleep(2)

    text_box = driver.find_element(by=By.NAME, value='password')
    text_box.clear()
    text_box.send_keys(password + Keys.ENTER)
    time.sleep(8)

    # skip
    sevapush = driver.execute_script("document.getElementsByClassName('_acan _acao _acas')[0].click()")
    time.sleep(8)
    onpush = driver.execute_script("document.getElementsByClassName('_a9-- _a9_1')[0].click()")
    time.sleep(8)

# Choose the right hashtags for you
    try:
        driver.get(f"https://www.instagram.com/explore/tags/{hashtag}")
        time.sleep(8)
        links = driver.find_elements(by=By.TAG_NAME, value="a")

        post_urls = []
        for item in links:
            link = item.get_attribute("href")

            # filter only posts(родительский пост)
            if "/p/" in link:
                post_urls.append(link)
                print(link)
            time.sleep(200)

        for url in post_urls:
            try:
                driver.get(url)
                time.sleep(3)
                like_button = WebDriverWait(driver, 10).until((ec.element_to_be_clickable(By.XPATH, "//button//span//*[name()='svg' @aria-label=‘Нравится’]")))
                like_button.click()
                time.sleep(random.randrange(20, 30))

            except Exception as ex:
                print(ex)

    except Exception as ex:
        print(ex)


except Exception as ex:
    print(ex)
