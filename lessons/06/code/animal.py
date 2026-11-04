# test-input: no | no | no | yes | yes | no | no | no
# 🕵️ 动物猜猜猜：规则版「AI」/ Animal guesser: a rule-based "AI"
# 它只会我们写进去的规则。想一个动物，回答 yes 或 no。
# It only knows the rules we wrote. Think of an animal and answer yes or no.

again = "yes"
while again == "yes":
    print("想好一个动物了吗？我来猜！/ Think of an animal. I'll guess!")
    fur = input("它有毛吗？Does it have fur? (yes/no) ")
    fly = input("它会飞吗？Can it fly? (yes/no) ")
    water = input("它住在水里吗？Does it live in water? (yes/no) ")

    if water == "yes":
        print("🦈 是鲨鱼 shark？")
    elif fur == "yes" and fly == "no":
        print("🐱 是猫 cat？")
    elif fur == "yes" and fly == ___:          # 填空：蝙蝠 bat 会飞吗？/ Fill in: can a bat fly? ("yes" or "no")
        print("🦇 是蝙蝠 bat？")
    elif fur == "no" and fly == "yes":
        print("🐦 是 tūī？")
    elif fur == "no" and fly == "no":
        print("🥝 是奇异鸟 kiwi？")
    else:
        print("🤷 我不知道！我的规则里没有它 / I don't know! It's not in my rules")

    again = input("再玩一次？Play again? (yes/no) ")

print("👋 再见 Bye!")
