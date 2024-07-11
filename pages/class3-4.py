import streamlit as st

if "Eatlist" not in st.session_state:
    st.session_state.Eatlist = []


def add(WYW):
    st.session_state.Eatlist.append(WYW)


st.title("點餐機")
WYW = st.text_input("你要吃什麼？")
if st.button("點餐"):
    add(WYW)
    st.rerun()

st.title("購物籃")


count = 0
for i in st.session_state.Eatlist:
    count += 1
    cols = st.columns([1, 1])
    with cols[0]:
        st.markdown(f"### {i}")
    with cols[1]:
        if st.button("刪除", "food" + str(count)):
            print(i)
            st.session_state.Eatlist.pop(count - 1)
            st.rerun()
