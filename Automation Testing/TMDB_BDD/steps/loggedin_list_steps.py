from behave import *


@Given('I am on the user account page')
def step_impl(context):
    context.home_page.navigate_to_home_page()
    context.home_page.click_accept_cookies()
    context.login_page.navigate_to_login_page()
    context.login_page.insert_username(username="Danielabdr")
    context.login_page.insert_password(password="Tmdb1994@#@#")
    context.login_page.click_login_button()

@When('I click lists')
def step_impl(context):
    context.loggedin_list_page.click_list_link()
@When('I click create list')
def step_impl(context):
    context.loggedin_list_page.click_create_list_button()

@When('I insert "{name}" into the name input field')
def step_impl(context, name):
    context.loggedin_list_page.insert_list_name(name)

@When('I click continue button')
def step_impl(context):
    context.loggedin_list_page.click_continue_button()


