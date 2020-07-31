# part of wstradepyapp - backend

from typing import List

class Account:
    def __init__(self):
        self.object = None
        self.id = None
        self.created_at = None
        self.updated_at = None
        self.opened_at = None
        self.deleted_at = None
        self.buying_power = None
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

def get_account_list(json_list) -> List[Account]:
    account_list = []
    for json in json_list:
        account = Account()
        account.object = json.get("object", None)
        account.id = json.get("id", None)
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