import json
import random
import string
from pathlib import Path


DATABASE = "data.json"


def _load() -> list:
    if Path(DATABASE).exists():
        with open(DATABASE) as f:
            return json.load(f)
    return []


def _save(data: list):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=2)


def _generate_account() -> str:
    parts = (
        random.choices(string.ascii_letters, k=5)
        + random.choices(string.digits, k=1)
        + random.choices("!@#$^&*", k=1)
    )
    random.shuffle(parts)
    return "".join(parts)


def _find_user(data: list, account: str, pin: int):
    for user in data:
        if user["account"] == account and user["pin"] == pin:
            return user
    return None


# ── Public API ────────────────────────────────────────────────────────────────

def create_account(name: str, age: int, email: str, pin: int) -> tuple[bool, str]:
    if age < 18:
        return False, "Age must be 18 or above."
    if len(str(pin)) != 4 or pin < 1000:
        return False, "PIN must be exactly 4 digits."
    if not name.strip() or not email.strip():
        return False, "Name and email are required."

    data = _load()
    account_no = _generate_account()
    data.append({
        "name": name.strip(),
        "age": age,
        "email": email.strip(),
        "pin": pin,
        "account": account_no,
        "balance": 0,
    })
    _save(data)
    return True, account_no


def deposit(account: str, pin: int, amount: int) -> tuple[bool, str]:
    data = _load()
    user = _find_user(data, account, pin)
    if not user:
        return False, "Account not found or wrong PIN."
    if amount <= 0 or amount > 10000:
        return False, "Deposit must be between ₹1 and ₹10,000."
    user["balance"] += amount
    _save(data)
    return True, f"Deposited ₹{amount}. New balance: ₹{user['balance']}"


def withdraw(account: str, pin: int, amount: int) -> tuple[bool, str]:
    data = _load()
    user = _find_user(data, account, pin)
    if not user:
        return False, "Account not found or wrong PIN."
    if amount <= 0:
        return False, "Enter a valid amount."
    if user["balance"] < amount:
        return False, f"Insufficient balance. Available: ₹{user['balance']}"
    user["balance"] -= amount
    _save(data)
    return True, f"Withdrew ₹{amount}. Remaining balance: ₹{user['balance']}"


def get_details(account: str, pin: int) -> tuple[bool, dict | str]:
    data = _load()
    user = _find_user(data, account, pin)
    if not user:
        return False, "Account not found or wrong PIN."
    return True, dict(user)


def update_details(account: str, pin: int, new_name: str = "",
                   new_email: str = "", new_pin: str = "") -> tuple[bool, str]:
    data = _load()
    user = _find_user(data, account, pin)
    if not user:
        return False, "Account not found or wrong PIN."

    changed = []
    if new_name.strip():
        user["name"] = new_name.strip()
        changed.append("name")
    if new_email.strip():
        user["email"] = new_email.strip()
        changed.append("email")
    if new_pin.strip():
        if not new_pin.strip().isdigit() or len(new_pin.strip()) != 4:
            return False, "New PIN must be exactly 4 digits."
        user["pin"] = int(new_pin.strip())
        changed.append("PIN")

    if not changed:
        return False, "No changes provided."
    _save(data)
    return True, f"Updated: {', '.join(changed)}."


def delete_account(account: str, pin: int) -> tuple[bool, str]:
    data = _load()
    user = _find_user(data, account, pin)
    if not user:
        return False, "Account not found or wrong PIN."
    data.remove(user)
    _save(data)
    return True, "Account deleted successfully."