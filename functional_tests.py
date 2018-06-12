from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # To-do app home page
        self.browser.get("http://localhost:8000")

    # Page header and title mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

    # Enter to-do item


    # Type into text box


    # Update the page - item added to to-do list


    # Add another item


    # Update again


    # Generates unique URL


    # visit URL


    # sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
