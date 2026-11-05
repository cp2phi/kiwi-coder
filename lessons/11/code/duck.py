# 🦆 小黄鸭法：把每一行念给小黄鸭听 / Rubber duck: explain every line to a duck
# 这个猜数字程序没有报错，但玩起来怪怪的。念出来，你就会发现！
# This guessing game has no error, but it feels wrong when you play. Say it out loud and you'll find it!
# test-input: 3 | 9 | 7

secret = 7

for i in range(3):
    guess = int(input("猜一个数 (1-10)："))
    if guess > secret:
        print("太小了，再大一点！")
    elif guess < secret:
        print("太大了，再小一点！")
    else:
        print("猜对了！🎉")
        break
