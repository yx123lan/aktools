from akshare.stock_fundamental.stock_finance import (
    stock_financial_abstract,
    stock_financial_report_sina,
    stock_financial_analysis_indicator,
    stock_add_stock,
    stock_ipo_info,
    stock_history_dividend_detail,
    stock_history_dividend,
    stock_circulate_stock_holder,
    stock_restricted_release_queue_sina,
    stock_fund_stock_holder,
    stock_main_stock_holder,
)

from akshare.stock_fundamental.stock_finance_ths import (
    stock_financial_abstract_ths,
    stock_financial_debt_ths,
    stock_financial_benefit_ths,
    stock_financial_cash_ths,
)

from akshare.stock_feature.stock_hist_em import (
    stock_zh_a_spot_em,
    stock_bj_a_spot_em,
    stock_new_a_spot_em,
    stock_kc_a_spot_em,
    stock_cy_a_spot_em,
    stock_sh_a_spot_em,
    stock_sz_a_spot_em,
    stock_zh_b_spot_em,
    stock_zh_a_hist,
    stock_hk_spot_em,
    stock_hk_main_board_spot_em,
    stock_hk_hist,
    stock_us_spot_em,
    stock_us_hist,
    stock_zh_a_hist_min_em,
    stock_zh_a_hist_pre_min_em,
    stock_hk_hist_min_em,
    stock_us_hist_min_em,
)
"""
东方财富-限售解禁股
"""
from akshare.stock_fundamental.stock_restricted_em import (
    stock_restricted_release_stockholder_em,
    stock_restricted_release_summary_em,
    stock_restricted_release_detail_em,
    stock_restricted_release_queue_em,
)

from akshare.stock_feature.stock_a_indicator import (
    stock_a_indicator_lg,
    stock_hk_indicator_eniu,
)

from akshare.stock_feature.stock_gdhs import (
    stock_zh_a_gdhs,
    stock_zh_a_gdhs_detail_em,
)

"""
董监高及相关人员持股变动
"""
from akshare.stock.stock_share_hold import (
    stock_share_hold_change_bse,
    stock_share_hold_change_sse,
    stock_share_hold_change_szse,
)

"""
新闻-个股新闻
"""
from akshare.news.news_stock import stock_news_em

"""
个股分红
"""
from akshare.stock.stock_dividend_cninfo import stock_dividend_cninfo

from akshare.stock_fundamental.stock_zyjs_ths import stock_zyjs_ths

"""
巨潮资讯-个股-公司概况
"""
from akshare.stock.stock_profile_cninfo import stock_profile_cninfo

import asyncio
import os
import math
import pandas as pd
from datetime import datetime, timedelta, date


def custom_zh_a_stock_spot_em(symbol: str = "600600") -> pd.DataFrame:
    df = stock_zh_a_spot_em()
    return df[df['代码'] == symbol]


# 假设这些函数已经被转换为异步函数
async def stock_profile_cninfo_async(symbol: str):
    return await asyncio.to_thread(stock_profile_cninfo, symbol=symbol)


async def stock_financial_analysis_indicator_async(symbol: str, start_year: str):
    return await asyncio.to_thread(stock_financial_analysis_indicator, symbol=symbol, start_year=start_year)


async def stock_restricted_release_queue_em_async(symbol: str):
    return await asyncio.to_thread(stock_restricted_release_queue_em, symbol=symbol)


async def stock_circulate_stock_holder_async(symbol: str):
    return await asyncio.to_thread(stock_circulate_stock_holder, symbol=symbol)


async def stock_share_hold_change_async(symbol: str):
    return await asyncio.to_thread(stock_share_hold_change, symbol=symbol)


async def stock_dividend_cninfo_async(symbol: str):
    return await asyncio.to_thread(stock_dividend_cninfo, symbol=symbol)


async def stock_fund_stock_holder_async(symbol: str):
    return await asyncio.to_thread(stock_fund_stock_holder, symbol=symbol)


async def stock_news_em_async(symbol: str):
    return await asyncio.to_thread(stock_news_em, symbol=symbol)


async def stock_info(symbol: str):
    # 获取当前日期
    current_date = datetime.now()
    # 计算最近一年的起始日期
    one_year_ago = current_date - timedelta(days=365)

    tasks = [
        stock_profile_cninfo_async(symbol),
        stock_financial_analysis_indicator_async(symbol, one_year_ago.strftime("%Y")),
        stock_restricted_release_queue_em_async(symbol),
        stock_circulate_stock_holder_async(symbol),
        stock_share_hold_change_async(symbol),
        stock_dividend_cninfo_async(symbol),
        stock_fund_stock_holder_async(symbol),
        stock_news_em_async(symbol)
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results


def handle_exception(value):
    return value if not isinstance(value, Exception) else pd.DataFrame()


def custom_stock_overview(symbol: str = "600600") -> pd.DataFrame:
    # 获取当前日期
    current_date = datetime.now()

    results = asyncio.run(stock_info(symbol))

    zyjs_df, b_df, jiejing_df, holder_df, hold_change_df, dividend_df, fund_holder_df, news_df = [handle_exception(item) for item in results]

    six_month_ago = current_date - timedelta(days=180)
    three_year_ago = current_date - timedelta(days=365 * 5)
    three_month_ago = current_date - timedelta(days=90)
    if is_a_stock(symbol):
        indicator_temp_df = stock_a_indicator_lg(symbol=symbol)
        indicator_df = indicator_temp_df.sort_values(by='trade_date', ascending=False).head(1)
    else:
        indicator_temp_df = stock_hk_indicator_eniu(symbol="hk" + symbol)
        indicator_df = indicator_temp_df.sort_values(by='date', ascending=False).head(1)
    one_year_fund_holder_df = fund_holder_df[(fund_holder_df['截止日期'] > three_month_ago.date())]
    # 排序
    sorted_fund_holder = one_year_fund_holder_df.sort_values(by='持仓数量', ascending=False)
    # 使用head获取前10行数据
    records_json = {"公司概况": zyjs_df.head(1),
                    "限售解禁情况": jiejing_df[(jiejing_df['解禁时间'] > six_month_ago.date())],
                    "历史分红数据": dividend_df[(dividend_df['实施方案公告日期'] > three_year_ago.date())],
                    "最近1年董监高人员股份变动": hold_change_df,
                    "流通股东详情": holder_df[(holder_df['截止日期'] > three_month_ago.date())],
                    "最近3个月持有当前股票的前十大基金": sorted_fund_holder.head(10),
                    "最近关于此公司的新闻": news_df.head(10),
                    "股价概况": indicator_df,
                    "最近一个季度财报的关键指标": b_df.head(1)}
    result_df = pd.Series(records_json).to_frame().T
    result_df.columns = records_json.keys()
    return result_df


def custom_stock_overview_simple(symbol: str = "600600") -> pd.DataFrame:
    # 获取当前日期
    current_date = datetime.now()

    results = asyncio.run(stock_info(symbol))

    zyjs_df, b_df, jiejing_df, holder_df, hold_change_df, dividend_df, fund_holder_df, news_df = [handle_exception(item) for item in results]

    six_month_ago = current_date - timedelta(days=180)
    three_year_ago = current_date - timedelta(days=365 * 5)
    three_month_ago = current_date - timedelta(days=90)
    if is_a_stock(symbol):
        indicator_temp_df = stock_a_indicator_lg(symbol=symbol)
        indicator_df = indicator_temp_df.sort_values(by='trade_date', ascending=False).head(1)
    else:
        indicator_temp_df = stock_hk_indicator_eniu(symbol="hk" + symbol)
        indicator_df = indicator_temp_df.sort_values(by='date', ascending=False).head(1)
    one_year_fund_holder_df = fund_holder_df[(fund_holder_df['截止日期'] > three_month_ago.date())]
    # 排序
    sorted_fund_holder = one_year_fund_holder_df.sort_values(by='持仓数量', ascending=False)
    # 使用head获取前10行数据
    records_json = {"公司概况": zyjs_df.head(1),
                    "限售解禁情况": jiejing_df[(jiejing_df['解禁时间'] > six_month_ago.date())],
                    "历史分红数据": dividend_df[(dividend_df['实施方案公告日期'] > three_year_ago.date())],
                    "最近1年董监高人员股份变动": hold_change_df,
                    "流通股东详情": holder_df[(holder_df['截止日期'] > three_month_ago.date())],
                    "最近3个月持有当前股票的前十大基金": sorted_fund_holder.head(10),
                    "最近关于此公司的新闻": news_df.head(5),
                    "股价概况": indicator_df}
    result_df = pd.Series(records_json).to_frame().T
    result_df.columns = records_json.keys()
    return result_df

def serialize_data(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    elif isinstance(obj, dict):
        return {k: serialize_data(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [serialize_data(item) for item in obj]
    elif isinstance(obj, float):
        if obj == float('inf'):
            return "Infinity"
        elif obj == float('-inf'):
            return "-Infinity"
        elif math.isnan(obj):
            return "NaN"
        else:
            return obj
    else:
        return obj


def stock_share_hold_change(symbol) -> pd.DataFrame:
    try:
        if is_a_stock(symbol):
            exchange = identify_stock_exchange(symbol)
            if exchange == 'Shanghai':
                hold_change_df = hold_change_df_limit(stock_share_hold_change_sse(symbol=symbol))
            elif exchange == 'Shenzhen':
                hold_change_df = hold_change_df_limit(stock_share_hold_change_szse(symbol=symbol))
            elif exchange == 'Beijing':
                hold_change_df = hold_change_df_limit(stock_share_hold_change_bse(symbol=symbol))
            else:
                hold_change_df = pd.DataFrame()
        else:
            hold_change_df = pd.DataFrame()
    except Exception as e:
        print(e)
        hold_change_df = pd.DataFrame()
    return hold_change_df


def hold_change_df_limit(indicator_temp_df):
    current_date = datetime.now()
    one_year_ago = current_date - timedelta(days=365)
    return indicator_temp_df[(indicator_temp_df['变动日期'] > one_year_ago.date())]


def identify_stock_exchange(stock_code):
    """
    Identify the stock exchange based on the stock code.

    Args:
    stock_code (str): A six-digit stock code.

    Returns:
    str: The name of the stock exchange (Shanghai, Shenzhen, or Beijing).
    """
    if stock_code.startswith(('600', '601', '603')):
        return 'Shanghai'
    elif stock_code.startswith(('000', '002', '300')):
        return 'Shenzhen'
    elif stock_code.startswith('430'):
        return 'Beijing'
    else:
        return 'Unknown'


def custom_stock_financial_report_sina(stock: str = "sh600600", symbol: str = "资产负债表",
                                       start_date: str = '20230101', end_date: str = '20231231') -> pd.DataFrame:
    df = stock_financial_report_sina(
        stock=stock, symbol=symbol
    )
    return df[(df['报告日'] > start_date) & (df['报告日'] < end_date)]


def is_a_stock(stock_code):
    # 检查股票代码是否为6位纯数字
    if len(stock_code) == 6 and stock_code.isdigit():
        return True
    else:
        return False


if __name__ == "__main__":
    os.environ['NO_PROXY'] = "quotes.sina.cn"
    # indicator_temp_df = stock_share_hold_change_szse(symbol='000001')
    # current_date = datetime.now()
    # two_year_ago = current_date - timedelta(days=1230)
    # change_df = indicator_temp_df[(indicator_temp_df['变动日期'] > two_year_ago.date())]
    # print(change_df.to_json())
    df = custom_stock_overview(
        symbol="600489"
    )
    print(df.to_json(orient="table", date_format="iso"))
    # stock_financial_report_sina_df = custom_stock_financial_report_sina(
    #     stock="sh600600", symbol="现金流量表"
    # )
    # print(stock_financial_report_sina_df)
    #
    # stock_financial_report_sina_df = stock_financial_report_sina(
    #     stock="sh600600", symbol="资产负债表"
    # )
    # print(stock_financial_report_sina_df)
    #
    # stock_financial_report_sina_df = stock_financial_report_sina(
    #     stock="sh600600", symbol="利润表"
    # )
    # print(stock_financial_report_sina_df)
    #
    # stock_financial_abstract_df = stock_financial_abstract(symbol="600004")
    # print(stock_financial_abstract_df)
    #
    # stock_financial_analysis_indicator_df = stock_financial_analysis_indicator(
    #     symbol="600004", start_year="2020"
    # )
    # print(stock_financial_analysis_indicator_df)
    #
    # stock_history_dividend_df = stock_history_dividend()
    # print(stock_history_dividend_df)
    #
    # stock_history_dividend_detail_df = stock_history_dividend_detail(
    #     symbol="600012", indicator="分红", date=""
    # )
    # print(stock_history_dividend_detail_df)
    #
    # stock_history_dividend_detail_df = stock_history_dividend_detail(
    #     symbol="600012", indicator="分红", date="2019-07-08"
    # )
    # print(stock_history_dividend_detail_df)
    #
    # stock_history_dividend_detail_df = stock_history_dividend_detail(
    #     symbol="000002", indicator="配股"
    # )
    # print(stock_history_dividend_detail_df)
    #
    # stock_history_dividend_detail_df = stock_history_dividend_detail(
    #     symbol="000002", indicator="配股", date="1999-12-22"
    # )
    # print(stock_history_dividend_detail_df)
    #
    # stock_ipo_info_df = stock_ipo_info(stock="600004")
    # print(stock_ipo_info_df)
    #
    # stock_add_stock_df = stock_add_stock(stock="600004")
    # print(stock_add_stock_df)
    #
    # stock_restricted_release_queue_sina_df = stock_restricted_release_queue_sina(
    #     symbol="600000"
    # )
    # print(stock_restricted_release_queue_sina_df)
    #
    # stock_circulate_stock_holder_df = stock_circulate_stock_holder(symbol="600000")
    # print(stock_circulate_stock_holder_df)
    #
    # stock_fund_stock_holder_df = stock_fund_stock_holder(symbol="601318")
    # print(stock_fund_stock_holder_df)
    #
    # stock_main_stock_holder_df = stock_main_stock_holder(stock="600000")
    # print(stock_main_stock_holder_df)