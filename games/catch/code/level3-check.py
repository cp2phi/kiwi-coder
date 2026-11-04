if FRUIT_COLOUR != "red" and BASKET_COLOUR != "brown":
    print("__KC_WIN__")
elif FRUIT_COLOUR == "red":
    print("__KC_HINT__ 水果还是 red。改 FRUIT_COLOUR 那一行|The fruit is still red. Change the FRUIT_COLOUR line")
else:
    print("__KC_HINT__ 篮子还是 brown。改 BASKET_COLOUR 那一行|The basket is still brown. Change the BASKET_COLOUR line")
