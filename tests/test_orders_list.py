import requests
import allure

from endpoints import Endpoint
from constants import Constants


class TestOrdersList:
    @allure.title('В тело ответа возвращается список заказов')
    @allure.description('Проверка, что в ответе на запрос списка заказов содержится поле "orders"')
    def test_orders_list(self):
        with allure.step('Отправка запроса на получение списка заказов'):
            response = requests.get(f'{Constants.BASE_URL}{Endpoint.CREATE_ORDER}')
            allure.attach(f'Ответ сервера: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка кода ответа и наличия поля "orders"'):
            assert response.status_code == 200
            assert "orders" in response.json()