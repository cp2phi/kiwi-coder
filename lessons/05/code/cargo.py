# test-input: food
# 🚀 火箭货舱：in、remove()、pop() / Rocket cargo bay: in, remove(), pop()
cargo = ["water", "food", "oxygen", "telescope", "robot"]
print(f"货舱里有 {len(cargo)} 样 / {len(cargo)} items: {cargo}")

item = input("要拿出哪一样？Which item should we unload? ")
if item in cargo:                            # in：列表里有它吗？/ in: is it in the list?
    cargo.remove(item)                       # remove：按名字拿走 / remove: take it out by name
    print(f"✅ 拿出了 {item} / unloaded {item}")
else:
    print(f"❌ 货舱里没有 {item} / no {item} on board")

last = cargo.pop()                           # pop()：拿走最后一个，还把它交给你 / pop(): takes out the last one AND hands it to you
print(f"最后装上去的 {last} 也拿出来了 / the last one loaded, {last}, came out too")

first = cargo.pop(0)                         # pop(0)：拿走第 0 个 / pop(0): takes out drawer 0
print(f"第 0 个是 {first} / drawer 0 was {first}")
print(f"还剩 Left: {cargo}")
