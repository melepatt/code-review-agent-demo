"""Account lookup text."""

def account_query(account: str) -> str:
    return f"SELECT * FROM accounts WHERE name = '{account}'"
