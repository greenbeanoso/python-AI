# 終極密碼小遊戲
import random

TAnser = random.randint(1, 100)
# print(TAnser)
userAns = 0
bigest = 100
smallest = 1
while TAnser != userAns:
    userAns = int(
        input(f"請輸入你的答案({smallest}~{bigest})：".format(bigest, TAnser))
    )
    if userAns > TAnser:
        print("你的答案太大了！")
        bigest = userAns
    elif userAns < TAnser:
        print("你的答案太小了！")
        smallest = userAns
print("你的答案是正確的！")
