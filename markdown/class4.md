

---

## 條件式迴圈

```python
i = 0
while i < 5:  # 當 i < 5 時執行迴圈
    print(i)
    i += 1  # i = i + 1
```

---

## 算術指定運算子

```python
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
```

### 運算子優先順序

1. `()`
2. `**`
3. `* / // %`
4. `+ -`
5. `== != > < >= <=`
6. `not`、`and`、`or`
7. `= += -= *= /= //= %= **=`

---

## `break` 跳出迴圈

```python
i = 1
while i < 6:  # 當 i < 6 時執行迴圈
    print(i)
    if i == 3:
        break  # 當 i 等於 3 時跳出迴圈
    i += 1

for i in range(1, 6):  # i 從 1 到 5
    print(i)
    if i == 3:
        break  # 當 i 等於 3 時跳出迴圈
```

---

## 隨機數範例

```python
import random  # 匯入 random 模組

print(random.randrange(10))  # 隨機產生 0 到 9 的整數
print(random.randrange(1, 10))  # 隨機產生 1 到 9 的整數
print(random.randrange(1, 10, 2))  # 隨機產生 1 到 9 的奇數
# randrange 和 range 一樣，第一個數字是開始，第二個數字是結束，第三個數字是間隔
# 不會數到結束的數字，randrange(1, 10) 只會從 1~9 隨機選一個數字

print(random.randint(1, 10))  # 隨機產生 1 到 10 的整數
# randint 跟 randrange 一樣，第一個數字是開始，第二個數字是結束
# 但 randint 一定要設定兩個數字，且會數到結束的數字
```

---

## 終極密碼小遊戲

```python
import random

TAnser = random.randint(1, 100)
# print(TAnser)
userAns = 0
bigest = 100
smallest = 1

while TAnser != userAns:
    userAns = int(input(f"請輸入你的答案({smallest}~{bigest})："))
    if userAns > TAnser:
        print("你的答案太大了！")
        bigest = userAns
    elif userAns < TAnser:
        print("你的答案太小了！")
        smallest = userAns

print("你的答案是正確的！")
```

---

