=====
Usage
=====

To use badoo in a project

    import badoo

.. code-block:: python
:caption: example.py
:name: example-py
import badoo as b
b.login("/path/to/chromedriver","username","password")
print (b.get_profile_data("1817947789", like=True)) #print profile of user and click the like button
tovisit=["1835042774","111024333","1835683614","1789599278"]
b.visit_many(tovisit) #visit multiple profiles
b.visit_many(b.get_more_visitors(4)) #visit first 4 pages of people who have visited you
print(b.get_nearby()) #print ids of first page of people nearby
print(get_more_nearby(5))  #print ids of first 5 pages of people nearby
b.play_encounters(10) #Like 10 people in encounters game
b.send_message(10799844886","tu es la?") #Send message to user, first argument user id




 login(chromedriver, username, password, headless=False, login_url=ault_login_url)
  

 logout()


 can_vote()


 get_more_nearby(pages=3)


 get_nearby(page=1)


 get_visitors(page=1)


 get_more_visitors(pages=3)


 visit_many(ids, like=False)


 get_profile_data(id, like=False)


 visit(id, like=False)


 play_encounters(xtimes=10)


 send_message(id, msg)


 change_browser_window_size(x, y)
