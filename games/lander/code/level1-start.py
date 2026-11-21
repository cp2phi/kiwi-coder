# 🛬 第 1 关：自由落体 / Level 1: free fall
# 发动机坏了 😱 助推器从 height 那么高的地方掉下来（height 和 g 每次运行都会变）
# The engine is broken 😱 The booster falls from height (height and g change every run)
# 每一拍 / every tick:
#   1. speed 加 g（越掉越快）/ speed grows by g (faster and faster)
#   2. height 减 speed（往下掉）/ height drops by speed
#   3. draw(height) 把助推器画出来 / draw the booster
#   4. height <= 0 就到海面了：打印  Touchdown at tick 9, speed 9  然后 break
#      height <= 0 means it hit the sea: print  Touchdown at tick 9, speed 9  then break

for tick in range(1, 60):
    # TODO: 第 1、2 步 / steps 1 and 2
    draw(height)
    if height <= 0:
        print("Touchdown")
        break
