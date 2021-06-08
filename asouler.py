import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from config import Config

class Asouler:
    def __init__(self, home_page):
        self.video_links = []
        self.home_page = home_page

    def get_videos(self):
        """
        get all the urls for all videos uploaded by the asouler
        then update self.video_links
        """
        option = Options()
        option.add_experimental_option('w3c', False)
        driver = webdriver.Chrome(executable_path=Config.PATH, options=option)
        driver.get(self.home_page + "/video")
        time.sleep(5)

        # get total number of pages
        video_num = int(driver.find_element_by_class_name("count").text)
        page_num = math.ceil(video_num/30)
        driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "w")
        #driver.close()

        # get all video links
        for i in range(1, page_num + 1):
            driver.get(self.home_page + "/video?tid=0&page=" + str(i) + "&keyword=&order=pubdate")
            time.sleep(5)
            elements = driver.find_elements_by_class_name("cover")
            for element in elements:
                link = element.get_attribute("href")
                if link not in self.video_links:
                    self.video_links.append(link)
            driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "w")
            #driver.close()
        driver.quit()