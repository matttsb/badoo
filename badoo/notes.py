def messages():
    browser.find_element_by_link_text("Messages").click()
    
    browser.find_element_by_css_selector(".scroll__inner .option:nth-child(3) > .option__in").click()
    browser.find_element_by_css_selector( ".select-field__label").click()
    
    browser.find_element_by_css_selector( ".scroll__inner .option:nth-child(4) > .option__in").click()
    browser.find_element_by_css_selector( ".select-field__label").click()

    browser.find_element_by_css_selector("#u_805172015 > .contact-card").click()
    browser.find_element_by_tag_name("body").send_keys('Hello')
    browser.find_element_by_tag_name('body').send_keys(Keys.RETURN)


  
    browser.find_element_by_css_selector("contacts js-contacts")


    def read_messages(id):
    #try:
    messages=[]
    id=str(id)
    url="https://badoo.com/profile/"+id
    browser_get(url)
    sleep(7)
    browser.find_element_by_css_selector(".js-profile-header-chat").click()
    sleep(10)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    sleep(10)
    for message in soup.find_all('div', {'class' : 'message'}): 
        messages.append(message)
    #except:
        #return False
    return messages