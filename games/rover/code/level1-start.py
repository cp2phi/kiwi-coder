# 🛰️ 第 1 关：钻三块岩石 / Level 1: drill three rocks
# 这是昨天的程序，昨天第一块岩石刚好在 4 格外……可是地图每次运行都会变！
# This is yesterday's program — yesterday the first rock was 4 cells away... but the map changes every run!
# 改成「一直往前开，直到 rock_ahead()，就 break」，三段路都能用
# Change it to "keep driving until rock_ahead(), then break" so it works for all three legs
move()
move()
move()
drill()
turn_left()
