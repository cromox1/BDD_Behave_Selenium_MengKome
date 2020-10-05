from behave import given, when, then

from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonSteps import *

@given("I have a user")
def existing_valid_user(context):
    user1 = 'bacaone'
    pswd1 = 'qawsed123456'
    return user1,pswd1

@when("I type email")
def fill_in_user(context):
    pass

@when("I type password")
def fill_in_pswd(context):
    pass

@when("I click on 'Login'")
def fill_in_pswd(context):
    pass

@then("I should see the text Welcome")
def chk_success_login(context):
    pass

