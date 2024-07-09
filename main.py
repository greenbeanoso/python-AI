import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="一個網頁", initial_sidebar_state="collapsed", layout="wide"
)
components.html(
    """
    <html>
  <head>
    <style>
      #catalog {
        float: left;
        display: block;
        margin-right: 70%; /* 右邊留白 */
        width: 25%; /* 寬度 */
      }
      .bigger {
        font-size: 2em;
      }
      .TitleText {
        background: linear-gradient(45deg, hsl(0, 0%, 100%), hsl(0, 0%, 0%));
        background-clip: text;
        color: transparent;
        display: flex; /* 元素垂直居中 */
        align-items: center; /* 元素水平居中 */
        justify-content: center; /* 元素對齊 */
        padding: 0;
        margin: 0px; /* 去掉元素頂部和底部的間隔 */
        text-shadow: -15px 5px #5e5e5e, 15px -5px #c7c7c7;
        -webkit-text-stroke: 2px#ffffff;
      }
      .lightText {
        background: linear-gradient(180deg, hsl(0, 0%, 58%), hsl(0, 0%, 0%));
        background-clip: text;
        color: transparent;
        display: flex; /* 元素垂直居中 */
        align-items: center; /* 元素水平居中 */
        justify-content: center; /* 元素對齊，可以讓元素在其他元素上居中 */
        padding: 0; /* padding 可以讓元素在其他元素上留白 */
        margin: 0px; /* 去掉元素頂部和底部的間隔 */
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
        margin: 0; /* 去掉元素頂部和底部的間隔 */
        border-style: double double; /* 兩個線條同時顯示 */
        border-width: 10px 20px;
      }
    </style>
  </head>
  <title>有</title>
  <body class="coolDark">
    <h1 class="TitleText"><big class="bigger">A   Website</big></h1>
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
    </script>
  </body>
  <slide>
    <div id="catalog">
      <div class="linearBG_B Up"><h1 class="lightText">目錄</h1></div>
      <h2 class="SonPart">
        <p></p>
      </h2>
      <div class="linearBG_B Down"><h1 class="lightText">😀</h1></div>
    </div>
  </slide>
</html>

    """,
    height=1000,
)
