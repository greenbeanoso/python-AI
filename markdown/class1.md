import streamlit as st

st.title("這是標題")
st.write(
    "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
)
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
st.markdown(
    '''
這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
例如：
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 代碼塊：
`python
print("Hello, Streamlit!")
`
'''
)
st.markdown(
    '''
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
'''
)
