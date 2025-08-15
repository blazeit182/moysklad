import requests
from unittest.mock import Mock, patch

import pytest

from main import get_json


def test_get_json_success() -> None:
    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_response.json.return_value = {"ok": True}

    with patch("requests.get", return_value=mock_response) as mock_get:
        assert get_json("http://example.com") == {"ok": True}
        mock_get.assert_called_once_with(
            "http://example.com", headers=None, params=None
        )
        mock_response.raise_for_status.assert_called_once()


def test_get_json_http_error() -> None:
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("error")

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(requests.HTTPError):
            get_json("http://example.com")

