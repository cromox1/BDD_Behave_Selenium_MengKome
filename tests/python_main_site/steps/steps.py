from behave import given, when, then
from selenium.webdriver.common.keys import Keys

from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonSteps import *
from time import sleep

@given("I have a valid user")
def existing_valid_user(context):
    context.usertype = 'valid'
    return 'bacaone','qawsed123456'

@given("I have an invalid user")
def existing_invalid_user(context):
    context.usertype = 'invalid'
    return 'qwertyone','thequickbrownfox'

@given("I have no user")
def existing_no_user(context):
    context.usertype = 'nouser'
    return '','thequickbrownfox'

@when("I type username")
def fill_in_user(context):
    context.user1 = usertype_userpswd(context, context.usertype)[0]
    context.driver.find_element_by_name('username').click()
    context.driver.find_element_by_name('username').send_keys(context.user1 + Keys.ENTER)
    print('USERNAME = ' + str(context.user1))

@when("I type password")
def fill_in_pswd(context):
    context.pswd1 = usertype_userpswd(context, context.usertype)[1]
    context.driver.find_element_by_name('password').click()
    # context.driver.find_element_by_name('password').send_keys(context.pswd1 + Keys.ENTER)
    context.driver.find_element_by_name('password').send_keys(context.pswd1)
    print('PASSWORD = ' + str(len(context.pswd1) * '*'))

@when("I type invalid format username")
def invalid_format_user(context):
    context.usertype = 'informat'
    fill_in_user(context)

@when("I type random password")
def random_passwd(context):
    context.usertype = 'random'
    fill_in_pswd(context)

@when("I click on 'Login'")
def click_on_login(context):
    sleep(2)
    context.driver.find_element_by_xpath('//*[@value="Log in"]').click()
    print('CLICK login SUCCESSFULL')

@then("I should see the user information")
def chk_success_login(context):
    userpage1 = context.driver.find_element_by_xpath('//*[@id="user-tools"]/strong').text
    print('Name of the user = ' + userpage1)
    sleep(2)
    context.driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
    print('Check User1 = ' + context.user1)
    context.driver.find_elements_by_link_text(str(context.user1))[-1].click()  # user has grp with the same name
    email1 = context.driver.find_element_by_xpath('//*[@class="form-row field-email"]/*/*[@class="readonly"]').text
    join1 = context.driver.find_element_by_xpath('//*[@class="form-row field-date_joined"]/*/*[@class="readonly"]').text
    print('User email = ' + email1)
    print('User Joined date = ' + join1)

@then("I should see the error appeared")
def outcome_message1(context):
    pass

@then("I should see the text error 'Please fill out this filed.'")
def outcome_message2(context):
    pass

@then("I logout")
def logout_user_page(context):
    context.driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()
    if context.driver.find_element_by_xpath("//*[@id='content']/h1").text == 'Logged out':
        print('User ' + context.user1 + ' successfully LOGGED OUT')
    else:
        print('User ' + context.user1 + ' IS NOT LOGGED OUT YET')

@then("I close the browser")
def close_browser(context):
    context.driver.close()

def usertype_userpswd(context, usertype):
    if usertype:
        if usertype == 'valid':
            user = existing_valid_user(context)
        elif usertype == 'invalid':
            user = existing_invalid_user(context)
        elif usertype == 'nouser':
            user = existing_no_user(context)
        else:
            user = ('qwertyone','thequickbrownfox')
    else:
        user = ('hentam','hkgfDHLFGDF')
    return user