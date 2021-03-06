"""
Description: Test module for module src/factory/simple_factory.py

@author: Paul Bodean
@date: 12/08/2017
"""

from unittest import TestCase

import time

from src.factory.factory_method import MenuAndSearchTest
from src.utils import get_selenium_driver


class TestFactoryMethod(TestCase):
    """
    Check simple factory functionality
    """

    def setUp(self):
        """
        Driver + factory setup
        :return: driver
        :rtype: object
        """
        self.dr = get_selenium_driver('chrome')
        self.dr.set_window_size(1200, 800)
        self.dr.get('https://www.youtube.com/')

    def test_menu_and_search(self):
        """
        Perform some clicks and search for a song
        """
        # driver = self.setUp()
        demo = MenuAndSearchTest(self.dr)
        time.sleep(2.0)
        demo.get_sections()['menu'].get_actions('click_menu')
        demo.get_sections()['menu'].get_actions('trend')
        demo.get_sections()['menu'].get_actions('history')
        demo.get_sections()['search'].get_actions('set_query', 'python')
        demo.get_sections()['search'].get_actions('click_search')

    def tearDown(self):
        """
        Quit browser
        """
        self.dr.quit()
