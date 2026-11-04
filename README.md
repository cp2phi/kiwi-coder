# 🥝 Kiwi Coder：我的 AI + Python 编程冒险

## 🌐 网站：https://cp2phi.github.io/kiwi-coder/

👆 先点这个！课本、游戏、作业、作品墙、小词典、笔记本都在网站上。

---

## 🧒 给小程序员

| 我想…… | 去哪里 |
|---|---|
| 看这周的课 / 预习 | 网站首页 → ⭐ 本周任务 |
| 边玩边练 | 🎮 游戏板块（7 个游戏，每个 6 关，过关得徽章） |
| 交作业 | 在作业画板点 **📤 存到作品墙**，文件名用 `weekNN-homework` |
| 看我的作品 | 🎨 作品墙（存完刷新就能看到） |
| 忘了指令怎么写 | 📖 Python 小词典 |
| 写笔记 | 改 [`notebook.md`](notebook.md) |
| 改我的名片 | 改 [`_data/me.yml`](_data/me.yml) |
| 看老师的反馈 | [`feedback.md`](feedback.md) |
| 我的大项目页面 | [`my-project/index.md`](my-project/index.md)（第 10–12 课） |

改完任何文件，点绿色的 **Commit changes** 存档，1～2 分钟后网站就会更新（在 **Actions** 里能看到进度）。作品墙不用等，它直接从 GitHub 读。

---

## 👩‍🏫 给老师：仓库说明

### 12 课一览

| 课 | 主题 | 核心 Python | 带回家的作品 | 游戏 |
|---|---|---|---|---|
| 1 | 🐢 AI 初体验 + 海龟画画 | print、turtle、顺序执行 | 房子 | 海龟迷宫 |
| 2 | 💬 会聊天的程序 | 变量、input()、f-string、int() | 聊天机器人 | 密码破译 |
| 3 | 🌀 重复的魔法 | for、range()、缩进 | 彩虹螺旋 / 万花筒 | 宝石机器人 |
| 4 | 🎲 猜数字游戏 | if/elif/else、比较、random、break；四步法 | 猜数字 | 虫虫医院 |
| 5 | 🎰 随机生成器 | 列表、下标、append、len、random.choice | 故事生成器 / 毛利语测验 | 图案复刻 |
| 6 | 🧠 会思考的机器 | while、布尔、and/or/not；规则 vs 数据学习 | 动物猜猜猜 + Teachable Machine | 读心术 |
| 7 | 📦 把代码打包 | def、参数、return | 用函数画小镇 | 宝石机器人 |
| 8 | ✊ 迷你项目：石头剪刀布 | 综合 + 字符串方法 | 能对战记分的游戏 | 虫虫医院 |
| 9 | 🕵️ 聪明的 AI 用户 | 字典、in、.get() | AI 侦探 + 问答机 | 密码破译 |
| 10 | 🗺️ 项目策划 + 开发流程 | 读代码、assert 测试、计划→写→测→修→发布 | 项目计划书 + 骨架 | 接水果 |
| 11 | 🛠️ 项目制作 | 调试技巧、键盘事件 onkey/ontimer | 可运行的项目 | 接水果 |
| 12 | 🏆 展示日 + 部署上线 | GitHub Pages 部署、回顾 | 上线的项目页 + 证书 | 读心术 |

第 1–4 课「老师做，我看」，5–8 课「一起做」，9–12 课「我做，老师看」。完整设计见网站的 **课程地图 → 课程总览**。

### 第一次设置

1. **打开 GitHub Pages**：Settings → Pages → Source: **Deploy from a branch** → Branch: **main** / **(root)** → Save。
2. 等 Actions 里的 “pages build and deployment” 变绿，打开上面的网址。
3. **账号与年龄**：GitHub 和 OpenAI（Codex）都要求用户满 13 岁。孩子不到 13 岁时，用家长账号、家长陪同使用；满 13 岁后可以给孩子开自己的账号，在 Settings → Collaborators 加为协作者。

### 文件结构

```
_config.yml              网站设置；每周改 current_lesson
_data/me.yml             孩子的名片（首页显示）
_data/lessons.yml        12 课的元数据（标题、知识点、作品、页面标签、作业文件名）
_data/games.yml          游戏列表
_data/cheatsheet/NN.yml  每课新学的指令 → 自动合并成「小词典」
lessons/NN/              每课：index(今日任务) learn(学一学) homework(作业) teacher(教案) code/(起始代码)
games/<id>/              游戏页面 + 隐藏的关卡代码（setup / check / target）
my-work/                 孩子的作品和作业（.py 自动出现在作品墙）
my-project/              孩子的大项目页面（第 12 课上线）
notebook.md              工程师笔记本（孩子写）
feedback.md              老师反馈（老师写，12 课模板已备好）
playground.md            自由画板
cheatsheet.md            Python 小词典
ai-rules.md              AI 伙伴守则 + 卡住了四步法
assets/                  样式和脚本（playground.js = 网页里运行 Python 的画板引擎）
docs/AUTHORING.md        教材写作规范（写新课 / 新游戏前必读）
tools/                   自动检查：跑所有示例代码、构建网站、查坏链接
```

### 每周流程

**课前**
1. `_config.yml`：`current_lesson` 改成这一课的序号（首页「本周任务」和游戏解锁都看它）。
2. 打开这一课的 **👩‍🏫 教案** 标签，按课前准备清单过一遍。

**课后**
1. 孩子把作业存为 `my-work/weekNN-homework.py`，作业页会实时显示「✅ 已交」。
2. 在 `feedback.md` 对应的课下面写反馈。

### 网页画板（playground）能做什么

- 在浏览器里运行 Python（[Skulpt](https://skulpt.org)），支持 `turtle`、`random`、`math`、`time`、`input()`（页面内输入框）、f-string、列表、字典、函数、while、assert、`onkey` / `ontimer` 键盘游戏。
- 报错会翻译成孩子能看懂的话，并标出行号；一键复制「问 AI 要提示」的话。
- 游戏关卡：隐藏的 setup / check 代码、期望输出对比、目标图案相似度、过关徽章。
- `📤 存到作品墙` 直接打开 GitHub 新建文件页；作品墙实时从 GitHub 读取，可生成缩略图。

写新页面时的组件和属性说明都在 [docs/AUTHORING.md](docs/AUTHORING.md)。

### 自动检查（改教材后跑一下）

```bash
cd tools && npm i && cd ..       # 第一次
node tools/check-code.js         # 用网页 Python 跑所有 .py（教材、游戏、作品）
tools/build.sh                   # 用 Docker 构建网站（和 GitHub Pages 一样的环境）
node tools/check-links.js        # 检查坏链接
node tools/serve.js              # 本地预览 http://localhost:4000/kiwi-coder/
```

### 中英双语

网站右上角的 **EN / 中文** 按钮会切换全站语言（浏览器会记住选择）。写新教材时：

- 行内文字：`<span class="zh">中文</span><span class="en">English</span>`
- 整段：`<p class="zh">…</p><p class="en">…</p>`
- 页面开头加 `title_en: 英文标题`
- 画板加 `data-title-en="English title"`；输入框提示用 `data-ph-zh="…" data-ph-en="…"`
- 孩子要自己改的文件（笔记本、反馈）直接写「中文 / English」，不用标签
