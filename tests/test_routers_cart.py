# from fastapi import status
# from fastapi.testclient import TestClient
# from shopping_cart.dependencies.user_deps import get_current_user
# from main import app
# from unittest.mock import patch
# import pytest
# from shopping_cart.controllers.cart import fetch_cart_by_email

# client = TestClient(app)
# @patch("shopping_cart.cruds.user.get_user_by_email")
# @patch("shopping_cart.cruds.product.product_by_id")
# def test_router_1(mock_get_user_by_email,mock_product_by_id):
#     mock_get_user_by_email.return_value = {"email": "email"}
#     mock_product_by_id.return_value = 1
#     bory = {  "product_id": 0,
#   "quantity": 0}   
#     respost = client.post("/carts/?email=pam%40pam.com", json=bory)
# #caso a busca sej possível deve retornar o status 200 OK
#     assert respost.status_code == status.HTTP_201_CREATED

