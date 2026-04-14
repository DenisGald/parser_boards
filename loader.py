import json
import time

import requests

from config import AJAX_URL, BASE_URL, HEADERS, REQUEST_DELAY


def fetch_map_data(session):
    payload = {
        "SHOW_ONLY_LINKED": "N",
        "LINKED_ELEMENT_ID": "",
    }
    for i in range(12):
        payload[f"FILTER[MONTHES][{i}]"] = "false"

    response = session.post(AJAX_URL, headers=HEADERS, data=payload, timeout=30)
    response.raise_for_status()

    try:
        return response.json()
    except ValueError:
        return json.loads(response.text)


def fetch_card_html(session, code, side, cache):
    key = f"{code}_{side}"
    if key in cache:
        return cache[key]

    url = f"{BASE_URL}/banner/{code}/?side={side}"
    html = None

    try:
        response = session.get(url, headers=HEADERS, timeout=30)
        if response.status_code == 200:
            html = response.text
    except requests.RequestException as e:
        print(f"Ошибка при загрузке {url}: {e}")

    cache[key] = html
    time.sleep(REQUEST_DELAY)
    return html
