#importing the libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os

#path for chrome driver
# chrome_path = "C:\\Users\\ARKAJIT\\linkedin\\chromedriver.exe"

#initializing web browser with headless to stop auto opening browser
op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument('--headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-sh-usage')
# browser = webdriver.Chrome(chrome_path, options=op)
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op)

#function to scroll down the web page
def scroller(browser):
    # scroll down
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

#fetching the image urls
def fetch_image_url(number):
    thumbnail_result = browser.find_elements_by_css_selector("img.Q4LuWd")
    image_urls = set()
    # print(thumbnail_result)

    for img in thumbnail_result[:number]:
        try:
            img.click()

            time.sleep(6)

            actual_images = browser.find_elements_by_css_selector('img.n3VNCb')
            # print(actual_images)
            #     time.sleep(5)
            for actual_image in actual_images:
                #         print(actual_images)
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    print(actual_image.get_attribute('src'))
                    image_urls.add(actual_image.get_attribute('src'))
        except:
            pass

    return image_urls

#saving the images
def save_images(image_urls, search_string):
    if os.path.isdir("./static/images/" + search_string):
        pass
    else:
        os.makedirs("./static/images/" + search_string)
    for count, pics_url in enumerate(image_urls, 1):
        try:
            image_content = requests.get(pics_url).content
            f = open(os.path.join("./static/images/" + search_string, str(count) + ".jpg"), 'wb')
            f.write(image_content)
            f.close()
        except:
            print("cannot save image")

class image_scrapper:
    def __init__(self, image_name, number_of_image):
        self.search_string = image_name.replace(' ', '')
        # search url
        browser.get(
            "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q=" + self.search_string + "&oq=" +
            self.search_string + "&gs_l=img")
        scroller(browser)
        self.im = fetch_image_url(number_of_image)
        save_images(self.im, self.search_string)


