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
import os
import pandas as pd

def custom_stock_info(symbol: str = "sh600600") -> pd.DataFrame:



def custom_stock_financial_report_sina(stock: str = "sh600600", symbol: str = "资产负债表",
                                   start_date: str = '20230101', end_date: str = '20231231') -> pd.DataFrame:
    df = stock_financial_report_sina(
        stock=stock, symbol=symbol
    )
    return df[(df['报告日'] > start_date) & (df['报告日'] < end_date)]


if __name__ == "__main__":
    os.environ['NO_PROXY'] = "quotes.sina.cn"
    stock_financial_report_sina_df = custom_stock_financial_report_sina(
        stock="sh600600", symbol="现金流量表"
    )
    print(stock_financial_report_sina_df)
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