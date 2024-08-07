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
      #content {
        overflow: auto;
        align-items: center;
        color: rgb(255, 255, 255);
        text-shadow: 0px 1px 10px #eaeaea, 0px 0px 10px #a5a0ff;
        width: 65%; /* 調整內容的寬度 */
        margin-left: 5%; /* 左邊留白 */
      }
      #catalog {
        overflow: auto;
        align-items: center;
        width: 25%; /* 調整目錄的寬度 */
      }
      .item {
        white-space: nowrap;
        background-color: rgb(255, 192, 255);
        text-overflow: ellipsis;
        margin: 3px;
        border-radius: 30px;
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
    <h1 class="TitleText"><big class="bigger">A Website</big></h1>
    <div style="display: flex">
      <div id="catalog">
        <div class="linearBG_B Up"><h1 class="lightText">目錄</h1></div>
        <h2 class="SonPart">
          <button
            class="button item"
            onclick="window.open('http://localhost:8501/class2-2')"
          >
            <p>HOME</p>
          </button>
          <button
            class="button item"
            onclick="window.open('https://just-a-web-by-osogreenbean.streamlit.app/class1-2','_self')"
          >
            <p>《註解、資料型別與運算技巧》</p>
          </button>
          <button
            class="button item"
            onclick="window.open('http://localhost:8501/class2-2')"
          >
            <p>第二天筆記</p>
          </button>
        </h2>
        <div class="linearBG_B Down"><h1 class="lightText">😀</h1></div>
      </div>
      <div id="content">
        <p>
          這是一段用來測試的長文本。設計網頁時，我們常常需要一些示例文本來查看效果。這些文本不一定要有意義，但必須足夠長，以便模擬實際使用中的情況。以下是一些隨機生成的段落：
        </p>
        <p>
          在遙遠的過去，有一個美麗的村莊，村莊裡的人們過著幸福而平靜的生活。每天清晨，太陽從東邊升起，陽光灑在村莊的每一個角落，照亮了人們的一天。村莊的中央有一個大廣場，廣場上有一棵古老的橡樹。這棵橡樹已經有幾百年的歷史，是村莊的象徵。人們常常在橡樹下聚集，聊天、唱歌、跳舞，分享彼此的喜悅和悲傷。
        </p>
        <p>
          時間在不知不覺中流逝，村莊裡發生了很多變化。年輕人開始離開村莊，到外面的世界去闖蕩。村莊變得越來越安靜，只有橡樹依然屹立在那裡，見證著一代又一代人的成長和離去。每當節日來臨，村莊裡的老少們都會回到橡樹下，舉行盛大的慶祝活動。他們唱起古老的歌謠，跳起傳統的舞蹈，仿佛時光倒流，回到了那個充滿歡笑和歡樂的年代。
        </p>
        <p>
          然而，有一天，一場突如其來的暴風雨襲擊了村莊。大風呼嘯，雷電交加，村莊裡的房屋和樹木都受到了不同程度的損壞。那棵古老的橡樹也被風吹倒了。人們悲痛欲絕，因為橡樹不僅是村莊的象徵，也是他們心靈的寄託。
        </p>
        <p>
          暴風雨過後，人們開始重建家園。他們發現，在橡樹倒下的地方，居然長出了一棵新的小橡樹。這棵小橡樹象徵著新的希望和新的開始。村莊裡的人們重新聚集在一起，他們用愛心和汗水澆灌著這棵小橡樹，期待著它再次長成參天大樹，見證村莊的未來。
        </p>
      </div>
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
    </script>
  </body>
</html>


    """,
    height=1000,
)
