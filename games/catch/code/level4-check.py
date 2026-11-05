if MAX_MISSES >= 5:
    print("__KC_WIN__")
else:
    print("__KC_HINT__ 现在漏掉 " + str(MAX_MISSES) + " 个就结束。改 MAX_MISSES 那一行|Right now " + str(MAX_MISSES) + " misses ends the game. Change the MAX_MISSES line")
