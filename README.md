# BDD_Behave_Selenium_MengKome
Selenium on MengKome DJango website using BDD Behave

### https://mengkome.pythonanywhere.com/ 

Assignment 1 (Test1) :

- Go to main page https://mengkome.pythonanywhere.com/
- Login (with admin username / passwd = bacaone / qawsed123456 )
- Check some infos inside 
  - go & click Users button
  - click at your username
  - check email address & date joined
  - go back to home page
- Logout

## 1) BDD Behave

To run :

### (inside directory -> BDD_Behave_Selenium_MengKome directory )
### behave

## 2) Basic UnitTest :

To run :

### (inside directory -> BDD_Behave_Selenium_MengKome directory/UnitTests )
### python3 testOne_basictest.py

## 3) pytest Automation Framework

MengKome Automation Framework consise these directories:

1) apps
2) base
3) configfiles
4) features
5) pages
6) tests
7) utilities
8) screenshots (screenshot's pictures - create automatically if ERROR occured)

To run tests (example) :

### py.test -v -s tests/p01google/p01searchgithubcromox1_test1.py --browser "$browser"

"$browser" = [ ie / chrome / firefox / opera ]

