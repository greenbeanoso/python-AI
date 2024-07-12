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
    st.image(f"image/{item}.png",width=500)
    st.write(
        f"{item}{detail['圖']} 定價:{detail['price']}元 庫存:{detail['量']}個"
    )
    if st.button("購買", key=f"{field}{count}"):
        if detail["量"] > 0:
            detail["量"] -= 1
            if "購量" not in detail:
                detail["購量"] = 0
            detail["購量"] +=1
        else:
            st.write("庫存為0，無法購買")
        st.rerun()
    field -= 1
for item, detail in st.session_state.markit.items():
    count +=1
    
    col1,col2, col3, col4,col5,col6= st.columns([1,1,1,1,1,1])
    if field > 0:
        with col1:
            if count == 1:
                OnecolMake(item, detail)
            else: continue
        with col2:
            if count == 2:
                OnecolMake(item, detail)
            else:continue
        with col3:
            if count == 3:
                OnecolMake(item, detail)
            else: continue
        with col4:
            if count == 4:
                OnecolMake(item, detail)
            else: continue
        with col5:
            if count == 5:
                OnecolMake(item, detail)
            else: continue
        with col6:
            OnecolMake(item, detail)
    else:
        field = Ifield
        
            

st.markdown("### 購買列表")

for item, detail in st.session_state.markit.items():
    if "購量" in detail:
        st.write(f"{item}有{detail['購量']}個 共{detail["購量"]*detail['price']}元")
if st.button("全補貨"):
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
