from main_page import MainPage


class TestSearchPO:
    def test_search(self):
        assert MainPage().to_search().search("alibaba").get_price() > 200