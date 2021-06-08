from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.chrome.options import Options
import time
from config import PATH


class CommentsFetcher:   
    def __init__(self, video_url):
        self.url = video_url
    
    def get_full_html(self):
        option = Options()
        option.add_experimental_option('w3c', False)
        driver = webdriver.Chrome(executable_path=PATH, options=option)
        driver.get(self.url)

        action = TouchActions(driver)
        action.scroll(0, 1000)
        time.sleep(5)

        item = driver.find_element_by_class_name("loading-state")

        while item.text != "没有更多评论":
            action.perform()
            time.sleep(1)
            item = driver.find_element_by_class_name("loading-state")
        driver.quit()
        return driver.page_source