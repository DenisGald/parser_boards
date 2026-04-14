import re

import requests
from bs4 import BeautifulSoup

from loader import fetch_card_html
from normalizer import (
    normalize_construction_format,
    normalize_display_type,
    normalize_lighting,
    normalize_size,
)


def extract_properties(soup):
    properties = {
        "size": None,
        "lighting": None,
        "material": None,
    }

    for block in soup.find_all(["tr", "li", "div"]):
        text = block.get_text(" ", strip=True)
        lower = text.lower()

        if len(text) > 200:
            continue

        if any(k in lower for k in ["формат", "размер", "габарит"]):
            size = normalize_size(text)
            if size:
                properties["size"] = size

        if any(k in lower for k in ["подсвет", "освещ"]):
            lighting = normalize_lighting(text)
            if lighting is not None:
                properties["lighting"] = lighting

        if "материал" in lower:
            match = re.search(
                r"материал(?:\s+плаката)?\s*[:\-]\s*([^.,;]+)",
                text,
                re.IGNORECASE,
            )
            if match:
                material = match.group(1).strip()
                material = re.sub(r"^только\s+", "", material, flags=re.IGNORECASE)
                if len(material) > 2:
                    properties["material"] = material

    if not properties["size"]:
        full_text = soup.get_text(" ", strip=True)
        properties["size"] = normalize_size(full_text)

    return properties


def parse_objects(raw_data, limit=100):
    session = requests.Session()
    cache = {}
    results = []

    for item in raw_data.values():
        if len(results) >= limit:
            break

        try:
            lat = float(item.get("PROPERTY_LATITUDE_VALUE"))
            lon = float(item.get("PROPERTY_LONGITUDE_VALUE"))
        except (TypeError, ValueError):
            continue

        gid = str(item.get("ID"))
        address = item.get("NAME", "").strip()
        code = item.get("CODE")
        type_value = item.get("PROPERTY_TYPE_VALUE", "")
        side = item.get("PROPERTY_SIDE_VALUE")
        name = side.strip() if side else gid

        card_details = {"size": None, "lighting": None, "material": None}
        if code and side:
            html = fetch_card_html(session, code, side, cache)
            if html:
                soup = BeautifulSoup(html, "lxml")
                card_details = extract_properties(soup)

        display_type_source = " ".join(filter(None, [type_value, address]))

        results.append({
            "gid": gid,
            "address": address,
            "name": name,
            "lon": lon,
            "lat": lat,
            "construction_format": normalize_construction_format(type_value),
            "display_type": normalize_display_type(display_type_source),
            "lighting": card_details["lighting"],
            "size": card_details["size"],
            "Material": card_details["material"],
        })

    return results
