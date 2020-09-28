=====
badoo
=====


.. image:: https://img.shields.io/pypi/v/badoo.svg
        :target: https://pypi.python.org/pypi/badoo




remotely control badoo



* Free software: GNU General Public License v3



Features
--------

* Send messages to users programmatically. 
* Easily get user ids of users online, nearby, and who have visited your profile
* Can be used in "headless" mode on a remote server with no GUI.
* Automatically play the "encouters" game.
* Collect profile data as Python dictionary with a single line of code.

.. code-block:: console

        print (b.get_profile_data("0817947789"))

will return a dictionary like this:

.. code-block:: console

   {'location' 'Caen, Calvados', 
   'Relationship': "I'm single", 
   'Sexuality': "I'm straight", 
   'Appearance': '165 cm, average body', 
   'Living': 'By myself', 
   'Children': 'Already have', 
   'Smoking': 'I smoke occasionally', 
   'Drinking': 'I drink socially', 
   'interests': ['Abd Al Malik', 
                 'Diana Krall', 
                 'Le Petit Journal', 
                 'Butterfly Effect', 
                 'Thelonious Monk', 
                 'Barry White', 
                 'Les Lascars']}
			
			
			v


* TODO: Screenshots of profile pages
* TODO: Handle chat messages

