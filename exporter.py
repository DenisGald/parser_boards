import json

import pandas as pd

from config import RESULT_JSON, RESULT_XLSX


def export_to_json(data, filename=RESULT_JSON):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"construction_sides": data}, f, ensure_ascii=False, indent=2)


def export_to_excel(data, filename=RESULT_XLSX):
    df = pd.DataFrame(data)
    df["lighting"] = df["lighting"].map({True: "true", False: "false"}).fillna("null")
    df.to_excel(filename, index=False)
