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

"""
交易日历
"""
from akshare.tool.trade_date_hist import tool_trade_date_hist_sina


"""
新浪-指数实时行情和历史行情
"""
from akshare.index.index_stock_zh import (
    stock_zh_index_daily,
    stock_zh_index_spot,
    stock_zh_index_daily_tx,
    stock_zh_index_daily_em,
)

"""
stock-summary
"""
from akshare.stock.stock_summary import (
    stock_sse_summary,
    stock_szse_summary,
    stock_sse_deal_daily,
    stock_szse_area_summary,
    stock_szse_sector_summary,
)

"""
港股股票指数数据-新浪-东财
"""
from akshare.index.index_stock_hk import (
    stock_hk_index_spot_sina,
    stock_hk_index_daily_em,
    stock_hk_index_spot_em,
    stock_hk_index_daily_sina,
)

"""
全球宏观-美国宏观
"""
from akshare.economic.macro_usa import (
    macro_usa_eia_crude_rate,
    macro_usa_non_farm,
    macro_usa_unemployment_rate,
    macro_usa_adp_employment,
    macro_usa_core_pce_price,
    macro_usa_cpi_monthly,
    macro_usa_cpi_yoy,
    macro_usa_crude_inner,
    macro_usa_gdp_monthly,
    macro_usa_initial_jobless,
    macro_usa_lmci,
    macro_usa_api_crude_stock,
    macro_usa_building_permits,
    macro_usa_business_inventories,
    macro_usa_cb_consumer_confidence,
    macro_usa_core_cpi_monthly,
    macro_usa_core_ppi,
    macro_usa_current_account,
    macro_usa_durable_goods_orders,
    macro_usa_trade_balance,
    macro_usa_spcs20,
    macro_usa_services_pmi,
    macro_usa_rig_count,
    macro_usa_retail_sales,
    macro_usa_real_consumer_spending,
    macro_usa_ppi,
    macro_usa_pmi,
    macro_usa_personal_spending,
    macro_usa_pending_home_sales,
    macro_usa_nfib_small_business,
    macro_usa_new_home_sales,
    macro_usa_nahb_house_market_index,
    macro_usa_michigan_consumer_sentiment,
    macro_usa_exist_home_sales,
    macro_usa_export_price,
    macro_usa_factory_orders,
    macro_usa_house_price_index,
    macro_usa_house_starts,
    macro_usa_import_price,
    macro_usa_industrial_production,
    macro_usa_ism_non_pmi,
    macro_usa_ism_pmi,
    macro_usa_job_cuts,
    macro_usa_cftc_nc_holding,
    macro_usa_cftc_c_holding,
    macro_usa_cftc_merchant_currency_holding,
    macro_usa_cftc_merchant_goods_holding,
    macro_usa_phs,
)

"""
全球宏观-中国宏观
"""
from akshare.economic.macro_china import (
    macro_china_bank_financing,
    macro_china_insurance_income,
    macro_china_mobile_number,
    macro_china_vegetable_basket,
    macro_china_agricultural_product,
    macro_china_agricultural_index,
    macro_china_energy_index,
    macro_china_commodity_price_index,
    macro_global_sox_index,
    macro_china_yw_electronic_index,
    macro_china_construction_index,
    macro_china_construction_price_index,
    macro_china_lpi_index,
    macro_china_bdti_index,
    macro_china_bsi_index,
    macro_china_cpi_monthly,
    macro_china_cpi_yearly,
    macro_china_m2_yearly,
    macro_china_fx_reserves_yearly,
    macro_china_cx_pmi_yearly,
    macro_china_pmi_yearly,
    macro_china_daily_energy,
    macro_china_non_man_pmi,
    macro_china_rmb,
    macro_china_gdp_yearly,
    macro_china_shrzgm,
    macro_china_ppi_yearly,
    macro_china_cx_services_pmi_yearly,
    macro_china_market_margin_sh,
    macro_china_market_margin_sz,
    macro_china_au_report,
    macro_china_exports_yoy,
    macro_china_hk_market_info,
    macro_china_imports_yoy,
    macro_china_trade_balance,
    macro_china_shibor_all,
    macro_china_industrial_production_yoy,
    macro_china_gyzjz,
    macro_china_lpr,
    macro_china_new_house_price,
    macro_china_enterprise_boom_index,
    macro_china_national_tax_receipts,
    macro_china_new_financial_credit,
    macro_china_fx_gold,
    macro_china_money_supply,
    macro_china_stock_market_cap,
    macro_china_cpi,
    macro_china_gdp,
    macro_china_ppi,
    macro_china_pmi,
    macro_china_gdzctz,
    macro_china_hgjck,
    macro_china_czsr,
    macro_china_whxd,
    macro_china_wbck,
    macro_china_bond_public,
    macro_china_xfzxx,
    macro_china_reserve_requirement_ratio,
    macro_china_consumer_goods_retail,
    macro_china_society_electricity,
    macro_china_society_traffic_volume,
    macro_china_postal_telecommunicational,
    macro_china_international_tourism_fx,
    macro_china_passenger_load_factor,
    macro_china_freight_index,
    macro_china_central_bank_balance,
    macro_china_insurance,
    macro_china_supply_of_money,
    macro_china_swap_rate,
    macro_china_foreign_exchange_gold,
    macro_china_retail_price_index,
    macro_china_real_estate,
    macro_china_qyspjg,
    macro_china_fdi,
    macro_shipping_bci,
    macro_shipping_bcti,
    macro_shipping_bdi,
    macro_shipping_bpi,
    macro_china_urban_unemployment,
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
from dateutil.relativedelta import relativedelta


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
    if not jiejing_df.empty:
        jiejing_df = jiejing_df[(jiejing_df['解禁时间'] > three_month_ago.date())]
    if not dividend_df.empty:
        dividend_df = dividend_df[(dividend_df['实施方案公告日期'] > three_year_ago.date())]
    if not holder_df.empty:
        holder_df = holder_df[(holder_df['截止日期'] > three_month_ago.date())].head(5)
    # 使用head获取前10行数据
    records_json = {"公司概况": zyjs_df.head(1),
                    "限售解禁情况": jiejing_df,
                    "历史分红数据": dividend_df,
                    "最近1年董监高人员股份变动": hold_change_df,
                    "前五大流通股股东": holder_df,
                    "前五大持有当前股票的基金": sorted_fund_holder.head(5),
                    "最近关于此公司的新闻": news_df.head(5),
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
                    "最近3个月持有当前股票的前五大基金": sorted_fund_holder.head(5),
                    "最近关于此公司的新闻": news_df.head(5),
                    "股价概况": indicator_df}
    result_df = pd.Series(records_json).to_frame().T
    result_df.columns = records_json.keys()
    return result_df


def custom_macro_china_cpi_monthly() -> pd.DataFrame:
    temp_df = macro_china_cpi_monthly()
    temp_df.index = temp_df.index - pd.DateOffset(months=1)
    # 创建一个日期范围
    new_df = pd.DataFrame({'月份': temp_df.index.strftime("%Y-%m"), '环比增长(百分比)': temp_df.values})
    return new_df


def custom_macro_china_imports_yoy() -> pd.DataFrame:
    temp_df = macro_china_imports_yoy()
    # 创建一个日期范围
    temp_df.index = temp_df.index - pd.DateOffset(months=1)

    # 创建一个新的 DataFrame，将数据和日期合并
    new_df = pd.DataFrame({'月份': temp_df.index.strftime('%Y-%m'), '同比增长(百分比)': temp_df.values})
    return new_df


def custom_macro_china_exports_yoy() -> pd.DataFrame:
    temp_df = macro_china_exports_yoy()
    temp_df.index = temp_df.index - pd.DateOffset(months=1)

    # 创建一个新的 DataFrame，将数据和日期合并
    new_df = pd.DataFrame({'月份': temp_df.index.strftime('%Y-%m'), '同比增长(百分比)': temp_df.values})
    return new_df


def custom_macro_china_industrial_production_yoy() -> pd.DataFrame:
    temp_df = macro_china_industrial_production_yoy()
    temp_df.index = temp_df.index - pd.DateOffset(months=1)
    # 创建一个新的 DataFrame，将数据和日期合并
    new_df = pd.DataFrame({'月份': temp_df.index.strftime('%Y-%m'), '同比增长(百分比)': temp_df.values})
    return new_df


def custom_macro_china_fx_reserves_yearly() -> pd.DataFrame:
    temp_df = macro_china_fx_reserves_yearly()
    temp_df.index = temp_df.index - pd.DateOffset(months=1)
    # 创建一个新的 DataFrame，将数据和日期合并
    new_df = pd.DataFrame({'月份': temp_df.index.strftime('%Y-%m'), '同比增长(亿美元)': temp_df.values})
    return new_df


def custom_macro_china_m2_yearly() -> pd.DataFrame:
    temp_df = macro_china_m2_yearly()
    temp_df.index = temp_df.index - pd.DateOffset(months=1)
    # 创建一个新的 DataFrame，将数据和日期合并
    new_df = pd.DataFrame({'月份': temp_df.index.strftime('%Y-%m'), '同比增长(百分比)': temp_df.values})
    return new_df


def custom_macro_usa_cpi_monthly() -> pd.DataFrame:
    temp_df = macro_usa_cpi_monthly()
    temp_df.index = temp_df.index - pd.DateOffset(months=1)
    # 创建一个新的 DataFrame，将数据和日期合并
    new_df = pd.DataFrame({'date': temp_df.index.strftime('%Y-%m'), 'value': temp_df.values})
    return new_df


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


# 假设这些函数已经被转换为异步函数
async def stock_zh_index_spot_async():
    return await asyncio.to_thread(stock_zh_index_spot)


async def stock_hk_index_spot_sina_async():
    return await asyncio.to_thread(stock_hk_index_spot_sina)


async def stock_sse_summary_async():
    return await asyncio.to_thread(stock_sse_summary)


async def stock_szse_summary_async(date: str):
    return await asyncio.to_thread(stock_szse_summary, date=date)


async def market_info():
    # 获取当前日期
    current_date = datetime.now()
    trade_date_df = tool_trade_date_hist_sina()
    # 将日期列的字符串转换为Datetime对象
    trade_date_df["trade_date"] = pd.to_datetime(trade_date_df["trade_date"])
    # 获取今天的日期
    today_date = datetime.today()
    # 筛选出小于等于今天的日期
    filtered_data = trade_date_df[trade_date_df["trade_date"] <= today_date]
    # 如果有符合条件的日期，则取第一个，否则返回None
    if not filtered_data.empty:
        first_date = filtered_data.tail(1)["trade_date"].iloc[0]
        formatted_date = first_date.strftime("%Y%m%d")
    else:
        formatted_date = current_date.strftime("%Y%m%d")
    tasks = [
        stock_zh_index_spot_async(),
        stock_hk_index_spot_sina_async(),
        stock_sse_summary_async(),
        stock_szse_summary_async(formatted_date)
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results


def custom_market_info() -> pd.DataFrame:
    results = asyncio.run(market_info())
    a_share_df, hk_df, sse_df, szse_df = [handle_exception(item) for item in results]
    a_share_index_df = a_share_df[a_share_df["代码"].isin(["sh000001", "sz399001", "sz399006", "sh000688", "sh000300"])]
    hk_index_df = hk_df[hk_df["代码"].isin(["HSI", "HSTECH"])]

    # 定义要转换的列名
    columns_to_convert = ["成交金额", "总市值", "流通市值"]
    columns_to_convert2 = ["成交额"]
    # 使用apply方法将值除以1亿来转换为亿元
    szse_df[columns_to_convert] = szse_df[columns_to_convert].apply(lambda x: x / 100000000)
    a_share_index_df[columns_to_convert2] = a_share_index_df[columns_to_convert2].apply(lambda x: x / 100000000)

    records_json = {"A股指数": a_share_index_df,
                    "港股指数": hk_index_df,
                    "上海交易所总览": sse_df,
                    "深圳交易所总览": szse_df}
    result_df = pd.Series(records_json).to_frame().T
    result_df.columns = records_json.keys()
    return result_df


if __name__ == "__main__":
    os.environ['NO_PROXY'] = "quotes.sina.cn"
    df = custom_market_info()

    # indicator_temp_df = stock_share_hold_change_szse(symbol='000001')
    # current_date = datetime.now()
    # two_year_ago = current_date - timedelta(days=1230)
    # change_df = indicator_temp_df[(indicator_temp_df['变动日期'] > two_year_ago.date())]
    # print(change_df.to_json())
    # df = custom_stock_overview(
    #     symbol="600489"
    # )
    #df = custom_macro_china_cpi_monthly()
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