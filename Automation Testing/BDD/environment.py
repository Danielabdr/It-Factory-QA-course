from pages.home_page import Home_page
from pages.join_TMDB_page import JoinTMDBPage
from pages.loggedin_account_page import LoggedinAccountPage
from pages.login_page import LoginPage

from pages.search_results_page import Search_Results_Page


def before_all(context):
    context.home_page = Home_page()
    context.search_results_page = Search_Results_Page()
    context.join_TMDB_page = JoinTMDBPage()
    context.login_page = LoginPage()
    context.loggedin_account_page = LoggedinAccountPage()


def after_all(context):
    context.browser.close_browser()


