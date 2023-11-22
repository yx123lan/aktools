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

from akshare.stock_fundamental.stock_zyjs_ths import stock_zyjs_ths

import os
import pandas as pd
from datetime import datetime, timedelta


def custom_zh_a_stock_spot_em(symbol: str = "600600") -> pd.DataFrame:
    df = stock_zh_a_spot_em()
    return df[df['代码'] == symbol]


def custom_stock_info(symbol: str = "600600") -> pd.DataFrame:
    zyjs_df = stock_zyjs_ths(symbol)
    # 获取当前日期
    current_date = datetime.now()
    # 计算最近一年的起始日期
    one_year_ago = current_date - timedelta(days=365)
    b_df = stock_financial_analysis_indicator(symbol=symbol, start_year=one_year_ago.strftime("%Y"))
    gdhs_df = stock_zh_a_gdhs_detail_em(symbol=symbol)
    jiejing_df = stock_restricted_release_queue_em(symbol=symbol)
    holder_df = stock_circulate_stock_holder(symbol=symbol)
    six_month_ago = current_date - timedelta(days=180)
    three_month_ago = current_date - timedelta(days=180)
    if is_a_stock(symbol):
        indicator_temp_df = stock_a_indicator_lg(symbol=symbol)
        indicator_df = indicator_temp_df[(indicator_temp_df['trade_date'] > three_month_ago.date())]
    else:
        indicator_temp_df = stock_hk_indicator_eniu(symbol="hk" + symbol)
        indicator_df = indicator_temp_df[(indicator_temp_df['date'] > three_month_ago.date())]
    return pd.DataFrame([{"主营介绍": zyjs_df},  {"最近一年关键财务指标": b_df}, {"股东户数": gdhs_df.iloc[0]},
                         {"限售解禁": jiejing_df}, {"个股指标": indicator_df},
                         {"流通股东": holder_df[(holder_df['截止日期'] > six_month_ago.date())]}])


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
    df = custom_stock_info(
        symbol="600489"
    )
    print(df.to_json())
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