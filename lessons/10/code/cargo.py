# test-input: 1 | 卫星 | 300 | 1 | 宇航员的食物 | 50 | 1 | 大石头 | 900 | 3 | 2 | 1 | 3 | 4
# 🛰️ 火箭货舱清单  Rocket cargo manifest
# 读代码练习：先别改，看懂它是怎么工作的 / Reading practice: understand it before changing it

cargo = []                                  # 货舱里有什么 / what's in the cargo bay
weights = []                                # 每一件多重（公斤）/ how heavy each one is (kg)
MAX_LOAD = 1000                             # 火箭最多能带多重 / the most the rocket can carry

def total():                                # 现在一共多重 / total weight right now
    t = 0
    for w in weights:
        t = t + w
    return t

def show():                                 # 显示货舱清单 / show the manifest
    print("\n🛰️ 货舱清单 Cargo:")
    if len(cargo) == 0:
        print("  （空的 empty）")
    for i in range(len(cargo)):
        print(f"  {i + 1}. {cargo[i]}  {weights[i]} kg")
    print(f"  总重 total: {total()} / {MAX_LOAD} kg")

def load(thing, kg):                        # 装一件货 / load one item
    if total() + kg > MAX_LOAD:
        print(f"❌ 太重了，火箭飞不起来！/ Too heavy, the rocket can't lift off!")
    else:
        cargo.append(thing)
        weights.append(kg)
        print(f"✅ 装好了 loaded: {thing}")

def unload(number):                         # 卸下第几件 / unload item number …
    thing = cargo.pop(number - 1)
    weights.pop(number - 1)
    print(f"📦 卸下了 unloaded: {thing}")

while True:                                 # 主循环：一直问，直到选 4 / main loop until 4
    print("\n1 装货 load  2 卸货 unload  3 看清单 show  4 发射！launch")
    choice = input("选 choose: ")
    if choice == "1":
        load(input("装什么？what? "), int(input("多少公斤？how many kg? ")))
    elif choice == "2":
        unload(int(input("卸第几件？which number? ")))
    elif choice == "3":
        show()
    elif choice == "4":
        print(f"🚀 带着 {len(cargo)} 件货发射！/ Launching with {len(cargo)} items!")
        break
