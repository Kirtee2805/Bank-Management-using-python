import streamlit as st
import Bank as Bank

st.set_page_config(page_title="Bank App", page_icon="🏦")

st.title("🏦 Bank App")
st.divider()

menu = st.sidebar.radio("Menu", [
    "Create Account",
    "Deposit",
    "Withdraw",
    "Account Details",
    "Update Details",
    "Delete Account",
])

# ── Create Account ────────────────────────────────────────────────────────────
if menu == "Create Account":
    st.header("Create Account")

    name  = st.text_input("Full Name")
    email = st.text_input("Email")
    age   = st.number_input("Age", min_value=0, max_value=120, step=1)
    pin   = st.number_input("PIN (4 digits)", min_value=1000, max_value=9999, step=1)

    if st.button("Create"):
        ok, result = Bank.create_account(name, int(age), email, int(pin))
        if ok:
            st.success("Account created successfully!")
            st.info(f"Your Account Number: **{result}**\nPlease save this.")
        else:
            st.error(result)

# ── Deposit ───────────────────────────────────────────────────────────────────
elif menu == "Deposit":
    st.header("Deposit Money")

    account = st.text_input("Account Number")
    pin     = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
    amount  = st.number_input("Amount (₹)", min_value=1, max_value=10000, step=100)

    if st.button("Deposit"):
        ok, msg = Bank.deposit(account, int(pin), int(amount))
        if ok:
            st.success(msg)
        else:
            st.error(msg)

# ── Withdraw ──────────────────────────────────────────────────────────────────
elif menu == "Withdraw":
    st.header("Withdraw Money")

    account = st.text_input("Account Number")
    pin     = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
    amount  = st.number_input("Amount (₹)", min_value=1, step=100)

    if st.button("Withdraw"):
        ok, msg = Bank.withdraw(account, int(pin), int(amount))
        if ok:
            st.success(msg)
        else:
            st.error(msg)

# ── Account Details ───────────────────────────────────────────────────────────
elif menu == "Account Details":
    st.header("Account Details")

    account = st.text_input("Account Number")
    pin     = st.number_input("PIN", min_value=1000, max_value=9999, step=1)

    if st.button("View"):
        ok, result = Bank.get_details(account, int(pin))
        if ok:
            st.metric("Balance", f"₹{result['balance']}")
            st.write(f"**Name:** {result['name']}")
            st.write(f"**Email:** {result['email']}")
            st.write(f"**Age:** {result['age']}")
            st.write(f"**Account No:** {result['account']}")
        else:
            st.error(result)

# ── Update Details ────────────────────────────────────────────────────────────
elif menu == "Update Details":
    st.header("Update Details")
    st.caption("Leave a field blank to keep the current value.")

    account   = st.text_input("Account Number")
    pin       = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
    new_name  = st.text_input("New Name (optional)")
    new_email = st.text_input("New Email (optional)")
    new_pin   = st.text_input("New PIN (optional, 4 digits)", max_chars=4)

    if st.button("Update"):
        ok, msg = Bank.update_details(account, int(pin), new_name, new_email, new_pin)
        if ok:
            st.success(msg)
        else:
            st.error(msg)

# ── Delete Account ────────────────────────────────────────────────────────────
elif menu == "Delete Account":
    st.header("Delete Account")
    st.warning("This action cannot be undone.")

    account = st.text_input("Account Number")
    pin     = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
    confirm = st.checkbox("I confirm I want to permanently delete my account.")

    if st.button("Delete Account"):
        if not confirm:
            st.error("Please check the confirmation box first.")
        else:
            ok, msg = Bank.delete_account(account, int(pin))
            if ok:
                st.success(msg)
            else:
                st.error(msg)