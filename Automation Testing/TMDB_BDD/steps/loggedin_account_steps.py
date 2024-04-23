from behave import *

@Then('I should be able to log into the application')
def step_impl(context):
    context.loggedin_account_page.check_account_created()
    context.loggedin_account_page.log_out()