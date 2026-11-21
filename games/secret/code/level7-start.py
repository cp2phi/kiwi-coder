# 🔐 第 7 关：会转圈的凯撒密码 / Level 7: the wrap-around Caesar cipher
# ⚠️ secret 和 key 每次运行都会变（是关卡给你的）！/ secret and key change every run (the level gives them to you)!
# 每个字母都往后推了 key 个，推过 z 就从 a 重新开始，像钟表转圈。空格没有变。
# Every letter was pushed forward by key places; past z it wraps round to a, like a clock. Spaces didn't change.
# 把解出来的密码放进变量 answer / Put the decoded message into the variable answer
print("secret:", secret)
print("key:", key)

answer = ""
for c in secret:
    answer = answer + chr(ord(c) - key)
print(answer)
