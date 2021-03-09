from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from threading import Thread

path2 ="C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"

def test_search(browser, url):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(firefox_binary=path2)

    driver.get(url)
    print(driver.current_url)
    print(driver.title)
    driver.find_element_by_name('q').send_keys('selenium')
    driver.find_element_by_name('q').send_keys(Keys.ENTER)
    print(driver.title)
    time.sleep(3)
    driver.close()
    driver.quit()

if __name__ == "__main__":
    # 浏览器和首页url
    data = {
        "chrome":"https://www.google.com.tw/",
        "edge":"https://www.google.com.tw/",
        "firefox": "https://www.google.com.tw/"
        }


    # 构建线程
    threads = []
    for b, url in data.items():
       t = Thread(target=test_search,args=(b,url))
       threads.append(t)

    # 启动所有线程
    for thr in threads:
        thr.start()