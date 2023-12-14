import requests
import os
import json
import pywencai


def search_iwencai(key_word: str, page_size: int, page_num: int, query_type: str) -> list:
    res = pywencai.get(query=key_word, page=page_num, perpage=page_size, query_type=query_type)
    if res is None:
        return []
    else:
        return json.loads(res.to_json(orient="records", date_format="iso"))


def search_company(key_word: str, page_size: int, page_num: int, mkt_value: str, pe_ration: str,
           pb_ration: str, main_point: str = "ALL") -> dict:
    url = "https://data.eastmoney.com/dataapi/search/company"
    params = {
        "st": "CHANGE_PERCENT",
        "sr": "-1",
        "ps": page_size,
        "p": page_num,
        "mainPoint": main_point
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
    if r.status_code == 200:
        data = remove_fields(r.json(), ['coreTheme', 'companyProfileOriginal', 'mainBusinessOriginal', 'companyScope', 'bk'])
        data['pageSize'] = page_size
        data['pageNum'] = page_num
        data['pageTotal'] = calculate_total_pages(data['hitsTotal'], page_size)
        return data
    else:
        return {}


def calculate_total_pages(total, page_size):
    """
    Calculate the total number of pages based on the total number of items and the page size.

    Parameters:
    total (int): The total number of items.
    page_size (int): The number of items per page.

    Returns:
    int: The total number of pages.
    """
    if page_size <= 0:
        raise ValueError("Page size must be greater than 0")

    return (total + page_size - 1) // page_size


def remove_fields(data, field_names):
    if "result" in data and "companyInfo" in data["result"]:
        for company in data["result"]["companyInfo"]:
            for field_name in field_names:
                if field_name in company:
                    del company[field_name]
    return data


