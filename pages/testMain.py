import streamlit as st
import streamlit.components.v1 as components
import extra_streamlit_components as stx
import os
<<<<<<< HEAD
import time

if "LoDM" not in st.session_state:
    st.session_state.LoDM = ["dark", "☀️", "#5e5e5e", "#c7c7c7", "#ffffff"]
LoDM = st.session_state.LoDM
=======

if "LoDM" not in st.session_state:
    st.session_state.LoDM = ["dark", "☀️", "#5e5e5e", "#c7c7c7", "#ffffff"]
>>>>>>> dc4d4ebaaaf008074bc021e327f75eec8ba21ba8
st.set_page_config(
    page_title="一個網頁",
    initial_sidebar_state="collapsed",
    layout="wide",
    page_icon="🐄",
)
<<<<<<< HEAD
if "howL" not in st.session_state:
    st.session_state.howL = 0
print(st.session_state.howL)
print(LoDM)


def LoD(mode):
    global howL
    if mode == "light":
        while st.session_state.howL > 0:
            st.session_state.howL -= 1
        LoDM[1] = "🌙"
        LoDM[0] = "dark"
        LoDM[2] = "#5e5e5e"
        LoDM[3] = "#c7c7c7"
        LoDM[4] = "#ffffff"

    else:
        while st.session_state.howL < 255:
            st.session_state.howL += 1
=======
LoDM = st.session_state.LoDM
if st.button(LoDM[1]):
    if LoDM[0] == "dark":
>>>>>>> dc4d4ebaaaf008074bc021e327f75eec8ba21ba8
        LoDM[1] = "☀️"
        LoDM[0] = "light"
        LoDM[2] = "#c7c7c7"
        LoDM[3] = "#5e5e5e"
        LoDM[4] = "#000000"
<<<<<<< HEAD


if st.button(LoDM[1]):
    LoD(LoDM[0])
    st.rerun()


st.markdown(
    f"""
<style>
[data-testid="stApp"]{{
  background-color: rgb({st.session_state.howL}, {st.session_state.howL}, {st.session_state.howL});
  
}}
</style>
### 測試123
""",
    unsafe_allow_html=True,
)


=======
        print(LoDM)
    else:
        LoDM[1] = "🌙"
        LoDM[0] = "dark"
        LoDM[2] = "#5e5e5e"
        LoDM[3] = "#c7c7c7"
        LoDM[4] = "#ffffff"
        print(LoDM)
    st.rerun()

>>>>>>> dc4d4ebaaaf008074bc021e327f75eec8ba21ba8
components.html(
    f"""
    <html>
  <head>
    <style>
      .bigger {{
        font-size: 2em;
      }}
      .TitleText {{
        background: linear-gradient(45deg, hsl(0, 0%, 100%), hsl(0, 0%, 0%));
        background-clip: text;
        color: transparent;
        display: flex; /* 元素垂直居中 */
        align-items: center; /* 元素水平居中 */
        justify-content: center; /* 元素對齊 */
        padding: 0;
        margin: 0px; /* 去掉元素頂部和底部的間隔 */
        text-shadow: -15px 5px {LoDM[3]}, 15px -5px {LoDM[2]};
        -webkit-text-stroke: {LoDM[4]} 2px;
      }}
      
    </style>
  </head>
    <h1 class="TitleText"><big class="bigger">A Website</big></h1>
</html>
    """,
    height=100,
)
col1, col2 = st.columns([3, 7])
with col1:
    components.html(
        """
<html>
  <head>
    <style>
      #catalog {
        overflow: auto;
        align-items: center;
      }
      .item {
        white-space: nowrap;
        background-color: rgb(255, 192, 255);
        text-overflow: ellipsis;
        border-radius: 30px;
      }

      .lightText {
        background: linear-gradient(180deg, hsl(0, 0%, 58%), hsl(0, 0%, 0%));
        background-clip: text;
        color: transparent;
        display: flex; /* 元素垂直居中 */
        align-items: center; /* 元素水平居中 */
        justify-content: center; /* 元素對齊，可以讓元素在其他元素上居中 */
        padding: 0; /* padding 可以讓元素在其他元素上留白 */
        text-shadow: 0px 1px 10px #eaeaea, 0px 0px 10px #a5a0ff;
        -webkit-text-stroke: 0.5px #ffffff;
      }
      .linearBG_B {
        background: linear-gradient(
          150deg,
          hsl(0, 30%, 49%),
          hsl(400, 30%, 48%)
        );
        background-clip: padding-box;
        color: transparent;
        margin: 0;
      }
      .Up {
        border-radius: 50px 50px 0 0;
      }
      .Down {
        border-radius: 0 0 50px 50px;
      }
      .coolDark {
        background-color: rgb(24, 24, 24);
      }
      .SonPart {
        background-color: rgb(216, 240, 255);
        border-style: double double; /* 兩個線條同時顯示 */
        border-width: 10px 20px;
        margin: 0;
      }
    </style>
  </head>
  <div style="position: sticky; top: 0px">
    <div class="linearBG_B Up lightText">目錄</div>
    <h2 class="SonPart">
      <button
        class="button item"
        onclick="WEBCHANGE(HOME)"
      >
        <p>HOME</p>
      </button>
      </br>
      <button
        class="button item"
        onclick="WEBCHANGE(1)"
      >
        <p>《註解、資料型別與運算技巧》</p>
      </button>
      </br>
      <button
        class="button item"
        onclick="WEBCHANGE(2)"
      >
        <p>第二天筆記</p>
      </button>
    </h2>
    <div class="linearBG_B Down lightText">😀</div>
  </div>
    <script>

      var H = 0;
      function Hloop() {
        H += 2;
        if (H >= 360) {
          H = 0;
        }
        var linear = document.querySelectorAll(".linearBG_B");
        linear.forEach(function (linear) {
          linear.style.background = `linear-gradient(150deg, hsl(${Math.abs(
            H - 360
          )}, 30%, 49%), hsl(${H}, 30%, 48%))`;
        });
      }

      // 使用 setInterval 每 100 毫秒執行一次 Hloop 函數
      setInterval(Hloop, 50);
      function WEBCHANGE(num) {
          document.cookie = "webNum=" + num.toString() + "; path=/";
      }
      WEBCHANGE(1)
    </script>
</html>

""",
        height=500,
    )
with col2:
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
cookie_manager = stx.CookieManager()
cookies = "HOME"
floderpath = "markdown"
files = os.listdir(floderpath)
oldcookie = cookies


<<<<<<< HEAD
@st.experimental_fragment(run_every=1)
def isCookieChange():
    global oldcookie
    global col2
    cookies = cookie_manager.get_all()
    if oldcookie != cookies:
        if "webNum" in cookies:
            print(cookies["webNum"])
            if cookies["webNum"] != "HOME":
                with col2:
                    with open(
                        floderpath + f"/class{cookies['webNum']}.md", encoding="utf-8"
                    ) as f:
                        cotent = f.read()
                    st.markdown(cotent)
            elif cookies["webNum"] == "HOME":
                with col2:
                    st.html(
                        """
          <html>
          <head>
            <style>
            #content {
              overflow: auto;
              align-items: center;
              color: rgb(255, 255, 255);
              text-shadow: 0px 1px 10px #eaeaea, 0px 0px 10px #a5a0ff;
              width: 65%; /* 調整內容的寬度 */
              margin-left: 5%; /* 左邊留白 */
            }
            </style>
          </head>
          <body>
            <div id="content">
            這是內容!
            </div>
          </body>
          </html>
          """
                    )
    else:
        pass
    oldcookie = cookies
=======
def pageUpdate():
    if "webNum" in cookies:
        print(cookies["webNum"])
        if cookies["webNum"] != "HOME":
            with col2:
                with open(
                    floderpath + f"/class{cookies['webNum']}.md", encoding="utf-8"
                ) as f:
                    cotent = f.read()
                st.markdown(cotent)
        elif cookies["webNum"] == "HOME":
            with col2:
                st.html(
                    """
				<html>
				<head>
					<style>
					#content {
						overflow: auto;
						align-items: center;
						color: rgb(255, 255, 255);
						text-shadow: 0px 1px 10px #eaeaea, 0px 0px 10px #a5a0ff;
						width: 65%; /* 調整內容的寬度 */
						margin-left: 5%; /* 左邊留白 */
					}
					</style>
				</head>
				<body>
					<div id="content">
					這是內容!
					</div>
				</body>
				</html>
				"""
                )


@st.experimental_fragment(run_every=1)
def isCookieChange():
    global oldcookie
    cookies = cookie_manager.get_all()
    if oldcookie != cookies:
        pageUpdate()
    else:
        pass
    oldcookie = cookies
    st.rerun()
>>>>>>> dc4d4ebaaaf008074bc021e327f75eec8ba21ba8


isCookieChange()
