import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestTableSearch:
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def navigate_and_search(self, driver, search_term):
        url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
        driver.get(url)
        driver.maximize_window()
        search_box = driver.find_element(By.CSS_SELECTOR, "#example_filter input")
        search_box.clear()
        search_box.send_keys(search_term)
        driver.implicitly_wait(3)

        table_rows = driver.find_elements(By.CSS_SELECTOR, "#example tbody tr")
        visible_rows = [row for row in table_rows if row.is_displayed()]
        return visible_rows, len(table_rows)

    def test_search_new_york(self, driver):
        visible_rows, total_rows = self.navigate_and_search(driver, "New York")
        print("Filtered Results:")
        for row in visible_rows:
            print(row.text)
        print(f"Number of result rows: {len(visible_rows)} out of {total_rows}")
        assert len(visible_rows) > 0, "No rows are visible after filtering for 'New York'"
        time.sleep(3)

    def test_search_result_count(self, driver):
        visible_rows, _ = self.navigate_and_search(driver, "New York")
        assert len(visible_rows) == 5, f"Expected 5 rows, but found {len(visible_rows)}"
        time.sleep(3)
