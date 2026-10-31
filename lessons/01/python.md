---
title: 第 1 课 · Python
lesson: "01"
tab: python
playground: true
---

# 🐍 Python 第一课：让电脑听我的话

**Python** 是一种和电脑说话的语言。今天不用装软件，**就在这个网页上写代码**：改左边的代码 → 点 **▶ 运行** → 看右边的结果。

---

## 第 1 步：Hello 👋

几乎每个程序员学的第一个程序，都是让电脑打个招呼。

<div class="playground" data-src="{{ '/lessons/01/code/hello.py' | relative_url }}" data-canvas="no" data-title="👋 Hello 程序" data-save="hello"></div>

<ul class="quests" data-key="l1-hello">
  <li>把 <code>___</code> 换成你的昵称，运行。电脑听你的话了吗？</li>
  <li>再加一行 <code>print("...")</code>，说出你最喜欢的游戏。</li>
  <li>🐞 故意删掉一个引号 <code>"</code>，运行，看电脑怎么「抱怨」，再修好它。</li>
</ul>

<div class="box box-good">💡 <b>报错不是失败</b>，是电脑在告诉你：哪一行、出了什么问题。</div>

---

## 第 2 步：海龟画正方形 🐢

Python 里有一只**拿着笔的海龟**：

<div class="cmds">
  <div class="cmd"><code>t.forward(100)</code><span>往前走 100 步（边走边画线）</span></div>
  <div class="cmd"><code>t.left(90)</code><span>向左转 90 度</span></div>
  <div class="cmd"><code>t.color("red")</code><span>换笔的颜色</span></div>
  <div class="cmd"><code>t.pensize(5)</code><span>笔变粗</span></div>
</div>

### 🤔 先猜，再运行

<div class="quiz" data-answer="2">
  <p class="q">下面的代码，海龟会画出什么？（先别点运行！）</p>
  <div class="opts"><button>一条直线</button><button>正方形</button><button>三角形</button></div>
  <div class="why">走 100 → 左转 90° → 一共 4 次，每次转直角，就是正方形！</div>
</div>

<div class="playground" data-src="{{ '/lessons/01/code/square.py' | relative_url }}" data-title="🟩 正方形" data-save="my-square"></div>

### 🔍 改一改

<div class="quiz" data-answer="2">
  <p class="q">如果把<b>所有的 90</b> 都改成 <b>120</b>，会画出什么？先猜，再去上面改了试试！</p>
  <div class="opts"><button>还是正方形</button><button>三角形</button><button>一团乱线</button></div>
  <div class="why">三角形！每次转 120°，转 3 次正好一圈（360°），海龟回到起点，第 4 条边和第 1 条重叠了。</div>
</div>

<ul class="quests" data-key="l1-modify">
  <li>🎨 加一行 <code>t.color("hotpink")</code> 换颜色（试试 red、gold、blue、purple）</li>
  <li>✏️ 加一行 <code>t.pensize(8)</code> 让线变粗</li>
  <li>📏 把 100 改成 200，让正方形变大</li>
</ul>

<div class="box box-tip">⚠️ 颜色要加<b>英文引号</b>：<code>"red"</code> ✅ &nbsp; <code>red</code> ❌ &nbsp; <code>“red”</code> ❌（中文引号）</div>

### 🏆 挑战：三角形，然后五角星！

把 <code>___</code> 换成正确的数字，画出三角形。画好了？再改一改，试试**五角星**！

<div class="playground" data-src="{{ '/lessons/01/code/challenge.py' | relative_url }}" data-title="🏆 挑战画板" data-save="my-shapes" data-draft="l1-challenge"></div>

<details class="hint"><summary>💡 三角形提示</summary>海龟走一圈一共转 360 度，三角形转 3 次，每次转 360 ÷ 3 = ？</details>
<details class="hint"><summary>🌟 五角星提示</summary>五角星走 5 次、转 5 次。每次转的角度在 130 到 150 之间，试试哪个能「合上」！</details>

---

## 第 3 步：✨ 让 AI 帮你画
{: #ai-magic}

正方形是你自己写的。现在请 **Codex** 帮你画一个更厉害的！记住：<b>你是队长，AI 是队员</b>。

### ① 写一段清楚的指令

<div class="recipe">
  <label for="r-what">🎯 画什么？</label>
  <input id="r-what" name="what" placeholder="比如：一朵有 8 片花瓣的花">
  <div class="chips" data-for="what"><button class="chip">一朵有 8 片花瓣的花</button><button class="chip">一个彩色的螺旋</button><button class="chip">黑夜里的满天星星</button></div>
  <label for="r-detail">🔍 细节（大小、数量……）</label>
  <input id="r-detail" name="detail" placeholder="比如：在画布中间，大大的">
  <label for="r-colors">🎨 颜色</label>
  <input id="r-colors" name="colors" placeholder="比如：彩虹色，黑色背景">
  <input type="hidden" name="extra" value="">
  <div class="result"></div>
  <div class="score"></div>
  <p><button class="pg-btn run copy-prompt">📋 复制这段指令</button></p>
</div>

### ② 发给 Codex，把代码贴到这里运行

<div class="playground" data-title="✨ AI 画板" data-save="ai-art-01" data-draft="l1-ai">
<textarea># 把 Codex 写的代码粘贴到这里（先删掉这两行）
# 然后点 ▶ 运行
</textarea>
</div>

### ③ 当检查员

<ul class="quests" data-key="l1-ai">
  <li>🔢 找 <b>1 个数字</b>改一改，看画有什么变化</li>
  <li>❓ 找一行看不懂的，问 Codex：「这一行是什么意思？用小学生能懂的话解释」</li>
  <li>📤 满意了？点 <b>存到作品墙</b>！</li>
</ul>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/01/homework/' | relative_url }}">下一步：看看作业 🏠 →</a></p>
