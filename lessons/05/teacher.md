---
title: 第 5 课 · 教案
title_en: Lesson 5 · Teacher plan
lesson: "05"
tab: teacher
---

# 👩‍🏫 第 5 课教案（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子能自己说出「列表是一排从 0 开始编号的抽屉」，会用 `[i]`、`[-1]`、`len`、`append`、`random.choice`、`for x in 列表`，并把它们和前面学的 `if`、`for`、f-string、计数器组合起来；加餐：会用 `in` 先检查、`remove()` / `pop()` 拿走，理解「列表会变」。

**今天的铁律：** 第二阶段开始了——**孩子写大部分，你只给提示。** 他卡住时先问「你觉得电脑在抱怨什么？」而不是指出错误。打字慢没关系，但从这课起，每个例子都至少有一处 ✍️ 是**自己写 1–5 行**，不再只是改数字。

<div class="box box-tip"><span class="box-title">📈 本课难度已上调（约 +30%）</span>
① 热身要自己补计数器、再自己加一个 <code>ones</code> 计数器；<br>
② 故事生成器要自己加第 4 个列表 + 写带编号的 for 循环；<br>
③ 毛利语测验除了填空，还要自己写「记错题」和最后的 <code>if len(wrong) == 0</code> 评语；<br>
④ 新增「加餐」：<code>in</code> / <code>remove()</code> / <code>pop()</code>（火箭货舱）+ 一个要「跟着列表一步步变」的猜一猜；<br>
⑤ 🏆 挑战换成「太空任务生成器」（不重复抽 3 人，只有设计说明）；<br>
⑥ 作业 🥉 要自己写 for 循环；🥈 自己写判断 + 用配对列表打印错题；🥇 是「不重复 + 错题再考」的测验 2.0，需要设计。作业里去掉了海龟部分。
</div>

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-5">
  <li>自己把 <a href="../learn/">学一学</a> 从头跑一遍，特别是毛利语测验的填空和「和 AI 一起」部分。</li>
  <li>把 AI 给的 5 个毛利语单词提前自己核对一次（<a href="https://maoridictionary.co.nz" target="_blank" rel="noopener">Te Aka</a>）。如果 AI 真的出了错，那是今天最好的教材；如果没出错，也要强调「这次对了，不代表下次对」。</li>
  <li>打开 <a href="{{ '/games/copy/' | relative_url }}">🎨 图案复刻</a>，确认第 1、2 关能过；第 5 关（螺旋 + 颜色列表）是今天知识的练习，可以留到回家玩。</li>
  <li>准备几张小纸条当「抽屉」：写上 0、1、2、3 贴在桌上，不插电演示 <code>animals[1]</code> 是哪一个。</li>
  <li>再准备 5 张纸条：water、food、oxygen、telescope、robot——加餐「货舱」时一张一张拿走，演示 remove / pop。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>骰子数 6。先运行——「怎么总是 0 个？」让他自己补 <code>sixes = sixes + 1</code>，再自己加 <code>ones</code> 计数器（3 个地方）。</td><td>计数器的三步（开头设 0、里面加 1、最后打印）他想得全吗</td></tr>
<tr><td><b>5–14</b></td><td>📦 列表</td><td>纸条抽屉游戏 2 分钟：「把 1 号抽屉的东西拿出来」——他会拿第二张纸条吗？<br>猜一猜 → 运行 drawers.py → <b>一定要</b>让他故意写 <code>animals[3]</code> 看报错。试 <code>[-1]</code>、<code>[-2]</code>，做 <code>len - 1</code> 那道猜一猜。</td><td>他第一次说「第 0 个」的时候——那一刻就学会了</td></tr>
<tr><td><b>14–22</b></td><td>🎲 故事生成器</td><td>运行 3 次，笑一笑。<b>他自己</b>做 <code>when</code> 列表，再用 for 写 5 个带编号的故事（复习缩进 + <code>i + 1</code>）。</td><td>缩进是不是自己想到的？逗号漏了会不会自己发现？</td></tr>
<tr><td><b>22–27</b></td><td>🌈 彩虹六边形</td><td>先做「第 3 次是什么颜色」的猜一猜（要他用手指一个一个点）。运行。改成五角星。揭秘第 3 课的 <code>colors[i % 6]</code>（30 秒）。</td><td>他能不能说出「for colour in colours 是一个一个拿」</td></tr>
<tr><td><b>27–38</b></td><td>🇳🇿 毛利语测验</td><td>填空 <code>english[i]</code> + 两处 ✍️。故意答错 2 个看 <code>wrong</code>。问「为什么 randint 那行加了词也不用改？」（<code>len - 1</code>）。<br>和 AI 一起：用页面上的问法要 5 个词，贴进去玩，然后<b>一起核对</b>。</td><td>他会不会直接相信 AI？核对时的态度</td></tr>
<tr><td><b>38–47</b></td><td>🚀 加餐：货舱</td><td><b>先不运行</b>：拿纸条摆出 5 样货，按代码一步步拿走，回答猜一猜。再运行验证。然后输入 pizza，再删掉 <code>if … in</code> 看报错——「in 是 remove 的保镖」。时间够就自己写「连续卸货 3 次」。</td><td>他能不能跟着列表一步步变（这是作业 🥇 的基础）</td></tr>
<tr><td><b>47–53</b></td><td>🌠 愿望清单</td><td>空列表 + append 在循环里造列表。✍️ 用 <code>in</code> 防重复。</td><td>能不能把加餐学的 <code>in</code> 用到新地方</td></tr>
<tr><td><b>53–60</b></td><td>📓 收尾</td><td>看作业页：🥉 要自己写 for 循环；🥇 先在纸上画列表怎么变。写笔记本 3 行，其中一行写「AI 的单词对了几个」。</td><td></td></tr>
</table>
</div>

<p>🏆 太空任务生成器和 🎨 图案复刻游戏留给快的孩子 / 回家。</p>

<div class="box box-warn"><span class="box-title">⏰ 时间不够 / 孩子吃力时怎么砍</span>
优先级：<b>列表 + 报错</b> &gt; <b>故事生成器（自己写 for）</b> &gt; 毛利语测验（含 AI 核对）&gt; 加餐货舱 &gt; 彩虹六边形 &gt; 愿望清单 &gt; 挑战 / 游戏。<br>
<b>如果孩子明显吃力：</b>① 热身的 <code>ones</code> 计数器跳过；② 测验只做填空 + <code>wrong.append</code>，评语那段留到作业；③ 加餐只做猜一猜 + 运行，不写循环；④ 作业告诉他 🥉 + TODO 3 就够，TODO 4 和 🥇 算加分。<br>
<b>如果孩子很快：</b>课上做 🏆 太空任务生成器，并挑战「换人」那一步。</div>

---

## 🗣️ 好用的话术

- 「第 **0** 个抽屉是哪个？」（每次他说「第一个」就反问一次，直到他自己改口）
- 「电脑说 IndexError，你觉得 Index 是什么意思？」（让他猜：编号）
- 「这个 for 和第 3 课的 for 有什么不一样？」（一个数数，一个拿东西）
- 「AI 说它『很确定』——我们怎么知道它真的对？」
- 夸过程：「你自己发现要改 `/ 5`，这就是程序员的仔细！」

## 🧱 常见卡点

| 卡点 | 怎么办 |
|---|---|
| 列表少逗号，报错指向下一行 | 「报错有时候指的是上一行，上一行最后少了什么？」 |
| `animals[3]` 报错后不敢再试 | 强调这是故意的，报错是线索；让他读画板的中文解释 |
| for 循环忘记缩进，或者只缩了一行 | 让他把要重复的行全部选中按 Tab |
| 填空写成 `english[0]`（固定答案） | 玩一局就会发现「怎么答案都是 hello」——让游戏本身告诉他 |
| 把 `random.choice` 写成 `random.choise` | 读报错：「不认识 choise」，对照小词典 |
| `remove` 一个不存在的东西报 ValueError | 「谁能在 remove 之前先检查一下？」→ `in` |
| `pop()` 和 `remove()` 分不清 | pop 按**编号**（不写就是最后一个）并且交给你；remove 按**名字** |
| 配对列表 pop 了一个忘了 pop 另一个，答案对不上 | 让他把两个列表都 print 出来看——「它们还是一对吗？」 |
| 毛利语的长音符 ā 不会打 | 答案是英文，不用打长音；告诉他电脑上输入 ā 的方法可以以后学 |

---

## ✅ 参考答案

<details class="hint"><summary>热身：sixes + ones 计数器</summary><pre>sixes = 0
ones = 0
for i in range(10):
    dice = random.randint(1, 6)
    if dice == 6:
        print(f"🎲 {dice}  哇！六点！")
        sixes = sixes + 1
    elif dice &gt;= 4:
        print(f"🎲 {dice}  不错")
    elif dice == 1:
        print(f"🎲 {dice}  💀 一点")
        ones = ones + 1
    else:
        print(f"🎲 {dice}  再来")
print(f"一共掷出 {sixes} 个 6，{ones} 个 1")</pre></details>
<details class="hint"><summary>故事生成器：when 列表 + 5 个带编号的故事</summary><pre>when = ["在半夜，", "在火星上，", "下课的时候，", "生日那天，"]
for i in range(5):
    a = random.choice(who)
    b = random.choice(where)
    c = random.choice(did)
    d = random.choice(when)
    print(f"{i + 1}. {d}{a}{b}{c}！")</pre></details>
<details class="hint"><summary>彩虹五角星</summary><pre>colours = ["red", "orange", "gold", "green", "blue"]
for colour in colours:
    t.color(colour)
    t.forward(150)
    t.left(144)</pre></details>
<details class="hint"><summary>毛利语测验：填空 + 两处 ✍️</summary><pre>    if answer == english[i]:
        ...
    else:
        print(f"❌ 是 {english[i]}")
        wrong.append(maori[i])

print(f"得分 Score: {score} / 5")
if len(wrong) == 0:
    print("💯 满分！")
else:
    print(f"要复习 Review: {wrong}")</pre>加了新词以后 <code>randint(0, len(maori) - 1)</code> 不用改，因为它自己会数列表有多长。</details>
<details class="hint"><summary>货舱：连续卸货 3 次 / 愿望清单防重复</summary><pre>for k in range(3):
    item = input("要拿出哪一样？")
    if item in cargo:
        cargo.remove(item)
        print(f"✅ 拿出了 {item}")
    else:
        print(f"❌ 货舱里没有 {item}")
print(f"还剩 {len(cargo)} 样")

# 愿望清单
for i in range(4):
    w = input("说一个愿望: ")
    if w in wishes:
        print("已经记下了 / already on the list")
    else:
        wishes.append(w)</pre></details>
<details class="hint"><summary>🏆 太空任务生成器</summary><pre>team = []
for k in range(3):
    person = random.choice(crew)
    team.append(person)
    crew.remove(person)
place = random.choice(places)
number = random.randint(1, 999)
print(f"🚀 任务 Mission #{number} → {place}")
for i in range(len(team)):
    print(f"  {i + 1}. {team[i]}")

name = input("谁想留在地球？")
if name in team:
    team.remove(name)
    new = random.choice(crew)
    team.append(new)
    crew.remove(new)
    print(f"🔁 {name} 留下，{new} 上！")
else:
    print(f"{name} 不在队伍里")</pre></details>
<details class="hint"><summary>作业 🥉 TODO 1 / 2</summary><pre>when = ["在半夜，", "在火星上，", "下课的时候，", "生日那天，"]
for i in range(3):
    print(f"{i + 1}. {random.choice(when)}{random.choice(who)}{random.choice(where)}{random.choice(did)}！")</pre></details>
<details class="hint"><summary>作业 🥈 TODO 3 / 4</summary><pre>for i in range(len(maori)):
    answer = input(...)
    if answer == english[i]:
        score = score + 1
        print("✅ Ka pai!")
    else:
        print(f"❌ 是 {english[i]}")
        wrong.append(maori[i])
        wrong_en.append(english[i])

print(f"得分 Score: {score} / {len(maori)}")
if len(wrong) == 0:
    print("💯 满分！")
else:
    for k in range(len(wrong)):
        print(f"📌 {wrong[k]} = {wrong_en[k]}")</pre></details>
<details class="hint"><summary>作业 🥇：测验 2.0（随机不重复 + 错题再考）</summary><pre>miss = []
miss_en = []
for q in range(len(maori)):          # range 只在开始算一次：5 次
    i = random.randint(0, len(maori) - 1)
    m = maori.pop(i)
    e = english.pop(i)
    answer = input(f"「{m}」是什么意思？")
    if answer == e:
        print("✅")
    else:
        print(f"❌ 是 {e}")
        miss.append(m)
        miss_en.append(e)

print("第二次机会 Second chance!")
for k in range(len(miss)):
    answer = input(f"再试一次「{miss[k]}」？")
    if answer == miss_en[k]:
        print("✅ 这次对了！")
    else:
        print(f"📌 记住：{miss[k]} = {miss_en[k]}")</pre>孩子可能会写成「先 pop 毛利语、忘了 pop 英文」——配对就乱了，这是很好的 debug 机会。</details>

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| 他能不用提示说出「从 0 开始」吗？ |
| 货舱的猜一猜：他能一步一步跟着列表变吗？ |
| 每个 ✍️ 用了几级提示？哪一个最卡？ | |
| 列表缺逗号时，他自己找到了吗？用了几步？ | |
| AI 给的 5 个词，对了几个？他的反应？ | |
| 今天哪一刻最兴奋？ | |
| 下节课要复习什么？ | |
