# 🧮 函数里改外面的变量要用 global / Use global to change an outside variable inside a function
fuel = 3

def burn():
    global fuel           # 告诉电脑：我要改外面那个 fuel / "I mean the fuel outside"
    fuel = fuel - 1
    print("燃料：", fuel)

burn()
burn()
burn()
print("最后燃料：", fuel)
