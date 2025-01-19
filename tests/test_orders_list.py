import requests
import allure

from endpoints import Endpoint
from constants import Constants


class TestOrdersList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_orders_list(self):
        response = requests.get(f'{Constants.BASE_URL}{Endpoint.CREATE_ORDER}')
        assert response.status_code == 200 and "orders" in response.json()