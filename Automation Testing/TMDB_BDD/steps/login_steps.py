from behave import *

@when('I click on the Login link')
def step_impl(context):
    context.login_page.navigate_to_login_page()

@When('I insert username "{username}"')
def step_impl(context, username):
    context.login_page.insert_username(username)

@When('I insert password "{password}"')
def step_impl(context, password):
    context.login_page.insert_password(password)

@When('I try to login 11 times with "{username}" and "{password}" and I click login button')
def step_impl(context, username, password):
    context.login_page.insert_username_password_11_times(username, password)

@When('I click on the Login button')
def step_impl(context):
    context.login_page.click_login_button()

@Then('I should not be able to log into the application')
def step_impl(context):
    context.login_page.check_user_not_logged()

@Then('I receive an error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page.check_error_message(error_message)
@Then('I receive an attempts error message "{attempts_error_message}"')
def step_impl(context, attempts_error_message):
    context.login_page.check_attempts_error_message(attempts_error_message)
#implementarea pasului cu 11 pasi cu o metoda cu un for care sa introduca cele 10 incercari





