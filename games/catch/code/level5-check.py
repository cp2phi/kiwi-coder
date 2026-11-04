# 🍎 接水果 第 5 关：过关检查 / Fruit Catcher level 5: win check
try:
    fruit2
    if not hasattr(fruit2, "ycor"):
        print("__KC_HINT__ fruit2 要是一个海龟（像 fruit 一样用 turtle.Turtle() 或 make_fruit() 做出来），不能只是一个数字|fruit2 must be a turtle (made with turtle.Turtle() or make_fruit(), like fruit), not just a number")
    elif fruit2 is fruit:
        print("__KC_HINT__ fruit2 和 fruit 是同一个水果！要再做一个新的|fruit2 is the same fruit as fruit! Make a brand-new one")
    else:
        print("__KC_WIN__")
except NameError:
    print("__KC_HINT__ 还没有叫 fruit2 的第二个水果。像做 fruit 一样再做一个，名字叫 fruit2|There is no second fruit called fruit2 yet. Make one the same way as fruit, and name it fruit2")
