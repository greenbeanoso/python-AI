import streamlit as st
import os
files = os.listdir("image")
Ifield = st.number_input("欄位", value=1, min_value=1, max_value=6)
field = Ifield

if "buylist" not in st.session_state:
    st.session_state.buylist = []
if "markit" not in st.session_state:
    st.session_state.markit = {
        "蘋果": {
            "price": 0.5,
            "量": 10,
            "圖": "🍎",
        },
        "梨": {
            "price": 0.3,
            "量": 20,
            "圖": "🍊",
        },
        "葡萄": {
            "price": 0.2,
            "量": 30,
            "圖": "🍇",
        },
        "番茄": {
            "price": 0.1,
            "量": 40,
            "圖": "🍅",
        },
        "西瓜": {
            "price": 0.05,
            "量": 50,
            "圖": "🍉",
        },
        "為什麼起司越多起司不會越少": {
            "price": 0.01,
            "量": 100,
            "圖": "🧀📖",
        },
    }

count=0
def OnecolMake(item, detail):
    global field
    st.image(f"image/{item}.png",use_column_width=True)
    st.write(
        f"{item}{detail['圖']} 定價:{detail['price']}元 庫存:{detail['量']}個"
    )
    if st.button("購買", key=f"{item}"):
        if detail["量"] > 0:
            detail["量"] -= 1
            if "購量" not in detail:
                detail["購量"] = 0
            detail["購量"] +=1
        else:
            st.write("庫存為0，無法購買")
        st.rerun()
    field -= 1
cols = st.columns(field)
for item, detail in st.session_state.markit.items():
    with cols[Ifield - field]:
        if field > 0:
            OnecolMake(item, detail)
        if field == 0:
            field = Ifield

st.markdown("### 購買列表")

for item, detail in st.session_state.markit.items():
    if "購量" in detail:
        st.write(f"{item}有{detail['購量']}個 共{detail["購量"]*detail['price']}元")
col1, col2 = st.columns([1, 1])
select = ""
with col1:
    select = st.selectbox("補", options=str(st.session_state.markit.keys())[11:-2].split(", "))
with col2:
    NSamo = st.number_input("幾個", value=1, min_value=1, max_value=100)
    if st.button("補貨"):
        st.session_state.markit[select[1:-1]]["量"] += NSamo
        st.rerun()
    


