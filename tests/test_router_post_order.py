from asyncio.windows_events import NULL
from fastapi import status
from fastapi.testclient import TestClient
from shopping_cart.dependencies.user_deps import get_current_user
from main import app
from unittest.mock import patch
import pytest

class ExternalAPI():
  def __init__(self,status_code,response=None):
    self.status_code = status_code
    self.response = response
  def json(self):
    return self.response
client = TestClient(app)

# @pytest.fixture
# def client_authenticated():
#     """
#     Returns an API client which skips the authentication
#     """
#     def skip_auth():
#         pass
#     app.dependency_overrides[get_current_user] = skip_auth
#     return TestClient(app)


@patch("shopping_cart.cruds.user.get_user_by_email")
@patch("shopping_cart.cruds.cart.get_user_cart")
@patch("shopping_cart.cruds.address.find_addresses_by_email")
@patch("shopping_cart.cruds.address.get_delivery_address")
@patch("shopping_cart.cruds.order.update_payment_status")
@patch("shopping_cart.cruds.order.create_order")
@patch("shopping_cart.cruds.cart.delete_cart")
def test_router_post_order(mock_user_by_email,mock_get_user_cart,mock_addresses_by_email,mock_get_delivery,mock_update_payment,mock_create_order,mock_delete_cart):
    mock_user_by_email.return_value = {"email": "email"}
    mock_get_user_cart.return_value = {"user.email": "email"}
    mock_addresses_by_email.return_value = ExternalAPI(201)
    mock_get_delivery.return_value = {"user.email": "email",
            "address.is_delivery": True}
    mock_update_payment.return_value = {"user.email": "email",
                "paid": True}
    mock_create_order.return_value = { "user.email": "email",
              "address": "delivery_address",
                "order_id": "order_id" ,"into":"order"}
    mock_delete_cart.retur_value = {"user.email": "email"}
 
    respost = client.post(f"/orders/?email=liviatestefinal%40gmail.com")
    assert respost.status_code == status.HTTP_201_CREATED




