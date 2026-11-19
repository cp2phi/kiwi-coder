# 🐞 病号 4：没有红框，可是答案错了！ Patient 4: no red box, but the answer is wrong!
# 95 分应该说「🏆 优秀」，它却说「👍 及格」。为什么？怎么治？（提示：elif 从上往下，第一个成立的才跑）
# A score of 95 should say "🏆 优秀" but it says "👍 及格". Why? How do you fix it? (Hint: top to bottom, the first true one wins)
score = 95

if score >= 60:
    print("👍 及格")
elif score >= 90:
    print("🏆 优秀")
else:
    print("💪 加油")
