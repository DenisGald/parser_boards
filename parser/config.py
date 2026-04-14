BASE_URL = "https://boards.by"
AJAX_URL = f"{BASE_URL}/local/ajax/map.php"
RESULT_JSON = "result.json"
RESULT_XLSX = "result.xlsx"
LIMIT = 100
REQUEST_DELAY = 0.2

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": BASE_URL,
    "Origin": BASE_URL,
}

DISPLAY_TYPE_MAP = {
    "призматрон": "Призматрон",
    "призмавижн": "Призматрон",
    "скролл": "Скроллер",
    "роллер": "Скроллер",
    "led": "Видеоэкран",
    "экран": "Видеоэкран",
    "светодиод": "Видеоэкран",
}

CONSTRUCTION_FORMAT_MAP = {
    "билборд": "Билборды",
    "ситиборд": "Ситиборды",
    "арка": "Арки",
    "путепровод": "Мосты",
    "мост": "Мосты",
    "брандмауэр": "Брандмауэры",
    "световой короб": "Сити-форматы",
    "ситиформат": "Сити-форматы",
    "city": "Сити-форматы",
    "юнипол": "Нетиповые форматы",
    "мегаборд": "Нетиповые форматы",
}
