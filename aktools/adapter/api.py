import requests


def search(key_word: str, page_size: int, page_num: int):
    url = "https://data.eastmoney.com/dataapi/search/company?st=CHANGE_PERCENT&sr=-1&ps=20&p=1&keyWord=%E9%9B%B7%E8%BE%BE&mktValue=100000000%7C&peRation=50%7C&mainPoint=ALL"
    params = {
        "st": "CHANGE_PERCENT",
        "sr": "-1",
        "ps": page_size,
        "p": page_num,
        "keyWord": key_word,
        "mktValue": key_word,
        "peRation": key_word,
        "keyWord": key_word,
    }
    r = requests.get(url, params=params)
    data_json = r.json()