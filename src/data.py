# part of wstradepyapp - backend

from typing import List

class Account:
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        self.object = None
        self.account_id = None
        self.created_at = None
        self.updated_at = None
        self.opened_at = None
        self.deleted_at = None
        self.buyer_power = None
        self.current_balance = None
        self.withdrawn_earnings = None
        self.net_deposits = None
        self.available_to_withdraw = None
        self.base_currency = None
        self.custodian_account_number = None
        self.status = None
        self.last_synced_at = None
        self.read_only = None
        self.external_esignature_id = None
        self.account_type = None
        self.position_quantities = None

class Position:
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-statements
    # pylint: disable=too-few-public-methods
    def __init__(self):
        self.currency = None
        self.security_type = None
        self.ws_trade_eligible = None
        self.cds_eligible = None
        self.active_date = None
        self.inactive_date = None
        self.active = None
        self.buyable = None
        self.sellable = None
        self.groups = None
        self.status = None
        self.stock = None
        self.asset_class = None
        self.ca_mutual_fund = None
        self.created_by = None
        self.default_quote_data_source = None
        self.euro_mutual_fund = None
        self.fx_rate = None
        self.investment_type = None
        self.is_invalid = None
        self.management_expense_ratio = None
        self.manually_entered_security = None
        self.object = None
        self.price_interface_symbol = None
        self.quote_expiry_minutes = None
        self.security_entity = None
        self.settlement_period_business_days = None
        self.skip_sync = None
        self.updated_by = None
        self.updated_reason = None
        self.ws_tradibility_overwrite = None
        self.position_id = None
        self.user_id = None
        self.account_id = None
        self.start_of_day_quantity = None
        self.start_of_day_book_value = None
        self.start_of_day_market_value = None
        self.book_value = None
        self.market_book_value = None
        self.external_security_id = None
        self.quantity = None
        self.sellable_quantity = None
        self.created_at = None
        self.updated_at = None
        self.book_value_currency = None
        self.start_of_day_book_value_currency = None
        self.start_of_day_market_book_value_currency = None
        self.market_book_value_currency = None
        self.sparkline = None
        self.quote = None
        self.todays_earnings_baseline_value = None

def get_account_list(json_list) -> List[Account]:
    account_list = []
    for json in json_list:
        account = Account()
        account.object = json.get("object", None)
        account.account_id = json.get("id", None)
        account.created_at = json.get("created_at", None)
        account.opened_at = json.get("opened_at", None)
        account.deleted_at = json.get("deleted_at", None)
        account.buyer_power = json.get("buyer_power", None)
        account.current_balance = json.get("current_balance", None)
        account.withdrawn_earnings = json.get("withdrawn_earnings", None)
        account.net_deposits = json.get("net_deposits", None)
        account.available_to_withdraw = json.get("available_to_withdraw", None)
        account.base_currency = json.get("base_currency", None)
        account.custodian_account_number = json.get("custodian_account_number", None)
        account.status = json.get("status", None)
        account.last_synced_at = json.get("last_synced_at", None)
        account.read_only = json.get("read_only", None)
        account.external_esignature_id = json.get("external_esignature_id", None)
        account.account_type = json.get("account_type", None)
        account.position_quantities = json.get("position_quantities", None)
        account_list.append(account)
    return account_list

def get_positions_list(json_list) -> List[Position]:
    # pylint: disable=too-many-statements
    positions_list = []
    for json in json_list:
        position = Position()
        position.currency = json.get("currency", None)
        position.security_type = json.get("security_type", None)
        position.ws_trade_eligible = json.get("ws_trade_eligible", None)
        position.cds_eligible = json.get("cds_eligible", None)
        position.active_date = json.get("active_date", None)
        position.inactive_date = json.get("inactive_date", None)
        position.active = json.get("active", None)
        position.buyable = json.get("buyable", None)
        position.sellable = json.get("sellable", None)
        position.groups = json.get("groups", None)
        position.status = json.get("status", None)
        position.stock = json.get("stock", None)
        position.asset_class = json.get("asset_class", None)
        position.ca_mutual_fund = json.get("ca_mutual_fund", None)
        position.created_by = json.get("created_by", None)
        position.default_quote_data_source = json.get("default_quote_data_source", None)
        position.euro_mutual_fund = json.get("euro_mutual_fund", None)
        position.fx_rate = json.get("fx_rate", None)
        position.investment_type = json.get("investment_type", None)
        position.is_invalid = json.get("is_invalid", None)
        position.management_expense_ratio = json.get("management_expense_ratio", None)
        position.manually_entered_security = json.get("manually_entered_security", None)
        position.object = json.get("object", None)
        position.price_interface_symbol = json.get("price_interface_symbol", None)
        position.quote_expiry_minutes = json.get("quote_expiry_minutes", None)
        position.security_entity = json.get("security_entity", None)
        position.settlement_period_business_days = json.get(
            "settlement_period_business_days", None)
        position.skip_sync = json.get("skip_sync", None)
        position.updated_by = json.get("updated_by", None)
        position.updated_reason = json.get("updated_reason", None)
        position.ws_tradibility_overwrite = json.get("ws_tradibility_overwrite", None)
        position.position_id = json.get("id", None)
        position.user_id = json.get("user_id", None)
        position.account_id = json.get("account_id", None)
        position.start_of_day_quantity = json.get("start_of_day_quantity", None)
        position.start_of_day_book_value = json.get("start_of_day_book_value", None)
        position.start_of_day_market_value = json.get("start_of_day_market_value", None)
        position.book_value = json.get("book_value", None)
        position.market_book_value = json.get("market_book_value", None)
        position.external_security_id = json.get("external_security_id", None)
        position.quantity = json.get("quantity", None)
        position.sellable_quantity = json.get("sellable_quantity", None)
        position.created_at = json.get("created_at", None)
        position.updated_at = json.get("updated_at", None)
        position.book_value_currency = json.get("book_value_currency", None)
        position.start_of_day_book_value_currency = json.get(
            "start_of_day_book_value_currency", None)
        position.start_of_day_market_book_value_currency = json.get(
            "start_of_day_market_book_value_currency", None)
        position.market_book_value_currency = json.get("market_book_value_currency", None)
        position.sparkline = json.get("sparkline", None)
        position.quote = json.get("quote", None)
        positions_list.append(position)
    return positions_list
