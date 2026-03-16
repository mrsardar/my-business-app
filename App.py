import streamlit as st
import pandas as pd

# لاگ ان فنکشن
def check_password():
    if "password_correct" not in st.session_state:
        st.title("🔐 بزنس لاگ ان")
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Log In"):
            if user == "admin" and pwd == "12345":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("غلط پاس ورڈ")
        return False
    return True

if check_password():
    st.title("📊 میرا بزنس ڈیش بورڈ")
    
    # سیلز کا خلاصہ (اوپر والی پٹی)
    col1, col2, col3 = st.columns(3)
    col1.metric("آج کی فروخت", "PKR 12,500", "+5%")
    col2.metric("ماہانہ آمدن", "PKR 150,000", "+12%")
    col3.metric("کل آرڈرز", "24")

    st.divider()

    # ڈیٹا انٹری کا حصہ
    st.subheader("📝 نئی انٹری کریں")
    with st.expander("آئٹم شامل کرنے کے لیے یہاں کلک کریں"):
        item_name = st.text_input("آئٹم کا نام")
        item_price = st.number_input("قیمت", min_value=0)
        if st.button("محفوظ کریں"):
            st.success(f"{item_name} محفوظ ہو گیا!")

    st.divider()

    # گراف (سیلز کی رفتار)
    st.subheader("📈 سیلز کی رپورٹ")
    data = pd.DataFrame({
        'دن': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'سیلز': [1000, 2500, 1800, 4000, 3200, 5000, 4500]
    })
    st.line_chart(data.set_index('دن'))
    
