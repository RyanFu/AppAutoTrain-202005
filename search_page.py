class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def search(self, keyword):
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        self.driver.find_element_by_id('name').click()
        return self

    def get_price(self, keyword=None):
        price = self.driver.find_element_by_id('current_price').text
        return float(price)
