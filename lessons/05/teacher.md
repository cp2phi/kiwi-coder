---
title: 第 5 课 · 教案
title_en: Lesson 5 · Teacher plan
lesson: "05"
tab: teacher
---

# 👩‍🏫 第 5 课教案（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子能自己说出「列表是一排从 0 开始编号的抽屉」，会用 `[i]`、`len`、`append`、`random.choice`、`for x in 列表`，并把它们和前面学的 `if`、`for`、f-string 组合起来。

**今天的铁律：** 第二阶段开始了——**孩子写大部分，你只给提示。** 他卡住时先问「你觉得电脑在抱怨什么？」而不是指出错误。打字慢没关系，画板里有起始代码，大多数任务是**改**不是**写**。

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-5">
  <li>自己把 <a href="../learn/">学一学</a> 从头跑一遍，特别是毛利语测验的填空和「和 AI 一起」部分。</li>
  <li>把 AI 给的 5 个毛利语单词提前自己核对一次（<a href="https://maoridictionary.co.nz" target="_blank" rel="noopener">Te Aka</a>）。如果 AI 真的出了错，那是今天最好的教材；如果没出错，也要强调「这次对了，不代表下次对」。</li>
  <li>打开 <a href="{{ '/games/copy/' | relative_url }}">🎨 图案复刻</a>，确认第 1、2 关能过；第 5 关（螺旋 + 颜色列表）是今天知识的练习，可以留到回家玩。</li>
  <li>准备几张小纸条当「抽屉」：写上 0、1、2、3 贴在桌上，不插电演示 <code>animals[1]</code> 是哪一个。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>骰子程序。先问「会打印几行？」再运行。让他加 <code>elif dice == 1</code>——这是上节课的内容，应该不用提示。</td><td>if / elif 的缩进还记得吗？</td></tr>
<tr><td><b>5–15</b></td><td>📦 列表</td><td>纸条抽屉游戏 2 分钟：「把 1 号抽屉的东西拿出来」——他会拿第二张纸条吗？<br>然后做猜一猜 → 运行 drawers.py → <b>一定要</b>让他故意写 <code>animals[3]</code> 看报错。读画板的解释。</td><td>他第一次说「第 0 个」的时候——那一刻就学会了</td></tr>
<tr><td><b>15–25</b></td><td>🎲 故事生成器</td><td>运行 3 次，笑一笑。让他加自己的东西（用破冰时记下的兴趣）。然后挑战：用 for 循环讲 5 个故事。这是**复习**第 3 课的缩进，让他自己试，错了看报错。</td><td>缩进是不是自己想到的？逗号漏了会不会自己发现？</td></tr>
<tr><td><b>25–32</b></td><td>🌈 彩虹六边形</td><td>猜一猜「6 个颜色 60 度画什么」。运行。改成 4 个颜色 90 度。<br>然后揭秘第 3 课的 <code>colors[i % 6]</code>——这是个「啊原来如此」的时刻，别跳过。</td><td>他能说出「for colour in colours 是一个一个拿」吗</td></tr>
<tr><td><b>32–42</b></td><td>🇳🇿 毛利语测验</td><td>填空 <code>english[i]</code>。先让他看提示 1，还不行再看提示 2。玩一局。<br>和 AI 一起：用页面上的问法要 5 个词，贴进去玩，然后<b>一起核对</b>。</td><td>他会不会直接相信 AI？核对时的态度</td></tr>
<tr><td><b>42–50</b></td><td>🎮 图案复刻</td><td>游戏第 1 关。颜色列表 + 循环。过关得徽章。</td><td>能不能自己从目标图案反推出「几条边、转几度」</td></tr>
<tr><td><b>50–55</b></td><td>🌠 愿望清单</td><td>时间够就做；不够就跳过（作业用不到 append 也行）。重点：<code>[]</code> 空列表 + <code>append</code>。</td><td></td></tr>
<tr><td><b>55–60</b></td><td>📓 收尾</td><td>看作业页，说清楚 🥉 只要改列表。写笔记本 3 行，其中一行写「AI 的单词对了几个」。</td><td></td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>列表 + 报错</b> &gt; <b>故事生成器</b> &gt; 毛利语测验（含 AI 核对）&gt; 彩虹六边形 &gt; 游戏 &gt; 愿望清单。愿望清单和挑战可以留到作业时间。</div>

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
| 毛利语的长音符 ā 不会打 | 答案是英文，不用打长音；告诉他电脑上输入 ā 的方法可以以后学 |

---

## ✅ 参考答案

<details class="hint"><summary>毛利语测验填空</summary><pre>if answer == english[i]:</pre></details>
<details class="hint"><summary>故事生成器 5 个故事</summary><pre>for i in range(5):
    a = random.choice(who)
    b = random.choice(where)
    c = random.choice(did)
    print(f"{a}{b}{c}！")</pre></details>
<details class="hint"><summary>作业 🥇：画 5 个随机图形</summary><pre>for k in range(5):
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    shape = random.choice(shapes)
    t.color(random.choice(colours))
    size = random.randint(30, 100)
    if shape == "square":
        for i in range(4):
            t.forward(size)
            t.left(90)
    elif shape == "triangle":
        for i in range(3):
            t.forward(size)
            t.left(120)
    elif shape == "star":
        for i in range(5):
            t.forward(size)
            t.left(144)
    else:
        t.circle(size / 2)</pre></details>

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| 他能不用提示说出「从 0 开始」吗？ | |
| 列表缺逗号时，他自己找到了吗？用了几步？ | |
| AI 给的 5 个词，对了几个？他的反应？ | |
| 今天哪一刻最兴奋？ | |
| 下节课要复习什么？ | |
