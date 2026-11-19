# 🛬 火箭着陆 第 2 关：过关检查 / Rocket Lander level 2: win check
if _ok_count == _FLIGHTS:
    print("__KC_WIN__")
elif not _done:
    print(f"__KC_HINT__ 🛬 第 {_flight} 枚助推器还在天上（高度 {_h}）。三枚都要落地：循环要一直跑到 landed() 是 True 为止——次数够不够？|🛬 Booster #{_flight} is still in the air (height {_h}). All three must land: keep looping until landed() is True — does your loop run enough times?")
elif _f == _fs:
    print(f"__KC_HINT__ 🔥 第 {_flight} 枚一次火都没点（落地速度 {_touch}）！在 if 里写一个规则：什么时候 step(True)？|🔥 Booster #{_flight} never fired its engine (touchdown speed {_touch})! Write a rule in the if: when should you step(True)?")
elif _f == 0:
    print(f"__KC_HINT__ ⛽ 第 {_flight} 枚燃料用光了，最后掉下去了（速度 {_touch}）。是不是一直在点火、或者在空中悬停？只在速度太快的时候点火。|⛽ Booster #{_flight} ran out of fuel and fell (speed {_touch}). Were you burning all the time, or hovering? Only burn when you're going too fast.")
else:
    print(f"__KC_HINT__ 💥 第 {_flight} 枚落地速度是 {_touch}，要 {_SAFE} 或更小。试试：speed() 比某个数大就点火——那个数要小一点。|💥 Booster #{_flight} touched down at speed {_touch}; it must be {_SAFE} or less. Try: burn when speed() is bigger than some number — make that number smaller.")
