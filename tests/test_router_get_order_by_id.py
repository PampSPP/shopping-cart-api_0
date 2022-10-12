from asyncio.windows_events import NULL
from fastapi import status
from fastapi.testclient import TestClient
from shopping_cart.dependencies.user_deps import get_current_user
from main import app
from unittest.mock import patch
client = TestClient(app)


@patch("shopping_cart.cruds.order.get_order_by_id")
def test_router_get_order_by_id(mock_id):
    mock_id.return_value = {
    "order_id": "522dbbf6-4a3a-11ed-8522-00155d59380c",
    "address": {
      "street": "Rua Capitão João Paredes",
      "zip_code": "58055-190",
      "number": 39,
      "city": "Bayeux",
      "state": "Paraíba",
      "is_delivery": True,
      "complement": NULL
    },
    "paid": True,
    }
    respost = client.get(f"/orders/id?order_id=c2710cd4-4a39-11ed-8522-00155d59380c")
    assert respost.status_code == status.HTTP_200_OK