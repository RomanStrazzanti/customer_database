from unittest.mock import patch, MagicMock
import pytest
from customer_database import Customer

@patch("customer_database.sqlite3.connect")
def test_customer_with_patch(mock_connect):
    mock_connection = MagicMock()
    mock_connect.return_value = mock_connection

    customer = Customer()

    mock_connect.assert_called_once_with(":memory:")
    assert customer.con == mock_connection