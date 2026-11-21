# 🦆 小黄鸭法：把每一行念给小黄鸭听 / Rubber duck: explain every line to a duck
# 着陆模拟器：试 3 次着陆。规则：速度 ≤ 2 才安全。没有报错，但结果怪怪的。念出来，你就会发现！
# Landing simulator: 3 tries. Rule: speed ≤ 2 is safe. No error, but the results feel wrong. Say it out loud and you'll find it!
# test-input: 1 | 5 | 2

MAX_SPEED = 2

for i in range(3):
    speed = int(input(f"第 {i + 1} 次着陆，速度是？/ Landing {i + 1}, speed? "))
    if speed > MAX_SPEED:
        print("✅ 安全着陆！/ Safe landing!")
    else:
        print("💥 太快了，坠毁！/ Too fast — crash!")
