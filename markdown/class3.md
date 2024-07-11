

---

## 陣列常用編輯語法

```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l.append(11)          # 這可以加入新的值
l.insert(0, 0)        # 這可以在指定位置插入
l.remove(1)           # 這可以刪除指定值
l.pop()               # 這可以刪除最後一個值
l.pop(0)              # 這可以刪除指定位置的值

# pop 跟 remove 不同的是 pop 可以刪除最後一個值或指定位置的值，但是 remove 只能刪除指定值

l.reverse()           # 這可以反轉陣列
l.sort()              # 這可以排序陣列小到大
l.sort(reverse=True)  # 這可以排序陣列大到小
l.count(1)            # 這可以給出陣列中有多少個指定值
```

---

## Streamlit 程式碼範例

### 欄位元件示範

```python
import streamlit as st

st.title("欄位元件")

col1, col2 = st.columns([1, 1])
col1.button("按鈕1")
col2.button("按鈕2")

with col1:
    st.markdown("#這是欄位1")
    st.button("這是按鈕1")

with col2:
    st.markdown("#這是欄位2")
    st.button("這是按鈕2")

cols = st.columns([1, 1, 1])
cols[0].button("按鈕1", key="button1")
cols[1].button("按鈕2", key="button2")
cols[2].button("按鈕3", key="button3")
```

### 文字輸入元件示範

```python
import streamlit as st

st.title("文字輸入元件")
text = st.text_input("請輸入文字")
st.markdown(f"您輸入的文字是：{text}")

st.write("因為 button 被按下去時，頁面會被重新執行，所以 ans 不會變二")
ans = 0
if st.button("按鈕", key="button"):
    ans += 1
st.markdown(f"ans：{ans}")

if "ans" not in st.session_state:
    st.session_state.ans = 0

if st.button("session 按鈕", key="session"):
    st.session_state.ans += 1
st.markdown(f"ans：{st.session_state.ans}")
```

### 點餐機範例

```python
import streamlit as st

if "Eatlist" not in st.session_state:
    st.session_state.Eatlist = []

def add(WYW):
    st.session_state.Eatlist.append(WYW)

st.title("點餐機")
WYW = st.text_input("你要吃什麼？")
if st.button("點餐"):
    add(WYW)
    st.experimental_rerun()

st.title("購物籃")

count = 0
for i in st.session_state.Eatlist:
    count += 1
    cols = st.columns([1, 1])
    with cols[0]:
        st.markdown(f"### {i}")
    with cols[1]:
        if st.button("刪除", "food" + str(count)):
            st.session_state.Eatlist.pop(count - 1)
            st.experimental_rerun()
```

---

