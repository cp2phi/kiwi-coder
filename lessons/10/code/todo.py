# test-input: 1 | 喂猫 | 1 | 写作业 | 2 | 1 | 3 | 4
# 📝 迷你待办 app  Mini to-do app
# 读代码练习：先别改，看懂它是怎么工作的 / Reading practice: understand it before changing it

todo = []                                   # 要做的事，放在一个列表里 / things to do, in a list

def show():                                 # 显示所有待办 / show every item
    print("\n📝 我的待办：")
    if len(todo) == 0:
        print("  （空的）")
    for i in range(len(todo)):
        print(f"  {i + 1}. {todo[i]}")

def add(thing):                             # 加一件事 / add one thing
    todo.append(thing)
    print(f"✅ 加好了：{thing}")

def done(number):                           # 做完一件事，把它拿掉 / remove a finished thing
    thing = todo.pop(number - 1)
    print(f"🎉 做完了：{thing}")

while True:                                 # 主循环：一直问，直到选 4 / main loop until 4
    print("\n1 加事情  2 做完一件  3 看全部  4 退出")
    choice = input("选： ")
    if choice == "1":
        add(input("要做什么？ "))
    elif choice == "2":
        done(int(input("做完了第几件？ ")))
    elif choice == "3":
        show()
    elif choice == "4":
        print("👋 再见！")
        break
