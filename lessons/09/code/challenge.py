# 🏆 挑战：我的资料库 app  Challenge: my database app
# test-input: 查 | 皮卡丘 | 查 | 喷火龙 | 退出
# 主题你定 Pick your topic：宝可梦 → 属性？游戏角色 → 技能？朋友昵称 → 最爱的食物？
#   Pokémon → type? game character → skill? friend's nickname → favourite food?
# 必须有 Must have:
#   ① 查：用 .get，查不到也不报错                      look up: use .get, never crash
#   ② 加 / 改：标签已经有了，先问「要换掉吗？(y / n)」   add / update: if the label exists, ask "replace it? (y / n)" first
#   ③ 全部：用 .items() 整整齐齐打印出来                 list all: print them neatly with .items()
#   ④ 统计：用第二个字典数每个词被查了几次，退出时打印「最常查的是 ___」
#      stats: a second dict counts how often each word is looked up; on exit print "most looked-up: ___"

my_dict = {
    "皮卡丘": "电",
    "小火龙": "火",
    "杰尼龟": "水",
}
looked_up = {}       # 每个词被查了几次 / how many times each word was looked up

while True:
    cmd = input("查 / 加 / 全部 / 退出： ").strip()
    if cmd == "退出":
        break
    elif cmd == "查":
        word = input("查什么？ What? ").strip()
        print("👉", my_dict.get(word, "没有这个 / not found"))
        # ✍️ 在这里用 looked_up 数一数 / count it in looked_up here

    # ✍️ 加上「加」和「全部」/ add "加" and "全部" here

# ✍️ 打印最常查的词 / print the most looked-up word
print("👋 再见！ Bye!")
