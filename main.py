"""Simple script to fetch data from the MoySklad API."""

from typing import Any, Dict, Optional

import json
import requests


token = "TOKEN"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
params = {
    "stockType": "quantity",
    "include": "zeroLines",
}


def get_json(
    url: str,
    *,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, str]] = None,
) -> Any:
    """Fetch JSON from URL and raise for HTTP errors."""

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def save_json(filename: str, data: Any) -> None:
    """Save JSON data to ``filename`` using UTF-8 encoding."""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main() -> None:
    # получение каталога
    catalog = get_json(
        "https://online.moysklad.ru/api/remap/1.2/entity/assortment", headers=headers
    )
    save_json("catalog.json", catalog)
    print("catalog json data saved as a file")

    # получение остатков
    stock = get_json(
        "https://online.moysklad.ru/api/remap/1.2/report/stock/all/current",
        headers=headers,
        params=params,
    )
    save_json("stock.json", stock)
    print("stock json data saved as a file")

    # получение оборота по товарам
    turnover = get_json(
        "https://online.moysklad.ru/api/remap/1.2/report/turnover/all", headers=headers
    )
    save_json("turnover.json", turnover)
    print("turnover json data saved as a file")


if __name__ == "__main__":
    main()

