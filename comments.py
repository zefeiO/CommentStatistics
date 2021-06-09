from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.chrome.options import Options
from urllib3.exceptions import MaxRetryError
import time
from config import Config


class CommentsFetcher:   
    def __init__(self, video_url):
        self.url = "https:" + video_url
    
    def get_full_html(self):
        option = Options()
        option.add_experimental_option('w3c', False)
        driver = webdriver.Chrome(executable_path=Config.PATH, options=option)
        driver.get(self.url)

        action = TouchActions(driver)
        action.scroll(0, 10000)
        # 手动登录
        #time.sleep(10)
        driver.get(self.url)
        time.sleep(3)
        item = driver.find_element_by_class_name("loading-state")

        
        while item.text != "没有更多评论":
            try:
                action.perform()
                time.sleep(1)
                item = driver.find_element_by_class_name("loading-state")
            except MaxRetryError:
                time.sleep(60)

        html = driver.page_source
        driver.quit()
        return html