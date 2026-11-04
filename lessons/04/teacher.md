---
title: 第 4 课 · 教案
title_en: Lesson 4 · Teacher plan
lesson: "04"
tab: teacher
---

# 👩‍🏫 第 4 课教案：猜数字游戏（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子能写出 `if / elif / else`，分清 `=` 和 `==`，会用 `random.randint` 和 `break`，做出一个能给家人玩的猜数字游戏。**更重要的：** 正式学会「卡住了怎么办」四步法，并在找 bug 游戏里**自己**读报错、修 bug。

**今天的铁律：** 孩子卡住时，老师**先不说话**，指一指四步法：「第一步是什么？」让他自己读报错。老师是第四步。

**知识点：** if / elif / else、比较运算、random.randint、break。复习：input + int（第 2 课）、for（第 3 课）、变量。**不要**讲 while（第 6 课）、列表只在作业提示里当魔法用。

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-4">
  <li>把 <a href="../learn/">学一学</a> 的画板全跑一遍。注意 <code>input()</code> 现在是画板下面的输入框（不是弹窗），知道在哪里打字。</li>
  <li>自己先「治」一遍 3 个病号，看修好后是不是出现 🏆。</li>
  <li>玩 <a href="{{ '/games/bugs/' | relative_url }}">🐞 虫虫医院</a> 前 2 关。</li>
  <li>准备两张小卡片：一张写 <code>=</code>「放进去」，一张写 <code>==</code>「等于吗？」。讲到时举起来。</li>
  <li>看看孩子第 3 课作业，热身时提一句他的万花筒。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>倒计时改 5、螺旋改 120。问：「<code>range(3, 0, -1)</code> 数哪几个数？」不看代码说。</td><td>上周的 for 记住了吗</td></tr>
<tr><td><b>5–15</b></td><td>✨ if</td><td>下雨带伞的比喻。举两张卡片：<code>=</code> 放进去 / <code>==</code> 等于吗。<br><b>先做猜一猜</b>（输入 7 出几行），再运行例 1，输入 3、再输入 7。<br>改一改：加 elif 太大 / 太小。<b>故意</b>把 == 改成 =，读报错。</td><td>能不能说出「只走一条路」；「游戏结束」为什么总是出现（缩进！）</td></tr>
<tr><td><b>15–23</b></td><td>🎲 例 2</td><td>骰子跑 5 次，「每次一样吗？」改 20 面。加 <code>elif dice == 1</code>，问放哪儿——引出「从上往下第一个成立的」。<br>海龟掷硬币例子 2 分钟。</td><td>elif 顺序的理解</td></tr>
<tr><td><b>23–35</b></td><td>🎯 例 3</td><td>先做猜一猜（没有 break 会怎样）。填 3 个空。<b>老师玩一局，孩子指着代码说现在跑到哪一行</b>（这是最好的理解检查）。改成 1–100、7 次，聊「每次猜中间」的策略。</td><td>他能不能跟着程序走一遍</td></tr>
<tr><td><b>35–40</b></td><td>🐾 例 4</td><td>随机散步，改 300 步，加第三种方向。快速过，主要是「if 和 for 可以合在一起」。</td><td>看到 if 在 for 里面有没有疑问</td></tr>
<tr><td><b>40–50</b></td><td>🛟 四步法 + 找 bug</td><td>正式讲四步法（指着流程图）。然后 3 个病号：<b>老师一句话不说</b>，只问「第一步？」。每修好一个，让他说「bug 是什么」。写进笔记本的「我遇到过的报错」表。</td><td>第一反应：慌 / 猜 / 读报错？读了就夸</td></tr>
<tr><td><b>50–55</b></td><td>🤖 AI 排错</td><td>在病号上点「📋 复制问 AI」，看看它打包了什么。真的贴给 AI 一次，看它给的是提示还是答案。如果它直接给答案，让孩子说「只要提示」。</td><td>他会不会检验 AI 的提示</td></tr>
<tr><td><b>55–60</b></td><td>📓 收尾</td><td>给家人玩一局猜数字。笔记本 3 行 + 今天的 bug。看作业页，说清 🥉 只要填 TODO 1。</td><td>能否用自己的话说 == 和 = 的区别</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>例 1 + == 陷阱</b> &gt; <b>例 3 猜数字</b> &gt; <b>四步法 + 病号</b> &gt; 例 2 骰子 &gt; AI 排错 &gt; 例 4 &gt; 游戏。<br>
虫虫医院可以留给作业周。例 4 随机散步可以直接跳过。
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
| 随机数每次不一样，不知道答案 | 测试时猜不中 | 教他临时加一行 `print(secret)` 来「作弊调试」——这是真正的程序员技巧！ |

## ✅ 参考答案

<details class="hint"><summary>例 3 猜数字填空</summary><pre>secret = random.randint(1, 10)
...
    if guess == secret:
...
        print("📈 太小了 Too small")</pre></details>
<details class="hint"><summary>病号 1 / 2 / 3</summary><pre># 病号 1：for 后面加冒号
for i in range(3):
    print("嗨")

# 病号 2：== 比较
if answer == 5:
    print("正确")

# 病号 3：if 下面的行缩进；「结束」不缩进
if x > 3:
    print("大")
print("结束")</pre></details>
<details class="hint"><summary>作业 🥉 TODO 1</summary><pre>        print("📈 太小了 Too small")</pre></details>
<details class="hint"><summary>作业 🥈 TODO 2 / 3</summary><pre>colors = ["red", "gold", "cyan"]
t = turtle.Turtle()
t.speed(0)
...
    if guess == secret:
        print(f"🎉 猜对了！你用了 {count} 次")
        for i in range(60):
            t.color(colors[random.randint(0, 2)])
            t.forward(i * 2)
            t.left(91)
        break
...
answer = input("再玩一次吗? (y/n) ")
if answer == "y":
    print("太好了！按一下 ▶ 再来一局")
else:
    print("下次见！")</pre></details>
<details class="hint"><summary>作业 🥇 TODO 4</summary><pre>    elif guess > secret:
        print("📉 太大了")
    else:
        print("📈 太小了")
    diff = abs(guess - secret)
    if diff &lt;= 2:
        print("🔥 很热！")
    elif diff &lt;= 5:
        print("🌤 温的")
    else:
        print("🧊 很冷")</pre>（注意：冷热判断要放在 if/elif/else 之后、for 里面，缩进 4 格）</details>

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| == 和 = 他分清了吗？错了几次？ | |
| 3 个病号各用了多久？他读报错了吗？ | |
| 他跟着程序「指到哪一行」做到了吗？ | |
| AI 给的是提示还是答案？他检验了吗？ | |
| 下周要补的 | |
