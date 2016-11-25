import unittest
from selenium import webdriver

class SimpleTest(unittest.TestCase):

        def setUp(self):
          self.driver = webdriver.Remote(
                     command_executor='http://127.0.0.1:32781/wd/hub',
                     desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})

        def test_search_in_python_org(self):
            driver = self.driver
            driver.get("https://github.com")
            assert "GitHub" in driver.title

        def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()
