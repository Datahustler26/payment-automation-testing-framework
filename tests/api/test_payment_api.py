import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_transactions_success():
    """
    Validate successful response for transaction API
    """
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_transaction_by_id():
    """
    Validate single transaction details
    """
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_invalid_transaction():
    """
    Validate invalid transaction ID handling
    """
    response = requests.get(f"{BASE_URL}/posts/999999")

    assert response.status_code == 404
