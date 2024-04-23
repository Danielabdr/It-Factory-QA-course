from behave import *


@When('I click on the Join TMDB link')
def step_impl(context):
    context.home_page.navigate_to_join_TMDB_link()

@When('I insert "{username}" on the username field')
def step_impl(context, username):
    context.join_TMDB_page.insert_username(username)

@When('I insert "{password}" on the password field')
def step_impl(context, password):
    context.join_TMDB_page.insert_password(password)

@When('I insert "{confirm_password}" on the confirmation password field')
def step_impl(context, confirm_password):
    context.join_TMDB_page.insert_confirm_password(confirm_password)

@When('I insert "{email}" on the email field')
def step_impl(context, email):
    context.join_TMDB_page.insert_email(email)
@When('I click Sign In button')
def step_impl(context):
    context.join_TMDB_page.click_sign_in_button()

@Then('the user will be directed to a page with a message saying that he needs to activate the account from the email recieved')
def step_impl(context):
    context.join_TMDB_page.check_join_TMDB_message()

