import time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re

__author__ = """Matt Burke"""
__email__ = 'matttsburke@gmail.com'
__version__ = '1.3.2'

next_swipe = datetime.now
visited_ids = []
connected = False
default_login_url = "https://eu1.badoo.com/en/signin/?f=top"

def fix_label(s):
    return s.replace(':', '').strip().replace(' ', '').strip().lower()

def login(chromedriver, username, password, headless=False, login_url=default_login_url):
    global browser
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(chromedriver, options=chrome_options)
    except:
        return False

    try:
        browser.delete_all_cookies()
        browser.set_window_size(1200, 1080)
        browser.get(login_url)
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.element_to_be_clickable(find_element_by_name("post")))

        #sleep(9)
        # s = browser.page_source
        # pattern = "id=\"password(.*?)\""
        # code=re.search(pattern, s).group(1)
        # ^^^ code seems to be used for trying to prevent automated form submissions
        browser.find_element_by_name("email").send_keys(username)
        sleep(2)
        browser.find_element_by_name("password").send_keys(password)
        browser.find_element_by_name("post").click()
        #sleep(5)
        connected = True
    except:
        connected = False
    return (connected)


def browser_get(url):
    global next_swipe
    if browser.get(url):
        sleep(10)
        # Don't 'like' anyone for 2 hours after you have run out of 'likes'
        if "That’s all your swipes!" in browser.page_source():
            next_swipe = datetime.now() + timedelta(hours=2)
        # Prevent downloading when not logged int
        if "Meet New People on Badoo, Make Friends, Chat, Flirt" or "Sign in" in browser.page_source():
            return False
        # Accept cookies
        if "Accept all" in browser.page_source():
            browser.find_element_by_link_text("Accept all").click()
        return browser.page_source()
    else:
        return False


def can_vote():
    if next_swipe > datetime.now():
        return True
    else:
        return False


def logout():
    browser.quit
    browser.close


def get_more_nearby(pages=3):
    gan_ids = []
    x = range(pages)
    for n in x:
        ids = get_nearby(n)
        if ids:
            gan_ids.extend(ids)
    return gan_ids


def get_more_visitors(pages=3):
    gan_ids = []
    x = range(pages)
    for n in x:
        ids = get_visitors(n)
        if ids:
            gan_ids.extend(ids)
    return gan_ids


def get_nearby(page=1):
    ids = []
    browser_get("https://badoo.com/search?page="+str(page))
    sleep(10)
    elems = browser.find_elements_by_tag_name("figure")

    if not elems:
        return False
    else:
        for elem in elems:
            id = elem.get_attribute("data-user-id")
            ids.append(id)

    return (ids)


def get_visitors(page=1):
    ids = []
    url = "https://badoo.com/visitors?page="+str(page)
    browser_get(url)
    sleep(6)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for a in soup.find_all('a', class_="user-card__link"):
        pattern = r"/profile/(.*?)\?folder"
        id = re.search(pattern, str(a)).group(1)
        ids.append(id)
    return ids


def visit_many(ids, like=False):
    if ids:
        for id in ids:
            visit(id, like)


def get_profile_data(id, like, screenshot_dir, photo_dir):
    profile_data = {}
    source = visit(id, like)
    if screenshot_dir:
        browser.save_screenshot(screenshot_dir+id+".png")        
    soup = BeautifulSoup((source), features="lxml")
    try:
        nameandage=soup.title.string.split(" |")[0]
        profile_data["name"]=nameandage.split(",")[0]
        profile_data["age"]=nameandage.split(",")[1]
    except:
        pass
    try:
        location = soup.find('div', {
                         'class': "location-map-wrap__title js-location-label"}).text.rstrip('\n').strip()
    except:
        pass
    if location:
        profile_data["location"] = location
    try:
        about = soup.find('div', {
                         'class': "profile-section__txt profile-section__txt--about"}).text.rstrip('\n').strip()
        profile_data["about"] = about
    except:
        pass

    try:
        for pers in soup.find_all('div', {'class': 'personal-info__item'}):
            label = fix_label(pers.find(
                'div', {'class': 'personal-info__label'}).text.rstrip('\n').strip())
            profile_data[label] = pers.find(
                'div', {'class': 'personal-info__value'}).text.rstrip('\n').strip()
    except:
        pass
    interests = []
    for pers in soup.find_all('span', {'class': 'pill__text'}):
        interests.append(pers.text.rstrip('\n').strip())
    if interests:
        profile_data["interests"] = interests
    return profile_data


def visit(id, like=False):
    url = "https://badoo.com/search/"
    browser_get(url)
    sleep(6)
    id = str(id)
    url = "https://badoo.com/profile/"+id
    browser_get(url)
    sleep(5)
    if like == True:
        try:
            browser.find_element_by_css_selector(
                ".profile-action--color-yes").click()
            browser.find_element_by_css_selector(
                ".js-profile-header-more > .btn").click()
            sleep(7)
            browser.find_element_by_link_text("OK").click()
        except:
            pass
    return browser.page_source


def play_encounters(xtimes=10):
    browser.get("https://badoo.com/encounters")
    sleep(5)
    for i in range(xtimes):
        sleep(3)
        browser.find_element_by_tag_name("body").send_keys("1")
        if "You're out of votes!" in browser.page_source:
            try:
                browser.find_element_by_tag_name("body").send_keys(Keys.ESCAPE)
            except Exception:
                return False
    return i


def send_message(id, msg):
    try:
        id = str(id)
        url = "https://badoo.com/profile/"+id
        browser_get(url)
        sleep(7)
        browser.find_element_by_css_selector(".js-profile-header-chat").click()
        sleep(10)
        browser.find_element_by_id("t").send_keys(msg)
        browser.find_element_by_id("t").send_keys(Keys.RETURN)
    except:
        return False
    return True


def change_browser_window_size(x, y):
    browser.set_window_size(x, y)
    return True
