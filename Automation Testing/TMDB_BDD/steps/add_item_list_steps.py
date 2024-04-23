from behave import *

@Then('I should be able to create the list')
def step_impl(context):
    context.add_item_list_page.check_list_created()