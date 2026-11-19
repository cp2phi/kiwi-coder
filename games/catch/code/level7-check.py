# 🍎 接水果 第 7 关：过关检查（真的去玩一下你的函数）/ Fruit Catcher level 7: win check (actually plays your functions)
import turtle as _kt
import time as _time
def _kc7():
    global score, lives, game_over
    for _n in ["lives", "game_over", "fall", "restart", "fruit", "basket"]:
        if _n not in globals():
            print("__KC_HINT__ 还没有 " + _n + "。看看最上面的任务清单|There is no " + _n + " yet. Check the task list at the top")
            return False
    _start = lives
    if _start < 1 or game_over:
        print("__KC_HINT__ 游戏刚开始时 lives 要大于 0，game_over 要是 False|At the start lives must be above 0 and game_over must be False")
        return False
    _f = _kt.Turtle()
    _f.hideturtle()
    _f.penup()
    _f.speed(0)
    # 1) 接住：加分，不少命 / catch: +1 score, no life lost
    score = 0
    _f.goto(basket.xcor(), basket.ycor() + 10)
    fall(_f)
    if score != 1 or lives != _start:
        print("__KC_HINT__ 接住水果应该加 1 分、命不变。现在接住一个以后 score = " + str(score) + "，lives = " + str(lives) + "|Catching a fruit should add 1 point and keep your lives. After one catch: score = " + str(score) + ", lives = " + str(lives))
        return False
    # 2) 漏掉：少一条命 / miss: lose a life
    _f.goto(basket.xcor() + 200, -279)
    fall(_f)
    if lives != _start - 1:
        print("__KC_HINT__ 漏掉一个水果应该少 1 条命（在 fall 里掉到地上那一段叫 lose_life()）。现在 lives 从 " + str(_start) + " 变成了 " + str(lives) + "|Missing a fruit should cost 1 life (call lose_life() where the fruit hits the ground in fall). lives went from " + str(_start) + " to " + str(lives))
        return False
    if game_over and _start > 1:
        print("__KC_HINT__ 还有命呢，game_over 不应该是 True|There are lives left, so game_over shouldn't be True yet")
        return False
    # 3) 一直漏，直到没命 / keep missing until out of lives
    for _i in range(_start - 1):
        _f.goto(basket.xcor() + 200, -279)
        fall(_f)
    if lives != 0 or not game_over:
        print("__KC_HINT__ 漏掉 " + str(_start) + " 个以后应该 lives = 0 而且 game_over = True。现在 lives = " + str(lives) + "，game_over = " + str(game_over) + "|After " + str(_start) + " misses, lives should be 0 and game_over True. Now lives = " + str(lives) + ", game_over = " + str(game_over))
        return False
    # 4) 结束以后水果不能再掉 / nothing falls after game over
    _time.sleep(0.2)
    _y = fruit.ycor()
    _time.sleep(0.3)
    if fruit.ycor() != _y:
        print("__KC_HINT__ game_over 已经是 True 了，可水果还在往下掉。tick() 要在 game_over 的时候停下|game_over is True but the fruit is still falling. tick() must stop when game_over is True")
        return False
    # 5) 结束后按空格：重新开始 / space after game over: start again
    score = 7
    restart()
    if score != 0 or lives != _start or game_over:
        print("__KC_HINT__ restart() 以后应该：score = 0、lives 回到 " + str(_start) + "、game_over = False。现在 score = " + str(score) + "，lives = " + str(lives) + "，game_over = " + str(game_over) + "|After restart(): score = 0, lives back to " + str(_start) + ", game_over = False. Now score = " + str(score) + ", lives = " + str(lives) + ", game_over = " + str(game_over))
        return False
    _y = fruit.ycor()
    _time.sleep(0.3)
    if fruit.ycor() == _y:
        print("__KC_HINT__ restart() 以后水果没有重新动起来。restart() 最后要再叫一次 tick()，让心跳重新开始|After restart() the fruit doesn't move again. Call tick() at the end of restart() to restart the heartbeat")
        return False
    # 6) 游戏进行中按空格：不能清零（不然就能作弊了）/ space during a game: must not reset (that would be cheating)
    score = 5
    restart()
    if score != 5:
        print("__KC_HINT__ 游戏还在进行时按空格，分数被清零了！restart() 一开始要检查：如果 game_over 不是 True，就直接 return|Pressing space mid-game reset the score! At the start of restart(), if game_over isn't True, just return")
        return False
    score = 0
    return True
if _kc7():
    print("__KC_WIN__")
