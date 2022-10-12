from asyncio.windows_events import NULL
from fastapi import status
from fastapi.testclient import TestClient
from shopping_cart.dependencies.user_deps import get_current_user
from main import app
from unittest.mock import patch
import pytest

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


# @patch("shopping_cart.cruds.user.get_user_by_email")
# @patch("shopping_cart.cruds.cart.get_user_cart")
# @patch("shopping_cart.cruds.address.find_addresses_by_email")
# def test_router_post_order(mock_user_by_email,mock_get_user_cart,mock_addresses_by_email):
#     mock_user_by_email.return_value = {"email": "email"}
#     mock_get_user_cart.return_value = {"user.email": "email"}
#     mock_addresses_by_email.return_value = [{"user.email": "email"}]
 
#     respost = client.post(f"/orders/?email=liviatestefinal%40gmail.com")
#     assert respost.status_code == status.HTTP_200_OK




