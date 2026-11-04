# ✍️ 教材写作指南（给写课程 / 游戏的人和 AI Agent）

这份文件说明 Kiwi Coder 网站的**结构、组件和写作规范**。写新课、新游戏之前请先通读。
网站用 GitHub Pages（Jekyll）生成，所有页面是 Markdown + 一点 HTML；网页里的 Python 用 [Skulpt](https://skulpt.org) 运行。

## 0. 读者是谁

- **孩子**：小学 6 年级，中文为主、英文为辅，打字慢，注意力 10–15 分钟换一次活动。喜欢「改一个数字马上看到变化」。
- **老师 / 家长**：只看 `teacher.md`（教案）。教案只写中文即可。
- 口吻：活泼、短句、多用 emoji 当路标；**永远先猜再运行**（PRIMM）；报错是线索不是失败；AI 要提示不要答案。

## 1. 文件结构

```
_data/lessons.yml          12 课的元数据（标题、知识点、作品、tabs、作业文件名）——已写好，不要改结构
_data/tabs.yml             课程标签定义
_data/games.yml            游戏列表
_data/cheatsheet/NN.yml    每课新学的指令（小词典自动合并）—— 每课必写
lessons/NN/index.md        🎯 今日任务（清单）
lessons/NN/learn.md        📖 学一学（核心教学页，最重要）
lessons/NN/homework.md     🏠 作业
lessons/NN/teacher.md      👩‍🏫 教案（中文）
lessons/NN/code/*.py       画板起始代码（每个文件必须能在 Skulpt 里跑，见 §6）
games/<id>/index.md        游戏页面
games/<id>/code/*.py       游戏的隐藏代码（prelude / check / target）
my-work/                   孩子的作品（不要动）
```

第 1 课比较特殊，多了 `github.md`、`codex.md`，教学页叫 `python.md`（tabs 里写的是 `python` 而不是 `learn`）。

## 2. 页面开头（front matter）

```yaml
---
title: 第 3 课 · 学一学
title_en: Lesson 3 · Learn
lesson: "03"          # 两位数字符串，决定标签栏和上一课/下一课
tab: learn            # home | learn | homework | teacher（第 1 课还有 github / codex / python）
playground: true      # 页面里有画板就要写（会加载 Skulpt）
---
```

## 3. 中英双语

网站右上角可切换语言。所有给孩子看的文字都要两种：

- 行内：`<span class="zh">中文</span><span class="en">English</span>`
- 整段：`<p class="zh">…</p><p class="en">…</p>`
- 画板标题：`data-title="中文" data-title-en="English"`
- 输入框提示：`data-ph-zh="…" data-ph-en="…"`
- 代码里的注释：一行里中文在前英文在后，比如 `# 往前走 / move forward`
- 教案（teacher.md）只写中文，开头放一行 `<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>`

## 4. 组件速查（直接复制）

### 画板（最常用）

```html
<div class="playground" data-src="{{ '/lessons/03/code/spiral.py' | relative_url }}" data-title="🌀 螺旋" data-title-en="🌀 Spiral" data-save="my-spiral" data-draft="l3-spiral"></div>
```

- `data-canvas="no"`：只用 print / input（聊天程序）
- `data-draft="唯一名字"`：孩子改的代码自动记在浏览器里（作业和挑战都要加）
- `data-save`：存到作品墙时的默认文件名；作业用 `weekNN-homework`
- `data-rows="6"`：编辑器最少行数（短例子用小一点）
- 直接写代码而不是用文件：`<div class="playground" data-title="…"><textarea>代码</textarea></div>`（代码里不能出现 `</textarea>`）

关卡 / 自动判定（游戏和练习用）：

- `data-prelude="…py"`：隐藏在孩子代码**前面**跑（画迷宫、定义 `move()` 之类的指令）
- `data-check="…py"`：隐藏在孩子代码**后面**跑。检查代码里 `print("__KC_WIN__")` = 过关；`print("__KC_HINT__ 中文提示|English hint")` = 显示提示（这两种行不会出现在输出里；引擎每次运行会把 `__KC_` 换成随机口令，孩子自己 print 这个词不算过关）
- 也可以把隐藏代码写在 div 里：`<script type="text/x-python" data-role="prelude">…</script>`、`data-role="check"`、`data-role="target"`
- `data-expect="第一行\n第二行"`：输出和它一样就过关（会显示左右对比）
- `data-target="…py"`：旁边画出目标图案，运行后显示相似度，≥ `data-threshold`（默认 85）过关
- `data-badge="maze-3"`：过关时颁发徽章（游戏用 `<游戏id>-<关数>`）
- `data-autorun`：打开页面自动跑一次；`data-hide-code`：只显示画布（展示示例 / 目标）

隐藏代码里孩子的海龟通常叫 `t`，所以 prelude 创建 `t = turtle.Turtle()`，check 里直接用 `t.xcor()` 判断。孩子的代码如果出错，check 不会跑。

### 任务清单（点一下打勾，存在浏览器里）

```html
<div class="progress" data-for="l3"><span></span></div>
<ul class="quests" data-key="l3">
  <li><b>🔁 热身</b> <span class="pill">5 min</span><br><span class="zh">…</span><span class="en">…</span></li>
</ul>
```

`data-key` 必须唯一。**每课的主清单用 `lN`**（比如 `l3`），全部打勾会得到「第 N 课」徽章，首页地图会显示进度。页内小清单用 `l3-xxx`。

### 猜一猜（PRIMM 的 Predict）

```html
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">问题？</span><span class="en">Question?</span></p>
  <div class="opts"><button>A</button><button>B</button><button>C</button></div>
  <div class="why"><span class="zh">解释</span><span class="en">Why</span></div>
</div>
```

`data-answer` 是正确选项的序号（从 1 开始）。可加 `data-badge="reader-2"`。

### 其他

- 提示阶梯：`<details class="hint"><summary>💡 提示 1</summary>…</details>`（先给小提示，再给大提示，最后才给答案）
- 指令卡片：`<div class="cmds"><div class="cmd"><code>t.circle(50)</code><span>画圆 / circle</span></div></div>`（点代码可复制）
- 知识卡片（每课结尾总结）：`<div class="know"><div class="k"><b>for 循环</b><code>for i in range(4):\n    t.forward(100)</code><span>重复 4 次</span></div></div>`
- 提示框：`<div class="box box-tip|box-warn|box-good|box-rule|box-think">…</div>`
- 等级：`<div class="levels"><div class="level"><div class="medal">🥉</div><div><h3>必做</h3><p>…</p></div></div></div>`
- 步骤：`<ol class="steps"><li><strong>标题</strong><br>说明</li></ol>`
- 流程：`<div class="flow"><div class="f"><span class="e">✏️</span><b>改</b></div><div class="arrow">→</div>…</div>`
- 逐行讲解：`<ol class="code-walk"><li><code>t.forward(100)</code><span>往前走 / forward</span></li></ol>`
- 颜色盘：`<div class="swatches" data-colors="red gold blue"></div>`
- AI 提示词配方：复制第 1 课 python.md 里的 `.recipe`，文字程序加 `data-kind="text"`
- 复制按钮：`<pre>要复制的话</pre><button class="pg-btn copy-prev">📋 复制</button>`
- 两栏：`<div class="two"><div>…</div><div>…</div></div>`
- 对话示例：`<div class="chat"><div class="bubble me">我问</div><div class="bubble ai">AI 答</div></div>`
- 作业状态（实时从 GitHub 读）：`<div class="hw-status" data-file="week03-homework.py"></div>`（放在作业页，页面要有 `playground: true`）

## 5. 每一课的内容结构

### index.md 今日任务（短，5 分钟读完）
1. 标题 + 一句话目标 + 「今天带回家」4 张小卡片（`.grid .card`）
2. **主清单** `data-key="lN"`，5–7 项，每项带时间 `<span class="pill">10 min</span>` 和链接：热身复习 → 学一学 → 玩游戏 → 作业预览 → 笔记本 3 行
3. 一个 `box-rule`（这课的约定）或 `box-good`（鼓励）
4. 底部老师链接：`<a href="teacher/">教案</a>`

### learn.md 学一学（最重要，20–30 分钟）
按 PRIMM 组织，**每个知识点至少 3 个例子，难度递增，每个例子都有画板**：
1. `## 🔁 热身：上次学的还记得吗？` 一个小画板 + 2 个小任务，用**上一课**的知识
2. `## ✨ 今天的新魔法：XXX` 一句话 + 生活比喻 + 指令卡片
3. `### 🤔 先猜，再运行`（quiz） → 画板（例 1，最简单，直接能跑）
4. `### 🔍 改一改` quests：改数字 / 改颜色 / 故意弄坏看报错
5. `### 🧪 例 2`（中等，带 `___` 空要填）+ 提示阶梯
6. `### 🧪 例 3`（综合，把新旧知识合在一起，比如循环 + 变量）
7. `### 🏆 挑战`（开放题，`data-draft`，鼓励存到作品墙）
8. `## 🤖 和 AI 一起`：这课专用的问法（比如「请解释这段代码第 5 行」），用 `.chat` 给一个好问题的示范和一个坏问题
9. `## 📚 知识卡片`（`.know`），最后一行链接到小词典
10. 底部按钮：`<p style="text-align:center"><a class="pg-btn run" href="../homework/">下一步：作业 🏠 →</a></p>`

### homework.md 作业（30 分钟能做完）
1. 标题（有趣的名字，比如「海龟建筑师」「故事机 2000」）+ 时间 pill + `<div class="hw-status" data-file="weekNN-homework.py"></div>`
2. 🥉 必做（只用这课 + 上课的知识，有起始代码，改一改就行）🥈 加分（新组合）🥇 挑战（自己设计 / 问 AI 学一招）
3. 作业画板 `data-src="…/homework.py" data-save="weekNN-homework" data-draft="lN-homework"`
4. 提示阶梯 2–3 个
5. 怎么交（3 步）+ 下周预告 `box-think`

### teacher.md 教案（中文）
1. 目标（1 句）+ 今天的铁律（老师不碰键盘等）
2. 课前准备清单（`.quests data-key="teacher-prep-N"`）
3. 60 分钟时间表（表格：时间 / 环节 / 做什么说什么 / 观察点）
4. 时间不够怎么砍
5. 好用的话术 + 常见卡点和应对
6. 参考答案（`<details class="hint"><summary>参考答案</summary>…</details>`）
7. 观察记录表

### _data/cheatsheet/NN.yml
照 `01.yml` 的格式，列这课新学的指令（5–12 条），`example` 里可以用 `\n`。

## 6. 代码文件规范（lessons/NN/code/*.py）

- 第一行注释写标题（中 / 英），第二行写「作者」占位（作业文件）。
- 中文注释 + 英文注释同一行：`# 画屋顶 / draw the roof`
- `___` 表示要孩子填的空（画板会友好地提示）。**只把 `___` 放在它是一个独立名字的位置**（比如 `t.left(___)`、`random.choice(___)`），不要写成 `random.___()` 或 `t.___(100)`——那会报 AttributeError 而不是友好的「空没填」提示。
- 只能用 `turtle`、`random`、`math`、`time`、`input()`、`print()` 和基础语法。**不支持**：`turtle.colormode`、`shapesize`（画板会悄悄忽略）、`onkeypress`（自动转成 `onkey`）、`textinput`、文件、网络。
- 键盘游戏写法：`screen = turtle.Screen()` → `screen.onkey(函数, "Left")` → `screen.listen()` → `screen.ontimer(tick, 50)` 做游戏循环。主程序结束后画板会保持「游戏中」状态。
- 海龟默认速度慢：教学例子用 `t.speed(0)` 或 `t.speed(6)`，别让孩子等。
- **每个 .py 文件都要通过测试**：`node tools/check-code.js lessons/03`（见 tools/README）。含 `___` 的文件只要报的是「空没填」就算通过。想给测试喂 input() 的答案，在文件开头加 `# test-input: 5 | 小海龟 | yes`。

## 7. 难度梯度与复习（必须遵守）

- 每课只教**一个**核心语法点（见 `_data/lessons.yml` 的 `syntax`），但例子里要自然地用到前面课的东西（`review`）。
- 例子顺序：**能直接跑** → **填空** → **组合** → **开放挑战**。
- 作业的 🥉 必做只用已学知识，孩子 20 分钟内一定做得出来。
- 不要提前用没教过的语法（比如第 3 课不要出现 `if`）；真的需要时加一句「这个下节课学，先当魔法用」。

## 8. 写完之后

1. `node tools/check-code.js lessons/NN games/<id>` 全绿
2. `tools/build.sh` 构建网站没有报错（需要 Docker），`node tools/check-links.js` 没有坏链接
3. 自己用孩子的眼睛读一遍：有没有一段超过 5 行的文字？有没有一个例子没法「马上看到结果」？
