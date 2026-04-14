import re
from config import DISPLAY_TYPE_MAP, CONSTRUCTION_FORMAT_MAP


def normalize_display_type(text):
    if not text:
        return None
    text_lower = text.lower()
    for key, value in DISPLAY_TYPE_MAP.items():
        if key in text_lower:
            return value
    return "Статика"


def normalize_construction_format(text):
    if not text:
        return "Нетиповые форматы"
    text_lower = text.lower()
    for key, value in CONSTRUCTION_FORMAT_MAP.items():
        if key in text_lower:
            return value
    return "Нетиповые форматы"


def normalize_size(text):
    if not text:
        return None

    text = str(text).lower()
    text = text.replace(",", ".")
    text = text.replace("х", "x").replace("×", "x").replace("*", "x")
    text = text.replace("м.", "").replace("м", "")

    match = re.search(r"(\d+(?:\.\d+)?)\s*x\s*(\d+(?:\.\d+)?)", text)
    if match:
        return f"{match.group(1)}x{match.group(2)}"

    return None


def normalize_lighting(text):
    if not text:
        return None
    text_lower = text.lower()
    if any(word in text_lower for word in ["есть", "да", "освещ", "подсвет"]):
        return True
    if any(word in text_lower for word in ["нет", "без"]):
        return False
    return None
