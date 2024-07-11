i = 0
while i < 5:  # 條件式迴圈，當 i < 5 時執行迴圈
    print(i)
    i += 1  # i = i + 1

# 算術指定運算子
a = 10
a += 1  # 等同於 a = a + 1
print(a)
a -= 1  # 等同於 a = a - 1
print(a)
a *= 2  # 等同於 a = a * 2
print(a)
a /= 2  # 等同於 a = a / 2
print(a)
a //= 2  # 等同於 a = a // 2
print(a)
a %= 3  # 等同於 a = a % 3
print(a)
a **= 2  # 等同於 a = a ** 2
print(a)

# 根據以上符號列出優先順序
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
# 5. == != > < >= <=
# 6. not、and、or
# 7. = += -= *= /= //= %= **=


# break 跳出一層迴圈
i = 1
while i < 6:  # 條件式迴圈，當 i < 6 時執行迴圈
    print(i)  # 印出 i
    if i == 3:
        break  # 當 i 等於 3 時跳出迴圈
    i += 1

for i in range(1, 6):  # for 迴圈，i 從 1 到 5
    print(i)  # 印出 i
    if i == 3:
        break  # 當 i 等於 3 時跳出迴圈


# random
import random  # 匯入 random 模組

print(random.randrange(10))  # 隨機產生 0 到 9 的整數
print(random.randrange(1, 10))  # 隨機產生 1 到 9 的整數
print(random.randrange(1, 10, 2))  # 隨機產生 1 到 9 的奇數
# randrange跟range一樣，第一個數字是開始，第二個數字是結束，第三個數字是間隔
# 不會數到結束的數字，randrange(1, 10)只會從1~9隨機選一個數字

print(random.randint(1, 10))  # 隨機產生 1 到 10 的整數
# randint跟randrange一樣，第一個數字是開始，第二個數字是結束
# 但randint一定要設定兩個數字，且會數到結束的數字
