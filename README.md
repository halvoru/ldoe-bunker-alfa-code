LDOE-bunker-alfa-code
==============================

This project aims to simplify the task of finding todays Bunker Alfa code in Last Day On Earth.

About
--------

The pyhton script uses great python libraries to webscrape 'https://last-day-on-earth-survival.fandom.com/wiki/Bunker_Alfa' and searches for the correct bunker code.

Usage
-------

Basically just run the script:
`./bunker-alfa.py`


Known issues
----------------

The script uses the function "datetime.datetime.now()", however depending on you timezone this might give the wrong code.
If you experience this problem, let me know which timezone you use, and I'll try to fix the code. 

