from behave import *

@given('I am on TMDB home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()


@when('I click on the search input and I enter "{search_value}" text')
def step_impl(context, search_value):
    context.home_page.enter_search_value(search_value)

@when('I click "{key_entered}"')
def step_impl(context, key_entered):
    context.home_page.enter_key_from_keyboard(key_entered)