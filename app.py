import streamlit as st

st.set_page_config(page_title="SBI Bank", page_icon="🏦", layout="wide")

class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"✅ Transaction Successful. Collected ₹{amount}"
        else:
            return "❌ Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"✅ Deposit Successful. Total Balance: ₹{self.balance}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"📱 Mobile number updated: {self.mobile_number}"

    def check_balance(self):
        return f"💰 Total Account Balance: ₹{self.balance}"


# ---------- Custom CSS ----------
st.markdown("""
<style>
.main-title{
    font-size:40px;
    font-weight:bold;
    text-align:center;
    color:#1f4e79;
}
.card{
    padding:20px;
    border-radius:12px;
    background-color:#f5f7fa;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🏦 SBI Digital Bank</p>', unsafe_allow_html=True)


if "account" not in st.session_state:
    st.session_state.account = None


menu = ["🏠 Create Account", "💵 Deposit", "💸 Withdraw", "📊 Check Balance", "📱 Update Mobile"]
choice = st.sidebar.selectbox("Bank Services", menu)


# ---------- Create Account ----------
if choice == "🏠 Create Account":

    st.subheader("Open a New Account")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Customer Name")
        age = st.number_input("Age", min_value=18)

    with col2:
        acc = st.text_input("Account Number")
        mobile = st.text_input("Mobile Number")

    balance = st.number_input("Initial Deposit", min_value=0)

    if st.button("Create Account"):
        st.session_state.account = BankApplication(name, acc, age, mobile, balance)
        st.success("🎉 Account Created Successfully")


# ---------- Deposit ----------
elif choice == "💵 Deposit":

    st.subheader("Deposit Money")

    amount = st.number_input("Enter Amount", min_value=0)

    if st.button("Deposit"):
        if st.session_state.account:
            result = st.session_state.account.deposit(amount)
            st.success(result)
        else:
            st.error("⚠ Please create account first")


# ---------- Withdraw ----------
elif choice == "💸 Withdraw":

    st.subheader("Withdraw Money")

    amount = st.number_input("Enter Amount", min_value=0)

    if st.button("Withdraw"):
        if st.session_state.account:
            result = st.session_state.account.withdraw(amount)
            st.info(result)
        else:
            st.error("⚠ Please create account first")


# ---------- Balance ----------
elif choice == "📊 Check Balance":

    st.subheader("Account Details")

    if st.session_state.account:

        col1, col2, col3 = st.columns(3)

        col1.metric("Customer", st.session_state.account.name)
        col2.metric("Account No", st.session_state.account.account_number)
        col3.metric("Balance", f"₹{st.session_state.account.balance}")

    else:
        st.error("⚠ Please create account first")


# ---------- Update Mobile ----------
elif choice == "📱 Update Mobile":

    st.subheader("Update Mobile Number")

    new_mobile = st.text_input("New Mobile Number")

    if st.button("Update"):
        if st.session_state.account:
            result = st.session_state.account.update_mobile(new_mobile)
            st.success(result)
        else:
            st.error("⚠ Please create account first")