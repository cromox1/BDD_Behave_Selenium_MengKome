from behave import given, when, then

from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonSteps import *

@given("I have a user")
def existing_valid_user(context):
    user1 = 'bacaone'
    pswd1 = 'qawsed123456'
    print('USER / PSWD = ' + user1 + ' / ' + pswd1)
    return user1,pswd1

@when("I type email")
def fill_in_user(context):
    print('TEST DRIVER email = ' + str(context.driver))
    pass

@when("I type password")
def fill_in_pswd(context):
    print('TEST DRIVER pswd = ' + str(context.driver))
    pass

@when("I click on 'Login'")
def fill_in_pswd(context):
    print('TEST DRIVER login = ' + str(context.driver))
    pass

@then("I should see the text Welcome")
def chk_success_login(context):
    print('TEST DRIVER welcome = ' + str(context.driver))
    pass