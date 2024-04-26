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

@When('I click on a list')
def step_impl(context):
    context.loggedin_list_page.click_list()

@When('I click on "{list_name}"')
def step_impl(context, list_name):
    context.loggedin_list_page.click_on_a_list(list_name)



@When('I click Edit button')
def step_impl(context):
    context.loggedin_list_page.click_edit_button()
@When('I click Add/Edit Items')
def step_impl(context):
    context.loggedin_list_page.click_add_items_button()

@When('I insert "{movie_name}" text into Add Item field')
def step_impl(context, movie_name):
    context.loggedin_list_page.add_movie_name_into_add_items_field(movie_name)

@When('I click first movie from the movie dropdown')
def step_impl(context):
    context.loggedin_list_page.click_first_movie_from_the_dropdown()

@Then('I click save button and a succes message should appear')
def step_impl(context):
    context.loggedin_list_page.click_save_button()

@When('I click Delete List button')
def step_impl(context):
    context.loggedin_list_page.click_delete_list_button()

@When('I click Delete button')
def step_impl(context):
    context.loggedin_list_page.click_delete_button()

@Then('I click Yes button and the list should be deleted')
def step_impl(context):
    context.loggedin_list_page.click_yes_button()


