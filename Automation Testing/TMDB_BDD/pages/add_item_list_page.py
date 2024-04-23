import time

from pages.base_page import Base_page


class AddItemListPage(Base_page):

    def check_list_created(self):
        time.sleep(5)
        current_url = self.driver.current_url
        assert 'edit?sort_by=original_order.desc&active_nav_item=step_2' in current_url, f'Error: The list was not created'
