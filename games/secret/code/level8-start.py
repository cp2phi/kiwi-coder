# 🔐 第 8 关：找出密码机的规律 / Level 8: crack the machine's rule
# 间谍的密码机把消息变成了乱码。它以前加密过这两条：
# A spy machine scrambles messages. It scrambled these two before:
#     "kiwi"      →  "ipwbiqky"
#     "tui bird"  →  "dxrqiobz mieuutr"
# 🕵️ 第 1 步：拿纸笔对一对，找出规律（有两个步骤哦）。/ Step 1: compare them on paper and find the rule (it has two steps).
# 🛠 第 2 步：写 decode(text)，return 解密后的消息。/ Step 2: write decode(text) and return the decoded message.
# 🔬 检查员会用 3 条新的秘密消息考你的 decode！/ The inspector tests your decode on 3 new secret messages!

def decode(text):
    result = ""
    for i in range(len(text)):
        result = result + text[i]
    return result

print(decode("ipwbiqky"))    # 应该是 kiwi / should be kiwi
print(decode(secret))
