---
title: 第 4 课 · 教案
title_en: Lesson 4 · Teacher plan
lesson: "04"
tab: teacher
---

# 👩‍🏫 第 4 课教案：猜数字游戏（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子能**自己写出**（不是填空）`if / elif / else`，分清 `=` 和 `==`，会用 `random.randint`、`break` 和 `%`，能写一层「if 套 if」，做出一个能给家人玩的猜数字游戏。**更重要的：** 正式学会「卡住了怎么办」四步法，并在找 bug 游戏里**自己**读报错、修 bug——包括一个**没有报错的逻辑 bug**。

**今天的铁律：** 孩子卡住时，老师**先不说话**，指一指四步法：「第一步是什么？」让他自己读报错。老师是第四步。

**知识点：** if / elif / else、比较运算、random.randint、break、`%`（第 3 课当魔法用过，今天正式讲）、if 套 if。复习：input + int、f-string（第 2 课）、for（第 3 课）、变量。**不要**讲 while（第 6 课）、and / or（第 6 课）、列表（第 5 课）。

<div class="box box-tip"><span class="box-title">📈 本课难度已上调（约 +30%）</span>
第 1–3 课孩子觉得偏简单，所以这课做了这些改动：<br>
① 例 3 猜数字从「填 3 个空」变成<b>自己写 7 行 if/elif/else + break</b>（有 3 级提示）；<br>
② 新增「加餐」：<code>%</code> 余数 + 太空报数（elif 顺序陷阱）+ if 套 if；<br>
③ 新增病号 4：<b>没有红框的逻辑 bug</b>（elif 顺序错）；<br>
④ 新增 🏆 挑战「火箭发射控制中心」：只有设计说明，没有起始代码；<br>
⑤ 作业 🥉 不再是「改一句话」，要自己写判断；🥇 是「电脑猜你的数字」（二分法），需要先在纸上设计。<br>
⑥ 掷硬币选颜色（旧例 2b）删掉了，腾出时间。
</div>

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-4">
  <li>把 <a href="../learn/">学一学</a> 的画板全跑一遍。注意 <code>input()</code> 现在是画板下面的输入框（不是弹窗），知道在哪里打字。</li>
  <li>自己先「治」一遍 4 个病号，看修好后是不是出现 🏆（病号 4 要把 <code>&gt;= 90</code> 挪到上面）。</li>
  <li>自己写一遍例 3 的 7 行和 🏆 发射控制中心，体会孩子会卡在哪（主要是缩进层次）。</li>
  <li>玩 <a href="{{ '/games/bugs/' | relative_url }}">🐞 虫虫医院</a> 前 2 关。</li>
  <li>准备两张小卡片：一张写 <code>=</code>「放进去」，一张写 <code>==</code>「等于吗？」。讲到时举起来。</li>
  <li>看看孩子第 3 课作业，热身时提一句他的万花筒。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>先让他<b>在纸上</b>写出 <code>range(10, 0, -3)</code> 的数（10 7 4 1），再运行对答案。然后<b>自己写</b> 2 行 for 打印 Stage 1–3（考 <code>i + 1</code>）。</td><td>range 的「停在 b 之前」和步长还记得吗</td></tr>
<tr><td><b>5–13</b></td><td>✨ if + 例 1</td><td>下雨带伞的比喻。举两张卡片：<code>=</code> 放进去 / <code>==</code> 等于吗。<b>先做猜一猜</b>（输入 7 出几行），再运行。<br>改一改：<b>他自己打</b> elif 太大 / else 太小；再加一个单独的 <code>if guess &gt; 10</code>，问「输入 50 打印几行？」（单独的 if 和 elif 链的区别）。</td><td>能不能说出「只走一条路」；单独的 if 为什么也会跑</td></tr>
<tr><td><b>13–19</b></td><td>🎲 例 2 骰子</td><td>跑 5 次「每次一样吗？」。加 <code>elif dice &gt;= 5</code> 放在 &gt;= 4 下面→永远不出现→挪上去。引出「从上往下第一个成立的；严格的放上面」。</td><td>elif 顺序的理解（后面病号 4 和太空报数都考这个）</td></tr>
<tr><td><b>19–27</b></td><td>➗ 加餐：% 太空报数</td><td>先口算 <code>7 % 3</code>、<code>9 % 3</code>、<code>10 % 5</code>。做猜一猜（i = 10）。运行。把 <code>% 15</code> 挪到下面看 15 变成什么。<b>自己写 4 行</b>双数单数。if 套 if 那一题能做就做，不能做留作业（作业 🥈 会用到）。</td><td>他能不能把「余数是 0」翻译成「整除 / 倍数」</td></tr>
<tr><td><b>27–39</b></td><td>🎯 例 3 猜数字</td><td>先做猜一猜（3、9、7、2 → 问几次？）。然后<b>他自己写 7 行</b>。卡住先看提示 1，再看提示 2。写好后<b>老师玩一局，孩子指着代码说现在跑到哪一行</b>。快的话做「还剩几次」。</td><td>break 的缩进位置；他是照着模式写还是理解了</td></tr>
<tr><td><b>39–49</b></td><td>🛟 四步法 + 找 bug</td><td>正式讲四步法（指着流程图）。4 个病号：<b>老师一句话不说</b>，只问「第一步？」。病号 4 没有红框——问「这次第一步怎么做？」（读代码、自己当电脑走一遍）。写进笔记本「我遇到过的报错」表。</td><td>病号 4：他会不会「当电脑」一行一行走</td></tr>
<tr><td><b>49–54</b></td><td>🤖 AI 排错</td><td>在病号上点「📋 复制问 AI」，真的贴给 AI 一次，看它给的是提示还是答案。病号 4 让他<b>自己写</b>「我想让它___但它___」。</td><td>他会不会检验 AI 的提示</td></tr>
<tr><td><b>54–60</b></td><td>📓 收尾</td><td>给家人玩一局猜数字。笔记本 3 行 + 今天的 bug。看作业页，说清 🥉 要自己写 TODO 1、2；🥇 先在纸上设计。</td><td>能否用自己的话说 == 和 = 的区别</td></tr>
</table>
</div>

<p>例 4 卫星散步和 🏆 发射控制中心是<b>给快的孩子 / 回家玩</b>的，课上不必做。</p>

<div class="box box-warn"><span class="box-title">⏰ 时间不够 / 孩子吃力时怎么砍</span>
优先级：<b>例 1 + == 陷阱</b> &gt; <b>例 3 猜数字（自己写）</b> &gt; <b>四步法 + 病号 1–4</b> &gt; 例 2 骰子 &gt; % 太空报数 &gt; AI 排错 &gt; 例 4 &gt; 挑战。<br>
<b>如果孩子明显吃力：</b>① 例 3 直接给「提示 2」的前两行，让他只写 elif / else；② 加餐只做猜一猜 + 运行，不做 if 套 if；③ 作业告诉他 🥉 只做 TODO 1，TODO 2 算加分。<br>
<b>如果孩子很快：</b>课上就做 🏆 发射控制中心，作业直接冲 🥇。虫虫医院可以留给作业周。
</div>

---

## 🗣️ 好用的话术

- 「一个等号是**动作**，两个等号是**问题**。这一行是动作还是问题？」
- 「电脑说**哪一行**？它抱怨了什么？」（指四步法第一步，不替他读）
- 「if 和 else 是两条路，程序只能走**一条**。走了哪条？」
- 「老师玩，你来指：现在跑到哪一行了？」
- 「这个 bug 你自己找到的！写进笔记本，下次就不会卡了。」

## 🧱 常见卡点和应对

| 卡点 | 现象 | 怎么办 |
|---|---|---|
| `=` 当 `==` | `if x = 5:` 报 SyntaxError | 举卡片。「这是动作还是问题？」 |
| 忘冒号 | `if x > 3` 报错 | 「和 for 一样，这一行最后要什么？」 |
| if 下面没缩进 | 报错或「结束」只打印一次 | 读报错；用 Tab |
| `input()` 不变数字 | `guess > secret` 报 TypeError | 「input 给的是文字，怎么变成数字？」→ 第 2 课的 int() |
| 输入字母 | `int("abc")` 报 ValueError | 这是好机会：读报错框的解释，知道程序也会「被用户弄坏」 |
| elif 顺序 | `elif dice == 1` 放在 `>= 4` 之后也能跑，但放在 `else` 后面报错 | 「从上往下，第一个成立的才跑；else 必须最后」 |
| break 缩进 | break 放到了 for 外面 | 「break 要在 if 里面，if 要在 for 里面」，让他数空格 |
| 单独的 if vs elif | 加了 `if guess > 10` 后输入 50 打印了两行，他以为是 bug | 「这个 if 是新的一条链，还是接在上一个 if 后面？」——单独的 if 每次都会检查 |
| if 套 if 缩进 | 里面的 if 和外面对齐了，逻辑变了但不报错 | 让他用手指头量：里面的 if 应该比外面多 4 格 |
| `%` 看不懂 | 以为 `%` 是百分比 | 用分糖果：「7 颗糖分给 3 个人，每人 2 颗，还剩几颗？」 |
| 随机数每次不一样，不知道答案 | 测试时猜不中 | 教他临时加一行 `print(secret)` 来「作弊调试」——这是真正的程序员技巧！ |

## ✅ 参考答案

<details class="hint"><summary>热身：自己写 Stage 1–3</summary><pre>for i in range(3):
    print(f"第 {i + 1} 级 / Stage {i + 1}")</pre></details>
<details class="hint"><summary>例 3 猜数字（7 行 + 还剩几次 + 很接近）</summary><pre>for tries in range(5):
    guess = int(input(f"第 {tries + 1} 次 Try {tries + 1}: "))
    if guess == secret:
        print("🎉 猜对了！You got it!")
        break
    elif guess &gt; secret:
        print("📉 太大了 Too big")
        if guess - secret &lt;= 2:
            print("🔥 但是很接近！")
    else:
        print("📈 太小了 Too small")
        if secret - guess &lt;= 2:
            print("🔥 但是很接近！")
    print(f"还剩 {4 - tries} 次")</pre>（「还剩几次」和 if 对齐；猜对时 break 已经跳出去，所以不会打印）</details>
<details class="hint"><summary>太空报数：if 套 if 版 + 双数单数</summary><pre>for i in range(1, 16):
    if i % 3 == 0:
        if i % 5 == 0:
            print(f"{i} 🚀⭐")
        else:
            print(f"{i} 🚀")
    elif i % 5 == 0:
        print(f"{i} ⭐")
    else:
        print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} 🌍 双数")
    else:
        print(f"{i} 🌙 单数")</pre>把 <code>% 15</code> 挪到最下面时，15 会打印「15 🚀」，因为 <code>15 % 3 == 0</code> 先成立了。</details>
<details class="hint"><summary>病号 1 / 2 / 3 / 4</summary><pre># 病号 1：for 后面加冒号
for i in range(3):
    print("嗨")

# 病号 2：== 比较
if answer == 5:
    print("正确")

# 病号 3：if 下面的行缩进；「结束」不缩进
if x &gt; 3:
    print("大")
print("结束")

# 病号 4：严格的条件放上面
if score &gt;= 90:
    print("🏆 优秀")
elif score &gt;= 60:
    print("👍 及格")
else:
    print("💪 加油")</pre></details>
<details class="hint"><summary>🏆 挑战：火箭发射控制中心</summary><pre>if fuel &lt; 90:
    print("⛔ NO GO：燃料不够")
else:
    if wind &gt; 40:
        print("⛔ NO GO：风太大")
    else:
        print("✅ GO!")
        for s in range(10, 0, -1):
            if s % 2 == 0:
                print(f"{s} 📡 系统正常")
            else:
                print(s)
        print("🚀 点火！Ignition!")</pre>第 3 步（海龟火箭）没有标准答案：<code>t.left(90)</code> 朝上，循环里 <code>t.forward(10)</code> + <code>t.dot(8, "orange")</code> 就是一道火焰尾巴。</details>
<details class="hint"><summary>作业 🥉 TODO 1 / 2 + 🥈 TODO 3 / 4 / 5</summary><pre>for tries in range(7):
    guess = int(input("你猜 Your guess: "))
    count = count + 1
    if guess == secret:
        print(f"🎉 猜对了！你用了 {count} 次")
        break
    elif guess &gt; secret:
        print("📉 太大了")
        if guess - secret &lt;= 3:          # TODO 3
            print("🔥 很接近了！")
    else:
        print("📈 太小了")
        if secret - guess &lt;= 3:          # TODO 3
            print("🔥 很接近了！")
    print(f"还剩 {7 - count} 次机会")     # TODO 2
    if count % 3 == 0:                    # TODO 4
        if secret % 2 == 0:
            print("🎁 线索：答案是双数")
        else:
            print("🎁 线索：答案是单数")

print(f"答案是 The answer was {secret}")
if guess == secret:                       # TODO 5
    print("🏆 你赢了！")
else:
    print("😢 机会用完了")</pre></details>
<details class="hint"><summary>作业 🥇：电脑猜你的数字（二分法）</summary><pre>print("想一个 1 到 100 的数字，记在心里！")
low = 1
high = 100
for tries in range(7):
    guess = int((low + high) / 2)
    answer = input(f"是 {guess} 吗？(big / small / yes) ")
    if answer == "yes":
        print(f"🎉 我猜到了！用了 {tries + 1} 次")
        break
    elif answer == "big":
        high = guess - 1
    else:
        low = guess + 1</pre>2 的 7 次方是 128 &gt; 100，所以 7 次一定够（不用讲术语，问「每猜一次，剩下的可能少了多少？」——一半）。如果孩子没想到 low / high，先玩不插电版：老师想数，孩子当电脑，用纸记「答案在 __ 到 __ 之间」。</details>

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| == 和 = 他分清了吗？错了几次？ | |
| 4 个病号各用了多久？他读报错了吗？病号 4（没红框）怎么找的？ |
| 例 3 的 7 行用了几级提示？ | |
| 他跟着程序「指到哪一行」做到了吗？ | |
| AI 给的是提示还是答案？他检验了吗？ | |
| 下周要补的 | |
