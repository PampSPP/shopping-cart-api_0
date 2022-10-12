from fastapi import status
from fastapi.testclient import TestClient
from shopping_cart.dependencies.user_deps import get_current_user
from main import app
from unittest.mock import patch

client = TestClient(app)

@patch("shopping_cart.cruds.cart.get_user_cart")
@patch("shopping_cart.cruds.cart.check_cart_item")
@patch("shopping_cart.cruds.cart.delete_cart")

def test_router_delete_all_cart(mock_get_user_cart,mock_check_cart_item,mock_delete):
    mock_get_user_cart.return_value = {"user.email": "email"}
    mock_check_cart_item.return_value =  {"user.email": "email", 
    "order_items.product.code": "product_id"}
    mock_delete.return_value = {"user.email": "email"}
  
    
    bory = {
  "product_id": 1,
  "quantity": 1
}
    respost = client.delete(f"/carts/all?email=pam%40pam.com")
    assert respost.status_code == status.HTTP_202_ACCEPTED