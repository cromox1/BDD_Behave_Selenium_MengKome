from time import sleep

from behave import given, when, then
from selenium.webdriver.common.keys import Keys

from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonSteps import *

@given("I have a user")
def existing_valid_user(context):
    context.user1 = 'bacaone'
    context.pswd1 = 'qawsed123456'
    print('USER / PSWD = ' + context.user1 + ' / ' + str(len(context.pswd1) * '*'))

@when("I type username")
def fill_in_user(context):
    context.driver.find_element_by_name('username').click()
    context.driver.find_element_by_name('username').send_keys(context.user1 + Keys.ENTER)
    print('USERNAME = ' + str(context.user1))

@when("I type password")
def fill_in_pswd(context):
    context.driver.find_element_by_name('password').click()
    # context.driver.find_element_by_name('password').send_keys(context.pswd1 + Keys.ENTER)
    context.driver.find_element_by_name('password').send_keys(context.pswd1)
    print('PASSWORD = ' + str(len(context.pswd1) * '*'))

@when("I click on 'Login'")
def fill_in_pswd(context):
    context.driver.find_element_by_xpath('//*[@value="Log in"]').click()
    print('CLICK login SUCCESSFULL')

@then("I should see the user information")
def chk_success_login(context):
    userpage1 = context.driver.find_element_by_xpath('//*[@id="user-tools"]/strong').text
    print('Name of the user = ' + userpage1)
    context.driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
    print('Check User1 = ' + context.user1)
    context.driver.find_elements_by_link_text(str(context.user1))[-1].click()  # user has grp with the same name
    email1 = context.driver.find_element_by_xpath('//*[@class="form-row field-email"]/*/*[@class="readonly"]').text
    join1 = context.driver.find_element_by_xpath('//*[@class="form-row field-date_joined"]/*/*[@class="readonly"]').text
    print('User email = ' + email1)
    print('User Joined date = ' + join1)

@then("I logout")
def logout_user_page(context):
    context.driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()
    if context.driver.find_element_by_xpath("//*[@id='content']/h1").text == 'Logged out':
        print('User ' + context.user1 + ' successfully LOGGED OUT')
    else:
        print('User ' + context.user1 + ' IS NOT LOGGED OUT YET')