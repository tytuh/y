import streamlit as st
st.title("ツアー代表者・旅行者１（大人）")
option = st.selectbox("国籍", ("日本", "China", "China (Hong Kong)", "China (Macau)", "China(Taiwan)"))
def f(i):
    play = ("日本", "China", "China (Hong Kong)", "China (Macau)", "China(Taiwan)")
    return play[i]
titl = st.text_input("お名前（カナ）", value="ヤマダ　タロウ")
fruit =st.radio(label="性別", options=["男性","女性"],index=1)
st.write(fruit)
d=st.date_input("生年月日", date(1900, 1, 1))
tit = st.text_input("メールアドレス", value="yamada@skytour.com")
ti = st.text_input("連絡先電話番号", value="09012345678")
t = st.text_input("郵便番号", value="1231234")