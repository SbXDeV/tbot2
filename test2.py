from selenium import webdriver
import time 
import telebot

def main():
    driver = webdriver.Chrome()
    driver.get("https://keksik.net")

    q = driver.find_elements_by_css_selector("body > div.container-site.container-site-padding > div.h-mt-15 > div.h-clearfix.container-items > div:nth-child(1) > div.b-list-advert__title-wrapper > div.b-list-advert__title.clearfix > a")
    q[0].click()
    time.sleep(5)
    #Получаю заголовок
    title = driver.find_elements_by_css_selector('body > div.container-site.container-site-padding > div.h-mt-15 > h1')
    for titles in title:
        print("Наименование анкеты: " + titles.text)
    age = driver.find_elements_by_css_selector("body > div.container-site.container-site-padding > div.h-mt-15 > div.h-mt-5.h-block-info > div.h-mt-5 > span:nth-child(1)")
    for ages in age:
        print("Возраст: " + ages.text)
    city = driver.find_elements_by_css_selector("body > div.container-site.container-site-padding > div.h-mt-15 > div.h-mt-5.h-block-info > div:nth-child(1) > span.h-nowrap")
    for cit in city:
        print("Город: " + cit.text + " район")
    w = driver.find_elements_by_css_selector("#id-show-phones-trigger")
    dist = driver.find_elements_by_css_selector("body > div.container-site.container-site-padding > div.h-mt-15 > div:nth-child(3)")
    for disti in dist:
        print("Описание анкеты: " + disti.text)
    w[0].click()
    time.sleep(3)
    Phone = driver.find_elements_by_css_selector("body > div.container-site.container-site-padding > div.h-mt-15 > div.h-mv-10.h-bold > div.h-ib.h-pv-10.h-mr-10 > a")
    for phones in Phone:
        print("Номер телефона: " + phones.text)
    bot = telebot.TeleBot("1472540914:AAHJr8dN-F26D-xFcA_nj_gxrwiaYfN-ahY")
    
    bot.send_message(1419001337, "Наименование анкеты: " + titles.text + "\nВозраст: " + ages.text + "\nГород: " + cit.text + "\nОписание анкеты: \n" + disti.text +  "\nНомер телефона:" + phones.text) 
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    driver = webdriver.Chrome()
    driver.get("https://leylarelax.com")

    btn1 = driver.find_element_by_xpath("/html/body/header/div[1]/div[2]/ul/li[2]")
    btn1.click()

        #Логин
    log = driver.find_elements_by_css_selector("#user_login")
    log[0].send_keys("Логин")
    #Пароль
    pas = driver.find_elements_by_css_selector("#user_pass")
    pas[0].send_keys("Пароль")#Сори просто не могу сказать пароль от админки сайта
        #Вход
    aut = driver.find_elements_by_css_selector("#wp-submit")
    aut[0].click()
        #Нажатие на кнопку "Панель админа"
    step1 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[3]")
    step1[0].click()

    time.sleep(5)

    stat = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[3]/ul/li[5]/a")
    stat[0].click()


    title = driver.find_elements_by_css_selector("#title")
    title[0].send_keys("(" + cit.text + ") " + titles.text)




    other = driver.find_elements_by_css_selector("#description")
    other[0].send_keys("Возраст: " + ages.text + disti.text)
    time.sleep(5)



    nummer = driver.find_elements_by_css_selector("#classifiedadphone")
    nummer[0].send_keys(phones.text)
    time.sleep(5)


    bu = driver.find_elements_by_css_selector("body > div.all.all-body > div.contentwrapper > div > div:nth-child(1) > form > div.center > input")
    bu[0].click()
    driver.quit()

while True:
    try:
        main()
        driver = webdriver.Chrome()
        driver.quit()
        time.sleep(300)
    except Exception:
        driver = webdriver.Chrome()
        driver.quit()
        print("Ошибка нахуй")
