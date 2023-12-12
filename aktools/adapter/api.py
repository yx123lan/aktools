import requests
import os


def search(key_word: str, page_size: int, page_num: int, mkt_value: str, pe_ration: str, pb_ration: str) -> str:
    os.environ['NO_PROXY'] = "data.eastmoney.com"
    url = "https://data.eastmoney.com/dataapi/search/company"
    params = {
        "st": "CHANGE_PERCENT",
        "sr": "-1",
        "ps": page_size,
        "p": page_num,
        "mainPoint": "ALL"
    }
    if key_word and len(key_word) > 0:
        params["keyWord"] = key_word
    if mkt_value and len(mkt_value) > 0:
        params["mktValue"] = mkt_value
    if pe_ration and len(pe_ration) > 0:
        params["peRation"] = pe_ration
    if pb_ration and len(pb_ration) > 0:
        params["pbRation"] = pb_ration
    r = requests.get(url, params=params)
    data_json = r.json()
    return data_json

