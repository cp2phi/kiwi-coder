# 🐞 病号 3：它想在 x 很大的时候说「大」，再说「结束」。
# 🐞 Patient 3: it wants to say "大" when x is big, then say "结束".
# test-expect-error: Error
x = 10
if x > 3:
print("大")
print("结束")
