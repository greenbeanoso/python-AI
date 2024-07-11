import streamlit as st

# st.cols 示範
st.title("欄位元件")
col1, col2 = st.columns([1, 1])
col1.button("按鈕1")
col2.button("按鈕2")
with col1:  #
    st.markdown("#這是欄位1")
    st.button("這是按鈕1")
with col2:
    st.markdown("#這是欄位2")
    st.button("這是按鈕2")

cols = st.columns([1, 1, 1])
cols[0].button("按鈕1", key="button1")  # 在第0個欄位中加入按鈕
cols[1].button("按鈕2", key="button2")
cols[2].button("按鈕3", key="button3")


st.title("文字輸入元件")
text = st.text_input("請輸入文字")
st.markdown(f"您輸入的文字是：{text}")
st.write("因為button被按下去時 頁面會被重新執行 所以ans不會變二")
ans = 0
if st.button("按鈕", key="button"):
    ans += 1
st.markdown(f"ans：{ans}")
if "ans" not in st.session_state:
    st.session_state.ans = 0
if st.button("sension按鈕", key="sension"):
    st.session_state.ans += 1
st.markdown(f"ans：{st.session_state.ans}")
