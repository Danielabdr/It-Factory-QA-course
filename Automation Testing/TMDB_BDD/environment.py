from browser import Browser
from pages.add_item_list_page import AddItemListPage
from pages.home_page import Home_page
from pages.join_TMDB_page import JoinTMDBPage
from pages.loggedin_account_page import LoggedinAccountPage
from pages.loggedin_list_page import LoggedinListPage
from pages.login_page import LoginPage

from pages.search_results_page import Search_Results_Page


def before_all(context):
    context.browser = Browser()
    context.home_page = Home_page()
    context.search_results_page = Search_Results_Page()
    context.join_TMDB_page = JoinTMDBPage()
    context.login_page = LoginPage()
    context.loggedin_account_page = LoggedinAccountPage()
    context.loggedin_list_page = LoggedinListPage()
    context.add_item_list_page = AddItemListPage()


def after_all(context):
    context.browser.close_browser()

# def after_scenario(context):
#     try:
#         context.loggedin_account_page.log_out()
#     except:
#         pass




