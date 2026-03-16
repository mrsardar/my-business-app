import streamlit as st

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
    st.write("خوش آمدید! آپ کی ایپ لائیو ہو چکی ہے۔")
    st.metric("کل فروخت", "PKR 50,000")
  
