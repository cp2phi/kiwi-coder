# 🪐 例 3：行星资料库  Example 3: planet database
# 字典里的「东西」也可以是一个列表！ The thing in a drawer can be a whole list!
# test-input: 火星 | 冥王星
# 这些都是天文学家确认过的事实 / all of these are facts astronomers have confirmed

moons = {
    "水星": [],                       # Mercury：没有卫星 / no moons
    "金星": [],                       # Venus：没有卫星 / no moons
    "地球": ["月球"],                 # Earth：the Moon
    "火星": ["火卫一", "火卫二"],     # Mars：Phobos, Deimos
}

# .items() 一次拿到「标签」和「东西」两个 / .items() gives the label AND the thing together
for planet, moon_list in moons.items():
    print(planet, "有", len(moon_list), "颗卫星 / moons")

# 查一查 / look one up
name = input("想查哪颗行星？ Which planet? ").strip()
if name in moons:
    if len(moons[name]) == 0:
        print(name, "没有卫星 / has no moons")
    else:
        print(name, "的卫星 / moons:", ", ".join(moons[name]))   # 把列表连成一句话（第 8 课见过）/ glue the list into one string (seen in Lesson 8)
else:
    print("资料库里还没有", name, "/ not in the database yet")
