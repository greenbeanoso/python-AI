## Streamlit 程式碼範例

### 分數轉換成績範例

```python
import streamlit as st

number = st.number_input("請輸入你的分數", max_value=100, value=50, min_value=1)
grade = "F"
if number >= 90:
    grade = "A"
elif number >= 80:
    grade = "B"
elif number >= 70:
    grade = "C"
elif number >= 60:
    grade = "D"

st.write(f"你的分數是 {number}%，你的成績是 {grade}。")
```

### 布林值操作範例

```python
print(1 == 1)  # 布林值 True
print(1 == 2)  # 布林值 False
print(1 != 1)  # 布林值 False
print(1 != 2)  # 布林值 True
print(1 < 2)   # 布林值 True
print(1 > 2)   # 布林值 False
print(1 <= 2)  # 布林值 True
print(1 >= 2)  # 布林值 False
```

### 邏輯運算符範例

```python
# and 和 or 範例
print(False and True)   # 兩邊都要達成 True，結果 False
print(False and False)  # 兩邊都要達成 True，結果 False
print(True or True)     # 其中一邊達成 True，結果 True
print(True or False)    # 其中一邊達成 True，結果 True
print(False or False)   # 其中一邊達成 True，結果 False

# not 範例
print(not True)  # 布林值 False
print(not False) # 布林值 True
```

### 條件判斷範例

```python
if True:
    print("True")
elif False:
    print("False")
else:
    print("else")
```

#### 注意事項：
- 判斷一定是 `if` 開頭
- `if` 只能有一個
- `elif` 可以有多個
- `else` 只能有一個

### 迴圈範例

```python
for i in range(10):  # range(10) 可以用來產生 0 到 9
    print(i)  # 印出 0 到 9

for i in range(2, 200):
    print(i)  # 印出 2 到 199

for i in range(2, 200, 2):
    print(i)  # 印出 2 到 198 (2 的倍數)

for i in range(200, 3, -2):
    print(i)  # 印出 200 到 4 (2 的倍數)
```

### Streamlit 畫金字塔範例

```python
import streamlit as st

i = 1
y = st.number_input("奪大", min_value=1)
z = ""
for i in range(y + 1):
    z += " " * (y - i) + "*" * (i * 2 - 1) + "\n"
for i in range(y):
    z += " " * (y - 1) + "*" + "\n"
st.markdown(f"```\n這是箭頭\n {z}```")
```

### List 範例

```python
print([])  # 這是空的 list
print([1, 2, 3])  # 這是一個 list，包含三個數字元素
print([1, 2, 3, "早上好", [1, 3, 5]])  # python list 可以包含不同類型的元素

a = [1, 2, 3]  # 這是一個 list，包含三個數字元素
print(a[0])  # 語法: list[index] 這是取出 a 的第一個數字 1

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index in range(len(a)):  # 取出第 index 個元素
    print(a[index])

for index in l:
    print(index)  # 取出所有元素

a[0] = 10  # 語法: list[index] = value 這是改變 a 的第 index 個數字為 10
```

---

這樣整理後，應該可以更清晰地理解每個範例的用途和用法。