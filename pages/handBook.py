import streamlit as st
import os

with st.expander("手冊"):
    st.markdown(
        """
        這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
        例如：
        * **粗體文字**
        * *斜體文字*
        * [連結](https://www.example.com)
        * 代碼塊：
        `python
        print("Hello, Streamlit!")
        `
        
        ## Python 程式技巧筆記

        ### 1. `print` 函數
        用於在控制台印出訊息。

        `python
        print("hELlO wORLD?")  # 印出 hello world
        `

        ### 2. 單行註解
        使用 `#` 來標註單行註解。

        `python
        # 這是單行註解
        `

        ### 3. 多行註解
        使用三個雙引號 `'''` 或單引號 `'''` 來標註多行註解。

        `python
        '''
        這是多行註解
        '''
        `

        ### 4. 快速註解/取消註解
        使用 `Ctrl + /` 可以快速註解或取消註解選定的程式碼行。

        `python
        # if True: # ctrl + / 可以注解
        #     pass
        `

        ### 5. 印出各種資料型別
        用 `print` 函數可以印出字串、整數、浮點數、布林值等。

        `python
        print("a")       # 字串 str
        print(1)         # 數字 int
        print(1.123)     # 浮點數 float
        print(True)      # 布林值 bool
        print("'")       # 單引號字串
        print('"')       # 雙引號字串
        `

        ### 6. 常用數學運算子
        示範加法、減法、乘法、除法、整除、取餘數、次方等運算。

        `python
        print(1 + 1)    # 加法
        print(1 - 1)    # 減法
        print(1 * 1)    # 乘法
        print(1 / 1)    # 除法
        print(1 // 1)   # 整除
        print(1 % 1)    # 取餘數
        print(1 ** 1)   # 次方 指數
        `

        運算子的優先順序：
        1. `()`
        2. `**`
        3. `* / // %`
        4. `+ -`

        ### 7. 字串運算
        示範字串的加法、乘法、索引、切片等操作。

        `python
        a = "hello"
        b = "world"
        print(a + b)       # 字串加法 helloworld
        print(a * 3)       # 字串乘法 hellohellohello
        print(a + b * 3)   # 運算子優先順序 helloworldworldworld
        print(a[0])        # 字串索引 h
        print(a[0:2])      # 字串索引 he
        print(a[0:2] + b[1:3])  # 字串索引 heor
        `

        ### 8. `f-string` 格式化字串
        用於在字串中嵌入表達式。

        `python
        print(f"free {1+1} play")  # f-string 格式化字串
        `

        ### 9. 其他字串操作
        示範如何取得字串長度及型別轉換。

        `python
        print(len("hello"))    # 字串長度

        print(int("1"))        # 字串轉數字
        print(float("1.1"))    # 字串轉浮點數
        print(bool("True"))    # 字串轉布林值
        print(str(1))          # 數字轉字串
        `

        ### 10. `input` 函數
        用於讓用戶輸入，回傳值為字串。

        `python
        a = input("請輸入你的名字：")  # a 是回傳值
        print(type(a))                # 印出 input 回傳值的類型
        `

        ### 11. 匯入模組
        使用 `import` 可以匯入模組，不同模組可以用同一個名字。

        `python
        ### import 可以匯入模組 不同模組可以用同一個名字
        `
        """
    )
with st.expander("手冊2"):
    st.markdown(
        """
        當然，以下是整理過的筆記，並用 Markdown 格式進行排版：

---

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
"""
    )
floderpath = "markdown"
files = os.listdir(floderpath)

filesName = []
for file in files:
    if file.endswith(".md"):
        filesName.append(file)
for file in filesName:
    with open(floderpath + "/" + file, "r", encoding="utf-8") as f:
        cotent = f.read()
    with st.expander(file):
        st.markdown(cotent)
