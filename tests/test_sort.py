import time
from base.base_test import BaseTest



class TestSort(BaseTest):

    def test_sort(self):
        self.home_page.open()
        self.home_page.sort()