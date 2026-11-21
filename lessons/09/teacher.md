---
title: 第 9 课 · 教案
title_en: Lesson 9 · Teacher plan
lesson: "09"
tab: teacher
---

# 👩‍🏫 第 9 课教案（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 学会字典（键 → 值）这一个语法点——拿、放、改、<code>in</code>、<code>.get</code>、循环；进阶：<code>.items()</code>、抽屉里放列表、用字典数数（<code>d[k] = d.get(k, 0) + 1</code>）。同时建立「AI 说的话要检验」的习惯——孩子今天要**亲手抓到 AI 的错误**（事实错 + 代码错）。

**今天的铁律：** 第三阶段开始，老师**不碰键盘**、**不给代码**。孩子问「怎么写」时，回答「你觉得字典里应该放什么标签？」「例 2 是怎么做的？」。只在四步法走完后才出手。

<div class="box box-tip"><span class="box-title">📈 这一课比原版难了大约 30–40%</span>
① 热身改成用第 7、8 课的函数 + strip/lower 数数（引出「字典能只看一遍就数完」）；② 新增一道字典<b>追踪题</b>（更新值 + .get 默认值）；③ 翻译机加两个「照说明自己写」的命令（全部 / 改）；④ 新增进阶例 3「行星资料库」（抽屉里放列表 + <code>.items()</code>）和例 4「用字典数数」（数数公式 + 追踪题 + 故意 KeyError）；⑤ 例 5 变成「字典版会学习的电脑」；⑥ 挑战要求 4 个功能，其中一个用第二个字典计数；⑦ AI 侦探加了太空题和<b>代码题</b>，侦探行动有 <b>2 个错</b>。原来的「问答机」和「按名字画图形」两个例子删掉了（问答机的写法在侦探行动和作业 🥈 里仍然有）。<br>
<b>如果孩子吃力</b>：见下面「怎么砍」——例 3 / 例 5 / 挑战先砍，例 4 的数数公式尽量保留（第 10 课以后会常用）。
</div>

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-9">
  <li>自己把 <a href="../learn/">学一学</a> 的例子跑一遍，特别是：snacks 追踪题、例 2 自己加「全部 / 改」、例 4 故意改成 <code>counts[m] + 1</code> 看 KeyError、「侦探行动」的 detective.py。</li>
  <li>准备「三个来源」的道具：一本词典 / 一页打印好的小知识（新西兰首都惠灵顿；最有名的象征鸟几维鸟——新西兰其实没有官方「国鸟」；怀唐伊条约 1840 年；太阳系最大的行星是木星；1969 年阿波罗 11 号，阿姆斯特朗第一个踏上月球；火星有两颗卫星火卫一、火卫二）。最好再打开一个靠谱网站（NASA、百科全书）当「查书」。</li>
  <li>在你自己的 AI（Codex / ChatGPT）里，用学一学 ④ 的配方问一个「新西兰和太空 6 题问答机」，看看它这次有没有编错——有错更好，留着课上用。</li>
  <li>检查孩子上周作业（week08-homework）是否在作品墙上，准备一句具体的表扬（特别是他写的 to_chinese 或困难模式）。</li>
  <li>想好孩子最熟的一个领域（宝可梦 / 游戏角色 / 火箭），用来做「挑战：我的资料库」。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>填 <code>m.strip().lower()</code>，看到 4、2、1。问：「数 3 种拳要把列表看 3 遍。100 种呢？」——留个悬念给例 4。</td><td>能不能自己想到「先整理再比较」？</td></tr>
<tr><td><b>5–20</b></td><td>📖 字典</td><td>比喻：列表是编号的格子，字典是贴标签的抽屉。<br>例 1：<b>先做猜一猜</b>，再去掉 # 看 KeyError，再用 .get。<b>snacks 追踪题</b>让他在纸上一行一行算。<br>例 2 翻译机：教它一个新词——「它记住了！」。✍️ 自己加「全部」；「改」时间够再做。</td><td>KeyError 出现时他的第一反应是读报错还是叫老师？追踪题能想到「标签一样 = 换掉」吗？</td></tr>
<tr><td><b>20–30</b></td><td>🪐🔢 进阶：例 3 + 例 4</td><td>例 3：<code>moons["火星"][0]</code> 先猜；看 <code>.items()</code> 一次拿两个。✍️ order 字典（most_moons 可留作业）。<br>例 4：讲数数公式的读法，做 counts 追踪题，运行看字典一步步长大。🐞 故意改成 <code>counts[m] + 1</code> 看 KeyError——<b>这道题等下 AI 侦探会再出现</b>。</td><td>能用自己的话读出 <code>counts.get(m, 0) + 1</code> 吗？</td></tr>
<tr><td><b>30–43</b></td><td>🕵️ AI 侦探</td><td>① 四道「哪句是错的」quiz：首都、.get、<b>火星卫星</b>、<b>AI 写的计数代码</b>——讨论「为什么听起来很对」「代码一运行就露馅」。② 三个来源。③ 隐私 quiz——顺便问「你的昵称是什么？为什么不用真名？」。④ 配方：让他自己改出一个好问题。</td><td>他能不能举出一个自己遇到过的「AI 说错了」的例子？代码题他是读出来的还是猜的？</td></tr>
<tr><td><b>43–53</b></td><td>🔍 侦探行动</td><td>跑 detective.py，一条一条核实，每条后面写 <code># ✅ 查过：来源</code>。用准备好的道具查。<b>找到 2 个错</b>才算完成。<br>时间够：让他用配方真的问一次 AI，把代码贴进来核实。</td><td>他是先怀疑「两个奥克兰」，还是全盘相信？找到第 1 个错后会继续查剩下的吗？</td></tr>
<tr><td><b>53–60</b></td><td>📓 收尾</td><td>看<a href="../homework/">作业页</a>说清三个等级。笔记本 3 行 + 「我抓到 AI 的一个错误」。例 5、挑战、密码破译游戏回家选做。</td><td>能否用自己的话说「字典是什么」「AI 的话为什么要检验」</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够 / 太难时怎么砍</span>
优先级：<b>例 1 + snacks 追踪题</b> &gt; <b>例 2（含「全部」）</b> &gt; <b>侦探行动</b> &gt; AI 侦探 ① 的四道题 &gt; 例 4 数数公式 &gt; 隐私 quiz &gt; 例 3 &gt; 配方 &gt; 例 5 &gt; 挑战 &gt; 游戏。<br>
<b>孩子吃力时：</b>① 例 3 只运行 + 做第一个改一改，不写 order / most_moons；② 例 4 只做追踪题和 KeyError 实验，英文版数数留作业；③ 翻译机的「改」跳过；④ 挑战变成作业的额外选做。<b>侦探行动不要砍</b>——它是这一课的灵魂。<br>
<b>孩子很快时：</b>让他做 most_moons、例 4 的英文版、例 5 和挑战，或者把翻译机改成「一个词多个意思」（抽屉里放列表）。
</div>

---

## 🗣️ AI 侦探讨论脚本

1. **开场：**「上周 AI 帮你排错，它说得都对吗？」（让他回忆一次 AI 说错的经历；没有就讲你自己的。）
2. **为什么会编造？** 用小学生能懂的话：AI 读过非常多的文字，它很会「接着说」，但它不是在「查」，是在「猜最像的下一句」。猜得像 ≠ 猜得对。
3. **「越理所当然越要查」：** 首都那道题就是例子——奥克兰最大、最有名，所以很多人也错。太空题同理：土星的环最有名，所以 AI 可能把「最大」也安到它头上。
4. **会变的数字最危险：** 木星、土星的卫星数一直在变（天文学家不断发现新的），AI 可能记的是旧数字。所以例 3 故意只放了 4 颗卫星数很确定的行星。
5. **代码也会错：** AI 的计数代码看起来很对，<b>一运行就 KeyError</b>。代码类问题，运行就是最好的核实。
6. **三个来源的顺序：** 代码类 → 运行（电脑不撒谎）；知识类 → 书 / 老师 / 靠谱网站；都不方便 → 换个问法再问一次，两次不一样就要小心。
7. **隐私：** 问他「AI 知道你住哪里有什么坏处？」引导到：网站、AI、陌生人都一样——昵称可以，真名+学校+地址+电话+密码+照片不行。
8. **收尾一句话：**「AI 是很厉害的队员，但你是队长。队长要检查。」

## 🗣️ 好用的话术

- 「字典里，**标签**是什么？抽屉里装的是什么？」
- 「报错说 KeyError——它在找哪把钥匙？那个抽屉存在吗？」
- 「这个标签以前有没有？有的话，等号是在『新建』还是在『换掉』？」
- 「<code>counts.get(m, 0)</code> 读出来是什么意思？」
- 「你觉得 AI 这句话，**用哪个来源**查最快？」
- 夸过程：「你先怀疑了『两个奥克兰』，这就是侦探！」

## 🧱 常见卡点

| 卡点 | 应对 |
|---|---|
| 字典的冒号、逗号写丢了 | 让他对照例 1 一行一行数：每个「标签: 东西」后面要逗号 |
| `maori[word]` 和 `maori.get(word)` 分不清 | 问：「如果没有这个标签，你希望程序崩溃还是说『不知道』？」 |
| for k in dict 时想用 k 当答案 | 「k 是标签，答案在抽屉里：dict[k]」；或者换成 `.items()` |
| `"food" in maori` 以为是 True | 「in 只看标签」 |
| 数数时写成 `counts[m] += 1` | 正是 AI 代码题的 bug——让他自己读 KeyError，回到数数公式 |
| 「全部 / 改」的 if 顺序乱了 | 「先判断命令，再判断是不是一个词」：命令放前面，`elif word in ...` 放后面 |
| 中文输入法打出了 ：和 ， | 画板会提示中文符号；让他切换输入法重打 |
| 侦探行动全信 AI / 找到 1 个就停 | 不说答案，只问「第 1 题和第 3 题的答案一样，奇怪吗？」「一共有 2 个错，还差一个」 |

## ✅ 参考答案

<details class="hint"><summary>热身 + 两道追踪题</summary>空里填 <code>m.strip().lower()</code>，结果 rock 4、paper 2、scissors 1。<br>snacks 追踪题：<b>3 5 1</b>。counts 追踪题（例 4）：<b>3 3</b>。</details>

<details class="hint"><summary>例 1 改一改</summary>加 rā 之后 <code>len(maori)</code> 是 5。<code>"food" in maori</code> 是 False，因为 in 只看标签。</details>

<details class="hint"><summary>例 2 翻译机：全部 + 改</summary><pre>while True:
    word = input("词 / word: ").strip().lower()
    if word == "再见":
        break
    elif word == "全部":
        for k in maori:
            print(f"  {k} = {maori[k]}")
    elif word == "改":
        w = input("改哪个词？ ").strip().lower()
        if w in maori:
            maori[w] = input("新的意思： ")
            print("✅ 改好了！")
        else:
            print("没有这个词 / no such word")
    elif word in maori:
        print(f"👉 {word} = {maori[word]}")
    else:
        print("🤔 不知道这个词，你来教我？")
        maori[word] = input("它的意思是： ")
        print("✅ 学会了！")</pre>把 <code>if word in maori:</code> 改成 <code>if word in "maori":</code> 后：它在检查「这个词是不是 maori 这几个字母的一部分」，比如输入 <code>ma</code> 会以为认识，然后 <code>maori["ma"]</code> 报 KeyError。</details>

<details class="hint"><summary>例 3 行星资料库</summary><code>moons["火星"][0]</code> = 火卫一；<code>len(moons["地球"])</code> = 1。<pre>order = {"水星": 1, "金星": 2, "地球": 3, "火星": 4}
for planet, n in order.items():
    print(planet, "是第", n, "颗行星")

def most_moons(moons):
    best = ""
    for planet, moon_list in moons.items():
        if best == "" or len(moon_list) &gt; len(moons[best]):
            best = planet
    return best
# most_moons(moons) → 火星</pre></details>

<details class="hint"><summary>例 4 用字典数数</summary><pre>moves = ["Rock", " paper", "ROCK", "scissors ", "rock", "Paper", "rock"]
counts = {}
for m in moves:
    m = m.strip().lower()
    counts[m] = counts.get(m, 0) + 1
print(counts)    # {'rock': 4, 'paper': 2, 'scissors': 1}</pre>改成 <code>counts[m] = counts[m] + 1</code>：第一个词时 counts 还是空的，要先<b>读</b> counts["石头"]，抽屉不存在 → KeyError。</details>

<details class="hint"><summary>例 5 字典版石头剪刀布</summary><code>beats[me]</code> 是「我出的拳能赢的那个」，等于电脑出的就是我赢。<code>winner_against</code> 是 <code>beats</code> 的「反过来」：beats 里 石头→剪刀，winner_against 里 剪刀→石头。</details>

<details class="hint"><summary>挑战：我的资料库</summary><pre>while True:
    cmd = input("查 / 加 / 全部 / 退出： ").strip()
    if cmd == "退出":
        break
    elif cmd == "查":
        word = input("查什么？ ").strip()
        print("👉", my_dict.get(word, "没有这个"))
        looked_up[word] = looked_up.get(word, 0) + 1
    elif cmd == "加":
        word = input("标签？ ").strip()
        value = input("内容？ ").strip()
        if word in my_dict:
            if input("已经有了：" + my_dict[word] + "，要换掉吗？(y / n) ").strip().lower() == "y":
                my_dict[word] = value
        else:
            my_dict[word] = value
    elif cmd == "全部":
        for k, v in my_dict.items():
            print(f"  {k}: {v}")

top = ""
for word, n in looked_up.items():
    if top == "" or n &gt; looked_up[top]:
        top = word
if top != "":
    print("最常查的是", top, "（", looked_up[top], "次）")</pre></details>

<details class="hint"><summary>AI 侦探 ① 四道题 + detective.py 的错误</summary>四道题：首都是奥克兰（错，惠灵顿）；<code>.get</code> 会报错（错）；火星没有卫星（错，有火卫一、火卫二两颗）；计数代码（第一个词就 KeyError）。<br>
detective.py 的 <b>2 个错</b>：「新西兰的首都是？」应为<b>惠灵顿</b>；「太阳系最大的行星是？」应为<b>木星</b>（不是土星）。其余：最有名的象征鸟几维鸟 ✅（新西兰没有官方指定的「国鸟」，所以题目问的是「象征鸟」）、最大城市奥克兰 ✅、人类第一次登月 1969 年 ✅（阿波罗 11 号）、怀唐伊条约 1840 年 ✅。</details>

<details class="hint"><summary>作业 🥉🥈🥇 参考</summary>
<pre>import random
words = {
    "kia ora": "你好", "kai": "食物", "moana": "大海", "whānau": "家人",
    "aroha": "爱", "whare": "房子", "wai": "水", "kura": "学校",
}

# 🥉
new_words = 0
while True:
    word = input("词 / word: ").strip().lower()
    if word == "再见":
        break
    if word == "全部":
        for w, meaning in words.items():
            print(" ", w, "=", meaning)
    elif word in words:
        print("👉", words[word])
    else:
        words[word] = input("不认识！它的意思是： ").strip()
        new_words += 1
        print("✅ 学会了！")
print("这次教会了", new_words, "个新词")

# 🥈（放在最前面，用 mode 决定走哪一段）
mode = input("翻译 还是 测验？ ").strip()
if mode == "测验":
    mistakes = {}
    score = 0
    for i in range(5):
        w = random.choice(list(words))
        if input(w + " 的意思是？ ").strip() == words[w]:
            score += 1
        else:
            print("❌ 是", words[w])
            mistakes[w] = mistakes.get(w, 0) + 1
    print("得分", score, "/ 5")
    hardest = ""
    for w, n in mistakes.items():
        if hardest == "" or n &gt; mistakes[hardest]:
            hardest = w
    if hardest != "":
        print("你最容易错的词是", hardest)

# 🥇（示例数据：rā 其实是「太阳 / 白天」，不是「月亮」）
ai_words = {"kai": "食物", "moana": "大海", "rā": "月亮", "aroha": "爱"}
checked = {"kai": True, "moana": True, "rā": False}
right = 0
for w, meaning in ai_words.items():
    if w in checked:
        if checked[w]:
            print("✅", w, "=", meaning)
            right += 1
        else:
            print("❌", w, "≠", meaning)
    else:
        print("❓", w, "=", meaning, "（没查）")
print("AI 在查过的词里对了", int(right / len(checked) * 100), "%")</pre>
🥇 讨论题的答案：不能。只查了 3 个，样本太少——就像只尝了一口就说整锅汤咸不咸。查得越多，百分比越可信。</details>

## 📝 观察记录

| 项目 | 记录 |
|---|---|
| 最兴奋的瞬间 | |
| 遇到 KeyError 时的第一反应 | |
| 两道追踪题（snacks / counts）猜对了吗？ | |
| 数数公式能用自己的话读出来吗？ | |
| 自己举出的「AI 说错」例子 | |
| 侦探行动：先怀疑了哪一条？两个错都找到了吗？ | |
| 难度感受：太难 / 刚好 / 还能更难？ | |
| 下周想做什么项目（提前问一句） | |
