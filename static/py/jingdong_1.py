from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time
import pandas as pd
from sqlalchemy import create_engine


# jingdong_sniper
def jd_sc(name, a, b, c):
    driver = webdriver.Edge()
    url = "https://search.jd.com/Search?keyword={}&wq={}&pvid=4b97bd245b084ce4b9a3b81047f4c878&psort=3&click=1".format(
        name, name)
    driver.get(url)
    time.sleep(3)
    driver.maximize_window()
    it = []
    for u in range(3):
        it.append({})
        # it[u]['id'] = u
        try:
            it[u]['name'] = driver.find_elements(By.XPATH, "//div[@class='p-name'][1]")[u].text
        except:
            it[u]['name'] = "/"
        try:
            it[u]['price'] = driver.find_elements(By.XPATH, "//div[@class='p-price']/strong/i")[u].text
        except:
            it[u]['price'] = '/'
        try:
            it[u]['brand'] = driver.find_elements(By.XPATH, "//div[@class='p-shopnum']/a")[u].text
        except:
            it[u]['brand'] = '/'
        it[u]['volume'] = str(u + 1)
        try:
            it[u]['discuss'] = re.split("[+]", driver.find_elements(By.XPATH,
                                                                    "//li[@class='gl-item']/div/div[@class='p-commit']/strong/a")[
                u].text)[0]
            try:
                idxOfWan = it[u]['discuss'].find('万')
                if idxOfWan != -1:
                    it[u]['discuss'] = re.split("万", it[u]['discuss'])[0] + "0000"
            except:
                it[u]['discuss'] = it[u]['discuss']
        except:
            it[u]['discuss'] = '/'

        time.sleep(3)
        # driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)
        driver.find_elements(By.XPATH, "//li[@class='gl-item']/div/div[@class='p-img']")[u].click()
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        time.sleep(5)
        it[u]['url'] = driver.current_url
        driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)
        driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@data-fixed='pro-detail-hd-fixed']/ul/li[5]").click()
        time.sleep(5)
        try:
            it[u]['good_discuss'] = driver.find_element(By.XPATH, "//div[@class = 'percent-con']").text
        except:
            it[u]['good_discuss'] = "/"
        it[u]['score'] = round(
            (float(it[u]['price']) * float(a) + float(it[u]['volume'])) * float(b) + (
                        100000 / float(it[u]['discuss'])) * float(c), 2)
        it[u]['type'] = '京东商城'
        driver.switch_to.window(handles[0])
        print(it[u])
    jd_data_f = pd.DataFrame(it)
    time.sleep(4)
    driver.quit()

    return jd_data_f

# fin = jd_sc("眼镜蛇腰带")  # test
# print(fin)
