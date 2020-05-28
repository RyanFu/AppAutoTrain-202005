import pytest

from page.main_page import MainPage


class TestSearchPO:
    def setup_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize("name, price", [
        ('alibaba', 200),
        ('jd', 8),
        ('baidu', 20)
    ])
    def test_search(self, name, price):
        assert MainPage().to_search().search(name).get_price() > price
