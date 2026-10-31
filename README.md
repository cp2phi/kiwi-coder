# 🥝 Kiwi Coder：我的 AI + Python 编程冒险

## 🌐 网站：https://cp2phi.github.io/kiwi-coder/

👆 先点这个！课本、作业、作品墙、笔记本都在网站上。

---

## 🧒 给小程序员

| 我想…… | 去哪里 |
|---|---|
| 看这周的课 / 预习 | 网站首页 → ⭐ 本周任务 |
| 交作业 | 在作业画板点 **📤 存到作品墙**，或者把 `.py` 文件放进 [`my-work/`](my-work/) |
| 写笔记 | 改 [`notebook.md`](notebook.md) |
| 改我的名片 | 改 [`_data/me.yml`](_data/me.yml) |
| 看老师的反馈 | [`feedback.md`](feedback.md) |

改完任何文件，点绿色的 **Commit changes** 存档，1～2 分钟后网站就会更新（在 **Actions** 里能看到进度）。

---

## 👩‍🏫 给老师：仓库说明

### 第一次设置

1. **打开 GitHub Pages**：Settings → Pages → Source: **Deploy from a branch** → Branch: **main** / **(root)** → Save。
2. 等 Actions 里的 “pages build and deployment” 变绿，打开上面的网址。
3. **账号与年龄**：GitHub 和 OpenAI（Codex）都要求用户满 13 岁。孩子不到 13 岁时，用家长账号、家长陪同使用；满 13 岁后可以给孩子开自己的账号，在 Settings → Collaborators 加为协作者。

### 文件结构

```
_config.yml          网站设置；每周改 current_lesson
_data/me.yml         孩子的名片（首页显示）
_data/lessons.yml    12 关地图；教材放好后把 ready 改成 true
lessons/01/          第 1 课：index(今日任务) github codex python homework teacher(教案)
lessons/01/code/     课上画板用的起始代码（.py）
my-work/             孩子的作品和作业（.py 自动出现在作品墙，点 ▶ 可运行）
notebook.md          工程师笔记本（孩子写）
feedback.md          老师反馈（老师写）
playground.md        自由画板
ai-rules.md          AI 伙伴守则 + 卡住了四步法
assets/              样式和脚本（playground.js = 网页里运行 Python 的画板）
```

### 每周流程

**课前**
1. 复制上一课文件夹，比如 `lessons/01/` → `lessons/02/`，把每个文件开头的 `lesson: "01"` 改成 `"02"`，再改内容。
2. `_data/lessons.yml`：把这一课设为 `ready: true`。
3. `_config.yml`：`current_lesson` 改成这一课的序号。
4. 孩子打开网站首页，「本周任务」就会指向新课，可以预习。

**课后**
1. 孩子把作业存为 `my-work/weekNN-homework.py`，作业页会自动显示「✅ 已交」。
2. 在 `feedback.md` 最上面写反馈（文件底部的注释里有模板）。

### 在网页上写画板

在任何 `.md` 页面里（页面开头要有 `playground: true`）：

```html
<div class="playground" data-src="{{ '/lessons/02/code/xxx.py' | relative_url }}" data-title="标题" data-save="默认文件名"></div>
```

- `data-canvas="no"`：只用 `print`/`input`，不需要海龟画布
- `data-draft="名字"`：在孩子的浏览器里自动保存没写完的代码

画板用的是 [Skulpt](https://skulpt.org)（浏览器里的 Python），支持 `turtle`、`random`、`math`、`time`、`input()`。更复杂的程序请用电脑上的 Python（Thonny / VS Code）。

### 页面上的小互动

| 写法 | 效果 |
|---|---|
| `<ul class="quests" data-key="唯一名字"><li>…</li></ul>` | 可打勾的任务清单（全部完成撒彩带） |
| `<div class="quiz" data-answer="2">…</div>` | 猜一猜选择题（看 `lessons/01/python.md` 的例子） |
| `<details class="hint"><summary>提示 1</summary>…</details>` | 一级一级打开的提示 |
| `<div class="box box-tip">…</div>` | 提示框（还有 `box-warn` `box-good` `box-rule` `box-think`） |
