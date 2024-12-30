# Selenium Table Search Test Suite

This Python script (qa_selenium_test.py) navigates to the Selenium Easy Table Search Demo page (https://www.lambdatest.com/selenium-playground/table-sort-search-demo), interacts with the search box to filter rows containing "New York," and validates the search results against specified criteria.


## Approach

### 1. Environment Setup:
- Configured Selenium WebDriver with Chrome using headless mode for testing automation.
- Used Python's pytest framework for structured test cases.

### 2. Search Automation:
- Located the search input field by its ID and entered the query "New York."
### 3. Validation:
- Checked for the correct number of visible rows in the table matching the query.
- Verified the total number of table entries displayed in the UI.


## How to Run

### 1. Install Dependencies:
- Ensure Python 3.7+ is installed.
- Install required Python packages:

    ```
    pip install selenium pytest
    ```

### 2. Run the Test:

- Execute the script using pytest:

    ```
    pytest -v qa_selenium_test.py
    ```
